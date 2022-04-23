# capitalLetter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# def solution(s):
#     newString = ""
#     for letter in s:
#         if letter in capitalLetter:
#             newString += " " + letter
#         else:
#             newString += letter
#     return newString

def solution(s):
    newString = ""
    for letter in s:
        if letter.isupper():
            newString += " " + letter
        else:
            newString += letter
    return newString

print(solution("helloWorldAditLol"))

# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python