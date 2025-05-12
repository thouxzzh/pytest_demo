import pytest
import sys
# @pytest.mark.skip(reason="not working")
def test_sam1():
    print("Hai")

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.skipif(sys.version_info < (3,7),reason="different num")
def test_sam2():
    a=10
    b=10
    assert a==b

@pytest.mark.smoke
def test_sam3():
    a=5
    b=10
    assert a < b

@pytest.mark.smoke
def test_sam4():
    a="Beau"
    b="Beau"
    assert a.__eq__(b)

@pytest.mark.xfail(reason="Expected to fail")
def test_sam5():
    a=10
    b=10
    assert a!=b

@pytest.mark.xfail(reason="Expected to fail")
def test_sam6():
    a=10
    b=10
    assert a==b

@pytest.mark.parametrize("test_input,expected",[(1,3),(3,6),(5,7)])
def test_addition(test_input,expected):
    assert test_input +2 ==expected


