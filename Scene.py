import matplotlib.pyplot as plt


class Scene:
    def __init__(self, camera):
        self.camera = camera
        self.lights = []
        self.objects = []

    def add_light(self, light):
        self.lights.append(light)

    def add_object(self, mesh):
        self.objects.append(mesh)

    def render(self, filename):
        plt.imsave(filename, self.camera.render())
