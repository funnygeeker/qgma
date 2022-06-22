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
    
    def Num_Conversion(key,mode:str='int'):
        '''【数值转换】将字符串转换每隔一个空格拆分为列表
        '1 2 3 4' => [1,2,3,4]'''
        key = str(key).strip(' ').split(' ') # 先转为str形式以防配置为单数值时为int形式导致报错，除去两端的空格后进行分隔
        if mode == 'int':
            return [int(i) for i in key] # 将列表中的值转换回数字
        return key
        
