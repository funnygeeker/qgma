
import requests
from core.log_mgt import *
from core.function import *
from core.config_mgt import *


class Cq_Send():
    def send_msg_private(user_id: int, group_id: int = 0, message: str = '', auto_escape: bool = False):
        '''【发送私聊消息】
        user_id:对方QQ号
        group_id:主动发起临时会话群号(机器人本身必须是管理员/群主)
        message:要发送的内容
        auto_escape:消息内容是否作为纯文本发送(即不解析CQ码),只在message字段是字符串时有效
        返回: dict/None'''
        try:
            result = requests.post(
                url=f'http://{Config_Mgt.server_addr}:{Config_Mgt.server_send_port}/send_private_msg',
                data={
                    'user_id': user_id,
                    'group_id': group_id,
                    'message': message,
                    'auto_escape': auto_escape
                }).text  # 调用GO-CQHTTP的API，其中的requests也会记录debug日志
            result = Function.Data_To_Dict(result)  # 将返回的结果转换为:dict/None
            logger.info(
                f"【信息】私聊 {user_id} 发送：{message}（消息ID：{result['data']['message_id']}）")  # 记录日志
            return result
        except:
            logger.error(Log_Mgt.Get_Error())  # 出现错误则记录错误日志，返回None
            return None

    def send_group_msg(group_id: int, message: str = '', auto_escape: bool = False):
        '''【发送群消息】
        group_id:群号
        message:要发送的内容
        auto_escape:消息内容是否作为纯文本发送(即不解析CQ码),只在message字段是字符串时有效
        返回: dict/None'''
        try:
            result = requests.post(
                url=f'http://{Config_Mgt.server_addr}:{Config_Mgt.server_send_port}/send_group_msg',
                data={
                    'group_id': group_id,
                    'message': message,
                    'auto_escape': auto_escape
                }).text  # 调用GO-CQHTTP的API，其中的requests也会记录debug日志
            result = Function.Data_To_Dict(result)  # 将返回的结果转换为:dict/None
            logger.info(
                f"【信息】群聊 {group_id} 发送：{message}（消息ID：{result['data']['message_id']}）")  # 记录日志
            return result
        except:
            logger.error(Log_Mgt.Get_Error())  # 出现错误则记录错误日志，返回None
            return None

    def delete_msg(message_id: int):
        '''【撤回消息】
        message_id:消息ID
        返回: dict/None'''
        try:
            result = requests.post(
                url=f'http://{Config_Mgt.server_addr}:{Config_Mgt.server_send_port}/delete_msg',
                data={
                    'message_id': message_id
                }).text  # 调用GO-CQHTTP的API，其中的requests也会记录debug日志
            result = Function.Data_To_Dict(result)  # 将返回的结果转换为:dict/None
            logger.info(f'【信息】撤回 {message_id}')  # 记录日志
            return result
        except:
            logger.error(Log_Mgt.Get_Error())  # 出现错误则记录错误日志，返回None
            return None

    