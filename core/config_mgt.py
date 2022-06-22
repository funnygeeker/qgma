from configobj import ConfigObj
from core.text_mgt import *
import threading
lock=threading.Lock()

class Config_Mgt():
    '【存储设置变量及设置操作函数】'
    all_config = {}
    '所有设置'
    all_send = {}
    '所有发送语句'
    all_words = {}
    '所有词库'
    server_addr = ''
    'GO-CQHTTP服务器所在的IP地址'
    server_send_port = ''
    'GO-CQHTTP服务器接收QGMA指令的API端口'

    def Read_Config(file_path: str, encoding: str = '') -> dict:
        '''【读取设置文件】返回：dict'''
        if encoding == '':  # 如果没有设置读取文件的编码
            encoding = Text_Mgt.Encodeing_Detect(file_path=file_path)
        return ConfigObj(file_path, encoding=encoding)

    def Load_Config():
        '''【读取并加载配置文件到变量】'''
        # 读取ini配置文件
        conf_folder_path = './config/conf'
        files_name = os.listdir(conf_folder_path)  # 获取文件夹下的所有文件和文件夹名称
        with lock:
            for file_name in files_name:  # 遍历文件夹
                # 判断是否为需要读取的后缀
                if ((os.path.splitext(file_name)[1]).lower() == '.ini') and os.path.isfile(f'{conf_folder_path}/{file_name}'):
                    # 读取所有.ini文件扩展名的文件，并以{文件名(str):内容(dict)}的形式载入字典
                    Config_Mgt.all_config[os.path.splitext(file_name)[1]] = Config_Mgt.Read_Config(file_path=f'{conf_folder_path}/{file_name}')
                    # 判断是否为文件，小写处理文件扩展名，确定是否为需要读取的文件，并进行读取
        # 读取txt配置文件(send文件夹)
        send_folder_path = './config/send'
        dirs_name = os.listdir(send_folder_path)  # 获取文件夹下的所有文件和文件夹名称
        with lock:
            for dir_name in dirs_name:  # 遍历文件夹
                if os.path.isdir(f'{send_folder_path}/{dir_name}'): # 判断是否为目录
                    # 读取目录下所有txt文件
                    Config_Mgt.all_send[f'{dir_name}'] = Text_Mgt.List_Read_TXT_Under_Folder(folder_path=f'{send_folder_path}/{dir_name}',return_mode='dict')
        # 读取txt配置文件(words文件夹)
        words_folder_path = './config/words'
        dirs_name = os.listdir(words_folder_path)  # 获取文件夹下的所有文件和文件夹名称
        with lock:
            for dir_name in dirs_name:  # 遍历文件夹
                if os.path.isdir(f'{words_folder_path}/{dir_name}'): # 判断是否为目录
                    # 读取目录下所有txt文件
                    Config_Mgt.all_words[f'{dir_name}'] = Text_Mgt.List_Read_TXT_Under_Folder(folder_path=f'{words_folder_path}/{dir_name}',return_mode='dict')


if __name__ == '__main__':
    # print(Config_Mgt.Read_Config('./config/settings.ini'))
    pass
