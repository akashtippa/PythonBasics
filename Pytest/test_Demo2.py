# Any pytest file should start with test_

# pytest method names should start with test

# Any code should be wrapped in method only

# run with CMD py.test or py.test -v
# check results py.test -v -s

# run specific testcases py.test <filename> -v -s

# run specific methods in testcase py.test -k Summation -v -s

# -k stands for method names execution, -s logs output -v stands for more more
# meta data

# run group of test case mention above testmethond "@pytest.mark.smoke"
# and run command using  "py.test -m smoke -v -s"


# you can skip testing using @pytest.mark.skip

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_failedProgram(setup):
    msg = "Hello"
    assert msg == "Hello", "Test failed because string do not match"


@pytest.mark.skip
def test_Summation(setup):
    a = 6
    b = 7
    assert a + 2 == 6, "Addition do not match"

