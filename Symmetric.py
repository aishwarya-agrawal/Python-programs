def symmetric(list):
    n=len(list)
    i=0
    while i<n:
        j=0
        if(n==len(list[i])):
            while j<len(list[i]):
                if list[j][i]==list[i][j]:
                    j=j+1
                    continue
                else:
                    return False
        else:
            return False
        i=i+1
    return True
    # Your code here

print symmetric([[1, 2, 3],[2, 3, 4],[3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],["dog", "dog", "fish"],["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],["dog", "dog", "dog"],["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],[2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],[2, 3, 4, 5],[3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3], [2,3,1]])
#>>> False