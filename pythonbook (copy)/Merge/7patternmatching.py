#Pattern Matching

import re
match = re.match('Hello*(.*)world', 'Hello Python Ruby world')

print(match) #if matched then print will work
print(match.group(1)) #portions of the substring matched will be printed here as strings
print(len(match.group(1)))
print(match.groups()) # ,, ,, ,, ,, printed as lists
print(len(match.groups()))
match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match.groups())
print(re.split('[/:]', '/usr/home/lumberjack')) 

print(len(re.split('[/:]', '/usr/home/lumberjack')))
