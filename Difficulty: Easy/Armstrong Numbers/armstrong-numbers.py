class Solution:
    def armstrongNumber (self, n):
        num=n
        nod=len(str(n))
        self=0
        while num>0:
            ld=num%10
            self = self+ld**nod
            num//=10
        return self==n
        