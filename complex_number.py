import math


class ComplexNumber:
    def __init__(
            self,
            real_part: float = 0,
            imaginary_part: float = 0
    ):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    @property
    def as_tuple(self):
        """
        Method for use real number part and imaginary part as tuple
        :return:
        """
        return self.real_part, self.imaginary_part

    @classmethod
    def create_as_complex(cls, other):
        """
        method for create ComplexNumber as
        :param other:
        :return:
        """
        if type(other) is cls:
            return other
        else:
            return cls(other)

    def __add__(self, other):
        """
        override magic method for sum
        :param other: instant of complex number
        :type: ComplexNumber
        :return:
        """
        other = self.create_as_complex(other)
        real_part = self.real_part + other.real_part
        imaginary_part = self.imaginary_part + other.imaginary_part
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other: int):
        """
        override magic method for subtract
        :param other: instant of complex number
        :type: ComplexNumber
        :return:
       """
        other = self.create_as_complex(other)
        real_part = self.real_part - other.real_part
        imaginary_part = self.imaginary_part - other.imaginary_part
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        """
        override magic method for multiplication
        :param other: instant of complex number
        :return:
        """
        other = self.create_as_complex(other)
        real_part = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary_part = self.imaginary_part * other.real_part + self.real_part * other.imaginary_part
        return ComplexNumber(real_part, imaginary_part)

    def __truediv__(self, other):
        """
        override magic method for division
        :param other: instant of complex number
        :return:
        """
        other = self.create_as_complex(other)
        real_part = (self.real_part * other.real_part + self.imaginary_part * other.imaginary_part) / (
                other.real_part ** 2 + other.imaginary_part ** 2)
        imaginary_part = (self.imaginary_part * other.real_part - self.real_part * other.imaginary_part) / (
                other.real_part ** 2 + other.imaginary_part ** 2)
        return ComplexNumber(real_part, imaginary_part)

    def __abs__(self):
        """
        Calculate modulus of complex number
        :return:
        """
        return math.sqrt(self.imaginary_part ** 2 + self.real_part ** 2)

    def __str__(self):
        """
        return type as str
        :return:
        """
        return str(self.as_tuple)


