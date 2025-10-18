class RGB:
    def __init__(self, *, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


color = RGB(red=10, green=20, blue=30)
print(color)


class RGB:
    def __init__(self, *, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return (
            f"{type(self).__module__}"
            f".{type(self).__name__}("
            f"red={self.red!r}, "
            f"green={self.green!r}, "
            f"blue={self.blue!r})"
        )


color = RGB(red=10, green=20, blue=30)
print(color)


from dataclasses import dataclass


@dataclass(kw_only=True)
class DataclassRGB:
    red: int
    green: int
    blue: int


color = DataclassRGB(red=10, green=20, blue=30)
print(color)
