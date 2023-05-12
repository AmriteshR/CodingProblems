def four_sum(arr, req_sum):
    n = len(arr)
    arr.sort()
    for i in range(n):
        for j in range(i+1,n):
            startIdx =  j + 1
            endIdx = n - 1
            while(startIdx < endIdx):
                sum = arr[i] + arr[j] + arr[startIdx] + arr[endIdx]
                if sum == req_sum:
                    print(f"Possible quad found - {arr[i]} + {arr[j]} + {arr[startIdx]} + {arr[endIdx]}")
                if sum > req_sum:
                    endIdx -= 1
                else:
                    startIdx += 1

# Driver code
arr = [ 1, 4, 45, 6, 10, 8 ]
sum = 23
four_sum(arr, sum)