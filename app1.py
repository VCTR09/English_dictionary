import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word == '/end':
        pass
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


def translate2():
    word = input("Enter word: ")
    output = translate(word)
    if word == "/end":
        exit()
    elif type(output) == list:
        i = 1
        for item in output:
            print("%s. %s" % (i,item)) 
            i+=1
        translate2()
    else:
        print(output)
        translate2()
 
translate2()


# while True:
#     word = input("Enter a word: ")
#     output = translate(word)
#     if word == "/end":
#         break
#     else:
#         if type(output) == list:
#             i = 1
#             for item in output:
#                 print("%s. %s" % (i,item)) 
#                 i+=1
#         else:
#             print(output)
