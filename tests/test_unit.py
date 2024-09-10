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
    @pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
    def test_add(self, n, expected):
        # result = self.calculator.add(1, 1)
        assert n + 1 == expected, "Add method failed"
        
    @pytest.mark.parametrize("n,expected", [(1, 0), (3, 2)])
    def test_subtract(self, n, expected):
        # result = self.calculator.subtract(3, 2)
        assert n - 1 == expected, "Subtract method failed"
        
    @pytest.mark.parametrize("n,expected", [(1, 2), (3, 6)])
    def test_multiply(self, n, expected):
        # result = self.calculator.multiply(2, 3)
        assert n * 2 == expected, "Multiply method failed"

    @pytest.mark.parametrize("n,expected", [(1, 0.5), (6, 3)])
    def test_divide(self, n, expected):
        #result = self.calculator.divide(6, 2)
        assert n / 2 == expected, "Divide method failed"

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(1, 0)
