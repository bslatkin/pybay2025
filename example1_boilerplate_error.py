class BadRGB:
    def __init__(self, green, red, blue):
        self.red = red
        self.green = green
        self.bloe = blue


color = BadRGB(10, 20, 30)

print(color.red)  # 20 (wrong!)
print(color.green)  # 10 (wrong!)
print(color.blue)  # raises AttributeError
