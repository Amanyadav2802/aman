class A:
    def a(self):
        print("its class a")
class B:
    def b(self):
        print("Its class B")
class C(A,B):
    def c(self):
        print("its class c")
# a1=A()
# a1.a()
# b1=B()
# b1.a()
c1=C()
c1.b()
