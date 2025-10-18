class RGBA:
    def __init__(self, *, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha


color = RGBA(red=1, green=2, blue=3, alpha=1.0)


from dataclasses import dataclass


@dataclass(kw_only=True)
class DataclassRGBA:
    red: int
    green: int
    blue: int
    alpha: int = 1.0


class BadContainer:
    def __init__(self, *, value=[]):
        self.value = value


class BadContainer:
    def __init__(self, *, value=[]):
        self.value = value


obj1 = BadContainer()
obj2 = BadContainer()

obj1.value.append(1)

print(obj1.value)  # [1] as expected
print(obj2.value)  # [1] instead of []


class MyContainer:
    def __init__(self, *, value=None):
        if value is None:
            value = []  # Create when not supplied
        self.value = value


obj1 = MyContainer()
obj2 = MyContainer()
obj1.value.append(1)

print(obj1.value)  # [1] (as expected)
print(obj2.value)  # []  (as expected)


from dataclasses import field


@dataclass
class DataclassContainer:
    value: list = field(default_factory=list)


obj1 = DataclassContainer()
obj2 = DataclassContainer()
obj1.value.append(1)

print(obj1.value)  # [1] (as expected)
print(obj2.value)  # []  (as expected)
