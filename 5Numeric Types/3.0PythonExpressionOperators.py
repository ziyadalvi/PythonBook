#Python Expression Operators

#Mixed operators follow operator precedence
A = 1
B = 2
C = 3
D = 4

X = A * B + C * D
print(X)


#So, how does Python know which operation to perform first? The answer to this question
#lies in operator precedence. When you write an expression with more than one
#operator, Python groups its parts according to what are called precedence rules, and
#this grouping determines the order in which the expression’s parts are computed.
#Table 5-2 is ordered by operator precedence:
#• Operators lower in the table have higher precedence, and so bind more tightly in
#mixed expressions.
#• Operators in the same row in Table 5-2 generally group from left to right when
#combined (except for exponentiation, which groups right to left, and comparisons,
#which chain left to right).


#yield x Generator function send protocol
#lambda args: expression Anonymous function generation
#x if y else z Ternary selection (x is evaluated only if y is true)
#x or y Logical OR (y is evaluated only if x is false)
#x and y Logical AND (y is evaluated only if x is true)
#not x Logical negation
#x in y, x not in y Membership (iterables, sets)
#x is y, x is not y Object identity tests
#x < y, x <= y, x > y, x >= y
#x == y, x != y
#Magnitude comparison, set subset and superset;
#Value equality operators
#x | y Bitwise OR, set union
#x ^ y Bitwise XOR, set symmetric difference
#x & y Bitwise AND, set intersection
#x << y, x >> y Shift x left or right by y bits
#x + y
#x – y
#Addition, concatenation;
#Subtraction, set difference
#x * y
#x % y
#x / y, x // y
#Multiplication, repetition;
#Remainder, format;
#Division: true and floor
#−x, +x Negation, identity
˜#x Bitwise NOT (inversion)
#x ** y Power (exponentiation)
#x[i] Indexing (sequence, mapping, others)
#x[i:j:k] Slicing
#x(...) Call (function, method, class, other callable)
#x.attr Attribute reference
#(...) Tuple, expression, generator expression
#[...] List, list comprehension
#{...} Dictionary, set, set and dictionary comprehensions


