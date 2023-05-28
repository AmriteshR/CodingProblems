a = [2, 3, 5, 1, 9]
k = 10

prefixMap = {}
prefixSum = 0
max_length = 0
for i in range(len(a)):

    # calculate the prefix sum till index i:
    prefixSum += a[i]

    # if the sum = k, update the maxLen:
    if prefixSum == k:
        max_length = max(max_length,i+1)

    # calculate the sum of remaining part i.e. x-k:
    reqSum = prefixSum - k

    # Calculate the length and update maxLen:
    if reqSum in prefixMap:
        length = i - prefixMap[reqSum]
        max_length = max(max_length,length)
    
    # Finally, update the map checking the conditions:
    if prefixSum not in prefixMap:
        prefixMap[prefixSum] = i

print(max_length)