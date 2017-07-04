#Shared References and In-Place Changes

#there are objects and operations that perform
#in-place object changes—Python’s mutable types, including lists, dictionaries, and sets.

L1 = [2, 3, 4]
L2 = L1

print(L1,L2)

#L1 here is a list containing the objects 2, 3, and 4. Items inside a list are accessed by their
#positions, so L1[0] refers to object 2, the first item in the list L1. Of course, lists are also
#objects in their own right, just like integers and strings.

#To extend it lets say

L1 = 24
print(L1, L2)

#L2 doenst change because the object [2,3,4] still exist no matter if L1 has stopped referencing it
#L2 is still referencing it

#Now lets see the effect on mutating the list.

L1 = [2,3,4]
L2 = L1
L1[0] = 24

print(L1,L2) #SAME!, why because we have mutated the list, wherever it is being referenced
#will show the mutated resutls

#so to change it

L1 = [2,3,4]
L2 = L1.copy()
L1[0] = 24
print(L1,L2)
