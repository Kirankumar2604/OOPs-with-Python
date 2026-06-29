class A:
    print("char A")
class B:
    print("char B")
class C(A,B):
    print("char C")

c = C()
