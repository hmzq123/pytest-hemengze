#pytest框架结构

#setup 和 teardown
def setup_module():
    print("setup module:整个模块开始只执行一次！！！")
def teardown_module():
    print("teardown module:整个模块结束只执行一次！！！")
#类外测试
def setup_function():
    print("setup function:每个不在类中的用例开始前会执行")
def teardown_function():
    print("teardown function:每个不在类中的用例结束后会执行")
def test_one():
    print("正在执行测试模块:test one")

def test_two():
    print("正在执行测试模块:test two")
#测试类
class TestCase():
    def setup_class(self):
        print("setup class:class类里面所有用例执行前执行")
    def teardown_class(self):
        print("teardown class:class类里面所有用例结束后执行")
    def setup(self):
        print("setup:每个用例开始之前都会执行")
    def teardown(self):
        print("teardown:每个用例结束后执行")
    def  test_three(self):
        print("正在执行的模块:test three")
    def  test_four(self):
        print("正在执行的模块:test four")