def pair_sum(arr: list, sum: int):
    startIdx = 0
    endIdx = len(arr) - 1
    while(startIdx < endIdx):
        n = arr[startIdx] + arr[endIdx]
        if n == sum:
            print(f"Pair found at {startIdx} and {endIdx}")
            # startIdx += 1
            # endIdx -= 1
        if n > sum:
                endIdx -= 1
        else:
            startIdx += 1


# Driver code
arr = [2, 3, 5, 8, 9, 10, 11]
val = 17
pair_sum(arr, val)