# arr = [1, 1, 0, 1, 1, 1]
arr = [1, 0, 1, 1, 0, 1]

count = 0
max_count = 0
for i in range(len(arr)):
    if arr[i] == 1:
        count += 1
    else:
        max_count = max(max_count,count)
        count = 0

max_count = max(max_count,count)
print(max_count)