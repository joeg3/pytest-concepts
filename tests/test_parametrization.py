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

# @pytest.fixture(
#     params=
#     [
#         (3, 4, 12),
#         (0, 8, 0),
#         (1, 7, 7)
#     ]
# )
# def multiplication_data(request):
#     return request.param

@pytest.fixture
def multiplication_data(request):
    params = [
        (3, 4, 12),
        (0, 8, 0),
        (1, 7, 7)
    ]
    return params

@pytest.mark.parametrize(
    "multdata",
    ["multiplication_data"] # pass one or more fixtures
)
def test_product_by_parametrizing_fixture(multdata, request): # add request to arg list for accessing fixture
    """ Parametrize using a fixture. This test case basically calls multiplication_data() """
    """ three times. If we wanted, we could have code in the fixture that depends on which """
    """ parameter is being returned """
    datasets = request.getfixturevalue(multdata)
    print("||||||||||", datasets)
    # product = datasets[0] * datasets[1]
    # assert product == datasets[2]


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

@pytest.mark.parametrize("number", [1,2,3])
def test_parametrize_with_list(number):
    print(f"Number: {number}")
    assert number < 4

@pytest.mark.parametrize(
    "code, filename",
    [
        (123, "low.txt"),
        (456, "med.txt"),
        (789, "high.txt")
    ]
)
def test_parametrize_with_dictionary(code, filename):
    if code == 123:
        print(f"Run a test for code {code} using {filename}")
        assert filename == "low.txt"
    elif code == 456:
        print(f"Run a test for code {code} using {filename}")
        assert filename == "med.txt"
    elif code == 789:
        print(f"Run a test for code {code} using {filename}")
        assert filename == "high.txt"

