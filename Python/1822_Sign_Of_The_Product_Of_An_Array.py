"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""
class Solution:
    def arraySign(self, nums: List[int]) -> int:

        # Create a boilerplate sign
        sign = 1

        # Iterate over an array
        for num in nums:

            # Return zero if there is at least one zero within an array
            if num == 0:
                return 0

            # Return negative one if there is at least one negative element in the array
            elif num < 0:
                sign = - sign
                
        # Else return the boilerplate value
        return sign