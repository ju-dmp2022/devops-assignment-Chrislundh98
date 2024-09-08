from BE.calculator_helper import CalculatorHelper
from assertpy import assert_that
import pytest

class base_class():
    @classmethod
    def setup_calc(cls):
        "runs at start"

    @classmethod
    def teardown_calc(cls):
        "runs at end of test"

# class TestCalc():
#     base_class.setup_calc()

#     calculator = CalculatorHelper()
#     def test_add(self):
#         value = self.calculator.add(1,1)
#         assert_that(value).is_equal_to(2)
    
#     def test_sub(self):
#         value = self.calculator.subtract(3,2)
#         assert_that(value).is_equal_to(1)
    
#     def test_mul(self):
#         value = self.calculator.multiply(2,3)
#         assert_that(value).is_equal_to(6)

#     def test_div(self):
#         value = self.calculator.divide(6,2)
#         assert_that(value).is_equal_to(3)

#     base_class.teardown_calc()
    
@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestCalc2():
    def test_add(self, n, expected):
        assert n + 1 == expected

    def test_mul(self, n, expected):
        assert (n * 1) + 1 == expected
    
    def test_sub(self, n, expected):
        assert (n - 1) + 1 == expected

    def test_div(self, n, expected):
        assert (n / 1) + 1 == expected

