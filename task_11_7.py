class ComplexNumber:
    def __init__(self, z):
        self.z = z
        self.re_z, self.im_z = self.z.split()
        self.re_z = int(self.re_z)
        self.im_z = int(self.im_z[0:-1])

    def __add__(self, other):
        self.rez = self.re_z + other.re_z, self.im_z + other.im_z
        if self.rez[0] == 0 and self.rez[1] == 0:
            return "0"
        if self.rez[0] == 0:
            return self.rez[1]
        if self.rez[1] == 0:
            return self.rez[0]
        if self.rez[1] >= 0:
            return f'{self.rez[0]}+{self.rez[1]}i'
        else:
            return f'{self.rez[0]}{self.rez[1]}i'

    def __mul__(self, other):
        self.re_rez = self.re_z * other.re_z + self.im_z * other.im_z * (-1)
        self.im_rez = self.re_z * other.im_z + self.im_z * other.re_z
        if self.re_z == 0 and self.im_rez == 0:
            return 0
        if self.re_rez == 0:
            self.re_rez = ""
        if self.im_rez == 0:
            self.im_rez = ""
        else:
            self.im_rez = str(self.im_rez) + "i"
        if not self.im_rez[0] == "-":
            return f"{self.re_rez}+{self.im_rez}"
        else:
            return f"{self.re_rez}{self.im_rez}"

    def __sub__(self, other):
        self.rez = self.re_z - other.re_z, self.im_z - other.im_z
        if self.rez[0] == 0 and self.rez[1] == 0:
            return "0"
        if self.rez[0] == 0:
            return self.rez[1]
        if self.rez[1] == 0:
            return self.rez[0]
        if self.rez[1] >= 0:
            return f'{self.rez[0]}+{self.rez[1]}i'
        else:
            return f'{self.rez[0]}{self.rez[1]}i'

    def __floordiv__(self, other):
        "не рискну)))"
        pass


if __name__ == '__main__':
    """условно между мнимой и реальной частью дожен быть пробел"""
    z1 = ComplexNumber('4 -5i')
    z2 = ComplexNumber('-7 2i')
    z3 = ComplexNumber('0 -4i')
    z4 = ComplexNumber('1 -0i')
    z5 = ComplexNumber('2 0i')
    z6 = ComplexNumber("18 4i")
    print("сложение:")
    print(z1 + z2)
    print(z3 + z4)
    print(z5 + z6)
    print(z1 + z6)
    print(z6 + z3)
    print("умножение:")
    print(z1 * z2)
    print(z3 * z4)
    print(z5 * z6)
    print(z1 * z6)
    print(z1 * z5)
    print("вычитание:")
    print(z1 - z2)
    print(z3 - z4)
    print(z5 - z6)
    print(z1 - z6)
    print(z6 - z6)


