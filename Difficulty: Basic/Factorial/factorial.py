class Solution:
    def factorial(self, n: int) -> int:
        # code here
        if n==0:
                return 1
        if n==1:
                return 1                                                                                                                                                                                                                         
        self=1
        for i in range (2,n+1):
            
            
            self=i*self
        return self
            