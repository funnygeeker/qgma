from api.cq_set import *
from api.cq_get import *
from core.log_mgt import *  # 导入日志管理器
from core.config_mgt import *  # 导入配置文件管理器

from api.cq_send import *

class Api(Cq_Send,Cq_Set,Cq_Get):
    pass

    
'''[CQ:face,id=174]表情
4酷 5哭 12调皮 13呲牙 14微笑 15难过 20偷笑 27尴尬 31骂 32疑问 33嘘 
39再见 97擦汗 174摊手 176皱眉 178斜眼笑 212托腮
更多参照：https://github.com/kyubotics/coolq-http-api/wiki/%E8%A1%A8%E6%83%85-CQ-%E7%A0%81-ID-%E8%A1%A8
语音[CQ:record,file=http://xxxx.com/1.mp3]
艾特[CQ:at,qq=user_id]踢了踢[CQ:poke,qq={}]
链接分享[CQ:share,url=http://baidu.com,title=百度]'''