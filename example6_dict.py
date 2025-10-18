class RGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def _asdict(self):
        return dict(
            red=self.red,
            green=self.green,
            blue=self.blue,
        )


import json

color1 = RGB(red=10, green=20, blue=30)
data = json.dumps(color1._asdict())
print(data)  # {"red": 10, "green": 20, "blue": 30}

color2 = RGB(**color1._asdict())
print(color2.red, color2.green, color2.blue)  # 10, 20, 30


from dataclasses import dataclass


@dataclass(kw_only=True)
class DataclassRGB:
    red: int
    green: int
    blue: int


from dataclasses import asdict

color1 = DataclassRGB(red=10, green=20, blue=30)
print(asdict(color1))  # {'red': 10, 'green': 20, 'blue': 30}

color2 = DataclassRGB(**asdict(color1))
print(color2)  # DataclassRGB(red=10, green=20, blue=30)
