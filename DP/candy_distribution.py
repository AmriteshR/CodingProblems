A =[1,2,3]
n = len(A)
arr = [1] * n
for i in range(1,n):
    if A[i-1] < A[i]:
        arr[i] = arr[i-1] + 1
for i in range(n-2,-1,-1):
    if A[i] > A[i+1] and arr[i] <= arr[i+1]:
        arr[i] = arr[i+1] + 1
print(sum(arr))