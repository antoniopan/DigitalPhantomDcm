import Geometry3D as Geo3d
import copy
import numpy as np


class Volume3D(object):
    def __init__(self, x: int = 512, y: int = 512, z: int = 512, origin: Geo3d.Point = Geo3d.Point(0, 0, 0),
                dim: Geo3d.Vector = Geo3d.Vector(1000, 1000, 1000)):
        self.center = origin
        self.x_orientation = Geo3d.Vector(1, 0, 0)
        self.y_orientation = Geo3d.Vector(0, 1, 0)
        self.z_orientation = Geo3d.Vector(0, 0, 1)
        self.x_dim = x
        self.y_dim = y
        self.z_dim = z
        range_xyz = dim.v
        self.x_spacing = range_xyz[0] / x
        self.y_spacing = range_xyz[1] / y
        self.z_spacing = range_xyz[2] / z
        self.pixel_data = np.ones((self.x_dim, self.y_dim, self.z_dim), dtype='uint16') * 1000

    def origin(self):
        o = copy.deepcopy(self.center).move(self.x_orientation * self.x_spacing * self.x_dim * -0.5)
        o.move(self.y_orientation * self.y_spacing * self.y_dim * -0.5)
        o.move(self.z_orientation * self.z_spacing * self.z_dim * -0.5)
        return o

    def pixel_center(self, x, y, z):
        p = self.origin().move(self.x_orientation * self.x_spacing * (x + 0.5))
        p.move(self.y_orientation * self.y_spacing * (y + 0.5))
        p.move(self.z_orientation * self.z_spacing * (z + 0.5))
        return p

    def resize(self):
        self.pixel_data.resize(self.x_dim, self.y_dim, self.z_dim)

    def bounding_floor(self, point: Geo3d.Point) -> [int, int, int]:
        p0 = self.origin()
        o = np.array([p0.x, p0.y, p0.z])
        c = np.maximum(o, np.array([point.x, point.y, point.z]))
        return np.floor((c - o) / np.array([self.x_spacing, self.y_spacing, self.z_spacing]))

    def bounding_ceil(self, point: Geo3d.Point) -> [int, int, int]:
        p1 = copy.deepcopy(self.origin()).move(
            Geo3d.Vector(self.x_dim * self.x_spacing, self.y_dim * self.y_spacing, self.z_dim * self.z_spacing))
        o = np.array([p1.x, p1.y, p1.z])
        c = np.minimum(o, np.array([point.x, point.y, point.z]))
        return [self.x_dim, self.y_dim, self.z_dim] - \
            np.floor((o - c) / np.array([self.x_spacing, self.y_spacing, self.z_spacing]))
