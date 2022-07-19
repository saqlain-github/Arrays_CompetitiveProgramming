#Brute O[n2]  O(1)
def maxSubArray_Brute(A):
    n= len(A)
    max_sum = float('-inf')
    for i in  range(n):
        current_sum = A[i]
        max_sum = max(max_sum,A[i])
        for j in range(i+1,n):
            current_sum += A[j]
            max_sum = max(max_sum,current_sum)
                          
    return max_sum

#Kadane's Algo O[n]  O(1)
def maxSubArray(A):
    n = len(A)
    current_sum = 0
    max_sum = float('-inf')
    for i in range(n):
        #1
        current_sum += A[i]
        #2
        current_sum = max(current_sum,A[i])
        #3
        max_sum = max(max_sum,current_sum)
        
    return max_sum

a= [-2,1,-3,4,-1,2,1]
print(maxSubArray_Brute(a))
print(maxSubArray(a))
