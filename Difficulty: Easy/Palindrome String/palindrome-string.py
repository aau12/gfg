class Solution:
    def isPalindrome(self, s):
        return self.func(s,0,len(s)-1)
       
    def func(self,s,left,right):
           
        if left >= right :
            return True 
        if s[left] != s[right]:
            return False 
            
        return self.func(s,left+1,right-1)