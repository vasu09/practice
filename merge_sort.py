class MergeSort:
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums))
        return nums
        
    def mergeSort(self,  nums: List[int], start: int, end: int):
        if end-start>1:
            k = int((start+end)/2)
            
            self.mergeSort(nums,start,k)
            self.mergeSort(nums,k,end)
            self.merge(nums, start, k ,end)
        
    def merge(self,  nums: List[int], start: int, k:int, end: int):
        i = 0
        j = 0
        l_arr = nums[start:k]
        r_arr = nums[k:end]
        
        index = 0
        while i<len(l_arr) and j<len(r_arr):
            if l_arr[i]<r_arr[j]:
                nums[start+index] = l_arr[i]
                i +=1
            else:
                nums[start+index] = r_arr[j]
                j += 1
            index += 1
        
        while i<len(l_arr):
            nums[start+index] = l_arr[i]
            i +=1
            index+=1
        
        while j<len(r_arr):
            nums[start+index] = r_arr[j]
            j +=1
            index+=1
            
