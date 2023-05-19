arr = [5, 2, 6, 4]
n = len(arr)
d = 3
total = sum(arr)
if (total - d)%2 != 0:
    print('No partition')
    raise AssertionError
target = (total-d) // 2
dp = [[0 for _ in range(target+1)] for i in range(n)]

if arr[0] == 0:
    dp[0][0] = 2
else:
    dp[0][0] = 1
if arr[0] != 0 and arr[0]<=target:
    dp[0][arr[0]] = 1

for i in range(1,n):
    for j in range(1,target+1):
        notTaken = dp[i-1][j]
        taken = 0
        if arr[i] <= j:
            taken = dp[i-1][j-arr[i]]
        dp[i][j] = taken + notTaken

print(dp[n-1][target])