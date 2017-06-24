#Sortin Keys: for Loops
#Dictionaries are not sequences the dont maintain any order
#To sort them or put them in order we can use 'keys' method sort that
#with the list 'sort method' and then step through the result with Python for loop

D = {'b':2, 'a':1, 'c':3}
print(D)

#Three step process using keys() and sort()
###########################################

ks = list(D.keys()) #grab the list of keys with keys, list them down (these are unordered)
print(ks) 
ks.sort()
print(ks) #sorted keys

#for key=0; i<=len(ks); key++
for key in ks: #iterate through sorted keys
#A user-defined loop variable (key, here)
#is used to reference the current item each time through.
    print(key, '=>', D[key])


#Sorted function => 1 step process
##################################

for key in sorted(D):
    print(key, '=>', D[key])

#The for loop, and its more general colleague the while loop, are the main ways we code
#repetitive tasks as statements in our scripts. Really, though, the for loop, like its relative
#the list comprehension introduced earlier, is a sequence operation. It works on any
#object that is a sequence and, like the list comprehension, even on some things that are
#not. Here, for example, it is stepping across the characters in a string, printing the
#uppercase version of each as it goes

for c in 'Spam':
    print(c.upper())

for x in [4,3,2,1]:
    print('Spam'*x)

x = 4
while x > 0:
    print('Spam'*x)
    x -= 1
