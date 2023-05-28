arr = [1,2,4,5]

for i in range(1,len(arr)):
    if i not in arr:
        print(i)
        break

# Summation method
n = len(arr) + 1
s1 = (n*(n+1)) // 2
s2 = sum(arr)
print(s1 - s2)