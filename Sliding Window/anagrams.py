from collections import Counter
 
# function to check if two strings are
# anagram or not
def list_anagrams(str1, str2):
    k = len(str2)
    for i in range(len(str1)):
        j = i + k
        if(Counter(str1[i:j]) == Counter(str2)):
            print(f"Anagram present {str1[i:j]} at index {i}")
 
# driver code
x = "XYYZXZYZXXYZ"
y = "XYZ"
list_anagrams(x, y)