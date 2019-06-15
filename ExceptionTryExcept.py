#Dividing a number by 0 with give up a ZeroDivisionError Exception

num = -1
while num <= 0:
    try:
        num = int(input("\nEnter a number: "))

        if(num <= 0):
            print("Num must be greate than 0")
        else:
            num /= 0
            print(num)
    except ValueError:
        print("Invalid! Please enter an integer!")
    except ZeroDivisionError:
        print("You cannot divide a number by 0")
