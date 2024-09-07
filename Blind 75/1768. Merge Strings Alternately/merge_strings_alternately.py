class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_length= len(word1)
        word2_length= len(word2)
        longer = word1_length
        if word2_length > word1_length:
            longer = word2_length
        merged =""
        for i in range(longer):
            if i < word1_length:
                merged+=(word1[i])
            if i < word2_length:
                merged+=(word2[i])
            i+=1
        return merged

# mergeAlternately("abc","pqr")
# mergeAlternately("ab","pqrs")
# mergeAlternately("abcd","pq")

