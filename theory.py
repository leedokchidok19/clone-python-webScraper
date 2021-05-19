a_string = 'like this' # str
a_number = 3 # int
a_float = 3.12 # float
a_boolean = False # boolean, 0 이외 정수는 모두 True
a_none = None # NoneType

# 파이썬은 snake case를 기본적으로 사용한다
# 예) super_long_variable
# 자바스크립트는 camel case를 기본적으로 사용한다

# sequence type(열거형 타입) : list, tuple
# list mutable sequence
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
print(days)
days.append('Sat')
days.reverse()
print(days)

# immutable sequence

# function_arguments
def plus(a, b):
  return a+b

# b=0 default value, 인자 기본값 설정 가능
def minus(a, b=0):
  return a-b

result = plus(2, 5)
print(result)
result = minus(2)
print(result)

# Keyword argument
# 인자 위치를 기억할 필요 없다
result = plus(b=2, a=5)
print(result)

def say_hello(name, age):
  return f'Hello {name} you are {age} years old'

hello = say_hello('lorem', '12')
print(hello)