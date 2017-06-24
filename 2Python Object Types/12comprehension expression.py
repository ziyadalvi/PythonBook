#Comprehensions
#In addition to sequence operations and list methods, Python includes a more advanced
#operation known as a list comprehension expression, which turns out to be a powerful
#way to process structures like our matrix. Suppose, for instance, that we need to extract
#the second column of our sample matrix. It’s easy to grab rows by simple indexing
#because the matrix is stored by rows, but it’s almost as easy to get a column with a list
#comprehension

M = [[1,2,3], #row[1] = 2
    [4,5,6],  #row[1] = 5
    [7,8,9]]  #row[1] = 8

#for row

print(M[1])

#for column
#row is a looping construct here:
col = [row[1] for row in M] #Give me row[1] for each row in matrix M, in a new list.
print(col)

#This matrix structure works for small-scale tasks, but for more serious number crunching you will
#probably want to use one of the numeric extensions to Python, such as the open source NumPy and
#SciPy systems. Such tools can store and process large matrixes much more efficiently than our nested list
#structure.

#add 1 to each item in column 2
print([row[1]+1 for row in M])

#take out odd numbers only
print('\n',[row[1] for row in M if row[1] % 2 == 0])

#comprehensions can iterate over iteratable objects
print('\n',[M[i][i] for i in [0,1,2]]) #diagonal
