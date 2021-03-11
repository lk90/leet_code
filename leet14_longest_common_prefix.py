"""

"""

"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) < 1:
            return ""
        prefix = min(strs, key=len)
        for i, j in enumerate(prefix):
            for common in strs:
                if common[i] != j:
                    return prefix[:i]
        return prefix


z = Solution()
strs = ["flower", "flow", "flight"]
print(z.longestCommonPrefix(strs))


"""
strs = ["flower", "flow", "flight"]
str1 = min(strs, key=len)
for i, x in enumerate(str1):
    print(i, x)
    #for common in strs:
        #print(common)
        #if common[i] != x:
            #print(str1[:i])
# print(str1)
# x = len(i)
# print(min(strs))
# print(max(strs))
# print(sorted(strs))
# print(z.longestCommonPrefix(strs))
