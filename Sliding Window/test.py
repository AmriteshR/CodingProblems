def update_count(dmap: dict,increase: bool, key: str):
    if increase:
        if key in dmap:
            print(f"Increasing count of {key}")
            dmap[key] += 1
        else:
            print(f"Inserting count of {key} with 1")
            dmap[key] = 1
    else:
        print(f"Decreasing count of {key}")
        dmap[key] -= 1
        if dmap[key] == 0:
            print(f"Removing {key} from dict")
            del dmap[key]
    return dmap

def opt_lon_sub(sample, window):
    startIdx = 0
    endIdx = 0
    cmap = {}
    ans = -1
    while(endIdx < len(sample)):
        cmap = update_count(cmap,True,sample[endIdx])
        if len(cmap) == window:
            ans = max(ans,endIdx-startIdx+1)
            endIdx += 1
        elif len(cmap) > window:
            while(len(cmap) > window):
                cmap = update_count(cmap,False,sample[startIdx])
                startIdx += 1
        else:
            endIdx += 1
    print(ans)

# Driver code
opt_lon_sub("aabadbebebe",3)