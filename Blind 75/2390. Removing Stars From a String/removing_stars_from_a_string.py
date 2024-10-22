class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        s = "".join(stack)
        # print ('S:', s)
        return s

if __name__ == "__main__":
    solution = Solution()
    # s = "leet**cod*e"    
    s = "erase*****"

    solution.removeStars(s)