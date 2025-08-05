import pytest

# Example of how to group tests in a class. Some people use them for the ability to inherit helper classes or for grouping tests
# Run the tests in this class: pytest -v tests/test_using_test_class.py::TestBasics

# The fixture 'set_int_in_class_variable' sets class variable my_int and we use it here in test class
# One advantage is that you can then set the fixture once at the class level, where return_int and yield_int
# have to be set for each testcase that uses them.
@pytest.mark.usefixtures("set_int_in_class_variable")
class TestBasics:

    def test_some_testcase(self, return_int, yield_int):
        assert 7 == self.my_int
        assert 8 == return_int
        assert 9 == yield_int

    def test_another_testcase(self, return_int, yield_int):
        assert 7 == self.my_int
        assert 8 == return_int
        assert 9 == yield_int

