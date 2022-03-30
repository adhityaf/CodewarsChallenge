def merge_arrays(arr1, arr2):
    newArr = []
    newArr = arr1 + arr2
    nonDuplicate = []
    for item in newArr:
        if item not in nonDuplicate:
            nonDuplicate.append(item)
            
    nonDuplicate.sort()
    return nonDuplicate


arr1 = [1, 2, 3, 4, 5];
arr2 = [6, 7, 8, 9, 10];
arr3 = [1, 3, 5, 7, 9];
arr4 = [10, 8, 6, 4, 2];
arr5 = [1, 3, 5, 7, 9, 11, 12];
arr6 = [1, 2, 3, 4, 5, 10, 12];
print(merge_arrays(arr5, arr6))

# def merge_arrays(arr1, arr2):
#     newArr = sorted(set(arr1 + arr2))
            
#     return newArr