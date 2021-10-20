s = "abcde"
charset = set()
l = 0
longest = 0

for r in range(len(s)):
    while s[r] in charset:
        charset.remove(s[l])
        l+=1
    charset.add(s[r])
    if len(charset) > longest:
        longest = len(charset)


print(longest)