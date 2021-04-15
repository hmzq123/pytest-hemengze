import pytest
class Test_Demo2():
    @pytest.mark.demo1
    def test_demo1(Self):
        a=5
        b=-1
        assert a!=b
        print("测试用例1")
    @pytest.mark.demo2
    def test_demo2(self):
        a=2
        b=-1
        assert a!=b
        print("测试用例2")
