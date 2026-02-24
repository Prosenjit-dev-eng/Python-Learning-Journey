class A:
    def f1(self):
        print("f1 works")
    def f2(self):
        print("f2 works")

class B:
    def f3(self):
        print("f3 works")
    def f4(self):
        print("f4 works")

class C(A,B):
    def f5(self):
        print("f5 works")

obj1 = A()
obj1.f1()
obj2 = B()
obj2.f3()
obj3 = C()
obj3.f5()