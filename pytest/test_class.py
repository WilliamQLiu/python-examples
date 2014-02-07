# content of test_class.py
# group multiple tests together in classes and modules (here's a class example)
# Run in bash: $py.test test_class.py

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
"""
============================= test session starts =============================
platform win32 -- Python 2.7.3 -- pytest-2.5.1
collected 2 items

test_class.py .F

================================== FAILURES ===================================
_____________________________ TestClass.test_two ______________________________

self = <test_class.TestClass instance at 0x0000000002C37A88>

    def test_two(self):
        x = "hello"
>       assert hasattr(x, 'check')
E       assert hasattr('hello', 'check')

test_class.py:12: AssertionError
===================== 1 failed, 1 passed in 0.04 seconds ======================
"""