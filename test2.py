compile("""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# QGMA日志管理模块
# 作者：稽术宅（funnygeeker）
# QGMA项目交流QQ群：332568832
# 作者Bilibili：https://b23.tv/b39RG2r
# Github：https://github.com/funnygeeker/qgma
# 参考资料：
# https://www.cnblogs.com/xyztank/articles/13599165.html
# Python日期格式化：https://www.cnblogs.com/pyxiaomangshe/p/7918850.html
# logging模块日志颜色及基本使用：https://blog.csdn.net/qq_36072270/article/details/105345562

import os
import logging
import colorlog  # 需安装，用于控制台彩色日志显示
import traceback
from logging.handlers import RotatingFileHandler
'''
# 使用Pyinstaller打包不可用，弃用
# 检查日志存放目录是否存在，不存在则创建
cur_path = os.path.dirname(os.path.realpath(__file__))  # 当前项目路径
# log_path为存放日志的路径，'logs'为创建的文件夹名
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)  # 若不存在logs文件夹，则自动创建
'''

logger = logging.getLogger()


class Log_Mgt:
    '日志管理模块：首次运行时使用‘Log_Conf’函数初始化后，使用已实例化的‘logger’对象记录日志'

    def Log_Conf(log_file_name='QGMA.log', file_log_level=10, console_log_level=20, max_bytes=1*1024*1024, backup_count=2):
        '日志设置：日志文件名，文件日志等级(NOTICE=0,DEBUG=10,INFO=20,WARNING=30,ERROR=40,CRITICAL=50)，控制台日志等级，最大单个日志大小，日志拆分次数（不能为0，1为2份，2为3份，以此类推）'
        global logger
        # logger = builtins.logger = logging.getLogger() # 已弃用，使logger可以全局调用

        # cur_path = os.path.dirname(os.path.realpath(__file__))  # 当前项目路径
        # log_path为存放日志的路径，'logs'为创建的文件夹名
        #log_path = os.path.join(os.path.dirname(cur_path), 'logs')
        log_path = os.path.join(os.path.dirname('.'), 'logs')
        if not os.path.exists(log_path):
            os.mkdir(log_path)  # 若不存在logs文件夹，则自动创建

        # 检查日志文件名是否合法
        log_file_name = str(log_file_name)
        for i in ['\\', '/', ':', '*', '\"', '<', '>', '|']:
            log_file_name = log_file_name.replace(i, '')
        for i in ['', '.', '..']:
            if log_file_name == i:  # 避免文件名不合法
                log_file_name = 'QGMA.log'
                break

        # 终端输出日志颜色配置
        log_colors_config = {
            'DEBUG': 'bold_cyan',
            'INFO': 'white',
            'WARNING': 'black,bg_yellow',
            'ERROR': 'black,bg_red',
            'CRITICAL': 'black,bg_purple',
        }

        # 输出到控制台
        console_handler = logging.StreamHandler()
        # 输出到文件
        if backup_count == 0:  # 强制分割日志文件，防止日志文件大小无限增加
            backup_count = 1
        file_handler = RotatingFileHandler(filename=(
            log_path+'/'+log_file_name), mode='a', maxBytes=max_bytes, backupCount=backup_count, encoding='utf8')

        # 日志输出格式
        # 日志文件输出格式
        file_formatter = logging.Formatter(
            fmt='[%(asctime)s.%(msecs)03d]->[%(levelname)s]:\n%(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S'
        )
        # 控制台输出格式
        console_formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s[%(asctime)s.%(msecs)03d]->[%(levelname)s]:\n%(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=log_colors_config
        )
        console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(file_formatter)

        # 重复日志问题：
        # 1、防止多次addHandler；
        # 2、loggername 保证每次添加的时候不一样；
        # 3、显示完log之后调用removeHandler
        if not logger.handlers:
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        console_handler.close()
        file_handler.close()

        # 日志级别，logger 和 handler以最高级别为准，不同handler之间可以不一样，不相互影响
        # root日志等级
        logger.setLevel(logging.NOTSET)
        # 控制台日志等级
        for i in [0, 10, 20, 30, 40, 50]:  # 逐一匹配列表
            if i == console_log_level:  # 如果设置的日志等级符合规范
                console_handler.setLevel(console_log_level)
                break
        else:
            console_handler.setLevel(logging.DEBUG)
            logger.error('【日志等级-控制台】设置不正确，将默认使用DEBUG等级！')
        # 文件日志等级
        for i in [0, 10, 20, 30, 40, 50]:  # 逐一匹配列表
            if i == file_log_level:  # 如果设置的日志等级符合规范
                file_handler.setLevel(file_log_level)
                break
        else:
            file_handler.setLevel(logging.DEBUG)
            logger.error('【日志等级-日志文件】设置不正确，将默认使用DEBUG等级！')
        logger.debug('日志模块加载完成...')

    def Get_Error():
        '使用traceback获取捕获到的错误'
        return traceback.format_exc()


'''
输出format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
**注：1和3/4只设置一个就可以，如果同时设置了1和3，log日志中会出现一条记录存了两遍的问题。
'''

'''
格式化符号
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12） 
%M 分钟数（00=59）
%S 秒（00-59）

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身 
'''

if __name__ == '__main__':  # 代码测试
    Log_Mgt.Log_Conf()

    '''for i in range(5):
        logger.debug('debug')
        logger.info('info')
        logger.warning('warning')
        logger.error('error')
        logger.critical('critical')
    logger.debug(Log_Mgt.Get_Error())
    try: jjj
    except: logger.critical(Log_Mgt.Get_Error())'''
""","",'exec')

Log_Mgt.Log_Conf()
logger.warn("ok")