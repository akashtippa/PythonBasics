Greeting= "Good Morning"

if Greeting == "Morning":
    print("Condition Matches")
else:
    print("Condition do not match")
# print("if else condition code is complated")

# for loops

obj = [2, 3, 4, 5, 6]
for i in obj:
   print(i*2)
print("------------------------------")
#sum of First Natural numbers 1+2+3+4+5
summation = 0
for j in range(1, 6):
    summation = summation + j
    print(summation)
print("------------------------------")

for k in range(1, 10, 6):
    print(k)

print("-----------skipping First Index-------------------")

for m in range(10):
    print(m)


print("------------While loop condtion------------------")

it = 10
while it > 1:
    if it == 5:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1
print("while loop execution is done")