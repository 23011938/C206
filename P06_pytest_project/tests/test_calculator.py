from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_add_normal(self):
        # arrange
        a = 2
        b = 2
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 4
        assert result == expected

    def test_add_negative(self):
        # arrange
        a = -1
        b = -2
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = -3
        assert result == expected

    def test_subtract(self):
        # arrange
        a =  5
        b =  2
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3
        assert result == expected

    def test_subtract_normal(self):
        # arrange
        a =  14
        b =  7
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 7
        assert result == expected

    def test_subtract_negative(self):
        # arrange
        a =  5
        b =  10
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = -5
        assert result == expected


    def test_multiply(self):
        # arrange
        a =  2
        b =  2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 4
        assert result == expected

    def test_multiply_normal(self):
        # arrange
        a =  2
        b =  4
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 8
        assert result == expected
    
    def test_multiply_negative(self):
        # arrange
        a =  -2
        b =   1
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = -2
        assert result == expected

    def test_divide(self):
        # arrange
        a =  4
        b =  2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 2
        assert result == expected

    def test_divide_normal(self):
        # arrange
        a =  10
        b =  2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 5
        assert result == expected

    def test_divide_zero(self):
        # arrange
        a =  10
        b =  0
        cal = Calculator()

        # act and asset
        with pytest.raises(ZeroDivisionError, match = "Division by zero error"):
            result = cal.divide(a, b)



