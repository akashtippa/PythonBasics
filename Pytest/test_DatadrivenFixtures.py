import pytest

from Pytest.BaseClass import BaseClass
from Pytest.conftest import dataLoad
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will once before class initiated
# and at the end


@pytest.mark.usefixtures("dataLoad")
class TestDataDriven(BaseClass):
    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])



