#Type-Specific Methods
#Other than generic sequence operations, strings also have operations
#all their own, available as methods- funcitons that are attached to
#and act upon a specific object whic are triggered with a call expression

#re.g find

S = 'ziyad'
print(S.find('ya'))
print(S)

#replace
print(S.replace('d', 'dAlvi'))

#split
line = "aaa,bbb,ccc,dd"
print(line)
print(line.split(","))

#upper
print(S.upper)

#isalpha?
print(S.isalpha())

#remove whitespace chars on right
T = 'aa,bb,cc,\n'
print(T.rstrip())

print(T.rstrip().split(','))
