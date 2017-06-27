#The comprehension expressions can also be used to collect values if wrapped in a nested collection.
#The folling illustrates using range (a buit-in that generates successive integers
#and requires a surrounding list to display its values

count = list(range(4))
print(count) #count till 4 put it in the list

count = list(range(-100,1000,25))
print(count) #count from -100 to 1000 with 25 gap

multiples = [[x ** 2, x ** 3] for x in range(4)]
print(multiples) #comprehension expression for makring a matrix with column 1 to have
# powers of 2 and col2 having powers of 3 for range 1,2,3,4

timesmatrix = [[x*2,x*3,x*4] for x in range(-10,10) if x > 0]
print(timesmatrix) #comprehension expression for making a matrix with column 1,2,3 for multiples
#of 1,2 and 3 for range -10 till 10 but filtering out the range with positive values

#enlosing a comprehension in parenthesis can also be used to create generators
#that produce results on demand
M = [[1,2,4,5,6,7,8,9,10],
     [12,2,4,5,6,7,8,9,10],
     [13,2,4,5,6,7,8,9,10],
     ] 

G = (sum(row) for row in M) #comprehension exp for summing each row in M
print(next(G)) #creating generators for list for each row it is called
print(next(G))
print(next(G))
G = map(sum,M) # Map sum over items in M just like comprehension exp
print(next(G))
print(next(G))
print(next(G))
#the map built-in can do similar work, by generating the results of running items
#through a function, one at a time and on request. Like range, wrapping it in list
#forces it to return all values.

print(list(sum(row) for row in M))
print(list(map(sum,M)))

#comprehension syntax can also be used to create sets and
#dictionaries
print({sum(row) for row in M}) # Create a set of row sums

print({i : sum(M[i]) for i in range(3)}) # Creates key/value table of row sums

#In fact, lists, sets, dictionaries, and generators can all be built with comprehensions 
print([ord(x) for x in 'spaam']) # List of character ordinals

print({ord(x) for x in 'spaam'}) # Sets remove duplicates

print({x: ord(x) for x in 'spaam'}) # Dictionary keys are unique

print((ord(x) for x in 'spaam')) # Generator of values


