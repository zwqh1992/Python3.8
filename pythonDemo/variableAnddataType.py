print('——————————以下是变量——————————')
# 变量
# 变量赋值
name = '朝雾轻寒'
print('name = ', name)

# 同时多个变量赋值
a = b = c = 1
print('a = ', a)
print('b = ', b)
print('c = ', c)

# 为多个变量赋值
a, b, c = 1, 2, 'zwqh'
print('a = ', a)
print('b = ', b)
print('c = ', c)

print('——————————以下是数字——————————')
# 数字 Number
var1 = 1
print('定义的var1：', var1)
del var1
# print('删除了var1：', var1)

print('——————————以下是字符串——————————')
# 字符串 String
# 定义
s = 'python'
print(s[1:5])
s = '我用Python'
print(s + '！！！')
print(s * 2)
# 切片
print(s[0])  # '我'
print(s[-1])  # 'n'
print(s[3:])  # 'ython'
print(s[:3])  # '我用P'
print(s[::-1])  # 'nohtyP用我'
# 替换,还可以用正则表达式替换
print(s.replace('Python', 'Java'))  # '我用Java'
# 查找，find()、index()、rfind()、rindex()
print(s.find('P'))  # 2,返回第一次出现的子字符串的下标
print(s.find('t', 2))  # 4 , 设定下标2开始查找
print(s.find('zwqh'))  # -1 , 查找不到返回-1
print(s.index('y'))  # 3 , 返回第一次出现的子串的下标
print(s.rfind('P'))  # 2 , 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1
print(s.rindex('P'))  # 2 , 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间
# print(s.index('p'))  # 不同与find(), 查找不到会抛出异常
# 大小写转换, upper()、lower()、swapcase()、capitalize()、istitle()、isupper()、islower()
print(s.upper())  # '我用PYTHON' , 转大写
print(s.lower())  # '我用python' , 转小写
print(s.swapcase())  # '我用pYTHON' , 大小写互转
print('python'.capitalize())  # 'Python' , 把首字母大写
print(s.istitle())  # True , 检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
print(s.isupper())  # False , 检测字符串中所有的字母是否都为大写
print(s.islower())  # False , 检测字符串中所有的字母是否都为小写
# 去除指定字符
print('000Python000'.strip('0'))  # 'Python' , strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
print('   Python   '.strip())  # 'Python'
print('123Python321'.strip('123'))  # 'Python' , 字符序列为 '123'
print('123Python321'.lstrip('123'))  # 'Python321' , lstrip()方法用于截掉字符串左边的空格或指定字符
print('123Python32123'.rstrip('312'))  # '123Python'  ,rstrip()方法用于删除 string 字符串末尾的指定字符（默认为空格）.
# 连接与分割，使用 + 连接字符串，每次操作会重新计算、开辟、释放内存，效率很低，所以推荐使用join
ss = ['2020', '01', '01', '00:00']
x = '-'.join(ss)
print(x)  # '2020-01-01-00:00'
y = x.split('-')
print(y)  # ['2020', '01', '01', '00:00']
# 格式化
print('%s:%s' % ('年龄', 25))  # '年龄 25'
print('{}:{}'.format('年龄', 25))  # '年龄 25'  推荐使用format格式化字符串
print('{0},{1},{0}'.format('年龄', 25))  # '年龄,25,年龄'
print('{name}:{value}'.format(name='年龄', value=25))  # '年龄:25'
# 编码与解码
s = '我用Python'
# encode 将字符转换为字节
print(s.encode())  # 默认编码是 UTF-8,输出： b'\xe6\x88\x91\xe7\x94\xa8Python'
print(s.encode('gbk'))  # 输出：b'\xce\xd2\xd3\xc3Python'
# decode s将字节转换为字符
print(s.encode().decode('utf8'))   # 输出 '我用Python'
print(s.encode('gbk').decode('gbk'))  # 输出 '我用Python'

print('——————————以下是列表——————————')
# 列表 List
list1 = ['name', 'zwqh', 'height', 175, 'weight', 65.5]
list2 = ['name', 'zwqx', 'age', '25']
print(list1)  # 输出完整列表
print(list1[1])  # 'zwqh'  输出列表的第一个元素
print(list1[2:4])  # ['height', 175] 输出第三个至第四个元素
print(list1[2:])   # ['height', 175, 'weight', 65.5] 输出从第三个开始至列表末尾的所有元素
print(list2 * 2)  # ['name', 'zwqx', 'age', '25', 'name', 'zwqx', 'age', '25']  输出列表两次
print(list1 + list2)  # ['name', 'zwqh', 'height', 175, 'weight', 65.5, 'name', 'zwqx', 'age', '25']  打印组合的列表
print(list1.count('age'))  # 0 获取元素出现的此数
print(list1.__len__()) # 6 获取列表长度
# 搜索
print(list1.index('zwqh'))  # 1 获取指定元素的下标
# 增加元素
list1.append('!!!')
print(list1)  # ['name', 'zwqh', 'height', 175, 'weight', 65.5, '!!!']
# 删除元素
list1.remove('!!!')
print(list1)  # ['name', 'zwqh', 'height', 175, 'weight', 65.5]

print('——————————以下是元组——————————')
# 元组 Tuple
tuple1 = ('name', 'zwqh', 'height', 175, 'weight', 65.5)
tuple2 = ('name', 'zwqx', 'age', '25')
print(tuple1)  # 输出完整元组
print(tuple1[1])  # 'zwqh'  输出元组的第一个元素
print(tuple1[2:4])  # ('height', 175) 输出第三个至第四个元素
print(tuple1[2:])  # ('height', 175, 'weight', 65.5) 输出从第三个开始至列表末尾的所有元素
print(tuple2 * 2)  # ('name', 'zwqx', 'age', '25', 'name', 'zwqx', 'age', '25') 输出元组两次
print(tuple1 + tuple2)  # ('name', 'zwqh', 'height', 175, 'weight', 65.5, 'name', 'zwqx', 'age', '25') 打印组合的元组
print(tuple1.index('zwqh'))  # 1 获取指定元素的下标
print(tuple1.count('age'))  # 0 获取元素出现的此数
print(tuple1.__len__())  # 6 获取元组长度

print('——————————以下是集合——————————')
# 集合 Sets
set1 = {'name', 'zwqh', 'height', 175, 'weight', 65.5}
set2 = {'name', 'zwqx', 'age', '25'}
print(set1)  # 输出完整集合
# 添加
set1.add('!!!')
print(set1)  # {65.5, 'name', 'zwqh', 'weight', 175, '!!!', 'height'} 这个输出是无序的，再次执行顺序就可能变了
# 删除
set1.remove('!!!')   # 用于移除指定的集合元素
print(set1)  # {65.5, 'height', 'weight', 175, 'name', 'zwqh'}
set2.discard('age')  # 用于移除指定的集合元素,该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会
print(set2)   # {'zwqx', 'name', '25'}

print('——————————以下是字典——————————')
# 字典 Dictionary
userInfo = {
    'username': '朝雾轻寒',
    'qq': '466595865',
    'gender': '男'
}
print(userInfo)  # {'username': '朝雾轻寒', 'qq': '466595865', 'gender': '男'}
print(userInfo['username'])  # '朝雾轻寒'  输出键为 'username' 的值
print(userInfo.keys())  # dict_keys(['username', 'qq', 'gender'])   输出所有键
print(userInfo.values())  # dict_values(['朝雾轻寒', '466595865', '男'])  输出所有值
print(len(userInfo))  # 3 输出字段长度

