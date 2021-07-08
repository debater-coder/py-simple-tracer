import numpy as np
from Hittable import Hittable


class Sphere(Hittable):
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def normal(self, hit_point):
        return hit_point - self.centre

    def compute_hit_point(self, ray):
        oc = ray["origin"] - self.centre
        a = np.dot(ray["direction"], ray["direction"])
        half_b = np.dot(oc, ray["direction"])
        c = np.dot(oc, oc) - self.radius ** 2
        discriminant = half_b ** 2 - a * c
        if discriminant < 0:
            return -1
        else:
            return (-half_b - np.sqrt(discriminant)) / a
