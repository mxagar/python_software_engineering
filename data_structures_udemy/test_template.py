"""This file is a simple testing template
which uses no other lilbraries.

Author: Mikel Sagardia
Date: 2022-12
"""

# Function to be tested
def foo(value):
    return value ** 2

# Testing class, which testing functions: manual, type, parametrized
class MyFooTest():
    
    def test_1(self, foo):
        # Manual
        assert foo(2) == 4
        assert not (foo(3) == 10)
        print("test_2(): ALL PASSED")

    def test_2(self, foo):
        # Type
        assert isinstance(foo(2), int)
        print("test_2(): ALL PASSED")
        
    def test_3(self, foo):
        # Parametrized
        # Arguments of the function
        args = (
            1,
            2,
            3
        )
        # Solutions for each argument
        sols = (
            1,
            4,
            9
        )
        for i, a in enumerate(args):
            assert foo(a) == sols[i]
        print("test_3(): ALL PASSED")
        
if __name__ == "__main__":

    t = MyFooTest()
    t.test_1(foo)
    t.test_2(foo)
    t.test_3(foo)