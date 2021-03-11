"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(','[','{']
        closed_brackets = [')',']','}']
        brackets={')':'(',']':'[','}':'{'}
        lst =[]
        for i in s:
            if i in open_brackets:
                lst.append(i)
            elif i in closed_brackets:
                if len(lst) == 0:
                    return False
                if lst[-1] == brackets[i]:
                    lst.pop()
                else:
                    return False
        if len(lst)==0:
            return True
        else:
            return False