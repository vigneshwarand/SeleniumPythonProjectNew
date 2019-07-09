import pytest
import sys

# @pytest.mark.skip(reason="Skip This Test")
# def test_demo1():
#     assert True
#
# def test_demo2():
#     assert True
#
# @pytest.mark.skipif(sys.version_info > (3, 6), reason="requires python3.6 or higher")
# def test_demo3():
#     assert True

@pytest.mark.windows1
def test_Windows_1():
    assert True

@pytest.mark.windows1
def test_Windows_2():
    assert True

@pytest.mark.mac1
def test_Mac_1():
    assert True

@pytest.mark.mac1
def test_Mac_2():
    assert True