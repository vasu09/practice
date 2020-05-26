#We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

#The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

#The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

#Return true if and only if the number of global inversions is equal to the number of local inversions.


class IdealPermutation:
    def isIdealPermutation(self, A: List[int]) -> bool:
        #by contradiction
        #if ideal premutation: max(A)<A[i+2] at any point
        max_ele = 0
        for i in range(0, len(A)-2):
            max_ele = max(max_ele, A[i])
            if max_ele>A[i+2]:
                return False
        return True
