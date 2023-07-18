![](https://img.shields.io/github/actions/workflow/status/GuoXiCheng/AnyToAnki/build-and-test.yml?branch=main)
![](https://img.shields.io/codecov/c/github/GuoXiCheng/AnyToAnki)

# AnyToAnki
将文档内容转换为Anki卡片

# 启用虚拟环境
## 创建虚拟环境
```
python -m venv env
```
## 激活虚拟环境
```
.\env\Scripts\activate
```
## 退出虚拟环境
```
deactivate
```
# 插件打包

## 压缩工具

首先确保你已经安装：*7zip*，可以去官网：https://www.7-zip.org/ 下载安装

其次要将安装后的目录添加至环境变量才可以使用7z命令

## 执行打包

执行*package.sh*文件会自动生成打包后的插件：*AnyToAnki.ankiaddon*

打开Anki软件，在菜单栏中选择 "工具" -> "插件"

在插件管理器中，点击 "本地安装" 按钮，然后选择你的 "AnyToAnki.ankiaddon" 文件

## 测试

测试: `pytest -s`

测试覆盖率: `pytest --cov=src`

## 切换镜像源

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
