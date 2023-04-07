import os


def read_from_file(filename: str):
    """从文件中读取内容

    Args:
        filename: 文件名

    Returns:
        文件内容

    Raises:
        TypeError: 如果 filename 不是字符串类型
        ValueError: 如果 filename 为空字符串或不合法
        FileNotFoundError: 如果文件不存在或路径有误
        UnicodeDecodeError: 如果文件编码不是 utf-8

    """
    # 参数检查
    if not isinstance(filename, str):
        raise TypeError(f"Expected a string for filename, but got {type(filename)}")
    elif not filename.strip():
        raise ValueError("Invalid filename: filename must not be empty or whitespace only.")

    # 获取文件路径
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))

    # 读取文件内容
    with open(path, "r", encoding="utf-8") as f:
        file_str = f.read()

    return file_str
