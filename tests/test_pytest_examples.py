import pytest
from src import pytest_examples

# Here we verify our code under test function call of raise_exception()
# does indeed raise a SystemExit exception
def test_exception_raised():
    with pytest.raises(SystemExit):
        pytest_examples.raise_exception()

# Extract info from exception and verify
def test_exception_raised():
    with pytest.raises(SystemExit) as ex_obj:
        pytest_examples.raise_exception()
    expected = "My SystemExit exception message"
    assert expected in str(ex_obj.value)

# Parameters defined in the fixture
def test_param_fixture(param_fixture):
    print('Param printed in line above')

# Contrived example if you needed to explicitly fail a test
def test_pytest_fail():
    x = 3
    y = 3
    if x != y:
        pytest.fail(f"x and y are not equal: {x} != {y}")
