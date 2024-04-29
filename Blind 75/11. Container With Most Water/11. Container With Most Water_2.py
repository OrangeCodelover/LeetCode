from typing import List

def maxArea(height: List[int]) -> int:
    max_Area = 0
    i = 0
    j = len(height)-1
    while i<=j:
        if (j-i)*(min(height[i],height[j])) > max_Area:
            max_Area = (j-i)*(min(height[i],height[j]))

        if height[i] > height[j]:
            j -= 1
        else:
            i += 1

    return max_Area

#EX_1
height = [1,8,6,2,5,4,8,3,7]
a = maxArea(height)
print(a)
# 49

#EX_2
height = [1,1]
a = maxArea(height)
print(a)
# 1