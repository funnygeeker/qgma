import time
from core.settings_load import *
print('''---------------------正在初始化-------------------
--【欢迎使用：极客街-Q群管理助手-V1.1.0_220510】--
   ____   _____ __  __          
  / __ \ / ____|  \/  |   /\    
 | |  | | |  __| \  / |  /  \   
 | |  | | | |_ | |\/| | / /\ \  
 | |__| | |__| | |  | |/ ____ \ 
  \___\_\\\\_____|_|  |_/_/    \_\\
--------------------------------------------------
赞助作者-爱发电：https://afdian.net/@funnygeeker
作者Github：https://www.github.com/funnygeeker
作者B站个人主页：https://b23.tv/b39RG2r
作者技术社区官网：https://geekjie.com
Python小白早期作品，不喜勿喷！
感谢：QQ：98252***0的支持
项目交流QQ群：332568832
系统交流QQ群：759090242''')
time.sleep(2)
print('---------------------基本设置---------------------')
print('机器人QQ号:', bot_user_id)
print('需要管理的QQ群:', group_manage)
print('机器人管理员QQ号:', admin_user_id)
print('群聊宵禁时间范围:', curfew_time)
print('撤回禁言等任务执行周期:', task_cycle, '分')
print('异常场聊天报告发送周期:', report_cycle, '秒')
time.sleep(2)
print('---------------------服务设置---------------------')
print('GO-CQHTTP发送端口:', server_send_port)
print('GO-CQHTTP接收端口:', server_rec_port)
print('GO-CQHTTP服务所在IP:', server_ip)
time.sleep(2)
print('---------------------成员设置---------------------')
print('匹配增强:', matching_enhancement)
print('加群审批:', len(group_approval), '条')
print('入群欢迎:', len(welcome_tips), '条')
print('成员消息撤回间隔:', del_msg_time, '秒')
print('成员首次禁言次数:', gag_num, '次')
print('成员最大犯错次数:', fault_num, '次')
print('成员禁言规则列表:', gag_time)
time.sleep(2)
print('---------------------群管词库---------------------')
print('广告词库:', len(ads_word), '条')
print('脏话词库:', len(bad_word), '条')
print('广告消息提示:', len(ads_word_tips), '条')
print('脏话消息提示:', len(bad_word_tips), '条')
print('-----------------配置文件加载完毕-----------------')
time.sleep(1)
print('【信息】QQ群管助手1.1.0启动完成......')