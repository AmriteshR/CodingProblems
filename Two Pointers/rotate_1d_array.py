# Space complexity high
# def rotate(arr,k):
#     startIdx = len(arr) - k
#     print(arr[startIdx:] + arr[:startIdx-1])

def aux_rotate(arr,startIdx,endIdx):
    while(startIdx<endIdx):
        tmp = arr[startIdx]
        arr[startIdx] = arr[endIdx]
        arr[endIdx] = tmp
        startIdx += 1
        endIdx -= 1

# Rotate left
def opt_rotate(arr, k):
    n = len(arr)
    k = k%n
    aux_rotate(arr,k,n-1)
    aux_rotate(arr,0,k-1)
    aux_rotate(arr,0,n-1)
    print(arr)

# Rotate right
def opt_rotate(arr, k):
    n = len(arr)
    k = k%n
    aux_rotate(arr,n-k+1,n-1)
    aux_rotate(arr,0,n-1-k)
    aux_rotate(arr,0,n-1)
    print(arr)
arr = [1,2,3,4,5,6,7]
k = 1
opt_rotate(arr,k)