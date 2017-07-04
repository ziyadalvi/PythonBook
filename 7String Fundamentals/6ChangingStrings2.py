#Changing Strings II

S = 'spammy'
S = S[:3] + 'xx' + S[5:]
print(S)

S = 'spammy'
S = S.replace('mm', 'xx') #its called replace but it doesnt mutatle the string instead makes a copy
print(S)

#replace method is more general than this code implies. It takes as arguments the
#original substring (of any length) and the string (of any length) to replace it with, and
#performs a global search and replace:

print('aa$bb$cc$dd'.replace('$', 'SPAM'))

#####################
#String to List
#####################

#Convert strings into lists if you want to do many changes. It's easier

S = 'zyd'
S = list(S)
print(S)

S[1] = 'i'
S[2] = 'y'
S.append('ad')
print(S)


S = ''.join(S)
S = 'ziyad'.join(['nawaid','alvi'])

print(S)

