import numpy as np
from utils import lerp, normalize
from alive_progress import alive_bar
import matplotlib.pyplot as plt


def hit_sphere(centre, radius, ray):
    oc = ray["origin"] - centre
    a = np.dot(ray["direction"], ray["direction"])
    half_b = np.dot(oc, ray["direction"])
    c = np.dot(oc, oc) - radius ** 2
    discriminant = half_b ** 2 - a * c
    if discriminant < 0:
        return -1
    else:
        return (-half_b - np.sqrt(discriminant)) / a


class Camera:
    def __init__(self, resolution, image_plane, position, scene):
        self.width, self.height = resolution
        self.image_plane = image_plane
        self.position = position
        self.scene = scene

    def render(self, filename):
        image = np.zeros((self.height, self.width, 3))

        with alive_bar(self.height) as bar:
            for i, beta in enumerate(np.linspace(0, 1, self.height)):
                for j, alpha in enumerate(np.linspace(0, 1, self.width)):
                    image[i, j] = self.ray_trace(alpha, beta)  # Find the pixel color
                bar()  # Update progress bar
        plt.imsave(filename, image)

    def ray_trace(self, alpha, beta):
        # Define the image point
        imagePoint = lerp(
            lerp(self.image_plane["TL"], self.image_plane["TR"], alpha),
            lerp(self.image_plane["BL"], self.image_plane["BR"], alpha),
            beta
        )

        # Define the ray
        ray = {
            "origin":    self.position,
            "direction": imagePoint - self.position,
        }

        # If we intersect the sphere then color that pixel red
        t = hit_sphere(np.array([0, 0, -1]), 0.5, ray)
        if t > 0:
            N = normalize(
                lerp(
                    ray["origin"],
                    ray["direction"],
                    t
                ) - np.array([0, 0, -1])
            )
            return 0.5 * (N + 1)

        # Set a gradient background based on the ray
        return lerp(
            np.array([1, 1, 1]),
            np.array([0.5, 0.7, 1]),
            (normalize(ray["direction"])[1] + 1) / 2
        )
