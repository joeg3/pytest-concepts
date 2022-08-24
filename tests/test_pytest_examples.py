import pytest
from src import pytest_examples

def test_exception_raised():
    with pytest.raises(SystemExit):
        pytest_examples.raise_exception()

# The 'skip' marker comes with pytest, we don't need to put it in pytest.ini
@pytest.mark.skip(reason='Todo: Implement test when api finished')
def test_some_api():
    pass

# The 'sanity' marker is custom, created by us. Need to put it in pytest.ini so we
# don't get warning, and so it is listed when running: pytest --markers
@pytest.mark.sanity
def test_marked_as_sanity():
    pass

# The 'xfail' marker comes with pytest. Useful if code under test isn't finished, 
# but test case is. This way reports are more meaningful than just a fail
@pytest.mark.xfail(reason='Code under test is not implemented')
def test_marked_as_xfail():
    assert 2 == 4

# Parameters defined in the fixture
def test_param_fixture(param_fixture):
    print('Param printed in line above')

# Parameters defined in the marker
@pytest.mark.parametrize('a, b, final', [(1,2,3),(2,4,6),(7,8,15)])
def test_param_with_mark(a, b, final):
    assert a + b == final
