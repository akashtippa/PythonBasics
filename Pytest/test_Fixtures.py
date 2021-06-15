import pytest


# Fixtures are used as setup and tear down methods for test cases conftest file
# generalize and make it available to for every testcase

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo4(self):
        print("i will execute steps in fixtureDemo method")
