import json
import tempfile
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils import read_json_from_file

@pytest.fixture
def sample_json_data():
    return {
        "name": "John Smith",
        "age": 42,
        "email": "john.smith@example.com"
    }


@pytest.fixture
def sample_json_file(sample_json_data):
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        json.dump(sample_json_data, f)
        f.flush()
        return f.name


def test_read_json_from_file(sample_json_data, sample_json_file):
    # 读取存在的文件
    assert read_json_from_file(sample_json_file) == sample_json_data

    # 读取不存在的文件
    with pytest.raises(FileNotFoundError):
        read_json_from_file("not-exist.json")

    # 传递无效的参数
    with pytest.raises(ValueError):
        read_json_from_file("")

    # 读取 UTF-16 编码的文件
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-16") as f:
        json.dump(sample_json_data, f)
        f.flush()
        assert read_json_from_file(f.name, encoding="utf-16") == sample_json_data

    # 读取文件时使用缓冲区
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        json.dump(sample_json_data, f)
        f.flush()
        assert read_json_from_file(f.name, buffer_size=1024) == sample_json_data
