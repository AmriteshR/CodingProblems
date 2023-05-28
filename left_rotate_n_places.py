def reverse_arr(startIdx, endIdx, arr):
    while(startIdx <= endIdx):
        tmp = arr[startIdx]
        arr[startIdx] = arr[endIdx]
        arr[endIdx] = tmp
        startIdx += 1
        endIdx -= 1

arr = [1,2,3,4,5,6,7]
n = len(arr)
k = 3
reverse_arr(0,k-1,arr)
reverse_arr(k,n-1,arr)
reverse_arr(0,n-1,arr)
print(arr)

