arr = [1,4,2,5,7,8,9]
n = len(arr)

for i in range(n):
    minArr = i
    for j in range(i+1,n):
        if arr[j] < arr[minArr]:
            minArr = j
    arr[minArr], arr[i] = arr[i], arr[minArr]

print(arr)
    