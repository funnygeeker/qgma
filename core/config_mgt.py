from http import server
from configobj import ConfigObj
from core.text_mgt import *

class Config_Mgt():
    '存储设置变量及设置操作函数'
    all_config={}
    '所有设置'
    server_addr=''
    'GO-CQHTTP服务器所在的IP地址'
    server_send_port=''
    'GO-CQHTTP服务器接收QGMA指令的API端口'
    
    def Read_Config(file_path:str, encoding:str=''):
        '读取设置文件 返回：dict'
        if encoding == '':  # 如果没有设置读取文件的编码
            encoding = Text_Mgt.Encodeing_Detect(file_path=file_path)
        return ConfigObj(file_path, encoding=encoding)


if __name__ == '__main__':
    print(Config_Mgt.Read_Config('./config/settings.ini'))
