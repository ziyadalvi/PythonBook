#Unicode Strings
#Characters in the Japanese and Russian alphabets, for
#example, are outside the ASCII set. Such non-ASCII text can show up in web pages,
#emails, GUIs, JSON, XML, or elsewhere. When it does, handling it well requires Unicode
#support. Python has such support built in, but the form of its Unicode support
#varies per Python line, and is one of their most prominent differences.
#In Python 3.X, the normal str string handles Unicode text (including ASCII, which is
#just a simple kind of Unicode); a distinct bytes string type represents raw byte values
#(including media and encoded text)


print('spam') # Characters may be 1, 2, or 4 bytes in memory
print('spam'.encode('utf8')) # Encoded to 4 bytes in UTF-8 in files
print('spam'.encode('utf16')) # But encoded to 10 bytes in UTF-16


print(b'a\x01c') #bytearray
print('sp\xc4\u00c4\U000000c4m') #non-ASCII characters with \x hexadecimal and
#short \u and long \U Unicode escapes,

print('\u00A3')
print('\u00A3'.encode('latin1'))
print(b'\xA3'.decode('latin1'))


