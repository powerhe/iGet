import itchat
# import全部消息类型
from itchat.content import *

import xlwt

from xlrd import open_workbook
from xlutils.copy import copy

import time

number = 0

def updatexl(Number,Time,Nickname,Content):
    # 打开文件
    rb = open_workbook("example.xls")
    # 复制
    wb = copy(rb)
    # 选取表单
    s = wb.get_sheet(0)
    # 写入数据
    s.write(Number, 0, Number)
    s.write(Number, 1, '%s:%s' % (Time.tm_hour,Time.tm_min))
    s.write(Number, 2, Nickname)
    s.write(Number, 3, Content)
    # 保存
    wb.save('example.xls')

# 处理文本类消息
# 包括文本、位置、名片、通知、分享
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # 微信里，每个用户和群聊，都使用很长的ID来区分
    # msg['FromUserName']就是发送者的ID
    # 将消息的类型和文本内容返回给发送者
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

# 处理多媒体类消息
# 包括图片、录音、文件、视频
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    # msg['Text']是一个文件下载函数
    # 传入文件名，将文件下载下来
    msg['Text'](msg['FileName'])
    # 把下载好的文件再发回给发送者    
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

# 处理好友添加请求
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.add_friend(**msg['Text']) 
    # 加完好友后，给好友打个招呼
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

# 处理群聊消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        global number
        number = number + 1
        #itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
        print(msg.fromUserName)
        print(msg.CreateTime)
        # 将其转换为时间数组  
        timeArray = time.localtime(msg.CreateTime) 
        print ("本地时间为 :", timeArray)
        updatexl(number,timeArray,msg['ActualNickName'], msg['Content'])

# 在auto_login()里面提供一个True，即hotReload=True
# 即可保留登陆状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(True)
itchat.run()
