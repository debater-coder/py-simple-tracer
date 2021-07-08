from utils import *
from alive_progress import alive_bar
import matplotlib.pyplot as plt
import random


class Camera:
    def __init__(self, resolution, image_plane, position, scene, antialiasing, max_depth):
        self.width, self.height = resolution
        self.image_plane = image_plane
        self.position = position
        self.scene = scene
        self.antialiasing = antialiasing
        self.max_depth = max_depth

    def nearest_intersected_hittable(self, ray):
        distances = [hittable.hit(ray) for hittable in self.scene.hittables]
        nearest_hittable = None
        min_distance = np.inf
        for index, distance in enumerate(distances):
            if 0 < distance < min_distance:
                min_distance = distance
                nearest_hittable = self.scene.hittables[index]
        return nearest_hittable, min_distance

    def render(self, filename):
        image = np.zeros((self.height, self.width, 3))

        with alive_bar(self.height * self.width * self.antialiasing) as bar:
            for i, beta in enumerate(np.linspace(0, 1, self.height)):
                for j, alpha in enumerate(np.linspace(0, 1, self.width)):

                    total_color = 0
                    for k in range(self.antialiasing):
                        # Find the pixel color
                        total_color += self.ray_trace(
                            alpha + random.random() / self.width,
                            beta + random.random() / self.height,
                        )
                        bar()  # Update progress bar

                    # Find the average and gamma correct for gamma=2.0
                    image[i, j] = np.sqrt(total_color / self.antialiasing)

        plt.imsave(filename, image)  # Save the image to the file

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

        return self.ray_color(ray, self.max_depth)

    def ray_color(self, ray, max_depth):
        # If we exceed our max depth then gather no more light
        if max_depth <= 0:
            return np.array([0, 0, 0])

        # If we intersect an object then calculate the color of that pixel
        hittable, t = self.nearest_intersected_hittable(ray)
        if hittable and t > 0:
            hit_point = lerp(ray["origin"], ray["direction"], t)
            normal = hittable.normal(hit_point)
            target = hit_point + normal + random_unit_vector()
            return 0.5 * self.ray_color({"origin": hit_point, "direction": target}, max_depth-1)

        # Set a gradient background based on the ray
        return lerp(
            np.array([1, 1, 1]),
            np.array([0.5, 0.7, 1]),
            (normalize(ray["direction"])[1] + 1) / 2
        )
