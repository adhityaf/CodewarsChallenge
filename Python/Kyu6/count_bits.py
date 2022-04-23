def count_bits(n):
    biner = ""
    while n > 0:
        remainder = n % 2
        
        if remainder == 0:
            biner = "0" + biner
        else:
            biner = "1" + biner
            
        n //= 2
    
    return biner.count("1")
    
    
# def count_bits(n):
#     return bin(n).count("1")

print(count_bits(1234))