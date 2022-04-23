def make_readable(seconds):
    hour = seconds / 3600 // 99
    minute = seconds / 60 // 99
    second = seconds / 60 // 99
    
    print(hour, minute, second)
    
print(make_readable(60))
    
# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python