import pytest

# run script with repotrt py.test --html=report.html
@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Tippa", "rahulshetty.com"]


@pytest.fixture(params=[("chrome", "Akash", "tippa"), ("Firefox", "Rahul"), "IE", "rahulshetty.com"])
def crossBrowser(request):
    return request.param
