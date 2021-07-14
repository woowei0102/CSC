# Python AST
[![Python](https://img.shields.io/badge/python-3.8.0-blue.svg?style=popout)](https://www.python.org/downloads/release/python-380/)

## 介紹
如果想看python程式的抽象語法樹形式，我有寫一個小程式可給你們使用。
## Supported Language
- [x] Python

## 使用方式
~~~python=
# git clone my repository and go to this file.
git clone https://github.com/woowei0102/CSC.git
cd .\CSC\Python_AST\

# The testcase must be a "python file"
 py .\ast_present.py .\testcase.py
~~~

## 範例

### use
~~~python
 py .\ast_present.py .\test.py
~~~

### output
~~~python=
Module(body=[
    Assign(targets=[
        Name(id='i', ctx=Store()),
      ], value=Constant(value=0, kind=None), type_comment=None),
  ], type_ignores=[])
~~~


