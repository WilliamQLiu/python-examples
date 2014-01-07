# content of test_sample.py
# shows how to run a simple test function using 'assert'
# Run in shell using: $py.test test_sample.py
# Output: 1 failed in 0.03 seconds with red text showing 'E' on lines with errors

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

""" Output:
========================== test_answer ==========================
    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:9: AssertionError
========================== 1 failed in 0.03 seconds ==========================
"""