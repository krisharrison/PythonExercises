
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"What is up, home slice? My Name is {self.name}.")

kris = Person("Kris")

kris.talk()