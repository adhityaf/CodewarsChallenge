# https://www.codewars.com/kata/6167e70fc9bd9b00565ffa4e/train/python
def barista(coffees):
    totalTime = 0
    time_list = []
    for ind, num in enumerate(sorted(coffees, reverse=False)):
        if ind == 0:
            totalTime += num
            time_list.append(totalTime)
        else:
            totalTime += num + 2
            time_list.append(totalTime)
    
    return sum(time_list)

print(barista([4,3,2]))
print(barista([20,5,4,3,1,5,7,8]))