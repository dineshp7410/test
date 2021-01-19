import unittest
from tests.assignment.assign_tests import AssignmentTest


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(AssignmentTest)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)