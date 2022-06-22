from core.api_mgt import *
from core.log_mgt import *
from core.function import *
Log_Mgt.Log_Conf()
'''
Config_Mgt.server_addr='0.0.0.0'
Config_Mgt.server_send_port=5700
print(Api.set_group_ban(759090242,2804129672,30))
'''
from  core.receive import *
while True:
    # 对消息进行过滤
    try:
        rev = Receive.Rev_Msg()
        print(rev)
        if rev == None:
            continue
    except:
        continue
    print('\n--------------------------')
    #Receive.Reset_Listen_Port('0.0.0.0', 5700)'''

