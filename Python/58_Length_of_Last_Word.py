"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        """Split the string so each word can be treated as a separate entity,
        then type cast the string into a list and calculate the length of the last word by indexing it 
                                and applying len()"""
        return len(list(s.split())[-1])