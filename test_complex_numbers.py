import random

import pytest

from complex_number import ComplexNumber


class TestComplexNumbers:

    @pytest.fixture
    def create_data_for_test(self):
        complex_number_1 = ComplexNumber(
            random.uniform(1, 10),
            random.uniform(1, 10)
        )
        print(f"First complex: {complex_number_1}")
        complex_number_2 = ComplexNumber(
            random.uniform(1, 10),
            random.uniform(1, 10)
        )
        print(f"Second complex: {complex_number_2}")
        yield complex_number_1, complex_number_2

    def test_sum(self, create_data_for_test):
        """

        :return:
        """
        complex_number_1, complex_number_2 = create_data_for_test[0], create_data_for_test[1]
        complex_res = complex_number_1 + complex_number_2
        print(f"Result: {complex_res}")
        assert complex_res.real_part == complex_number_2.real_part + complex_number_1.real_part
        assert complex_res.imaginary_part == complex_number_2.imaginary_part + complex_number_1.imaginary_part

    def test_sub(self, create_data_for_test):
        """

        :param create_data_for_test:
        :return:
        """
        complex_number_1, complex_number_2 = create_data_for_test[0], create_data_for_test[1]
        complex_res = complex_number_1 - complex_number_2
        print(complex_res)
        assert complex_res.real_part == complex_number_1.real_part - complex_number_2.real_part
        assert complex_res.imaginary_part == complex_number_1.imaginary_part - complex_number_2.imaginary_part