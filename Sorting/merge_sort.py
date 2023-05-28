arr = [1,4,2,5,7,8,9]
n = len(arr)

def merge(arr,low,mid,high):
    tmp = []
    l = low
    r = mid+1
    while(l<=mid and r<=high):
        if arr[l] <= arr[r]:
            tmp.append(arr[l])
            l += 1
        else:
            tmp.append(arr[r])
            r += 1

    while(l<=mid):
        tmp.append(arr[l])
        l+=1
    while(r<=high):
        tmp.append(arr[r])
        r += 1
    for i in range(low,high+1):
        arr[i] = tmp[i-low]

def mergeSort(arr,low,high):
    if low>=high:
        return
    mid = (low+high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)

mergeSort(arr,0,len(arr)-1)
print(arr)