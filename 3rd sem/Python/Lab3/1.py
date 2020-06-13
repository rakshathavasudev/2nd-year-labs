class Fraction:

    def __init__(self,num,den):
        self.numerator=num
        self.denominator=den

    def inverse(self):
        """Returns the inverse of this Fraction"""
        a=self.numerator
        self.numerator=self.denominator
        self.denominator=a
        return(self)

    def add(self,f):
        """Adds the Fraction f to this Fraction and returns the result"""
        n=(self.numerator*f.denominator)+(self.denominator*f.numerator)
        d=self.denominator*f.denominator
        return(Fraction(n,d))

    def subtract(self,f):
        """Subtracts the Fraction f from this Fraction and returns the result"""
        n=(self.numerator*f.denominator)-(self.denominator*f.numerator)
        d=self.denominator*f.denominator
        return(Fraction(n,d))


    def multiply(self,f):
        """Multiplies the Fraction f to this Fraction and returns the result"""
        n=self.numerator*f.numerator
        d=self.denominator*f.denominator
        return(Fraction(n,d))

    def divide(self,f):
        """Divides the Fraction f from this Fraction and returns the result"""
        n=self.numerator*f.denominator
        d=self.denominator*f.numerator
        return(Fraction(n,d))

    def show(self):
        print(self.numerator,'/',self.denominator)

def main():
    f1 = Fraction(2,3)
    print('Fraction 1 is',end=' ')
    f1.show()
    f2 = Fraction(3,4)
    print('Fraction 2 is',end=' ')
    f2.show()
    print('The inverse of f1 is',end=' ')
    (f1.inverse()).show()
    print('The inverse of f2 is',end=' ')
    (f2.inverse()).show()
    f1 = Fraction(2,3)
    f2 = Fraction(3,4)
    print('f1+f2 is',end=' ')
    f1.add(f2).show()
    print('f1-f2 is',end=' ')
    (f1.subtract(f2)).show()
    print('f1 * f2 is',end=' ')
    (f1.multiply(f2)).show()
    print('f1 / f2 is',end=' ')
    (f1.divide(f2)).show()

if __name__ == '__main__':
    main()