class A:
    def m(self, x, y):
        print(x+y)
class B:
    def call_a(self):
        return A()
class C:
    def call_b(self):
        return B()	

C().call_b().call_a().m(1,2)