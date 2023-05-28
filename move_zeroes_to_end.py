# arr = [1,0,0,2,3,0,4,0,0,1]
arr = [1,2,3,5,6,7,0,9,8,0,5,0,0,2]

i = arr.index(0)

for j in range(i+1,len(arr)):
    print(f"Value of i {i}, {arr[i]} and value of j {j}, {arr[j]}")
    if arr[j] == 0:
        continue
    else:
        print(f"Swapping of i and j done")
        arr[i] = arr[j]
        arr[j] = 0
        i += 1
        print(arr)
print(arr)