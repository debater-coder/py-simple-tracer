import numpy as np
from Scene import Scene
from Camera import Camera

width, height = 640, 360

cameraPos = np.array([0, 0, 0])

imagePlane = {
    "TL": np.array([-2, 1, -1]),
    "TR": np.array([2, 1, -1]),
    "BL": np.array([-2, -1, -1]),
    "BR": np.array([2, -1, -1]),
}

scene = Scene()
camera = Camera((width, height), imagePlane, cameraPos, scene)

camera.render("image.png")
