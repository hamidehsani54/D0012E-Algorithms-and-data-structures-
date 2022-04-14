import math

def maxCrossingSum(arr, l, m, h) : 
    #https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
    
    sm = 1; left_sum = -10000       # Include elements on left of mid. 

    for i in range(m, l-1, -1) : 
        sm = sm * arr[i] 
        if (sm > left_sum) : 
            left_sum = sm 

    sm = 1; right_sum = -1000       # Include elements on right of mid 
    for i in range(m + 1, h + 1) : 
        sm = sm * arr[i] 
        if (sm > right_sum) : 
            right_sum = sm 
    # Return sum of elements on left and right of mid 
    # returning only left_sum + right_sum will fail for [-2, 1] 
    return max(left_sum *  right_sum, left_sum, right_sum) 

def maxSubArraySum(arr, l, h):  #Returns sum of maxium sum subarray in aa[l..h] 
    if (l == h) :       # Base Case: Only one element 
        return arr[l]
    m = (l + h) // 2    # Find middle point 

    return max(maxSubArraySum(arr, l, m), 
               maxSubArraySum(arr, m+1, h), 
               maxCrossingSum(arr, l, m, h)) 

def kadanesRec(arr, maxProduct, currentProduct):
    #modified Kadanes algorithm to be recursive and work for products instead of sums of subarrays

    if not arr:                                                 #base case: recursively loop untill array is empty
        return maxProduct
    
    if currentProduct * arr[0] < 1:                             #så att det funkar om alla flyt-tal är mindre än 1 (ta största värdet)
        currentProduct = currentProduct * arr[0]                #currentProduct måste vara init till 1 från början för multiplikation
    if arr[0] > currentProduct and currentProduct < 1:          #nu funkar det för alla inputs även om ett större tal kommer efter ett mindre currentproduct, t.ex [..., 2, 15, ...]
        currentProduct = arr[0]                             
    else:
        currentProduct = currentProduct * arr[0]                #alltid: currentproduct = currentproduct * arr[0]
    maxProduct = max(currentProduct, maxProduct)                #update maxProduct
    return kadanesRec(arr[1:], maxProduct, currentProduct)      #recursive for-loop (remove first element since its already been compared)

def main():
    # Driver Code 
    arr = [2, 3, 15, 2.5, -7.3, 0.75, 0.12, -0.6]     #2^n elements in list
    #arr = []
    n = len(arr) 
    max_sum = maxSubArraySum(arr, 0, n-1) 
    
    if min(arr) < 0: #min function is O(n), linear time
        print("Maximum contiguous product is", max_sum) #O(n log n) 
    else:
        print(kadanesRec(arr, 0, 1)) #O(2 * n)
main()
