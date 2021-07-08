import numpy as np


def lerp(a, b, t):
    return a * (1 - t) + b * t


def normalize(vector):
    return vector / np.linalg.norm(vector)


def random_unit_vector():
    point = np.random.rand(3)
    while np.dot(point, point) >= 1:
        point = np.random.rand(3)
    return normalize(point)
