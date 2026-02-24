class A:
    def __init__(self):
        print("In A init")
    def f1(self):
        print("f1 works")
class B(A):
    def __init__(self):
        super().__init__()
        print("In B init")
    def f2(self):
        super().f1()
        print("f2 works")
obj1 = B()
obj1.f1()
obj1.f2()