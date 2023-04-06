import json, os

def read_json_from_file(filename: str, encoding: str = "utf-8", buffer_size: int = -1):
    """
    从文件中读取 JSON 数据并返回解析后的 Python 对象。

    Args:
        filename: 要读取的文件名。
        encoding: 文件的编码格式，默认为 UTF-8。
        buffer_size: 读取文件时使用的缓冲区大小（以字节为单位），默认为系统默认值。

    Returns:
        解析后的 Python 对象。
    """
    # 检查参数是否合法
    if not isinstance(filename, str) or filename == "":
        raise ValueError("Invalid filename: {filename}")

    # 获取文件路径
    path = os.path.join(os.path.dirname(__file__), filename)

    # 读取文件内容
    with open(path, "r", encoding=encoding, buffering=buffer_size) as f:
        json_str = f.read()

    # 解析 JSON 数据
    return json.loads(json_str)
