from dataclasses import dataclass


@dataclass(kw_only=True)
class DataclassRGB:
    red: int
    green: int
    blue: int


bad = DataclassRGB(10, green=20, blue=30)  # raises TypeError
