#Kadane's Algo O[n]  O(n) or O(1)
def maxSubArray(A):
    n = len(A)
    current_sum = 0
    max_sum = float('-inf')
    start = 0
    end = 0
    temp = 0
    for i in range(n):
        #1
        current_sum += A[i]
        #2
        if current_sum < A[i]:
            current_sum  = A[i]
            temp = i
        #3
        #max_sum = max(max_sum,current_sum)
        if max_sum < current_sum:
            max_sum = current_sum
            start = temp
            end = i
           
    return A[start:end+1], max_sum

a= [-5,4,-1,2,1]
print(maxSubArray(a))