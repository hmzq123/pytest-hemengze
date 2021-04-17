import pytest
import random
#插件的使用

 #1、pytest-rerunfailures的使用
class Test_rerun():
    def test_rerun(self):
        r = random.randint(1,2)
        assert r == 1

#运行pytest -vs  --reruns 10 test_demo6.py


#2、分布式并发执行 pytest-xdist
class Test_xid():
    def test_xdi(self):
        a=1
        print("执行:")
        assert a==1
    
#运行pytest -n 2 -vs test_demo6.py::test_xdi


#3、控制⽤例的执⾏顺序：pytest-ordering
class Test_ord():
    @pytest.mark.run(order=2)
    @pytest.mark.demo1
    def test_demo1(Self):
        a=5
        b=-1
        assert a!=b
        print("测试用例1")
    
    @pytest.mark.run(order=1)
    @pytest.mark.demo2
    def test_demo2(self):
        a=2
        b=-1
        assert a!=b
        print("测试用例2")
