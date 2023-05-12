def longest_substring(s: str):
    char_set = set()
    max_len, start, j = 0, 0, 0
    while(j<len(s)):
        while s[j] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[j])
        max_len = max(max_len,j-start+1)
        j += 1
    return max_len
# driver code
sample = "bbbbb"
print(longest_substring(sample))