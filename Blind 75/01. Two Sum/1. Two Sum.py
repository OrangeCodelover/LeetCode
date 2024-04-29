nums = [2,7,11,15]
target = 9

# look through the entire array
for i in range(len(nums)-1):
    for j in range(len(nums)-1):
        if i != j and nums[i]+ nums[j] == target:
            print([i,j])
            break
    # break the nested loop 
    else:
        continue
    break
