# Optimal Solution
def optimalsubarraySum(nums: list[int], k: int) -> int:
    sum_map = {0:1}
    i = 0
    prefixSum = 0
    while (i<len(nums)):
        prefixSum = prefixSum + nums[i]
        req_sum = k - prefixSum
        if req_sum in sum_map:
            sum_map[req_sum] += 1
        else:
            sum_map[req_sum] = 1
        i += 1
    return max(sum_map.values())

# Brute force
def subarraySum(nums: list[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i+1,len(nums)):
            sum = sum + nums[i] + nums[j]
            if sum == k:
                count += 1
    return count
# Driver code
nums = [1,2,3]
k = 3
print(optimalsubarraySum(nums,k))