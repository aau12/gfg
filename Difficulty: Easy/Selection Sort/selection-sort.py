class Solution: 
    def selectionSort(self, arr):
        # code here
        n=len(arr)
        for i in range (0,n):
            min_in=i
            for j in range(i+1,n):
                if arr[j]<arr[min_in]:
                    min_in=j
            arr[i],arr[min_in]=arr[min_in],arr[i]
        