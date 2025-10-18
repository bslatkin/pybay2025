from dataclasses import dataclass


@dataclass
class DataclassRGB:
    red: int
    green: int
    blue: int


obj = DataclassRGB(10, "bad", 30)
obj.red = "also bad"
obj.bloe = 30
