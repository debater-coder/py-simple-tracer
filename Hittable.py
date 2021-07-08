import numpy as np
from abc import ABC, abstractmethod


class Hittable(ABC):
    @abstractmethod
    def normal(self, hit_point):
        pass

    @abstractmethod
    def compute_hit_point(self, ray):
        pass
