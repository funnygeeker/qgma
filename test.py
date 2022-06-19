from core.api_mgt import *
from core.log_mgt import *
from core.function import *
Log_Mgt.Log_Conf()
Config_Mgt.server_addr='0.0.0.0'
Config_Mgt.server_send_port=5700
print(Api.get_status())