import pprint
pp = pprint.PrettyPrinter(indent=4)
wt = [1, 2, 4, 5]
val = [5, 4, 8, 6]
W = 5
n = len(wt)
dp = [[0 for _ in range(W+1)] for _ in range(n)]

# base cases
for i in range(wt[0],W+1):
    dp[0][i] = val[0]

for i in range(1,n):
    for j in range(W+1):
        notTaken = dp[i-1][j]
        taken = -11111111111111
        if wt[i] <= j:
            taken = val[i] + dp[i-1][j-wt[i]]
        dp[i][j] = max(notTaken,taken)
        pp.pprint(dp)
print(dp[n-1][W])