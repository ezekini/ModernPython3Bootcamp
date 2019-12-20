class A:
    def do_something(self):
        print('Method defined in A')


class B(A):
    def do_something(self):
        print('Method defined in B')


class C(A):
    def do_something(self):
        print('Method defined in C')


class D(B, C):
    pass


testing = D()
print(D.__mro__)
print(D.mro())
help(D)
