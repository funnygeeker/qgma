import ast
import json
from core.log_mgt import *
class Function():
    def Match_List(list: list, text: str) -> bool:
        '''逐一匹配列表中的值是否包含在字符串中 返回:bool'''
        for i in list:  # 逐一匹配列表
            if str(i) in str(text):  # 如果文本在列表中
                return True
        else:
            return False
    
    def Data_To_Dict(data:str):
        '''【将str数据转换为dict形式】
        返回:dict/None'''
        logger.debug(data) # 日志记录原始结果
        try:
            return json.loads(data)
        except:
            # logger.warning(Log_Mgt.Get_Error())
            return None

    def Get_Message_Id(result):
        try:
            return result['data']['message_id']
        except:
            return None
        
