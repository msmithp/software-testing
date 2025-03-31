from grades import calc_grade
import pytest

def test_calc():
    assert calc_grade(70) == "C"