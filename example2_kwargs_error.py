class RGB:
    def __init__(self, *, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


bad = RGB(10, green=20, blue=30)  # raises TypeError
