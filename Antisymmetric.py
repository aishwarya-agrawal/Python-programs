def antisymmetric(A):
    n=len(A)
    i=0
    j=0
    while i<n:
        j=0
        if n == len(A[i]):
            while j<len(A[i]):
                if A[i][j]== -A[j][i]:
                    j=j+1
                    continue
                else:
                    return False
            i=i+1
        else:
            return False
    return True
    #Write your code here


# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
