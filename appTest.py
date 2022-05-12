from re import M
import calFunctions
import unittest.mock as mock

class TestCalculatorFunctions:
    def test_addFunction(self):
        assert 4==calFunctions.addFunction(2,2)
    def test_subtractTwoNum(self):
        assert 2==calFunctions.subtractTwoNum(4,2)
    def test_multiplyTwoNum(self):
        assert 6==calFunctions.multiplyTwoNum(2,3)
    def test_divideTwoNum(self):
        assert 2==calFunctions.divideTwoNum(14,7)
        assert 4.67==calFunctions.divideTwoNum(14,3)