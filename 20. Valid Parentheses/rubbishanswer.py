'''
Runtime: 980 ms, faster than 5.26% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        y = 0
        if l % 2 != 0 : return 0
        sl = list(s)
        for i in range(l//2):
            n = len(sl)
            for k in range(1,n):
                if 0<(ord(sl[k]) - ord(sl[k-1]) )<= 2 :
                    del sl[k]
                    del sl[k-1]
                    y = 1
                    break
            if y == 0: return 0   
        if len(sl) == 0: return 1
        else: return 0
