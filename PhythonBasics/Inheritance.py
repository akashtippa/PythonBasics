from oopsConcept import Calculator


class ChildIml(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 9)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildIml()
print(obj.getCompleteData())
