arr = [1,2,3,4,5,6,7]
n = len(arr)
target = 6
startIdx = 0
endIdx = n-1
while(startIdx<=endIdx):
    midIdx = (endIdx + startIdx) // 2
    if arr[midIdx] == target:
        print(f"Found at index {midIdx}")
        break
    elif arr[midIdx] < target:
        startIdx = midIdx + 1
    else:
        endIdx = midIdx - 1