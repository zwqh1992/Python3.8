#!/usr/local/bin/python3.8
# 运算符
print('——————————以下是算术运算符——————————')
# 算术运算符
a = 10
b = 3
c = 0  # 该变量用于表示 a 与 b 计算的结果

c = a + b
print('a + b =', c)  # a + b = 13
c = a - b
print('a - b =', c)  # a - b = 7
c = a * b
print('a * b =', c)  # a * b = 30
c = a / b
print('a / b =', c)  # a / b = 3.3333333333333335
# d = b / 0 除数不能为0，否则会报错
c = a % b
print('a % b =', c)  # a % b = 1
c = a ** b
print('a ** b =', c)  # a ** b = 1000
c = a // b
print('a // b =', c)  # a // b = 3
c = -a // b
print('-a // b =', c)  # -a // b = -4

print('——————————以下是比较运算符——————————')
# 比较运算符
a = 10
b = 3
c = 0  # 该变量用于表示 a 与 b 比较的结果

c = a == b
print('a == b : ', c)  # a == b :  False
c = a != b
print('a != b : ', c)  # a != b :  True
c = a > b
print('a > b : ', c)  # a > b :  True
c = a < b
print('a < b : ', c)  # a < b :  False
c = a >= b
print('a >= b : ', c)  # a >= b :  True
c = a <= b
print('a <= b : ', c)  # a <= b :  False

print('——————————以下是赋值运算符——————————')
# 赋值运算符
a = 10
b = 3
c = 3

c = a + b
print('c = a + b, c 为', c)  # c = a + b, c 为 13

c = 3
c += a
print('c += a，c 为', c)  # c += a，c 为 13

c = 3
c -= a
print('c -= a，c 为', c)  # c -= a，c 为 -7

c = 3
c *= a
print('c *= a，c 为', c)  # c *= a，c 为 30

c = 3
c /= a
print('c /= a，c 为', c)  # c /= a，c 为 0.3

c = 3
c %= a
print('c %= a，c 为', c)  # c %= a，c 为 3

c = 3
c **= a
print('c **= a，c 为', c)  # c **= a，c 为 59049

c = 3
c //= a
print('c //= a，c 为', c)  # c //= a，c 为 0

if (b := len('zwqh')) > 2:  # 赋值表达式可以避免调用 len() 两次
    print(f"字符串的长度为{b}，大于2输出")

print('——————————以下是位运算符——————————')
# 位运算符
a = 60  # 二进制 0011 1100
b = 13  # 二进制 0000 1101
c = 0

c = a & b  # 0000 1100
print('a & b =', c)  # a & b = 12
c = a | b  # 0011 1101
print('a | b =', c)  # a | b = 61
c = a ^ b  # 0011 0001
print('a ^ b =', c)  # a ^ b = 49
c = ~ a    #  1100 0011
print('~ a =', c)  # ~ a = -61
c = a << 2  # 1111 0000
print('a << 2 =', c)  # a << 2 = 240
c = a >> 2  # 0000 1111
print('a >> 2 =', c)  # a >> 2 = 15

print('——————————以下是逻辑运算符——————————')
# 逻辑运算符
# 布尔
a = True
b = False

if a and b:
    print('变量 a 和 b 都为 True')
else:
    print('变量 a 和 b 有一个不为 True')

if a or b:
    print('变量 a 和 b 都为 True，或其中一个变量为 True')
else:
    print('变量 a 和 b 都不为 true')

if not a:
    print('变量 a 为 False')
else:
    print('变量 a 为 True')

# 字符串
c = ''  # 相当于 False
d = 'zwqh'  # 相当于 True

if c and d:
    print('变量 c 和 d 都为 True')
else:
    print('变量 c 和 d 有一个不为 True')

if c or d:
    print('变量 c 和 d 都为 True，或其中一个变量为 True')
else:
    print('变量 c 和 d 都不为 true')

if not c:
    print('变量 c 为 False')
else:
    print('变量 c 为 True')

# 数字
e = 0  # 相当于 False
f = 20 # 相当于 True

if e and f:
    print('变量 e 和 f 都为 True')
else:
    print('变量 e 和 f 有一个不为 True')

if e or f:
    print('变量 e 和 f 都为 True，或其中一个变量为 True')
else:
    print('变量 e 和 f 都不为 true')

if not e:
    print('变量 e 为 False')
else:
    print('变量 e 为 True')

print('——————————以下是成员运算符——————————')
# 成员运算符
l = [1, 2, 3, 4, 5]
a = 4
b = 6

if a in l:
    print('变量 a 在列表 l 中')
else:
    print('变量 a 不在列表 l 中')

if b not in l:
    print('变量 b 不在列表 l 中')
else:
    print('变量 b 在列表 l 中')

print('——————————以下是身份运算符——————————')
# 身份运算符
a = 10
b = 10
c = 20

if a is b:
    print('a 和 b 有共同标识')
else:
    print('a 和 b 没有共同标识')

if id(a) is id(b):
    print('a 和 b 有共同标识')
else:
    print('a 和 b 没有共同标识')

if a is c:
    print('a 和 c 有共同标识')
else:
    print('a 和 c 没有共同标识')

if a is not c:
    print('a 和 c 没有共同标识')
else:
    print('a 和 c 有共同标识')
