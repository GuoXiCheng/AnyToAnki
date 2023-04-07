import os
import sys

import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils import read_from_file


@pytest.fixture
def file_contents():
    return "This is a test file."


def test_read_from_file(file_contents, tmp_path):
    # create test file
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_contents)

    # test read_from_file function
    result = read_from_file(str(file_path))
    assert result == file_contents
