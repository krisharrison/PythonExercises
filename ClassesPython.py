class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

#instance of a class
point1 = Point()
#calling draw method
point1.draw()

#Attributes
point1.x = 10
point1.y = 20

#Second object/instance
point2 = Point()