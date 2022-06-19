import requests
from core.log_mgt import *
from core.function import *
from core.config_mgt import *

class Cq_Set():
    def set_group_kick(group_id: int, user_id: int, reject_add_request: bool = False):
        '''【群组踢人】
        group_id:群号
        user_id:要踢的QQ号
        reject_add_request:拒绝此人的加群请求
        返回: dict/None'''
        try:
            result = requests.post(
                url=f'http://{Config_Mgt.server_addr}:{Config_Mgt.server_send_port}/set_group_kick',
                data={
                    'group_id': group_id,
                    'user_id': user_id,
                    'reject_add_request': reject_add_request
                }).text  # 调用GO-CQHTTP的API，其中的requests也会记录debug日志
            result = Function.Data_To_Dict(result)  # 将返回的结果转换为:dict/None
            logger.info(
                f"【信息】群聊 {group_id} 中，已踢出：{user_id}（屏蔽加群申请：{reject_add_request}）")  # 记录日志
            return result
        except:
            logger.error(Log_Mgt.Get_Error())  # 出现错误则记录错误日志，返回None
            return None

    def set_group_anonymous_ban(group_id: int, anonymous: dict={},flag:str='', duration: int = 30*60):
        '''【群组匿名用户禁言】
        group_id:群号
        anonymous:可选,要禁言的匿名用户对象（群消息上报的 anonymous 字段）
        flag:可选,要禁言的匿名用户的 flag（需从群消息上报的数据中获得）
        duration:禁言时长,单位秒,无法取消匿名用户禁言
        返回: dict/None'''
        try:
            result = requests.post(
                url=f'http://{Config_Mgt.server_addr}:{Config_Mgt.server_send_port}/set_group_anonymous_ban',
                data={
                    'group_id': group_id,
                    'anonymous':anonymous,
                    'flag': flag,
                    'duration': duration
                }).text  # 调用GO-CQHTTP的API，其中的requests也会记录debug日志
            result = Function.Data_To_Dict(result)  # 将返回的结果转换为:dict/None
            logger.info(
                f"【信息】群聊 {group_id} 中，已禁言匿名用户：{anonymous['flag']['name']}，时长：{duration}秒（{duration/60}分钟）")  # 记录日志
            return result
        except:
            logger.error(Log_Mgt.Get_Error())  # 出现错误则记录错误日志，返回None
            return None

    def set_group_ban(group_id: int, user_id: int, duration: int = 30*60):
        '''【群组禁言】
        group_id:群号
        user_id:要禁言的QQ号
        duration:禁言时长,单位秒,0表示取消禁言
        返回: dict/None'''
        try:
            result = requests.post(
                url=f'http://{Config_Mgt.server_addr}:{Config_Mgt.server_send_port}/set_group_ban',
                data={
                    'group_id': group_id,
                    'user_id': user_id,
                    'duration': duration
                }).text  # 调用GO-CQHTTP的API，其中的requests也会记录debug日志
            result = Function.Data_To_Dict(result)  # 将返回的结果转换为:dict/None
            if duration != 0: logger.info(
                f"【信息】群聊 {group_id} 中，已禁言：{user_id}，时长：{duration}秒（{duration/60}分钟）")  # 记录日志
            else:
                logger.info(
                f"【信息】群聊 {group_id} 中，已解除禁言：{user_id}")  # 记录日志
            return result
        except:
            logger.error(Log_Mgt.Get_Error())  # 出现错误则记录错误日志，返回None
            return None

    def set_group_whole_ban(group_id: int, enable: bool):
        '''【群组全体禁言】
        group_id:群号
        enable:是否禁言
        返回: dict/None'''
        try:
            result = requests.post(
                url=f'http://{Config_Mgt.server_addr}:{Config_Mgt.server_send_port}/set_group_whole_ban',
                data={
                    'group_id': group_id,
                    'enable': enable
                }).text  # 调用GO-CQHTTP的API，其中的requests也会记录debug日志
            result = Function.Data_To_Dict(result)  # 将返回的结果转换为:dict/None
            logger.info(
                f"【信息】群聊 {group_id} 中，全体禁言已设为 {enable}")  # 记录日志
            return result
        except:
            logger.error(Log_Mgt.Get_Error())  # 出现错误则记录错误日志，返回None
            return None

    def set_group_admin(group_id: int,user_id: int, enable: bool):
        '''【群组设置管理员】
        group_id:群号
        user_id:要设置管理员的 QQ 号
        enable:True为设置,False为取消
        返回: dict/None'''
        try:
            result = requests.post(
                url=f'http://{Config_Mgt.server_addr}:{Config_Mgt.server_send_port}/set_group_admin',
                data={
                    'group_id': group_id,
                    'user_id':user_id,
                    'enable': enable
                }).text  # 调用GO-CQHTTP的API，其中的requests也会记录debug日志
            result = Function.Data_To_Dict(result)  # 将返回的结果转换为:dict/None
            logger.info(
                f"【信息】群聊 {group_id} 中，已将 {user_id} 的管理员身份设置为 {enable}")  # 记录日志
            return result
        except:
            logger.error(Log_Mgt.Get_Error())  # 出现错误则记录错误日志，返回None
            return None

    def set_group_add_request(flag: str,sub_type: str, approve: bool,reason:str='',group_id:int=0,user_id:int=0):
        '''【处理加群请求／邀请】
        flag:加群请求的 flag（需从上报的数据中获得）
        sub_type:add或invite,请求类型（需要和上报消息中的sub_type字段相符）
        approve:是否同意请求/邀请
        reason:拒绝理由（仅在拒绝时有效）

        可选参数：
        group_id:群号，用于控制台输出信息（一般为事件中的group_id）
        user_id:加群用户，用于控制台输出信息（一般为事件中的user_id）
        返回: dict/None'''
        try:
            result = requests.post(
                url=f'http://{Config_Mgt.server_addr}:{Config_Mgt.server_send_port}/set_group_admin',
                data={
                    'flag': flag,
                    'sub_type':sub_type,
                    'approve': approve,
                    'reason':reason
                }).text  # 调用GO-CQHTTP的API，其中的requests也会记录debug日志
            result = Function.Data_To_Dict(result)  # 将返回的结果转换为:dict/None
            if group_id != 0 and user_id != 0: logger.info(
                f"【信息】群聊 {group_id} 中，已将 {user_id} 的加群申请设为 {approve}")  # 记录日志
            else:
                logger.info(
                f"【信息】已将加群申请设为 {approve}")  # 记录日志
            return result
        except:
            logger.error(Log_Mgt.Get_Error())  # 出现错误则记录错误日志，返回None
            return None