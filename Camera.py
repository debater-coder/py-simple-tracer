import numpy as np
from util import lerp


# noinspection DuplicatedCode
class Camera:
    def __init__(self, resolution, image_plane, position):
        self.width, self.height = resolution
        self.image_plane = image_plane
        self.position = position

    def render(self):
        image = np.zeros((self.height, self.width, 3))

        for i, beta in enumerate(np.linspace(0, 1, self.height)):
            for j, alpha in enumerate(np.linspace(0, 1, self.width)):
                imagePoint = lerp(
                    lerp(self.image_plane["TL"], self.image_plane["TR"], alpha),
                    lerp(self.image_plane["BL"], self.image_plane["BR"], alpha),
                    beta
                )

                image[i, j] = np.array([
                    (imagePoint[0] + 2) / 4,
                    (imagePoint[1] + 1) / 2,
                    0.5
                ])

        return image
