import pytest

# This creates a fixture called "my_setup_teardown". A fixture's scope is defined by specifying it in the
# fixture's parameter list. This fixture has the default scope of "function" because we didn't 
# specify scope as a parameter. Fixtures with a scope of function run before and after each test
# that have the fixture name in thier parameter list like test_demo_fixture() below.
# 
# In this fixture, setup code is run before the yield statement, then yield passes a parameter to the test.
# The test is run during the yield statement, then teardown code is run after that.
# If a fixture is used in many test files, it should be in conftest.py
# But if only used in one file, it can be done like this
@pytest.fixture
def my_setup_teardown():
    print('Open browser')
    print('Log into site')
    print('Browse product')
    yield "abc" # This is when test case runs
    print('Logoff')
    print('Close browser')

# We pass in above fixture that runs code before and after the test case
def test_demo_fixture(my_setup_teardown):
    assert my_setup_teardown == "abc"

# Even though the 'hi' fixture is set to autouse, we specify it as a parameter so we can reference
# the fixture's return value
def test_autouse_hi(hi):
    assert hi == 'hi'

# We pass in fixture from conftest.py that runs code before and after the test case
def test_add_item_to_cart2(setup_teardown_browser):
    print('Add item to cart')

def test_assert1(init_once_for_all_tests):
    assert 2==2

def test_assert2(init_once_for_all_tests):
    assert 2==2