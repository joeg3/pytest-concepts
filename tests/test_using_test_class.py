import pytest

# Example of how to group tests in a class. Some people use them for
# ability to inherit helper classes or for grouping tests
# Run the tests in this class: pytest -v tests/test_using_test_class.py::TestBasics
# The fixture fixture_sets_int_in_class_variable sets class variable my_int and we use it here in test class
@pytest.mark.usefixtures("fixture_sets_int_in_class_variable")
class TestBasics:

    def test_some_testcase(self, supply_int):
        assert 7 == self.my_int
        assert 8 == supply_int

    def test_another_testcase(self, supply_int):
        assert 7 == self.my_int
        assert 8 == supply_int

