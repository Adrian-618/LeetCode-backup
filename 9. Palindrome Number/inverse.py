'''
Runtime: 56 ms, faster than 80.56% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(abs(x))
        inv = int(temp[::-1])
        #print (inv)
        return (inv == x and 1 or 0)
