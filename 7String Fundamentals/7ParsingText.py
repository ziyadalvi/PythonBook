#Parsing Text
line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]

print(col1,col3)

#This technique passes for parsing, as long as the components of your data have
#fixed positions. If instead some sort of delimiter separates the data, you can pull out its
#components by splitting

line = 'aaa bbb ccc'
cols= line.split(' bbb ')
print(cols)

#Seperating by space

cols = line.split(' ')
print(cols)


#Comma-separated text data is part of
#the CSV file format; for more advanced tools on this front, see also the csv module in
#Python’s standard library.
