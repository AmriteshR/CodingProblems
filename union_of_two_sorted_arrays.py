arr1 = [1,2,3,4,5,6,7]
arr2 = [2,3,4,4,6,9]

# arr3 = arr1 + arr2
# print(set(arr3))

arr3 = []
i,j = 0,0
while(i<len(arr1) and j<len(arr2)):
    if arr1[i] == arr2[j]:
        if arr1[i] not in arr3:
            arr3.append(arr1[i])
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        if arr1[i] not in arr3:
            arr3.append(arr1[i])
        i += 1
    else:
        if arr2[j] not in arr3:
            arr3.append(arr2[j])
        j += 1
if i<len(arr1):
    arr3 = arr3 + arr1[i:]
else:
    arr3 = arr3 + arr2[j:]
print(arr3)