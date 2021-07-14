# Code Smell Checker(CSC)

## 介紹
程式碼異味(code smell)是針對程式中裡的敘述寫法可能在未來進行更新或修改都會會引起嚴重的問題。我便從論文中去所提的檢測項目去進行實作，並針對python程式去作檢測，期望未來寫python程式的使用者能透過此程式進行檢測，使程式寫的越好。

## 使用方式
~~~python=
# git clone this repository and go to this file
git clone https://github.com/woowei0102/CSC.git
cd .\CSC

# Install the required packages
pip install -r requirements.txt

# The testcase must be a "python file"
py CSC.py .\testcase.py
~~~



## 檢測類型

### Large Class (LC)
#### 簡單介紹
class區塊內太多內容

#### 標準
* LOC >= 200 (LOC: lines of code)
* NOA+NOM > 40 (NOA: number of attributes; NOM: number of methods)

#### 程式碼
```python=
class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < amount:
            print('{}的存款不足.'.format(self.name))
        else:
            self.balance -= amount
    def show(self):
        print('{}餘額NT${}元'.format(self.name, self.balance))
```

### Long Parameter List (LPL)
#### 簡單介紹
函式或方法太多參數

#### 標準
* PAR >= 5 (PAR: number of parameters)

#### 程式碼
```python=
def long_function_name(  # NOTE: There should be NO parameter here
            var_one,
            var_two,
            var_three,
            var_four,
            var_five,# NOTE: You can still have a comma at the last line
            ):
    pass
```

### Long Method (LM)

#### 簡單介紹
method或方法區塊內太多內容

#### 標準
* MLOC >= 100 (MLOC: method lines of code)

#### 程式碼
```python=
def factorial(n):
    sum=1
    for i in range(1, n + 1):
        sum *= i
    return sum
print(factorial(10))
```

### Long Message Chain (LMC)

#### 簡單介紹
A物件呼叫B物件，而B物件呼叫C物件，這種呼叫方式，一旦更改裡面的內容，使用者也要做出改變，盡量得這種連續呼叫越少越好

#### 標準
* LMC >= 4 (LMC: length of message chain)

#### 程式碼
```python=
class A:
    def m(self, x, y):
        print(x+y)
class B:
    def call_a(self):
        return A()
class C:
    def call_b(self):
        return B()	

C().call_b().call_a().m(1,2)
```

### Long Scope Chaining (LSC)

#### 簡單介紹
函式或方法內裡面也有多個函式或方法

#### 標準
* DOC >= 3 (DOC: depth of closure)

#### 程式碼
```python=
# Python program showing
# a scope of object
 
def some_func():
    var = 5
    print("Inside some_func")
    def some_inner_func():
        var = 10
        print("Inside inner function, value of var:",var)
    some_inner_func()
    print("Try printing var from outer function: ",var)
some_func()
```

### Long Base Class List (LBCL)

#### 簡單介紹
不能繼承太多

#### 標準
* NBC >= 3 (NBC: number of base classes)

#### 程式碼
```python=
class BaseClass(Object):
    def __init__(self, value):
        self.value = value
        print('Init BaseClass')
        print('value is :{0}'.format(self.value))

class TimesTwo(object):
    def __init__(self):
        self.value *=2
        print('Init TimesTwo')
        print('value is :{0}'.format(self.value))        
        
class PlusFive(object):
    def __init__(self):
        self.value +=5
        print('Init PlusFive')
        print('value is :{0}'.format(self.value))     
        
class SubClass(BaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        BaseClass.__init(self.value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)
        
subclass = SubClass(1)
print(subclass.value)
```

### Useless Exception Handling (UEH)

#### 簡單介紹
例外內容不能太廣泛，要針對各個例外解決

#### 標準
* (NEC = 1 and NGEC = 1) (NEC: number of except clauses; NGEC: number of general exception clauses) -> general exception clauses: 太籠統的例外事件 ex. Exception、StandardError
* NEC = NEEC (NEEC: number of empty except clauses) -> NEEC就是說except內容是空內容(pass)

#### 程式碼
```python=
try:
  print("Hello")
except:
  pass
```

### Long Lambda Function (LLF)

#### 簡單介紹
lambda內不能太多內容

#### 標準
* NOC >= 80 (NOC: number of characters in one expression)

#### 程式碼
```python=
max = lambda m, n: m if m > n else n
print(max(10, 3))  # 顯示 10
```

### Complex List Comprehension (CLC)

#### 簡單介紹
List內的運算式不能太複雜

#### 標準
* NOL + NOCC >= 4 (NOL: number of loops; NOCC: number of control conditions)

#### 程式碼
```python=
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```

### Long Element Chain (LEC)

#### 簡單介紹
跟LMC很像，不過是透過bracket operator

#### 標準
* LEC >= 3 (LEC: length of element chain)

#### 程式碼
```python=
A = [[0, [1, 2, 3], 2], 1, 2]
print([A[0][1][2]])
```

### Long Ternary Conditional Expression (LTCE)

#### 簡單介紹
三元運算式不能過長

#### 標準
* NOC >= 40 (NOC: number of characters in one expression)

#### 程式碼
```python=
def max(a, b):
    return a if a > b else b

print(max(1, 2))
```

## 結論
我透過python ast靜態分析的方式，把該論文所提的項目都有作出來，只差提供給使用者的介面顯示，在未來上會針對這點進行更新，給予使用者最好的使用回饋。

## 相關文件
* [Detecting Code Smells in Python Programs](https://ieeexplore.ieee.org/abstract/document/7780188)