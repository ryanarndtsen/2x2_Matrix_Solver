class matrix(object):
    def __init__(self, p1 =1, p2=0, p3=0, p4=1):
        self.a, self.b, self.c, self.d = p1, p2, p3, p4
    def __repr__(self):
        return "Matrix[{:3.2f},{:3.2f},{:3.2f},{:3.2f}]".format(self.a, self.b, self.c, self.d)
    def __eq__(self,other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d
    def __mul__(self, other):
        ans = matrix((self.a*other.a+self.b*other.c),(self.a*other.b+self.b*other.d),(self.c*other.a+self.d*other.c),(self.c*other.b+self.d*other.d))
        return ans
    def int_mult(self, q):
        ans = matrix(self.a*q,self.b*q,self.c*q,self.d*q)
        return ans
    def __truediv__(self, other):
        ans = self*other.inverse()
        return ans
    def __add__(self,other):
        return matrix(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
    def commutative(self,other):
        return self*other == other*self
    def __sub__(self, other):
        return matrix(self.a-other.a, self.b-other.b, self.c-other.c, self.d-other.d)
    def determinant(self):
        return self.a*self.d-self.b*self.c
    def inverse(self):
        mult = 1/self.determinant()
        ans = matrix(self.d,-self.b,-self.c,self.a).int_mult(mult)
        return ans
    def reduce_to_rref(self):
        print("{} can be reduced to rref using the following steps:".format(self))
        print("**If error is returned, matrix cannot be reduced to the identity matrix.**")
        print("**If your matrix has a zero in the a or d place, please swap the rows to avoid error.**")
        if self.a != 1:
            print("r1 --> r1/{}".format(self.a))
            self.a, self.b = self.a/self.a, self.b/self.a
            print(self)
            print()
            if self.c != 0:
                print("r2 --> r2 + -{}r1".format(self.c))
                self.c, self.d = (self.c +(-self.c*self.a)), (self.d+(-self.c*self.b))
                print(self)
                print()
                if self.d != 1:
                    print("r2 --> r2/{}".format(self.d))
                    self.d = self.d/self.d
                    print(self)
                    print()
                    if self.b != 0:
                        print("r1 --> r1 + -{}r2".format(self.b))
                        self.b = self.b + (-self.b*self.d)
                        print(self)
                        print("REDUCED")
                    else:
                        print("REDUCED")
                else:
                    if self.b != 0:
                        print("r1 --> r1 + -{}r2".format(self.b))
                        self.b = self.b + (-self.b*self.d)
                        print(self)
                        print("REDUCED")
                    else:
                        print("REDUCED")
            else:
                if self.d != 1:
                    print("r2 --> r2/{}".format(self.d))
                    self.d = self.d/self.d
                    print(self)
                    print()
                    if self.b != 0:
                        print("r1 --> r1 + -{}r2".format(self.b))
                        self.b = self.b + (-self.b*self.d)
                        print(self)
                        print("REDUCED")
                    else:
                        print("REDUCED")
                else:
                    if self.b != 0:
                        print("r1 --> r1 + -{}r2".format(self.b))
                        self.b = self.b + (-self.b*self.d)
                        print(self)
                        print("REDUCED")
                    else:
                        print("REDUCED")
        else:
            if self.c != 0:
                print("r2 --> r2 + -{}r1".format(self.c))
                self.c, self.d = (self.c +(-self.c*self.a)), (self.d+(-self.c*self.b))
                print(self)
                print()
                if self.d != 1:
                    print("r2 --> r2/{}".format(self.d))
                    self.d = self.d/self.d
                    print(self)
                    print()
                    if self.b != 0:
                        print("r1 --> r1 + -{}r2".format(self.b))
                        self.b = self.b + (-self.b*self.d)
                        print(self)
                        print("REDUCED")
                    else:
                        print("REDUCED")
                else:
                    if self.b != 0:
                        print("r1 --> r1 + -{}r2".format(self.b))
                        self.b = self.b + (-self.b*self.d)
                        print(self)
                        print("REDUCED")
                    else:
                        print("REDUCED")
            else:
                if self.d != 1:
                    print("r2 --> r2/{}".format(self.d))
                    self.d = self.d/self.d
                    print(self)
                    print()
                    if self.b != 0:
                        print("r1 --> r1 + -{}r2".format(self.b))
                        self.b = self.b + (-self.b*self.d)
                        print(self)
                        print("REDUCED")
                    else:
                        print("REDUCED")
                else:
                    if self.b != 0:
                        print("r1 --> r1 + -{}r2".format(self.b))
                        self.b = self.b + (-self.b*self.d)
                        print(self)
                        print("REDUCED")
                    else:
                        print("REDUCED")
        
