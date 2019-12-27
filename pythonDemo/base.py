# 注释
# 单行注释
# 第一个注释
print("hello, world") # 第二个注释
# 多行注释
# 第一个注释
# 第二个注释
print("hello, world")

# 缩进
# 正确示例
if True:
    print("True")
else:
    print("False")
# 错误示例
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
  print("False")

# 多行语句
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
# [],{},()的多行语句不需要加\
items = ['one', 'two', 'three',
        'four', 'five']

# 字符串
# 引号
str1 = '字符串一'
str2 = "字符串二"
str3 = """字符串三，
可以由多行组成"""

# 转义符
print("\\")
# 自然字符串
print(r"\n this is a line with \n")
# 处理unicode字符串
print(u"this is an unicode string")

# 输出 print
# 输出字符串
print('hello, world')
# 输出多个字符串
print('I','love', 'you')
# 输出数字及计算
print(1)
print(1 + 2)
print('1 + 2 = ',1 + 2)
# 不换行输出
print(1, end=' ')
print(2, end=' ')

