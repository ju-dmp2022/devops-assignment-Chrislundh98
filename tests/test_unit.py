import pytest
from BE.calculator_helper import CalculatorHelper

class BaseTest:
    def setup_method(self):
        """Setup before each test"""
        self.calculator = CalculatorHelper()

    def teardown_method(self):
        """Teardown after each test"""
        self.calculator = None

class TestCalc(BaseTest): 
    def test_add(self):
        result = self.calculator.add(1, 1)
        assert result == 2, "Add method failed"

    def test_subtract(self):
        result = self.calculator.subtract(3, 2)
        assert result == 1, "Subtract method failed"

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        assert result == 6, "Multiply method failed"

    def test_divide(self):
        result = self.calculator.divide(6, 2)
        assert result == 3, "Divide method failed"

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(1, 0)
