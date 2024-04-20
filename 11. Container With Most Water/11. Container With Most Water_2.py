from typing import List

def maxArea(height: List[int]) -> int:
    max_Area = 0
    for i, n in enumerate(height):
        while i < len(height):
            if (len(height) - i)*n > max_Area:
                max_Area = (len(height) - i)*n
                print("Max_Area:", max_Area)
            i += 1
    return max_Area

#EX_1
height = [1,8,6,2,5,4,8,3,7]
a = maxArea(height)
print(a)
# 49