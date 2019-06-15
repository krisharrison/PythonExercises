
numbers_mapping= {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}

phone = input("Phone: ")


for digit in phone:
    print(numbers_mapping[digit], end=' ')



#Alternative method. Using get method so that a digit entered will not cause an error
for digit in phone:
    print(numbers_mapping.get(digit, "Not a valid digit"), end=' ')
