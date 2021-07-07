import numpy as np


def lerp(a, b, t):
    return a * (1-t) + b * t


def normalize(vector):
    return vector / np.linalg.norm(vector)
