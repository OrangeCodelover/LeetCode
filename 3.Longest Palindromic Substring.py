s = "abc"
n = len(s)
palindromic = ""
# split into half

for i in range(n):
    # Even
    j = 0
    print("i",i)
    while i-j >=0 and i+1+j< n and s[i-j] == s[i+1+j]: 
        if 2 * (j+1) >= len(palindromic):
            # print("first",i-j)
            # print("last",i+1+j +1)
            palindromic = s[i-j:i+1+j +1]
            # print("palindromic_even",palindromic)
        j += 1
    # Odd
    k = 0
    while i-1-k >=0 and i+1+k < n and s[i-1-k] ==s[i+1+k]: 
        if 2*k +3 >= len(palindromic):
            # print("first",i-1-k)
            # print("last",i+1+k +1)
            palindromic = s[i-1-k:i+1+k+1]
            # print("palindromic_odd",palindromic)
        k += 1
if len(palindromic) <=1:
    palindromic = s[0]

# print("length:",len(palindromic))
# print(palindromic)
# print(s[1:3])
