height= [1,8,6,2,5,4,8,3,7]
max_water = 0
# for i in range(len(height)-1):
#     for j in range(len(height)-i-1):
#         print(i,j+i+1)
#         max_water = max(max_water, (j+1)*min(height[i], height[j+1+i]))

# print(max_water)
l = 0
r = len(height)-1
while l != r:
    
    if (r-l) * min(height[r],height[l]) > max_water:
        max_water = (r-l) * min(height[r],height[l])
        print("max water:",max_water)

    if height[l] < height[r]:
        l +=1
        print("l",l)
    else:
        r -=1
        print("r",r)

print(max_water)