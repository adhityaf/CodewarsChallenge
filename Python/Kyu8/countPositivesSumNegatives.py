def count_positives_sum_negatives(arr):
    countPositives = 0
    sumNegatives = 0
    
    if arr == None or len(arr) == 0:
        return []
    
    for item in arr:
        if item > 0:
            countPositives += 1
        else:
            sumNegatives += item
            
    return [countPositives, sumNegatives]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
print(count_positives_sum_negatives([]))


# Other Solutions:
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []

count_positives_sum_negatives = lambda arr: [len([e for e in arr if e>0]), sum(e for e in arr if e<0)] if arr else []

# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python