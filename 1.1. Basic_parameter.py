### integer ###
# Python可以处理任意大小的整数，包括负整数
print('十六进制 0xaabbcc :',0xaabbcc)

# Python允许在数字中间以_分隔
print(1_0000_0000_0000_0000 , 0xaa_bb_cc)

### float ###
# 把10用e替代，1.23x10^9就是1.23e9，或者12.3e8，0.000012可以写成1.2e^-5，等等
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。
print('0.1112e2 =' , 0.1112e2)
print('1112e-2 =' , 1112e-2)

# 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。

### String ###
# 字符串是以单引号'或双引号"括起来的任意文本
# 如果'本身也是一个字符，那就可以用""括起来
# \n表示换行，\t表示制表符
# 为了简化，Python还允许用r''表示''内部的字符串默认不转义
# 为了简化，Python允许用'''...'''的格式表示多行内容；如果是.py文件，不要...

print("I still remember that moment, \nwhen you said, \"I'm OK.\".")
#I still remember that moment,
#when you said, "I'm OK.".

print('''line 1\ttab1
line 2''')
#line 1  tab1
#line 2

print(r'\\\n')
#\\\n

### Boolean ###
# 布尔值可以用and、or和not运算。

print(True, 3<2)
#True False

print(True and 3<2)
#False

### None ###

### parameter ###
# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
# Python 是 动态语言，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量

a = 123     # a是整数
print(a)
a = 'ABC'   # a变为字符串
print(a)
#123
#ABC

#当我们写：a = 'ABC' 时，Python解释器干了两件事情：
#1. 在内存中创建了一个'ABC'的字符串；
#2. 在内存中创建了一个名为a的变量，并把它指向'ABC'。
#也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据

a = 'ABC'
b = a
a = 'XYZ'
print(b)
#ABC

# Python没有常量，在Python中，通常用全部大写的变量名表示常量
# 但事实上Python根本没有任何机制保证其不会被改变

### / ###
# 在Python中，有两种除法:
# 一种除法是/，/除法计算结果是浮点数
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数，只取结果的整数部分
# 所以Python还提供一个余数运算，可以得到两个整数相除的余数
# 无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的。

print(9/3,'|',10//3,'|',10%3)
#3.0 | 3 | 1

print(10.0//3)
#3.0

#-------------------------------------------------------------------------------------------
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,f,s1,s2,s3,s4)
#123 456.789 Hello, world Hello, 'Adam' Hello, "Bart" Hello,
#Lisa!