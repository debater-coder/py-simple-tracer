class Scene:
    def __init__(self):
        self.hittables = []

    def add_hittable(self, hittable):
        self.hittables.append(hittable)
