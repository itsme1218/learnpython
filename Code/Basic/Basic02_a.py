'''
功能：使用print函数连续输出多个字符串
重点：字符串的连接、print函数的sep参数
作者：薛景
最后修改于：2019/05/24
'''

name = input("请输入你的姓名：")    

# 方案一，将若干需要输出的字符串使用连接符号“+”连起来
print(name + "你好，欢迎你加入Python的大家庭！")

# 方案二，在print函数的参数中加一个表示分隔符的参数sep，并将该参数的内容设置为空字符串
# 所谓空字符串，就是一个里面什么都没有的字符串，用一对引号表示
print(name, "你好，欢迎你加入Python的大家庭！", sep="")