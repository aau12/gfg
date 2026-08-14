class Solution:
	def reverseSubArray(self,arr,l,r):
	    l = l - 1
        r = r - 1
        return self.reverse(arr, l, r)

    def reverse(self, arr, l, r):
        if l >= r:
            return arr

        arr[l], arr[r] = arr[r], arr[l]

        return self.reverse(arr, l + 1, r - 1)


		
		