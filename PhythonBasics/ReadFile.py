file = open('Test.txt')

# print(file.read())

# print(file.read(5))  # read specific charcater

# print(file.readline())  # read single line

# print line by line using readLine method

# line = file.readline()
# while line != "":
#   print(line)

#  line = file.readline()

for line in file.readlines():
    print(line)
file.close()
