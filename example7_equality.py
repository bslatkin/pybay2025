class RGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


color1 = RGB(10, 20, 30)
color2 = RGB(10, 20, 30)

print(color1 == color2)  # False
print(color1 == color1)  # True
print(color1 is color1)  # True
print(color1 != color2)  # True
print(color1 is not color2)  # True


class RGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def _astuple(self):
        return (self.red, self.green, self.blue)

    def __eq__(self, other):
        return (
            type(self) == type(other) and self._astuple() == other._astuple()
        )


color1 = RGB(10, 20, 30)
color2 = RGB(10, 20, 30)
color3 = RGB(50, 60, 70)

print(color1 == color1)  # True
print(color1 == color2)  # True
print(color1 is not color2)  # True
print(color1 != color3)  # True


from dataclasses import dataclass


@dataclass
class DataclassRGB:
    red: int
    green: int
    blue: int


color1 = DataclassRGB(10, 20, 30)
color2 = DataclassRGB(10, 20, 30)
color3 = DataclassRGB(50, 60, 70)

print(color1 == color1)  # True
print(color1 == color2)  # True
print(color1 is not color2)  # True
print(color1 != color3)  # True
