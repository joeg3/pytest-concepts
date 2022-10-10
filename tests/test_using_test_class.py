
# Example of how to group tests in a class. Some people use them for
# ability to inherit helper classes or for grouping tests
# Run the tests in this class: pytest -v tests/test_using_test_class.py::TestBasics
class TestBasics:

    def test_some_testcase(self):
        assert 2 == 2

    def test_another_testcase(self):
        assert 4 == 4

