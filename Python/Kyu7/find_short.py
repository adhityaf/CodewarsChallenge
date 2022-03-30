def find_short(s):
    strList = s.split(' ')
    shortest = len(strList[0])
    for word in strList:
        if len(word) < shortest:
            shortest = len(word)
            
    return shortest
    
print(find_short("bitcoin take over the world maybe who knows perhaps"))