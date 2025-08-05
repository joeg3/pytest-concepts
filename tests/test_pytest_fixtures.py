import pytest
import os


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

@pytest.mark.parametrize("user_fixture", ["user1", "user2"])
def test_parametrize_on_fixtures(request, user_fixture):
    """ Run test for each fixture """
    user = request.getfixturevalue(user_fixture)
    
    # Use os.environ.get('PYTEST_CURRENT_TEST') to see which parametrized fixture we're currently operating with
    if "test_parametrize_on_fixtures[user1]" in os.environ.get('PYTEST_CURRENT_TEST'):
        assert user == "Fred"
    elif "test_parametrize_on_fixtures[user2]" in os.environ.get('PYTEST_CURRENT_TEST'):
        assert user == "Jane"

@pytest.mark.parametrize("cleanup_after_test_case", ['some_text_file.txt'], indirect=True)
def test_run_fixture_after_test(cleanup_after_test_case):
    """ Example of marker sending data to the fixture """
    assert 1 == 1
    print('Leaving testcase')

def test_using_session_fixture(init_once_for_all_tests):
    pass

def test_using_function_fixture(init_for_each_test_tests):
    pass

def test_using_session_and_function_fixture(init_once_for_all_tests, init_for_each_test_tests):
    pass