def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

print(longest("aretheyhere", "yestheyarehere"))
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
print(longest("inmanylanguages", "theresapairoffunctions"))

# https://www.codewars.com/kata/5656b6906de340bd1b0000ac