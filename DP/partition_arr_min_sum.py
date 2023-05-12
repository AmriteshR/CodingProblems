def minSubsetSumDifference(arr, n):
    totSum = 0

    for i in range(n):
        totSum += arr[i]

    dp = [[False for i in range(totSum + 1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = True

    if arr[0] <= totSum:
        dp[0][totSum] = True

    for ind in range(1, n):
        for target in range(1, totSum + 1):
            notTaken = dp[ind - 1][target]

            taken = False
            if arr[ind] <= target:
                taken = dp[ind - 1][target - arr[ind]]

            dp[ind][target] = notTaken or taken

    mini = int(1e9)
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)
    
    return mini

def main():
    arr = [36,-36]
    n = len(arr)

    print("The minimum absolute difference is:", minSubsetSumDifference(arr, n))

if __name__ == '__main__':
    main()