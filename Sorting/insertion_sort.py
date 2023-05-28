arr = [1,4,2,5,7,8,9]
n = len(arr)

for i in range(n):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]

print(arr)