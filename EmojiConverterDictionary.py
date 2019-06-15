#ctrl + cmd + space will display emoji's for you to use
def convert_emjoi(message):
    emojis = {
        ":)": "😀",
        ":(": "😞"
    }

    words = message.split(" ")

    output = "\t"
    for word in words:
        output += emojis.get(word, word) + " "

    return output



message = input(">")


print(convert_emjoi(message))