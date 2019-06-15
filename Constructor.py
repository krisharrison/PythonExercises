class Point:
    def __init__(self, x, y): #Constructor
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point = Point(10, 20)
#Setting X
point.x = 21
print(f"{point.x}, {point.y}")