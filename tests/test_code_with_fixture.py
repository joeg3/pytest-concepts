import pytest

# This creates a fixture called "my_setup_teardown". A fixture's scope is defined by specifying it in the
# fixture's parameter list. This fixture has the scope of "function" which is the default, so it 
# can be ommitted, but we explicitly specified it. Fixtures with a scope of function run before and after
# each test that have the fixture name in thier parameter list like test_demo_fixture() below.
# 
# In this fixture, setup code is run before the yield statement, then yield passes a parameter to the test.
# The test is run during the yield statement, then teardown code is run after that.
# If a fixture is used in many test files, it should be in conftest.py
# But if only used in one file, it can be done like this
@pytest.fixture(scope='function')
def my_setup_teardown():
    # Code befor the yield is 'setup' code
    print('Open browser')
    print('Log into site')
    print('Browse product')
    yield 'abc' # This is when test case runs, and the value 'abc' can be accessed by each test case using this fixture
    # Code after the yield is 'tear down' code and is run even if the test case throws an exceptiion
    print('Logoff')
    print('Close browser')

# With my_setup_teardown as a parameter, this test case will use that fixture. The my_setup_teardown fixture has a scope of function,
# so it runs each time a test case specifies it.
def test_demo_fixture(my_setup_teardown):
    assert my_setup_teardown == "abc"
