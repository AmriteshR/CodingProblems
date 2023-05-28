arr = [1,4,2,5,7,8,9]
n = len(arr)

def calculatePivot(arr,low,high):
    pivot = arr[low]
    i,j = low, high
    while(i<j):
        while(i<=high-1 and arr[i]<=pivot):
            i += 1
        while(j>=low+1 and arr[j]>=pivot):
            j -= 1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j], arr[low]
    return j

def quickSort(arr,low,high):
    if low>=high:
        return
    partition = calculatePivot(arr,low,high)
    quickSort(arr,low,partition-1)
    quickSort(arr,partition+1,high)

quickSort(arr,0,len(arr)-1)
print(arr)