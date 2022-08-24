# The conftest.py file is a standard pytest file where you can store all
# your common functions and fixtures commonly used by many test cases.

import pytest

# With autouse=True in this fixture, this fixture is applied to all tests, even if fixture not passed in
# In the testcase, if you put the fixture in the parameter list, you can refernece its return value
@pytest.fixture(autouse=True)
def hi():
    return 'hi' # Send data to the test case

# With scope='session', the first time a test case is called with this fixture, the fixture will be run.
# But subsequent test cases with this fixture will not have the fixture run because of scope of session
# By default, the scope is 'function', run for each function (test case)
@pytest.fixture(scope='session')
def init_once_for_all_tests():
    print('Since scope is set to session, this fixture runs just once before all testcases')

# With autouse=True in this fixture, this fixture is applied to all tests
@pytest.fixture(scope='session', autouse=True)
def setup_teardown_browser(browser):
    if browser == 'firefox':
        print('Open firefox')
    elif browser == 'safari':
        print('Open safari')
    else:
        print('Provide valid browser')
    print('Log into site')
    print('Browse product')
    yield # This is when test case runs
    print('Logoff')
    print('Close browser')

# Parameterize with a fixture
@pytest.fixture(params=['a','b'])
def param_fixture(request):
    print(request.param)

# Define command line option --browser
def pytest_addoption(parser):
    parser.addoption('--browser')

## Returns value given to --browser option
@pytest.fixture(scope='session', autouse=True)
def browser(request):
    return request.config.getoption('--browser')