# a = [2, 3, 5, 1, 9]
# k = 10
a = [1,2,3]
k = 3
n = len(a) # size of the array.

preSumMap = {0:1}
Sum = 0
count = 0
for i in range(n):
    Sum += a[i]

    reqSum = Sum - k
    if reqSum in preSumMap:
        count += preSumMap[reqSum]
    if Sum not in preSumMap:
        preSumMap[Sum] = 1
    else:
        preSumMap[Sum] += 1

print(count)