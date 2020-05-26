class Inversion:
    def isIdealPermutation(self, A: List[int]) -> bool:
        li = self.find_local_inversion(A)
        gi = self.find_global_inversion(A, 0, len(A),0)
        
        return li==gi
    
    def find_local_inversion(self, A: List[int]) -> int:
        li =0
        for i in range(0, len(A)-1):
            if A[i]>A[i+1]:
                li+=1   
        return li
    
    def find_global_inversion(self, A: List[int], start: int, end: int, inversion:int) -> int:
        if end-start>1:
            k = int((start+end)/2)
            inv1 = self.find_global_inversion(A, start, k,inversion)
            inv2 = self.find_global_inversion(A, k, end,inversion)
            inversion += self.merge(A, start, k , end)+inv1+inv2
        return inversion
            
    
    def merge(self, A: List[int], start: int, k:int, end: int) -> int:
        i = j = index = 0
        l_arr = A[start:k]
        r_arr = A[k:end]
        count = 0
        
        while i<len(l_arr) and j<len(r_arr):
            if l_arr[i]<=r_arr[j]:
                A[start+index] = l_arr[i]
                i+=1
            else:
                count += len(l_arr)-i
                A[start+index] = r_arr[j]
                j+=1
            index+=1
        
        while i<len(l_arr):
            A[start+index] = l_arr[i]
            i+=1
            index+=1
        while j<len(r_arr):
            A[start+index] = r_arr[j]
            j+=1
            index+=1
     
        return count
