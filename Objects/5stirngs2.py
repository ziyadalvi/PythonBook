#Other Ways to code strings
#Python provides a variety of ways to code strings, for e.g special chars can be represented as backslash escape sequences '\xNN' hexadecimal escape notation, unless they represent printable chars

S = 'A\nB\tC' # Each stands for just one character
print(S)
print(len(S))

S = 'A\0B\0C' # \0, a binary zero byte, does not terminate string
print(S)
print(len(S))

#single and double quotes mean the same. but allows other type of quote to be embedded within an escape. It allows multiline string literals enclosed in triple quotes. when this form is used the lines are concatinated together

msg = """
aaa aaa aaa aaa
bbb'''bbbbbbbbbbbb""bbbbbb'bbbb
cccccccccccccccccc
"""

print(msg)

