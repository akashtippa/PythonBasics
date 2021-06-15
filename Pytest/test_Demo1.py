# Any pytest file should start with test_

# pytest method names should start with test

# Any code should be wrapped in method only

# run with CMD py.test or py.test -v
# check results py.test -v -s

# test method will run but result will not show in reporting
import pytest


def test_firstProgram():
    print("hello")


@pytest.mark.xfail
def test_scondProgram():
    print("Good Afternoon")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])