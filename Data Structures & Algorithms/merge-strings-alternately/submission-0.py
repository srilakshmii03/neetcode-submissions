class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #initialising the variables
        result = ""
        i,j = 0,0
        #appending the alternate characters from both strings
        while i < len(word1) and j < len(word2):
            result+=word1[i]
            result+=word2[j]
            i+=1
            j+=1
        #appending remaining characters from word1
        while i < len(word1):
            result+=word1[i]
            i+=1
        #appending remaining characters from word2
        while j < len(word2):
            result+=word2[j]
            j+=1

        return result