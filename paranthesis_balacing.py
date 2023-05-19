s = "()[{}()]"
st = []
for i in range(len(s)):
    if s[i] == "(" or s[i] == "{" or s[i] == "[":
        st.append(s[i])
    else:
        ch = st[-1]
        if (s[i] == ')' and ch == '(') or (s[i] == '}' and ch == '{') or (s[i] == ']' and ch == '['):
            st.pop()
            continue
        else:
            break
print(len(st)==0)