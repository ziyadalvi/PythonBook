import threenames # Grab the whole module: it runs here
print(threenames) # Access its attributes
print(threenames.a, threenames.c)

from threenames import a, b, c # Copy multiple names out (can cause variable clashes)
print(b,c) 