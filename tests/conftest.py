# The conftest.py file is a standard pytest file where you can store all
# your common functions and fixtures commonly used by many test cases.

import pytest

def pytest_addoption(parser):
    # action="store" stores value in a variable of the same name as the option
    parser.addoption("--browser", action="store", default="firefox", choices=("firefox", "safari"), help="Browser name, options are: 'firefox', 'safari'. Default is firefox")
    parser.addoption("--env", action="store", default="", help="Test environment name, options are: 'dev', 'stage'. Default is dev")

    # Examples of things you can do with addoption()
    parser.addoption('--foo', action='store_const', const='42') # If --foo is specified in cmd line, it's value is set to 42
    parser.addoption('--my_true_flag', action='store_true') # If --my_true_flag is specified in cmd line, it's value is set to true (specialized case of store_const)
    parser.addoption('--bar', default='abc') # If --bar is not specified, set to 'abc'
    parser.addoption('--baz', choices=['rock', 'paper', 'scissors']) # parameter must be one of three specifed choices
    parser.addoption('--y', action='store')
    parser.addoption('--z') # action='store' is the default
    # parser.addoption('--zz', required=True) # default is that flags are optional

@pytest.fixture(scope='session', autouse=True)
def foo(request):
    print('\n--foo: ', request.config.getoption('--foo')) # Will be '42' if flag used in cmd line
    print('--my_true_flag: ', request.config.getoption('--my_true_flag')) # Will be 'True' if flag used in cmd line
    print('--bar: ', request.config.getoption('--bar')) # Will be 'abc' if --bar not used in cmd line
    print('--baz: ', request.config.getoption('--baz')) # If not one of specified choices, will error out and not start test
    print('--y:', request.config.getoption('--y'))      # Stores argument of --y
    print('--z:', request.config.getoption('--z'))      # By default, argument to flag is stored
    # print('--zz:', request.config.getoption('--zz'))    # Required flag

# One approach is to have a fixture for each CLI arg. This returns value of --browser option
@pytest.fixture(scope='session', autouse=True)
def browser(request):
    return request.config.getoption('--browser')

# Another approach is to have a fixture for all CLI args and return one config object
@pytest.fixture(scope='session', autouse=True)
def config(request):
    config = {}
    config['browser'] = request.config.getoption('--browser')
    config['env'] = request.config.getoption('--env')
    return config

# Basic fixture to provide data to tests that use it
@pytest.fixture(scope='session')
def provide_data_for_test():
    return 8

# With autouse=True in this fixture, this fixture is applied to all tests, even if fixture not passed in
# In the testcase, if you put the fixture in the parameter list, you can reference its return value
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

# Here we are experimenting with a new implementation of an existing fixture. Rather
# than renaming the parameter list of each test that uses existing fixture, you can
# set the name of a fixture to something other than its function name.
@pytest.fixture(name="cmd_line_opt_parser")
def experimental_cmd_line_opt_parser():
    pass

# Parameterize with a fixture. Since this fixture has two parameters, a test case using this fixture
# would be run twice
@pytest.fixture(params=['a','b'])
def param_fixture(request): # Need to use 'request' argument to access params
    return request.param
