arr = [4,5,6,7,0,1,2]
target = 2
n = len(arr)
start, end = 0, n-1
while(start<=end):
    mid = (start + end) // 2
    if arr[mid] == target:
        print(f"Target found at index {mid}")
        break

    # Left half is sorted
    if arr[start] <= arr[mid]:
        # Target lies in between start and mid
        if arr[start]<=target and arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    
    # Right half is sorted
    else:
        if arr[mid]<=target and arr[end]>=target:
            start = mid + 1
        else:
            end = mid - 1