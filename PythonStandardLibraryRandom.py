import random
import math

#Displays random number between 0 and 1
for i in range(3):
    
    print(random.random(), end=' ')

print("\n")
#Displays three int values between 10 & 20
for i in range(3):
    print(f"{random.randint(10, 20)}", end=' ')

print()
#Method that random chooses an item from a list
members = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(members)

print(f"\n{leader}")