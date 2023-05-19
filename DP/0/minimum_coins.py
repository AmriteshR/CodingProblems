# Coins can be repeated
arr = [1, 2, 3]
T = 7
n = len(arr)
dp = [[0 for _ in range(T+1)] for _ in range(n)]

# Base cases
for i in range(T + 1):
    if i % arr[0] == 0:
        dp[0][i] = i // arr[0]
    else:
        dp[0][i] = int(1e9)

for i in range(1,n):
    for j in range(1,T+1):
        notTaken = dp[i-1][j]
        taken = int(1e9)
        if arr[i] <= j:
            taken = 1 + dp[i-1][j-arr[i]]
        dp[i][j] = min(notTaken,taken)
print(dp[n-1][T])
