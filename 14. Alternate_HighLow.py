
# O[n] O[1]
def alternate_lowHigh(A):
     n = len(A)
     for i in range(1,n,2):
        if A[i-1] > A[i]:
            A[i-1] , A[i] = A[i] , A[i-1]
        if i+1 < n and A[i+1] > A[i]:
            A[i+1] , A[i] = A[i] , A[i+1]
     return A
     
print(alternate_lowHigh([1,2,4,5,6,9]))