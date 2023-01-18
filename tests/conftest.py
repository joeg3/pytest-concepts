# The conftest.py file is a standard pytest file where you can store all
# your common functions and fixtures commonly used by many test cases.

import inspect
import logging
import pytest

def pytest_addoption(parser):
    # action="store" stores value in a variable of the same name as the option
    parser.addoption("--browser", action="store", default="firefox", choices=("firefox", "safari"), help="Browser name, options are: 'firefox', 'safari'. Default is firefox")
    parser.addoption("--env", action="store", default="", help="Test environment name, options are: 'dev', 'stage'. Default is dev")

    # Examples of things you can do with addoption()
    parser.addoption('--foo', action='store_const', const='42')      # If --foo is specified in cmd line, it's value is set to 42
    parser.addoption('--my_true_flag', action='store_true')          # If --my_true_flag is specified in cmd line, it's value is set to true (specialized case of store_const)
    parser.addoption('--bar', default='abc')                         # If --bar is not specified, set to 'abc'
    parser.addoption('--baz', choices=['rock', 'paper', 'scissors']) # Parameter must be one of three specifed choices
    parser.addoption('--y', action='store')                          # Explicitly store value
    parser.addoption('--z')                                          # action='store' is the default
    # parser.addoption('--zz', required=True)                        # Default is that cmd line flags are optional

@pytest.fixture(scope='session', autouse=True)
def foo(request):
    print('\n--foo: ', request.config.getoption('--foo'))                 # Will be '42' if flag used in cmd line
    print('--my_true_flag: ', request.config.getoption('--my_true_flag')) # Will be 'True' if flag used in cmd line
    print('--bar: ', request.config.getoption('--bar'))                   # Will be 'abc' if --bar not used in cmd line
    print('--baz: ', request.config.getoption('--baz'))                   # If not one of specified choices, will error out and not start test
    print('--y:', request.config.getoption('--y'))                        # Stores argument of --y
    print('--z:', request.config.getoption('--z'))                        # By default, argument to flag is stored
    # print('--zz:', request.config.getoption('--zz'))                    # Required flag

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

# Add request parameter to set class field that can be used by a test class that uses this fixture
@pytest.fixture(scope='class')
def set_int_in_class_variable(request):
    request.cls.my_int = 7
    yield

# Basic fixture to provide data to tests that use it
@pytest.fixture(scope='session')
def return_int():
    return 8

# Use yield to run fixture code both before and after test
@pytest.fixture(scope='class')
def yield_int(request):
    yield_int = 9  # Setup
    yield yield_int
    yield_int = 0  # Tear down

# Since it's a parameter, first return_int fixture runs, and returns its value to this fixture
@pytest.fixture(scope='session')
def chained_fixture(return_int):
    return 4 + return_int

# Here the fixture gets a value back from the test case
@pytest.fixture(scope='session')
def cleanup_after_test_case(request):
    yield
    print('***In cleanup_after_test_case(), received param:', request.param) # Close file, etc.

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

# The test can optionally use a marker to send data to the fixture
@pytest.fixture(scope="function")
def prefix_jones(request):
    last_name = "Jones"
    p = request.node.get_closest_marker("prefix") # Gets data from test case
    if p and len(p.args) > 0:
        prefix = p.args[0]
        return f"{prefix} {last_name}"
    else: # Test doesn't use prefix marker or doesn't give it an argument
        return last_name

# Since this fixture returns a value that is necessary for its use (logger), it doesn't help thatautouse=True.
# To access logger in the test case, we have to include the fixture name (logger) as a test case parameter anyhow.
@pytest.fixture(scope='session', autouse=True)
def logger():
        # Usual way to have test name displayed in log entries if this log setup code was in the same file as the tests
        #logger = logging.getLogger(__name__) # Passing in __name__ makes current file name being executed available for the log entry

        # Since we are setting up logging in conftest.py, 'tests.conftest' is the name displayed in the log entries
        # This hack gets the name of the test
        loggerName = inspect.stack()[2][3]
        logger = logging.getLogger(loggerName)

        file_handler = logging.FileHandler('logs/logfile.log')

        # <time> : <logger level> : <file name> : <message from log statement> | <filename>:<line number>
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s | (%(filename)s:%(lineno)s)")
        file_handler.setFormatter(format)

        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO) # Only log INFO and higher, this won't log DEBUG statements
        return logger
    