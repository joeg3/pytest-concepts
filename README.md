# pytest-concepts

## Project Initialization with Poetry
- First I created a Git project with only this README.md file.
- Next, I ran `poetry init` and only added the `pytest` dependency. This created the `pyproject.toml` file.
- Next, I ran `poetry install` to install the dependency packages defined in `pyproject.toml`. This created the `poetry.lock` file.
- Next, I created a `.gitignore` file and added a `/poetry.lock` entry to it.
- Next, I created `tests/test_basics.py` and added a simple test case. I also added an empty `tests/__init__.py` file.
- Finally I ran the test case: `poetry run pytest -vs tests/test_basics.py`, which created a `tests/__pycache__` file. I added `__pycache__/` to `.gitignore`.
