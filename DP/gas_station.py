A = [ 1, 2, 3, 4, 5 ]
B = [ 3, 4, 5, 1, 2 ]
if sum(A) < sum(B):
    print(-1)
total = 0
res = 0
for i in range(len(A)):
    total += (A[i] - B[i])

    if total < 0:
        total = 0
        res = i + 1
print(res)

# circuit = False
# n = len(A)
# for i in range(n):
#     gasLeft = 0
#     count = 0
#     j = i
#     while True:
#         if count == n:
#             break
#         Idx = j%(n)
#         gasLeft += A[Idx]
#         gasReq = B[Idx]
#         if gasLeft < gasReq:
#             circuit = False
#             break
#         gasLeft = gasLeft - B[Idx]
#         j += 1
#         count += 1
#         circuit = True
#     if circuit:
#         print(i)
# else:
#     print(-1)
