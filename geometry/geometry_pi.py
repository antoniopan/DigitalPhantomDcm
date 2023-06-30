import copy

import numpy as np

from geometry import geometry_ri
from volume import volume3d
from geometry import volume_phantom
from geometry import geometry_impl
import Geometry3D as Geo3d


class VolumeGenerator(object):
    def __init__(self):
        self.volume = volume3d.Volume3D()
        self.sampler = geometry_impl.UniformGenerator()
        self.geo_list = []
        self.sample_lvl = 2

    def sample_one_pixel(self, pixel_center: Geo3d.Point, pixel_size: Geo3d.Vector,
                         geo: geometry_ri.IConvexShape3D) -> [int, int, int]:
        inside_return = geo.inside_range(pixel_center, pixel_size)
        if inside_return == 0:
            return 0
        elif inside_return == 2:
            return geo.get_pixel_val()
        else:
            sample_list = self.sampler.generate_sample_point(pixel_center, pixel_size, self.sample_lvl)
            inside_num = int(0)
            for s in sample_list:
                if geo.inside(s):
                    inside_num = inside_num + 1
            return int(geo.get_pixel_val() * inside_num / len(sample_list))

    def process_one_shape(self, vol: volume3d.Volume3D, geo: geometry_ri.IConvexShape3D):
        """
        Update the voxel values for one geometry
        :param vol:
        :param geo:
        :return:
        """
        [start_point, end_point] = geo.bounding_box()
        start_pixel = vol.bounding_floor(start_point)
        end_pixel = vol.bounding_ceil(end_point)
        pixel_vertices_inside = np.zeros(
            (int(end_pixel[0] - start_pixel[0] + 1), int(end_pixel[1] - start_pixel[1] + 1),
             int(end_pixel[2] - start_pixel[2] + 1)), dtype='uint8')
        o = vol.origin()
        # Assume that there is no overlap or spacing between adjacent voxels,
        # Adjacent voxels share four vertices spatially.
        # Calculate each vertex if it is inside or outside the geometry
        for k in range(int(start_pixel[2]), int(end_pixel[2]) + 1):
            for j in range(int(start_pixel[1]), int(end_pixel[1]) + 1):
                for i in range(int(start_pixel[0]), int(end_pixel[0]) + 1):
                    p = copy.deepcopy(o).move(Geo3d.Vector(vol.x_spacing * i, vol.y_spacing * j, vol.z_spacing * k))
                    if geo.inside(p):
                        pixel_vertices_inside[
                            i - int(start_pixel[0]), j - int(start_pixel[1]), k - int(start_pixel[2])] = 1
        k = 0
        for z in range(int(start_pixel[2]), int(end_pixel[2])):
            j = 0
            for y in range(int(start_pixel[1]), int(end_pixel[1])):
                i = 0
                for x in range(int(start_pixel[0]), int(end_pixel[0])):
                    pixel_center = vol.pixel_center(x, y, z)
                    inside_return = pixel_vertices_inside[i, j, k] + pixel_vertices_inside[i, j, k + 1] + \
                                    pixel_vertices_inside[i, j + 1, k] + pixel_vertices_inside[i, j + 1, k + 1] + \
                                    pixel_vertices_inside[i + 1, j, k] + pixel_vertices_inside[i + 1, j, k + 1] + \
                                    pixel_vertices_inside[i + 1, j + 1, k] + pixel_vertices_inside[i + 1, j + 1, k + 1]
                    if inside_return == 0:
                        # All the vertices are outside the geometry
                        # do not change the pixel value
                        vol.pixel_data[x, y, z] = vol.pixel_data[x, y, z]
                    elif inside_return == 8:
                        # All the vertices are inside the geometry
                        vol.pixel_data[x, y, z] = geo.get_pixel_val()
                    else:
                        # The voxel is located across the geometry surface
                        # sample inside the geometry to determine blend factor
                        sample_list = self.sampler.generate_sample_point(
                            pixel_center, Geo3d.Vector(self.volume.x_spacing,
                                                       self.volume.y_spacing, self.volume.z_spacing), self.sample_lvl)
                        inside_num = int(0)
                        for s in sample_list:
                            if geo.inside(s):
                                inside_num = inside_num + 1
                        vol.pixel_data[x, y, z] = (geo.get_pixel_val() * inside_num + vol.pixel_data[x, y, z] *
                                                   (len(sample_list) - inside_num)) / len(sample_list)
                    i += 1
                j += 1
            k += 1

    def process_volume(self) -> volume3d.Volume3D:
        for geo in self.geo_list:
            self.process_one_shape(self.volume, geo)
        return self.volume

    def from_xml(self, xml_path: str):
        vol_config = volume_phantom.CreateFromDocument(open(xml_path).read())
        self.volume = volume3d.Volume3D(vol_config.dim_x, vol_config.dim_y, vol_config.dim_z,
                                        Geo3d.Point(vol_config.origin.x, vol_config.origin.y, vol_config.origin.z),
                                        Geo3d.Vector(vol_config.dimension.x, vol_config.dimension.y,
                                                     vol_config.dimension.z))
        for cylinder in vol_config.cylinder:
            c = geometry_impl.Cylinder(Geo3d.Point(cylinder.center.x, cylinder.center.y, cylinder.center.z),
                                       cylinder.height, cylinder.radius, cylinder.p_value)
            self.geo_list.append(c)
        for cube in vol_config.cube:
            c = geometry_impl.Cube(Geo3d.Point(cube.center.x, cube.center.y, cube.center.z),
                                   Geo3d.Vector(cube.dim.x, cube.dim.y, cube.dim.z), cube.p_value)
            self.geo_list.append(c)
        for ellipsoid in vol_config.ellipsoid:
            e = geometry_impl.Ellipsoid(Geo3d.Point(ellipsoid.center.x, ellipsoid.center.y, ellipsoid.center.z),
                                        ellipsoid.a, ellipsoid.b, ellipsoid.c, ellipsoid.p_value)
            self.geo_list.append(e)
        for sphere in vol_config.sphere:
            s = geometry_impl.Sphere(Geo3d.Point(sphere.center.x, sphere.center.y, sphere.center.z),
                                     sphere.radius, sphere.p_value)
            self.geo_list.append(s)

        self.sampler = geometry_impl.UniformGenerator()
        return
