import requests
from time import *
from core.log_mgt import *
from core.function import *
from core.config_mgt import *
class Cq_Get():
    def get_status():
        '''【获取状态】
        常用返回的key值说明:
        online(表示BOT是否在线,bool)
        stat(运行统计,dict)
        返回: dict/None'''
        try:
            result = requests.post(
                url=f'http://{Config_Mgt.server_addr}:{Config_Mgt.server_send_port}/get_status').text  # 调用GO-CQHTTP的API，其中的requests也会记录debug日志
            result = Function.Data_To_Dict(result)  # 将返回的结果转换为:dict/None
            logger.debug(f"【尝试获取CQ-HTTP状态...】")  # 记录日志
            return result
        except:
            logger.error(Log_Mgt.Get_Error())  # 出现错误则记录错误日志，返回None
            return None
