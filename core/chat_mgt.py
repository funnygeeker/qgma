import socket
import requests  # 需要安装
from core.log_mgt import *
from urllib import parse

from core.settings_load import *


def send_msg_private(user_id, msg):  # 发送消息【对方QQ号），消息内容】
    server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_client.connect((server_ip, server_send_port))
    # 将字符中的特殊字符进行url编码
    # msg = msg.replace(" ", "%20") #已弃用
    # msg = msg.replace("\n", "%0a") #已弃用
    msg = parse.quote(msg, safe='')
    payload = "GET /send_private_msg?user_id=" + str(user_id) + "&message=" + msg + " HTTP/1.1\r\nHost:" + str(
        server_ip) + ":" + str(server_send_port) + "\r\nConnection: close\r\n\r\n"
    server_client.send(payload.encode("utf-8"))
    print("【私聊】" + str(user_id), "发送：\n" + parse.unquote(msg))
    server_client.close()
    return 0


def send_msg_group(group_id, msg):  # 发送消息【对方群号，消息内容】
    server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_client.connect((server_ip, server_send_port))
    # 将字符中的特殊字符进行url编码
    # msg = msg.replace(" ", "%20") #已弃用
    # msg = msg.replace("\n", "%0a") #已弃用
    msg = parse.quote(msg, safe='')
    payload = "GET /send_group_msg?group_id=" + str(group_id) + "&message=" + msg + " HTTP/1.1\r\nHost:" + str(
        server_ip) + ":" + str(server_send_port) + "\r\nConnection: close\r\n\r\n"
    server_client.send(payload.encode("utf-8"))
    print("【群聊】" + str(group_id), "发送：\n" + parse.unquote(msg))
    server_client.close()
    return 0


def del_msg(msg_id):  # 撤回消息【消息ID】
    server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_client.connect((server_ip, server_send_port))
    payload = "GET /delete_msg?message_id=" + str(msg_id) + " HTTP/1.1\r\nHost:" + str(
        server_ip) + ":" + str(server_send_port) + "\r\nConnection: close\r\n\r\n"
    server_client.send(payload.encode("utf-8"))
    print("【撤回】" + str(msg_id))
    server_client.close()
    return 0


def group_kick(group_id, user_id, reject_add_request='false'):  # 踢出成员【群号，QQ号，屏蔽加群申请】
    server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_client.connect((server_ip, server_send_port))
    payload = "GET /set_group_kick?group_id=" + str(group_id) + "&user_id=" + str(user_id) + "&reject_add_request=" + str(
        reject_add_request) + " HTTP/1.1\r\nHost:" + str(server_ip) + ":" + str(server_send_port) + "\r\nConnection: close\r\n\r\n"
    server_client.send(payload.encode("utf-8"))
    print("【提示】群聊：" + str(group_id) + " 中，已踢出",
          str(user_id) + "，屏蔽加群申请：" + reject_add_request)
    server_client.close()
    return 0


def group_ban(group_id, user_id, duration=1):  # 禁言成员【群号，QQ号，禁言时长，单位：分】
    server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_client.connect((server_ip, server_send_port))
    payload = "GET /set_group_ban?group_id=" + str(group_id) + "&user_id=" + str(user_id) + "&duration=" + str(
        int(duration)*60) + " HTTP/1.1\r\nHost:" + str(server_ip) + ":" + str(server_send_port) + "\r\nConnection: close\r\n\r\n"
    server_client.send(payload.encode("utf-8"))
    print("【提示】群聊：" + str(group_id) + " 中，已禁言 " + str(user_id), duration, "分钟")
    server_client.close()
    return 0


def group_whole_ban(group_id, enable='false'):  # 全体禁言【群号，是否启用(true/false】
    server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_client.connect((server_ip, server_send_port))
    payload = "GET /set_group_whole_ban?group_id=" + str(group_id) + "&enable=" + str(
        enable) + " HTTP/1.1\r\nHost:" + str(server_ip) + ":" + str(server_send_port) + "\r\nConnection: close\r\n\r\n"
    server_client.send(payload.encode("utf-8"))
    print("【提示】群聊：" + str(group_id) + " 中，全体禁言已设为 " + str(enable))
    server_client.close()
    return 0


def set_group_add_request(flag: str, sub_type: str, approve: bool = True, reason: str = ''):
    '''flag: 加群请求的 flag（需从上报的数据中获得）
    sub_type: add 或 invite, 请求类型（需要和上报消息中的 sub_type 字段相符）
    approve: 是否同意请求／邀请
    reason: 拒绝理由（仅在拒绝时有效）'''
    try:
        return requests.post(url='http://'+server_ip+':'+str(server_send_port)+'/set_group_add_request', data={
            "flag": flag,
            'sub_type': sub_type,
            'approve': approve,
            'reason': reason})
    except:
        logger.warning('【警告】加群审批处理结果发送失败！')


def get_status():
    '获取go-cqhttp状态'
    try:
        #print('getting-------------')
        return requests.get(url='http://'+server_ip+':'+str(server_send_port)+'/get_status').json()['data']['online']
    except:
        #logger.warning('【警告】无法连接至go-cqhttp！')
        return None


'''示例
send_msg('private', user_id,'你好') # 私聊消息
send_msg('group', group_id, '大家好') # 群聊消息
send_msg('group', group_id, '
del_msg(msg_id) # 撤回消息【消息ID】
group_kick(group_id, user_id, false)  # 踢出成员【群号，QQ号，屏蔽加群申请】
group_ban(group_id, user_id, 1)  # 禁言成员【群号，QQ号，禁言时长，单位：分】
'''
