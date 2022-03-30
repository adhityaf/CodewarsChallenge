# def reverse_words(string):
#     ## splitting the string on space
#     words = string.split()
#     ## reversing the words using reversed() function
#     words = list(reversed(words))
#     ## joining the words and printing
#     return " ".join(words)

def reverse_words(str):
    return ' '.join(reversed(str.split(' ')))

print(reverse_words("The greatest victory is that which requires no battle"))