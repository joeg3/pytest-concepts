# pytest-concepts

## Project Initialization with Poetry
- First I created a Git project with only this README.md file.
- Next, I ran `poetry init` and only added the `pytest` dependency. This created the `pyproject.toml` file.
- Next, I ran `poetry install` to install the dependency packages defined in `pyproject.toml`. This created the `poetry.lock` file.
- Next, I created a `.gitignore` file and added a `/poetry.lock` entry to it.
- Next, I created `tests/test_basics.py` and added a simple test case. I also added an empty `tests/__init__.py` file.
- Finally I ran the test case: `poetry run pytest -vs tests/test_basics.py`, which created a `tests/__pycache__` file. I added `__pycache__/` to `.gitignore`.

## General
- Official site: [pytest](https://pytest.org)
- [pytest at PyPI](https://pypi.org/project/pytest)

## Command Line
- `pytest <options> <test cases>`
- `poetry run pytest` recursively runs all tests in current directory. In the output, each dot after a test file indicates a passed test case.
- `poetry run pytest tests/subdir1` recursively run tests only in specified folder
- `poetry run pytest tests/test_misc.py tests/test_thing.py` only run tests in specified file(s)
- `poetry run pytest tests/test_misc.py::test_some_test_case_name` runs a single test case
- `poetry run pytest tests/test_using_test_class.py::TestBasics` runs tests that are part of a class
- `poetry run pytest tests/test_using_test_class.py::TestBasics::test_some_testcase` run individual test from class

## Command Line Options
- `pytest -h` to see all the command line options
- `pytest -v` is verbose, will give you more details
- `pytest -s` show output of print() statements
- `pytest -vs` combine `-v` and `-s` for verbose and print() output
- `pytest -k TestMod` run tests matching name pattern
- `pytest --tb=short` for less traceback information in output
- `pytest --setup-show` shows the order of operations of tests and fixtures, including the setup and teardown phases of the fixtures
    - `SETUP    F` and `TEARDOWN F` are in the output, where the `F` means the fixture is using the function scope, meaning the fixture is called before each test function that uses it, and torn down after each function that uses it.
    - `SETUP    M` and `TEARDOWN M`, where the `M` means the fixture is using the module scope
    - `SETUP    S` and `TEARDOWN S`, where the `S` means the fixture is using the session scope
- `pytest --fixtures` shows list of available fixtures, incuding builtin fixtures we can use. Run from a particular directory (or supply a directory or file name) to see the visibility for that directory.  It also returns the first line of any docstring. Adding `-v` returns the entire docstring.
- `pytest --fixtures-per-test ` shows what fixtures are used by each test and where the fixtures are defined. Example: `pytest --fixtures-per-test test_thing.py::test_something`

- `pytest -rP` shows the captured output of passed tests.
- `pytest -rx` shows the captured output of failed tests (default behaviour).
- `pytest -rA` shows the captured output of all tests.
- The formatting of the output is prettier with -r than with -s.

## Fixtures
- [pytest builtin fixtures](https://docs.pytest.org/en/latest/reference/fixtures.html)

## Test Results
- Fail: An exception or assert failure within the test case itself
- Error: An excepction or some failure with a test fixture
- `>` in output indicates line where failure occurred.
- `E` lines in ouput give extra info about failure




## Run Tests
- `poetry run pytest --tb=short` uses `--tb=short` to shorten the traceback of what exception was raised
- `poetry run pytest --setup-show` shows the order of execution of fixture and test case code
- `poetry run pytest --fixtures` shows a list of available fixtures a test can use
- `poetry run pytest --fixtures-per-test tests/test_misc.py::test_get_test_case_name` shows fixtures used for a particular test, file, or folder

## Notes
- `assert` is a keyword that is part of Python, not Pytest
- An exception that happens in the test case code results in a “Fail” result.
- An exception that happens in the test fixture code results in an “Error” result.
- Fixtures return data with `return` or `yield`.
- In a fixture, code before a `yield` statement is 'setup' code, and code after the `yield` is 'tear down' code and is run even if the test case fails or throws an exceptiion
- The values for fixture scope: function, class, module, package, session. Scope is set in the fixture definition, not the test.
- Fixtures can depend on other fixtures of same or wider scope.
- Instead of including `-s` for pytest to display the output of `print()` statements, you can use the pytest built-in fixture `capsys` which will show output even if `-s` isn't used.

## Resources
- [Pytest official site](https://docs.pytest.org)