"""
    You are given a string s, which contains stars *.

    In one operation, you can:

    Choose a star in s.
    Remove the closest non-star character to its left, as well as remove the star itself.
    Return the string after all stars have been removed.

    Note:

    The input will be generated such that the operation is always possible.
    It can be shown that the resulting string will always be unique.
"""

class Solution:
  def removeStars(self, s: str) -> str:

    # Use a stack to store the characters
    ans = []

    # Iterate over every character in a string
    for c in s:

      # Pop one character off the stack every time an asterisk sign is encountered  
      if c == '*':
        ans.pop()

      # Otherwise, push the character onto the stack.  
      else:
        ans.append(c)

    return ''.join(ans)