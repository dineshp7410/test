from pages.assignment.assign_page import AssignmentPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AssignmentTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.rpm = AssignmentPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test1_FilltheForm(self):
        self.log.info("*#" * 20)
        self.log.info("RPM Software 2020 Coding Assignment started")
        self.log.info("*#" * 20)
        self.rpm.launchApplication()
        self.rpm.fillForm()
        self.rpm.submitForm()
        self.rpm.verifyFormSubmittedLink()
        self.rpm.verifyDataEnteredMatches()
        self.rpm.verifyEmployeeNameMatches()
        self.rpm.verifyAddressMatches()

