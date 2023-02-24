# Given two strings s and t, return true if (t) is an 
# anagram of (s), and false otherwise.

# An anagram is a word/phrase formed by rearranging the letters
# of a different word of phrase, typically using all the original
# letters exactly once

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ''' Check if the lengths of both input strings
        are equal'''
        if len(s) is not len(t):
            return False

        ''' create two dictionaries to store the letters we will
        traverse through'''
        countS, countT = {}, {}

        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

solution = Solution()

test1 = solution.isAnagram(s = "anagram", t = "nagaram")
test2 = solution.isAnagram(s="rat", t="car")
print(test1, test2)
