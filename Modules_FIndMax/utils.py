def find_max(list):
    maximum = list[0]

    for number in list:
        if( number > maximum):
            maximum = number

    return maximum

