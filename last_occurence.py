arr = [3,4,13,13,13,20,40]
target = 13
result = -1
n = len(arr)

start, end = 0, n-1
while(start<=end):
    mid = (start+end) // 2
    if arr[mid] == target:
        result = mid
        start = mid + 1
    elif arr[mid] < target:
        start = start + 1
    else:
        end = mid - 1

print(result)