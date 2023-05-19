import pytest


################################## Parametrizing Functions #############################

# The test cases in this file all use a tuple for each iteration. If only one value for each
# iteration, you would use: testdata = ["a", "b", "c"]
testdata = [
    (3, 4, 12),
    (0, 8, 0),
    (1, 7, 7)
]


@pytest.mark.parametrize("a, b, expected", testdata)
def test_product_by_parametrizing_function_with_variable(a, b, expected):
    """ Parametrize the test case function by using a variable for the test data """
    product = a * b
    assert product == expected

def get_test_data():
    return testdata

@pytest.mark.parametrize("a, b, expected", get_test_data())
def test_product_by_parametrizing_function_with_function(a, b, expected):
    """ Parametrize the test case function calling a function for the test data """
    product = a * b
    assert product == expected

@pytest.mark.parametrize(
    "a, b, expected", 
    [
        (3, 4, 12),
        (0, 8, 0),
        (1, 7, 7)
    ]
)
def test_product_by_parametrizing_function_with_marker(a, b, expected):
    """ Parametrize the test case function by putting the test data in the marker """
    product = a * b
    assert product == expected


################################## Parametrizing Fixtures #############################

@pytest.fixture(
    params=
    [
        (3, 4, 12),
        (0, 8, 0),
        (1, 7, 7)
    ]
)
def multiplication_data(request):
    return request.param

def test_product_by_parametrizing_fixture(multiplication_data):
    """ Parametrize using a fixture. This test case basically calls multiplication_data() """
    """ three times. If we wanted, we could have code in the fixture that depends on which """
    """ parameter is being returned """
    product = multiplication_data[0] * multiplication_data[1]
    assert product == multiplication_data[2]


################################## Parametrizing with pytest_generate_tests #############################

def pytest_generate_tests(metafunc):
    if "mult_data" in metafunc.fixturenames:
        metafunc.parametrize(
            "mult_data",
            [
                (3, 4, 12),
                (0, 8, 0),
                (1, 7, 7)
            ]
        )

def test_product_with_pytest_generate_tests(mult_data):
    """ Parametrize using hook function pytest_generate_tests(), which generates tests """
    product = mult_data[0] * mult_data[1]
    assert product == mult_data[2]