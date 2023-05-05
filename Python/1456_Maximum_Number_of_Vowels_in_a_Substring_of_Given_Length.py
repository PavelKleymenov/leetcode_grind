"""
Given a string s and an integer k, return the maximum number of vowel 
                letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""
class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    ans = 0
    maxi = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for i, c in enumerate(s):
      if c in vowels:
        maxi += 1
      if i >= k and s[i - k] in vowels:
        maxi -= 1
      ans = max(ans, maxi)

    return ans
