#Iteration and optimization

#an object is iterable if it is either a physically stored sequence in memory,
#or and object that generates one item at a time in context of an iteration operation

#they are iterable because they support iteration protoc

#they respond to iter call with an object and advances in response to next calls

#The generator comprehension expression we saw earlier is such an object.: its values
#aren’t stored in memory all at once, but are produced as requested, usually by iteration
#tools

squares = [ x ** 2 for x in [1,2,3,4,5]]
print(squares)

squares = []
for x in [1,2,3,4,5]:
    squares.append(x ** 2)

print(squares)
