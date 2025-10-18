class RGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def _astuple(self):
        return (self.red, self.green, self.blue)


color1 = RGB(10, 20, 30)
print(color1._astuple())  # (10, 20, 30)

color2 = RGB(*color1._astuple())
print(color2.red, color2.green, color2.blue)  # 10, 20, 30


from dataclasses import dataclass


@dataclass
class DataclassRGB:
    red: int
    green: int
    blue: int


from dataclasses import astuple

color1 = DataclassRGB(10, 20, 30)
print(astuple(color1))  # (10, 20, 30)

color2 = DataclassRGB(*astuple(color1))
print(color2)  # DataclassRGB(red=10, green=20, blue=30)
