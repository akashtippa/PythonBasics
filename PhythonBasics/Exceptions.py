ItemsInCart = 0

if ItemsInCart != 2:
    # raise Exception("Product cart count not matching")

    pass

    assert (ItemsInCart == 0)

# Try Catch == except in python

try:
    with open('Test.txt', 'r') as reader:
        reader.read()
        print("file found")

except:
    print("File not found")

try:
    with open('Test1.txt', 'r') as reader:
            reader.read()
            print("file found")

except Exception as e:
        print(e)
finally:
    print("cleaning up resources")
