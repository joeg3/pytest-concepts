# pytest-concepts

## Project Initialization with Poetry
- First I created a Git project with only this README.md file.
- Next, I ran `poetry init` and only added the `pytest` dependency. This created the `pyproject.toml` file.
- Next, I ran `poetry install` to install the dependency packages defined in `pyproject.toml`. This created the `poetry.lock` file.
- Next, I created a `.gitignore` file and added a `/poetry.lock` entry to it.
- Next, I created `tests/test_basics.py` and added a simple test case. I also added an empty `tests/__init__.py` file.
- Finally I ran the test case: `poetry run pytest -vs tests/test_basics.py`, which created a `tests/__pycache__` file. I added `__pycache__/` to `.gitignore`.

## Run Tests
- `poetry run pytest` recursively runs all tests in current directory. In the output, each dot after a test file indicates a passed test case.
- `poetry run pytest -v` runs in verbose mode
- `poetry run pytest -s` use to see output of print functions
- `poetry run pytest tests/subdir1` recursively run tests only in specified folder
- `poetry run pytest tests/test_misc.py` only run tests in specified file
- `poetry run pytest tests/test_misc.py::test_get_test_case_name` runs a single test case
- `poetry run pytest tests/test_using_test_class.py::TestBasics` runs tests that are part of a class
- `poetry run pytest tests/test_using_test_class.py::TestBasics::test_some_testcase` run individual test from class
- `poetry run pytest --tb=short` uses `--tb=short` to shorten the traceback of what exception was raised
- `poetry run pytest --setup-show` shows the order of execution of fixture and test case code
- `poetry run pytest --fixtures` shows a list of available fixtures a test can use
- `poetry run pytest --fixtures-per-test tests/test_misc.py::test_get_test_case_name` shows fixtures used for a particular test, file, or folder

## Notes
- `assert` is a keyword that is part of Python, not Pytest
- An exception that happens in the test case code results in a “Fail” result.
- An exception that happens in the test fixture code results in an “Error” result.
- Fixtures return data with `return` or `yield`.
- In a fixture, code before a `yield` statement is 'setup' code, and code after the `yield` is 'tear down' code and is run even if the test case throws an exceptiion
- The values for fixture scope: function, class, module, package, session. Scope is set in the fixture definition, not the test.
- Fixtures can depend on other fixtures of same or wider scope.

## Resources
- [Pytest official site](https://docs.pytest.org/en/7.1.x)