# https://www.codewars.com/kata/56b22765e1007b79f2000079/train/python
def is_narcissistic(i):
    total = 0
    for num in str(i):
        total += int(num)**len(str(i))
        
    if total == int(i):
        return True
    else:
        return False

# def is_narcissistic(i):
#     return sum([int(n)**len(str(i)) for n in str(i)])==i

# def is_narcissistic(n):
#     t = str(n)
#     l = len(t)
    
#     return n == sum(int(d) ** l for d in t)

print(is_narcissistic(153))
print(is_narcissistic(1634))
