#Python’s core data types is that they support arbitrary nesting—we
#can nest them in any combination, and as deeply as we like. For example, we can have
#a list that contains a dictionary, which contains another list, and so on. One immediate
#application of this feature is to represent matrixes, or “multidimensional arrays” in
#Python. 


M = [[1, 2, 3], # A 3 × 3 matrix, as nested lists
 [4, 5, 6], # Code can span lines if bracketed
 [7, 8, 9]]

print(M[1]) # Get row 2

print(M[1][2]) # Get row 2, then get item 3 within the row

