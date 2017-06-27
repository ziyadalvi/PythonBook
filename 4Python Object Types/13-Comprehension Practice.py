matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#single column operations
col2 = [row[1] for row in matrix]
print(col2)
#single column operations
evensincol1 = [row[1] for row in matrix if row[1] %2 == 0]
print(evensincol1)
#iterations
iterate = [matrix[i] for i in [0,1,2]]
print(iterate)
#iterations
diagonal = [matrix[i][i] for i in [0,1,2]]
print(diagonal)
#assigning values
col2 = [row[1]+1 for row in matrix]
print(col2)
#assigning values
doubles = [c * 2 for c in 'spam']
print(doubles)
