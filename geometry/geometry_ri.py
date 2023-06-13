import abc
import copy
import typing
import Geometry3D as Geo3d


class ISampleGenerator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def generate_sample_point(self, point: Geo3d.Point, dim_range: Geo3d.Vector, coefficient: int)\
            -> typing.Iterable[Geo3d.Point]:
        pass


class IConvexShape3D(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def inside(self, point: Geo3d.Point) -> bool:
        pass

    @abc.abstractmethod
    def bounding_box(self) -> [Geo3d.Point, Geo3d.Point]:
        pass

    @abc.abstractmethod
    def get_pixel_val(self) -> int:
        pass

    def inside_range(self, point: Geo3d.Point, pixel_size: Geo3d.Vector) -> int:
        """
        :param point:
        :param pixel_size:
        :return:
            0   pixel is outside of the geometry
            1   pixel intersects with the geometry
            2   pixel is inside of the geometry
        """
        sample_list = [
            copy.deepcopy(point).move(Geo3d.Vector(pixel_size.v[0] * -0.5, pixel_size.v[1] * -0.5, pixel_size.v[2] * -0.5)),
            copy.deepcopy(point).move(Geo3d.Vector(pixel_size.v[0] * -0.5, pixel_size.v[1] * -0.5, pixel_size.v[2] * 0.5)),
            copy.deepcopy(point).move(Geo3d.Vector(pixel_size.v[0] * -0.5, pixel_size.v[1] * 0.5, pixel_size.v[2] * -0.5)),
            copy.deepcopy(point).move(Geo3d.Vector(pixel_size.v[0] * -0.5, pixel_size.v[1] * 0.5, pixel_size.v[2] * 0.5)),
            copy.deepcopy(point).move(Geo3d.Vector(pixel_size.v[0] * 0.5, pixel_size.v[1] * -0.5, pixel_size.v[2] * -0.5)),
            copy.deepcopy(point).move(Geo3d.Vector(pixel_size.v[0] * 0.5, pixel_size.v[1] * -0.5, pixel_size.v[2] * 0.5)),
            copy.deepcopy(point).move(Geo3d.Vector(pixel_size.v[0] * 0.5, pixel_size.v[1] * 0.5, pixel_size.v[2] * -0.5)),
            copy.deepcopy(point).move(Geo3d.Vector(pixel_size.v[0] * 0.5, pixel_size.v[1] * 0.5, pixel_size.v[2] * 0.5))
        ]
        count = int(0)
        for p in sample_list:
            if self.inside(p):
                count += 1
        if count == 0:
            return 0
        elif count < 8:
            return 1
        else:
            return 2

