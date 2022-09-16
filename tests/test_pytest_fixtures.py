import pytest


def test_command_line_flags(browser, config):
    print('Browser from browser fixture: ', browser)
    print('Browser from config fixture: ', config['browser'])

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

# The fixture 'param_fixture' has two params 'a' and 'b' that it simply returns. Since this
# testcase uses the parameterized fixture, it'll be run twice, once for each fixture parameter.
def test_use_fixture_with_params(param_fixture):
    assert param_fixture in ['a', 'b']