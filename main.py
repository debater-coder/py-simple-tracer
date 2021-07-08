import numpy as np
from Scene import Scene
from Camera import Camera
from Sphere import Sphere

width, height = 400, 200

cameraPos = np.array([0, 0, 0])

imagePlane = {
    "TL": np.array([-2, 1, -1]),
    "TR": np.array([2, 1, -1]),
    "BL": np.array([-2, -1, -1]),
    "BR": np.array([2, -1, -1]),
}

scene = Scene()
scene.add_hittable(Sphere(np.array([0, 0, -1]), 0.5))
scene.add_hittable(Sphere(np.array([0, -100.5, -1]), 100))

camera = Camera((width, height), imagePlane, cameraPos, scene, 2, 50)
camera.render("image.png")
