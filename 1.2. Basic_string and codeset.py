# https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896
# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符

print('中:', ord('中'), '\t中+3:', chr(ord('中')+3))
#中: 20013       中+3: 丰