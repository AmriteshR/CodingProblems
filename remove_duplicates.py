arr = [1,1,2,2,2,3,3]

def remove_duplicates(arr):
    n = len(arr)
    i = 0
    for j in range(1,n):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    # Returning index till which all unique elements are present
    return i + 1


k = remove_duplicates(arr)
print(arr[:k])