import os
import sys
import shutil
import importlib

from core.config_mgt import *
from .log_mgt import *
# 获取文件所在目录并更改程序工作路径
run_path = os.path.dirname(os.path.realpath(__file__)) # 获取程序所在的原始运行目录
temp_path = os.path.dirname(os.path.realpath(sys.argv[0])) # 获取pyc预编译文件所在目录
logger.debug(f'程序原始运行目录：{run_path}\n程序实际运行目录：{temp_path}')
if run_path != temp_path: # 判断预编译文件是否与程序于同一目录，使pyinstaller打包程序后仍能正常加载插件
    shutil.copytree(f'{run_path}/plugin',f'{temp_path}')

class Plugin_Mgt():
    all_plugin=[]
    enable_plugin=[]
    def Get_Plugin(path:str='./plugin'):
        '''【获取插件目录下的所有有效插件并存储到Plugin_Mgt.all_plugin】
        注意：当前版本只能执行一次'''
        files_name=os.listdir(path)
        for file_name in files_name:
            if os.path.isfile(f'./plugin/{file_name}/__init__.py'):
                Plugin_Mgt.all_plugin.append(file_name)
        for plugin in Plugin_Mgt.all_plugin:
            if Config_Mgt.all_config['plugin']['plugin_enable'] != '':
                #TODO
                pass
        
    def Load_Plugin():
        #TODO
        importlib.import_module('plugin') 