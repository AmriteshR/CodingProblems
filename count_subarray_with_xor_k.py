a = [4, 2, 2, 6, 4]
k = 6
sum_map = {0:1}
i = 1
prefixSum = 0
while (i<len(a)):
    prefixSum = prefixSum ^ a[i]
    req_sum = k ^ prefixSum
    if req_sum in sum_map:
        sum_map[req_sum] += 1
    else:
        sum_map[req_sum] = 1
    i += 1
print(sum_map)