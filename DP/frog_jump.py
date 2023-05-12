"""
Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.
"""
heights = [30, 10, 60, 10, 60, 50]
n = len(heights)
dp = [-1] * n
dp[0] = 0
for idx in range(1,n):
    step2 = float('inf')
    step1 = dp[idx - 1] + abs(heights[idx]-heights[idx-1])
    if idx > 1:
        step2 = dp[idx - 2] + abs(heights[idx] - heights[idx-2])
    dp[idx] = min(step1,step2) # type: ignore
print(dp[n-1])