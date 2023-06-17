class TestClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    @staticmethod
    def add(x, y):
        return x + y
    
    def printAdd(self):
        print(TestClass.add(self.a, self.b))

c = TestClass(1, 4)
c.printAdd()
