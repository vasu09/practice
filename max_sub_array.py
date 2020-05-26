#code
import math
def max_sub_array(arr, low, high):
#     print(low, high)
    if low==high:
        if arr[low]<0:
            return low, high,-math.inf
        return low, high, arr[low]
    
    mid = int((low+high)/2)
    l_low, l_high, l_sum =  max_sub_array(arr, low, mid)
    r_low, r_high, r_sum =  max_sub_array(arr, mid+1, high)
    c_low, c_high, c_sum =  max_cross_sum(arr, low, mid, high)
    if l_sum>r_sum:
        if l_sum>c_sum:
            return l_low, l_high, l_sum
        else:
            return c_low, c_high, c_sum
    else:
        if r_sum>c_sum:
            return r_low, r_high, r_sum
        else:
            return c_low, c_high, c_sum
    
def max_cross_sum(arr, low, mid, high):
#     print(low, mid, high)
    i = low
    l_sum = -math.inf
    l_index = 0
    s=0
    for i in range(mid,low-1,-1):
        if arr[i]<0:
            break
        s +=arr[i]
        if s>l_sum:
            l_sum = s
            l_index = i
    i = mid
    r_sum = -math.inf
    r_index = mid
    s=0
    for i in range(mid+1,high+1):
        if arr[i]<0:
            break
        s += arr[i]
        if s>r_sum:
            r_sum = s
            r_index = i
#     print('u ',l_index,r_index,l_sum+r_sum)
    return l_index,r_index,l_sum+r_sum        


if __name__=='__main__':
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        l,r,_ = max_sub_array(arr,0,n-1)
        for i in range(l,r+1):
            print(arr[i],end=" ")
        print()
        
        
