#nesting in dictionaries

#Here, we again have a three-key dictionary at the top (keys “name,” “jobs,” and “age”),
#but the values have become more complex

rec = {'name': {'first':'Bob', 'last':'Smith'},
       'jobs' : ['dev','mgr'],
       'age': 40.5}


print(rec) 

print(rec['name']['first']) #accessing elements

print(rec['jobs'][1]) #accessing list inside dictionary
print(rec['jobs'][-1])

rec['jobs'].append('janitor') #adding a value to the list inside dictionary
rec['name']['middle'] = 'Nawaid' #adding a value to the dictionary inside a dictionary

print(rec)


#Just as importantly, in a lower-level language we would have to be careful to clean up
#all of the object’s space when we no longer need it. In Python, when we lose the last
#reference to the object—by assigning its variable to something else, for example—all
#of the memory space occupied by that object’s structure is automatically cleaned up
#for us:
rec = 0 # Now the object's space is reclaimed
#Technically speaking, Python has a feature known as garbage collection that cleans up
#unused memory as your program runs and frees you from having to manage such details
#in your code. 
