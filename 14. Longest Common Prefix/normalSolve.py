'''
Runtime: 36 ms, faster than 49.61% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        end = 0
        if strs == []:
            return ""
        for m in range (len(strs[0])):
            for i in range (len(strs)):
                if m >= len(strs[i]) :
                    end = 1
                    break
                elif (strs[0][m] != strs[i][m]):
                    end = 1
                    break
                # print (strs[i][m])
            if end == 1:
                break
            res += strs[0][m]
        return ("".join(res))
