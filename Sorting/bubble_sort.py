arr = [1,4,2,5,7,8,9]
n = len(arr)

for i in range(n-1,-1,-1):
    for j in range(i):
        if arr[j] >= arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)