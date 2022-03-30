def xo(s):
    strList = list(s.lower())
    if 'x' not in strList and 'o' not in strList:
        return True
    elif strList.count('x') == strList.count('o'):
        return True
    else:
        return False

# def xo(s):
#     return s.lower().count('x') == s.lower().count('o')

print(xo("OoXx"))
