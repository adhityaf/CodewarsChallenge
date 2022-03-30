# def find_it(seq):
#     # loop setiap nomor di dalam seq
#     for num in seq:
#         # buat copy dari seq
#         copySeq = seq[:]
#         # set inital value untuk setiap nomor
#         numSum = 0

#         cond = True
#         while cond:
#             if num in copySeq:
#                 numSum += 1
#                 copySeq.remove(num)

#             if num not in copySeq and numSum % 2 == 0:
#                 cond = False
#             # jika jumlah num ganjil maka print num nya
#             elif num not in copySeq and numSum % 2 != 0:
#                 return num

def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num


print(find_it([7]))
print(find_it([0]))
print(find_it([1,1,2]))
print(find_it([0,1,0,1,0]))
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_it([1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1]))
