from geometry import geometry_ri
import Geometry3D as Geo3d
import copy
import typing
import numpy as np


class Cylinder(geometry_ri.IConvexShape3D):
    def __init__(self, center: Geo3d.Point, height: float, radius: float, val: int):
        self.center = center
        self.height = height
        self.radius = radius
        self.val = val

    def inside(self, point: Geo3d.Point) -> bool:
        if abs(point.z - self.center.z) > self.height / 2:
            return False
        a = point.x - self.center.x
        b = point.y - self.center.y
        if a ** 2 + b ** 2 > self.radius ** 2:
            return False
        return True

    def bounding_box(self) -> [Geo3d.Point, Geo3d.Point]:
        return [
            copy.deepcopy(self.center).move(Geo3d.Vector(-self.radius, -self.radius, -self.height / 2)),
            copy.deepcopy(self.center).move(Geo3d.Vector(self.radius, self.radius, self.height / 2))
        ]

    def get_pixel_val(self) -> int:
        return self.val


class Cube(geometry_ri.IConvexShape3D):
    def __init__(self, center: Geo3d.Point, dim: Geo3d.Vector, val: int):
        self.center = center
        self.dim = dim
        self.val = val

    def inside(self, point: Geo3d.Point) -> bool:
        if abs(point.x - self.center.x) > self.dim.v[0] / 2:
            return False
        if abs(point.y - self.center.y) > self.dim.v[1] / 2:
            return False
        if abs(point.z - self.center.z) > self.dim.v[2] / 2:
            return False
        return True

    def bounding_box(self) -> [Geo3d.Point, Geo3d.Point]:
        return [
            copy.deepcopy(self.center).move(-self.dim * 0.5),
            copy.deepcopy(self.center).move(self.dim * 0.5)
        ]

    def get_pixel_val(self) -> int:
        return self.val


class Sphere(geometry_ri.IConvexShape3D):
    def __init__(self, center: Geo3d.Point, radius: float, val: int):
        self.center = center
        self.radius = radius
        self.val = val

    def inside(self, point: Geo3d.Point) -> bool:
        return self.center.distance(point) < self.radius

    def bounding_box(self) -> [Geo3d.Point, Geo3d.Point]:
        return [
            copy.deepcopy(self.center).move(Geo3d.Vector(1, 1, 1) * -self.radius),
            copy.deepcopy(self.center).move(Geo3d.Vector(1, 1, 1) * self.radius),
        ]

    def get_pixel_val(self) -> int:
        return self.val


class Ellipsoid(geometry_ri.IConvexShape3D):
    def __init__(self, center: Geo3d.Point, a: float, b: float, c: float, val: int):
        self.center = center
        self.a = a
        self.b = b
        self.c = c
        self.val = val

    def inside(self, point: Geo3d.Point) -> bool:
        x = self.center.x - point.x
        y = self.center.y - point.y
        z = self.center.z - point.z
        return (x/self.a)**2 + (y/self.b)**2 + (z/self.c)**2 < 1

    def bounding_box(self) -> [Geo3d.Point, Geo3d.Point]:
        return [
            copy.deepcopy(self.center).move(Geo3d.Vector(-self.a, -self.b, -self.c)),
            copy.deepcopy(self.center).move(Geo3d.Vector(self.a, self.b, self.c))
        ]

    def get_pixel_val(self) -> int:
        return self.val


class RandomGenerator(geometry_ri.ISampleGenerator):
    def generate_sample_point(self, point: Geo3d.Point, dim_range: Geo3d.Vector, coefficient: int) -> typing.Iterable[Geo3d.Point]:
        num = (2**coefficient)**3
        point_list = []
        spacing = np.array(dim_range.v)
        for i in range(num):
            point_list.append(copy.deepcopy(point).move(Geo3d.Vector(spacing * (np.random.random(3)-0.5))))

        return point_list


class UniformGenerator(geometry_ri.ISampleGenerator):
    def generate_sample_point(self, point: Geo3d.Point, dim_range: Geo3d.Vector, coefficient: int) -> typing.Iterable[Geo3d.Point]:
        num = 2**coefficient
        point_list = []
        spacing = np.array(dim_range.v) / num
        vx = Geo3d.Vector.x_unit_vector() * spacing[0]
        vy = Geo3d.Vector.y_unit_vector() * spacing[1]
        vz = Geo3d.Vector.z_unit_vector() * spacing[2]
        origin = copy.deepcopy(point).move(-dim_range*0.5).move(Geo3d.Vector(spacing/2))
        for i in range(num):
            for j in range(num):
                for k in range(num):
                    point_list.append(copy.deepcopy(origin).move(vx*i+vy*j+vz*k))
        return point_list
