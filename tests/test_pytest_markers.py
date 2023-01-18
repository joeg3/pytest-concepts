import pytest

from src.rectangle import Rectangle


@pytest.mark.skip(reason='More work needed to finish test case code')
def test_some_api():
    """ With skip marker, this test will not be run, the reason parameter is optional but recommended """
    assert 2 == 1 + 5

@pytest.mark.skipif(
    Rectangle(3,4).version < 3,
    reason='Rectangle class not yet version 3')
def test_another_api():
    """ With skipif marker, skip if any condition(s) are true """
    assert 2 == 1 + 5

# The 'xfail' marker is useful if code under test isn't finished, 
# but test case is. This way reports are more meaningful than just a fail.
@pytest.mark.xfail(reason='Code under test is not implemented')
def test_marked_as_xfail():
    """ Use xfail marker if you want to run tests, even though you know they'll fail """
    assert 2 == 4

# The 'smoke' marker is custom, created by us. Need to put it in pytest.ini so we
# don't get warning, and so it is listed when running: pytest --markers
# To only run tests marked 'smoke': poetry run pytest -vs -m smoke
@pytest.mark.smoke
def test_marked_as_smoke():
    pass

# Parameters defined in the marker for a particular test case
@pytest.mark.parametrize('a, b, sum', [(1,2,3),(2,4,6),(7,8,15)])
def test_param_with_mark(a, b, sum):
    assert a + b == sum

############################ Combine Markers and Fixtures ##########################
# Use a custom marker to specify data for the fixture
# Omitting param or omitting marker sends no data to fixture

# Use marker with param to send 'Dr.' to fixture
@pytest.mark.prefix('Dr.')
def test_marker_with_param(prefix_jones):
    assert prefix_jones == "Dr. Jones"

# Use same marker without param
@pytest.mark.prefix
def test_marker_without_param(prefix_jones):
    assert prefix_jones == "Jones"

# Same test without marker
def test_no_markerm(prefix_jones):
    assert prefix_jones == "Jones"