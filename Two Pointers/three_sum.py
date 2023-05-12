def three_sum(arr: list, req_sum: int):
    n = len(arr)
    arr.sort()
    for i in range(n):
        startIdx = i+1
        endIdx = n - 1
        while(startIdx < endIdx):
            sum = arr[i] + arr[startIdx] + arr[endIdx]
            if sum == req_sum:
                print(f"Pair found {arr[i],arr[startIdx],arr[endIdx]}")
            if sum > req_sum:
                endIdx -= 1
            else:
                startIdx += 1

# Driver code
arr = [ 1, 4, 45, 6, 10, 8 ]
sum = 22
three_sum(arr, sum)