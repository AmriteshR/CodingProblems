arr1 = [1,2,3,4,5,6,7]
arr2 = [2,3,4,4,6,9]

i,j = 0,0
m = len(arr1)
n = len(arr2)
arr3 = []
while(i<m and j<n):
    if arr1[i] == arr2[j]:
        if arr1[i] not in arr3:
            arr3.append(arr1[i])
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1
print(arr3)