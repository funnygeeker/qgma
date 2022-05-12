#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Socket接收数据
# 作者：稽术宅（funnygeeker）
# QGMA项目交流QQ群：332568832
# 作者Bilibili：https://b23.tv/b39RG2r
# Github：https://github.com/funnygeeker/qgma
#
# 参考资料：
# 通过socket进行数据接收：https://blog.csdn.net/qq_44809707/article/details/119959864
# 超长socket数据接收：https://developer.aliyun.com/article/456224

import socket
import json


class Receive:
    'Socket接收数据，接收消息请使用Rev_Msg()函数'
    server_addr = '0.0.0.0'  # 默认监听ip
    server_event_port = 5701  # 默认监听端口
    ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ListenSocket.bind((server_addr, server_event_port))
    ListenSocket.listen(100)
    HttpResponseHeader = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

    def Reset_Listen_Port(server_addr, server_event_port):
        '重新设置监听端口'
        Receive.ListenSocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        Receive.ListenSocket.bind((server_addr, server_event_port))

    def Request_To_Json(msg):
        '将接收到的数据转化为json 返回：json'
        for i in range(len(msg)):
            if msg[i] == "{" and msg[-1] == "\n":
                return json.loads(msg[i:])
        else:
            return None

    def Rev_Msg():
        '【线程阻塞】接收的消息（没有进行过滤） 返回：json / None'
        Client, Address = Receive.ListenSocket.accept()
        # 长数据接收
        total_data = bytes()
        cycle_num = 0  # 循环计数，以防接收数据过长

        while True:
            # 将收到的数据拼接起来
            rev_data = Client.recv(1024)
            total_data += rev_data  # 与当前接收到的数据合并
            cycle_num += 1  # 循环次数计数
            if len(rev_data) < 1024:  # 如果数据接收完成
                Request = total_data.decode(encoding='utf-8')  # 解码接收到的数据
                rev_Json = Receive.Request_To_Json(Request)  # 将接收到的数据转化为json
                Client.sendall((Receive.HttpResponseHeader).encode(
                    encoding='utf-8'))  # 返回接收成功状态码
                Client.close()  # 断开连接
                #print(rev_json)#
                return rev_Json
            elif cycle_num >= 1024:
                Client.close()  # 断开连接
                return None  # 数据过长（大于1024kb）的返回内容


if __name__ == '__main__':
    while True:
        # 对消息进行过滤
        try:
            rev = Receive.Rev_Msg()
            print(rev)
            if rev == None:
                continue
        except:
            continue
        print(str(rev)+'\n--------------------------')
        #Receive.Reset_Listen_Port('0.0.0.0', 5700)
