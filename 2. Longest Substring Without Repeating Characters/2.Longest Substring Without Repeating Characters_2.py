
def lengthOfLongestSubstring(s: str) -> int:
    max = 0
    start_index = 0
    List = ''
    for i, n in enumerate(s):
        if n not in List:
            List = List +n
            print("List:",List)
            if len(List) >= max:
                max = len(List)
        
        else:
            List = List +n
            List = List[1:]
            print(List)
    return max
            



#EX_1
s = "abcabcbb"
a = lengthOfLongestSubstring(s)
print(a)
# 3

#EX_2
s = "bbbbb" 
b = lengthOfLongestSubstring(s)
print(b)
# 1

#EX_3
s = "pwwkew"
c = lengthOfLongestSubstring(s)
print(c)
# 3


#EX_4
s = " "
d = lengthOfLongestSubstring(s)
print(d)
# 1


#EX_5
s = "au"
c = lengthOfLongestSubstring(s)
print(c)
# 2

#EX_6
s = "dvdf"
c = lengthOfLongestSubstring(s)
print(c)
# 3