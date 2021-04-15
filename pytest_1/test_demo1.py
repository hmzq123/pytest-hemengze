import pytest

def add_function(a,b):
    return a+b
#参数化
@pytest.mark.parametrize("a,b,expected",[(3,3,6),(3,-2,1)])

def test_add1(a,b,expected):
    assert add_function(a,b)==expected


#参数化别名
@pytest.mark.parametrize("a,b,expected",[(3,3,6),(-3,-3,-6)],ids=["int","minus"])

def test_add2(a,b,expected):
     assert add_function(a,b)==expected


