class RGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


color1 = RGB(red=10, green=20, blue=30)
color2 = RGB(10, 20, 30)
color3 = RGB(10, 20, blue=30)


class RGB:
    def __init__(self, *, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


color1 = RGB(red=10, green=20, blue=30)
color2 = RGB(green=20, red=10, blue=30)
color3 = RGB(blue=30, green=20, red=10)


from dataclasses import dataclass


@dataclass(kw_only=True)
class DataclassRGB:
    red: int
    green: int
    blue: int


color1 = DataclassRGB(red=10, green=20, blue=30)
color2 = DataclassRGB(green=20, red=10, blue=30)
color3 = DataclassRGB(blue=30, green=20, red=10)
