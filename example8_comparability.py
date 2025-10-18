class Planet:
    def __init__(self, distance, size):
        self.distance = distance
        self.size = size

    def _astuple(self):
        return (self.distance, self.size)

    def __eq__(self, other):
        return (
            type(self) == type(other) and self._astuple() == other._astuple()
        )

    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self._astuple() < other._astuple()

    def __le__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self._astuple() <= other._astuple()

    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self._astuple() > other._astuple()

    def __ge__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self._astuple() >= other._astuple()


far = Planet(10, 2)
near = Planet(1, 5)
data = [far, near]
data.sort()

print([near, far] == data)  # True


from functools import total_ordering


@total_ordering
class Planet:
    def __init__(self, distance, size):
        self.distance = distance
        self.size = size

    def _astuple(self):
        return (self.distance, self.size)

    def __eq__(self, other):
        return (
            type(self) == type(other) and self._astuple() == other._astuple()
        )

    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self._astuple() < other._astuple()


far = Planet(10, 2)
near = Planet(1, 5)
data = [far, near]
data.sort()

print([near, far] == data)  # True


from dataclasses import dataclass


@dataclass(order=True)
class DataclassPlanet:
    distance: float
    size: float


far = DataclassPlanet(10, 2)
near = DataclassPlanet(1, 5)
data = [far, near]
data.sort()

print([near, far] == data)  # True
