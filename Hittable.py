import numpy as np
from abc import ABC, abstractmethod


class Hittable(ABC):
    @abstractmethod
    def normal(self, hit_point):
        pass

    @abstractmethod
    def hit(self, ray):
        pass
