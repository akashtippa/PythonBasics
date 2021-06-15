# List is data type that allows multiple values and can be different types

values = [1, 2, "test", 4, 5]

print(values[0])
print(values[3])
print(values[-1])

print(values[1:3])

values.insert(3, "python")

print(values)

values.append("End")

print(values)

del values[0]
print(values)