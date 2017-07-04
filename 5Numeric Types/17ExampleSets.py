#sets are also convenient when you’re dealing with large data sets (database
#query results, for example)—the intersection of two sets contains objects common to
#both categories, and the union contains all items in either set. To illustrate, here’s a
#somewhat more realistic example of set operations at work, applied to lists of people
#in a hypothetical company

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}

'bob' in engineers # Is bob an engineer?
#True

engineers & managers # Who is both engineer and manager?
#{'sue'}

engineers | managers # All people in either category
#{'bob', 'tom', 'sue', 'vic', 'ann'}

engineers - managers # Engineers who are not managers
#{'vic', 'ann', 'bob'}

managers - engineers # Managers who are not engineers
#{'tom'}

engineers > managers # Are all managers engineers? (superset)
#False

{'bob', 'sue'} < engineers # Are both engineers? (subset)
#True

(managers | engineers) > managers # All people is a superset of managers
#True

managers ^ engineers # Who is in one but not both?
#{'tom', 'vic', 'ann', 'bob'}

(managers | engineers) - (managers ^ engineers) # Intersection!
#{'sue'}
