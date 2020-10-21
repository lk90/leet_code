"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store 
integers within the 32-bit signed integer range: [−231,  231 − 1]. For
the purpose of this problem, assume that your function returns 0 when 
the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x > 0:
            pop = x % 10
            rev = rev * 10 + pop
            x = int(x / 10)
        rev = rev * sign
        if rev < -2147483648 or rev > 2147483647:
            return 0
        return int(rev)
