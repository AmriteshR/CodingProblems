n = 3
count = 0
dp = [1]
for i in range(1,n+1):
    fs,ss = 0,0
    fs = dp[i-1]
    if i > 1:
        ss = dp[i-2]
    dp.append(fs + ss)
print(dp[n])