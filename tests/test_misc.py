import re

from os import environ

# Might come in handy when verifying that test data in a file is associated with this test case.
def test_get_test_case_name():
    tc_name = get_current_test_case_name()
    assert tc_name == 'test_get_test_case_name'

def get_current_test_case_name():
    full_path = environ["PYTEST_CURRENT_TEST"] # This will be something like: tests/test_basics.py::test_get_test_case_name (call)
    return re.search('::(.+?) ', full_path).group(1) # Returns something like this: test_get_test_case_name
