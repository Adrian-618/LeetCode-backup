class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l % 2 != 0 : return 0
        sl = list(s)
        for i in range(l//2):
            n = len(sl)
            if 0<(ord(sl[n//2]) - ord(sl[n//2 - 1]) )<= 2 :
                del sl[n//2]  
                del sl[n//2 - 1]
            elif n == 2: break
            elif 0<(ord(sl[n//2 + 1]) - ord(sl[n//2]) )<= 2 :
                del sl[n//2 + 1]  
                del sl[n//2]
            elif 0<(ord(sl[n//2 - 1]) - ord(sl[n//2 - 2]) ) <= 2 :
                del sl[n//2 - 1]  
                del sl[n//2 - 2]
        if len(sl) == 0: return 1
        else: return 0
