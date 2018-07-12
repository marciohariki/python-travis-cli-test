import pytest

from models.calculator import Calculator


class TestCalculator():
    @pytest.fixture
    def calculator(self):
        return Calculator()

    def test_sum(self, calculator):
        result = calculator.sum(1, 2)

        assert result == 3

    def test_subtract(self, calculator):
        result = calculator.subtract(1, 2)

        assert result == -1

    def test_multiply(self, calculator):
        result = calculator.multiply(1, 2)

        assert result == 2