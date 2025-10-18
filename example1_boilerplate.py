class RGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


color = RGB(10, 20, 30)

print(color.red)  # 10
print(color.green)  # 20
print(color.blue)  # 30


from dataclasses import dataclass


@dataclass
class DataclassRGB:
    red: int
    green: int
    blue: int


color = DataclassRGB(10, 20, 30)

print(color.red)  # 10
print(color.green)  # 20
print(color.blue)  # 30
