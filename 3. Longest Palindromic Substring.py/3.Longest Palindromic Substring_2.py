
def longestPalindrome(s: str) -> int:
    Palindromic =''
    for i in range(0,len(s)):
        k = 0
        # even number
        while  (i-k >=0 and i+k+1 < len(s)) and s[i-k] == s[i+1+k]:
            if len(s[(i-k):(i+1+k+1)]) > len(Palindromic):
                Palindromic = s[(i-k):(i+1+k+1)]
                #print(Palindromic)
            k = k+1
        # odd number
        while  (i-k >=0 and i+k < len(s)) and s[i-k] == s[i+k]:
            if len(s[(i-k):(i+k+1)]) > len(Palindromic):
                Palindromic = s[(i-k):(i+k+1)]
                #print(Palindromic)
            k = k+1

    return Palindromic  


#EX_1
s = "babad"
a = longestPalindrome(s)
print(a)
# bab

#EX_2
s = "cbbd" 
b = longestPalindrome(s)
print(b)
# bb