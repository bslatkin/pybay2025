class Planet:
    def __init__(self, distance, size):
        self.distance = distance
        self.size = size


far = Planet(10, 5)
near = Planet(1, 2)
data = [far, near]
data.sort()
