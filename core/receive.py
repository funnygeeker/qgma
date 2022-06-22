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


from core.function import *
import socket


class Receive():
    '''【Socket接收数据】
    接收消息请使用Rev_Msg()函数'''
    server_addr = '0.0.0.0'  # 默认监听ip
    server_receive_port = 5701  # 默认监听端口
    ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ListenSocket.bind((server_addr, server_receive_port))
    ListenSocket.listen(100)
    HttpResponseHeader = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

    def Reset_Listen_Port(server_addr:str, server_receive_port:int):
        '''【重新设置监听端口】
        server_addr:服务器地址
        server_receive_port:监听端口'''
        Receive.ListenSocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        Receive.ListenSocket.bind((server_addr, server_receive_port))

    def Request_To_Dict(msg:str):
        '''【将接收到的数据转化为dict】
        返回:dict'''
        all_text = msg.split('\n')
        all_text = [text.strip("\n") for text in all_text if text.strip("\n") != ""]
        for line in all_text:
            if line[0] == '{':
                return Function.Data_To_Dict(line)
        else:
            return None

    """def Request_To_Json(msg:str):
        '''【将接收到的数据转化为json】
        返回:dict'''
        for i in range(len(msg)):
            if msg[i] == "{" and msg[-1] == "\n":
                return json.loads(msg[i:])
        else:
            return None""" # 弃用，Request_To_Dict将代替此函数，效率提升200%（100000条7.5=>2.5秒）(启用日志则为18.5秒)

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
                #print(Request)
                rev_Json = Receive.Request_To_Dict(msg
                =Request)  # 将接收到的数据转化为json
                Client.sendall((Receive.HttpResponseHeader).encode(
                    encoding='utf-8'))  # 返回接收成功状态码
                Client.close()  # 断开连接
                #print(rev_json)#
                return rev_Json
            elif cycle_num >= 1024:
                Client.close()  # 断开连接
                return None  # 数据过长（大于1024kb）的返回内容


if __name__ == '__main__':
    '''while True:
        # 对消息进行过滤
        try:
            rev = Receive.Rev_Msg()
            print(rev)
            if rev == None:
                continue
        except:
            continue
        print(str(rev)+'\n--------------------------')'''
        #Receive.Reset_Listen_Port('0.0.0.0', 5700)
