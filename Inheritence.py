# pass is used for empty classes or to tell python interpreter to not worry about an error
# Python doesn't like empy classes. It will cause an error. Pass allows for you to have an empty class
'''class Dog(Mammal):
    pass'''
#Use a partent class as an argument to the child class for inheritence

class Mammal:
    def walk(self):
        print("walk!")

class Dog(Mammal):
    def bark(self):
        print("Bark!")

class Cat(Mammal):
    def meow(self):
        print("Meow!")


dog = Dog()
cat = Cat()

dog.bark()
cat.meow()
dog.walk()
cat.walk()