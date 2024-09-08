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

@pytest.mark.parametrize("n,expected_add,expected_mul,expected_sub,expected_div", [
    (1, 2, 1, 0, 1),
    (3, 4, 3, 2, 3)
])
class TestCalc2():
    def test_add(self, n, expected_add):
        assert n + 1 == expected_add

    def test_mul(self, n, expected_mul):
        assert (n * 1) == expected_mul

    def test_sub(self, n, expected_sub):
        assert n - 1 == expected_sub

    def test_div(self, n, expected_div):
        assert n / 1 == expected_div
