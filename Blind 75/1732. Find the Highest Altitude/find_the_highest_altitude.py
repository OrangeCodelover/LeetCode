from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_a = 0
        a = 0
        for i in gain:
            
            a += i
            print("a",a)
            max_a = max(a,max_a)
        
        print("max_a",max_a)
        return max_a
    

if __name__ == "__main__":
    solution = Solution()
    gain = [-5,1,5,0,-7]
    
    solution.largestAltitude(gain)