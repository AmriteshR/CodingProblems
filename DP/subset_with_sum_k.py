arr = [1, 2, 3, 4]
k = 4
n = len(arr)
dp = [[False for j in range(k+1)] for i in range(n)]
if arr[0] <= k:
    dp[0][arr[0]] = True
for i in range(n):
    dp[i][0] = True
for i in range(1,n):
    for j in range(1,k+1):
        notTaken = dp[i-1][j]
        taken = False
        if arr[i] <= k:
            taken = dp[i-1][j-arr[i]]
        dp[i][j] = taken or notTaken
print(dp[n-1][k])
