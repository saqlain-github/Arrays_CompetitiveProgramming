# Smaller value appears before larger value

#Brute Force
#On2 O1
def maxDiff_Brute(A):
    max_diff = 0
    n = len(A)
    for i in range(n):
        for j in range(i+1,n):
            if A[j] > A[i]:
                max_diff = max(max_diff,A[j]-A[i])
    return max_diff


#O(n) O(1)
def maxDiff(A):
    n = len(A)
    maxDiff = 0
    max_value = 0
    for i in range(n-1,-1,-1):
        max_value = max(max_value,A[i])
        maxDiff = max(maxDiff,max_value-A[i])
        
    return maxDiff

a = [2,7,9,5,1,3,5]
print(maxDiff_Brute(a))
print(maxDiff(a))