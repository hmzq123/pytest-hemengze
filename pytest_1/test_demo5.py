import pytest
#fixture类似setup和teardown，
#1、可以使我们自定义测试用例的前置条件，
#2、并且可以跨文件使用，
#3、也可以写在conftest.py文件里面
'''
@pytest.fixture()
def myfixture():
    print("执行myfixxture")
'''

class Test_firstFile():
    def test_one(self):
        print("执行test one")
        assert 2+3==5
    def test_two(self,myfixture):
        print("执行test two")
        assert 2+3==5
    def test_three(self):
        print("执行test three")
        assert 2+3==5
