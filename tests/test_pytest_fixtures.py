import pytest


def test_command_line_flags(browser, config):
    print('Browser from browser fixture: ', browser)
    print('Browser from config fixture: ', config['browser'])

def test_fixture_returns_data_for_test(return_int):
    assert return_int == 8

def test_fixture_yields_data_for_test(yield_int):
    assert yield_int == 9

def test_chained_fixtures(chained_fixture):
    assert chained_fixture == 12

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

# Pass tuples from fixtures to get multiple values to testcase
# First time will be: ('a1','b1'), second time: ('a2', 'b2')
def test_use_fixture_with_tuple_params(param_fixture_tuple_per_test_run):
    first_item = param_fixture_tuple_per_test_run[0]
    assert first_item in ['a1', 'a2']

# Here the test case can return data to the cleanup_after_test_case fixture
@pytest.mark.parametrize("cleanup_after_test_case", ['some_text_file.txt'], indirect=True)
def test_run_fixture_after_test(cleanup_after_test_case):
    assert 1 == 1
    print('Leaving testcase')