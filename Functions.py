#def key word is used to define a function
#after a function is implemented there need to be at least two line breaks after

def greet_user(first_name, last_name):
    print(f"Hey {first_name} {last_name}, What's up?")

'''name is a keywork arguement
For key word arguments position doesn't matter. E.g. order of the arguments passed through the method call do not need to match the order
of the parameters in the method during implementation.
Keyword arguments can be helpful for numerical arguments
'''

greet_user(last_name = "Harrison",first_name = "Kris")

#Positional argument
greet_user("Kris", "Harrison")

#Keyword arguments should be the last arguments in the list
#E.g.
greet_user("Kris", last_name="Harrison")