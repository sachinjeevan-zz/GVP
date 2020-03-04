class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print(self.a+self.b)
class B(A):
    def __init__(self,a,b):
        super().__init__(a,b)
    def sum(self):
        print(self.a*self.b)
    def test(self):
        self.sum()
obj = B(10,20)
obj.test()