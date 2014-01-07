# content of test_sysexit.py
# shows how to assert that a certain exception is raised using the 'raises' helper
# Run using $py.test test_sysexit.py
# Output: 1 passed in 0.01 seconds

import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
