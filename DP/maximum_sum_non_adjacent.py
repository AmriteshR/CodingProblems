arr = [2, 1, 4, 9]
n = len(arr)
dp = [-1] * n
dp[0] = arr[0]
for i in range(1,n):
    rsum = -1
    lsum = dp[i-1] + 0
    if i > 1:
        rsum = dp[i-2] + arr[i]
    dp [i] = max(lsum,rsum)
print(dp[n-1])