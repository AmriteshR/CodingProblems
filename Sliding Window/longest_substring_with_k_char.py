# Brute Force
def possible_substrings(sample: str):
    n = len(sample)
    for i in range(n):
        for j in range(i+1,n+1):
            print(sample[i:j])

def longest_substring(sample: str,k: int):
    ans = -1
    n = len(sample)
    for i in range(n):
        for j in range(i+1,n+1):
            dist = set(sample[i:j])
            if len(dist) == k:
                sub = sample[i:j]
                ans = max(ans, len(sub))
    print(ans)

# Linear time solution

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
    
def opt_lon_sub(sample: str, window: int):
    ans = -1
    n = len(sample)
    i,j = 0, 0
    sub_map = {}
    while (j<n):
        print("======================================================================================")
        sub_map = update_count(sub_map,True,sample[j])
        if len(sub_map) < window:
            print(f"Required unique characters are less. Status of map - {sub_map}")
            j += 1
        elif len(sub_map) > window:
            while(len(sub_map) > window):
                print("-----------------------------------------------------------------------------")
                print(f"Required unique characters are more. Status of map - {sub_map}, i - {i}, j - {j}, {sample[i]},{sample[i:j+1]}")
                sub_map = update_count(sub_map,False,sample[i])
                i += 1
        else:
            print(f"Required unique characters found. Status of map - {sub_map}")
            ans = max(ans,j-i+1)
            print(f"Answer {ans}")
            j += 1
    print(ans)
if __name__=="__main__":
    # possible_substrings("aabbcc")
    # longest_substring("aabbcc",3)
    # longest_substring("aabacbebebe",3)
    opt_lon_sub("aabadbebebe",3)