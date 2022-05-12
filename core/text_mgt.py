#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# QGMA文本管理模块
# 作者：稽术宅（funnygeeker）
# QGMA项目交流QQ群：332568832
# 作者Bilibili：https://b23.tv/b39RG2r
# Github：https://github.com/funnygeeker/qgma
# 参考资料：
# Python读大型文本：https://blog.csdn.net/potato012345/article/details/88728709
# chardet文本编码检测：https://blog.csdn.net/tianzhu123/article/details/8187470

import os
import chardet  # 文件编码检测，需安装


class Text_Mgt():
    '文本管理模块，包含：文本编码检测，文本以列表形式读取，判断文本中包含的内容，文本文件存在性检查'
    def Encodeing_Detect(file_path: str) -> str:
        '文本编码检测，无法识别则默认为"utf-8"编码 返回：str'
        with open(file_path, 'rb') as file:
            result = chardet.detect(file.read(1048576))  # 最多读取1MB文件进行检测
            #print(result['confidence'])#
            if float(result['confidence']) >= 0.5:  # 如果置信度大于50%
                return result['encoding'].lower()
            else:
                return 'utf-8'  # 无法识别则默认为"utf-8"编码

    def List_Read_Text(file_path: str, choose: str = '', choose_mode: int = 0, read_mode: int = 0, encoding: str = ''):
        '读取文本文件并以列表的形式输出，可选排除(0)或选择(1)某字符串开头的行，可选从行头选择(0)还是从行尾选择(1)，不支持匹配换行符 返回：list'
        if encoding == '':  # 如果没有文本编码参数，则自动识别编码
            encoding = Text_Mgt.Encodeing_Detect(file_path)
        with open(file_path, "r", encoding=encoding) as all_text:
            if choose == '':  # 如果不需要排除或选择某字符串开头的文本行
                text_list = [text.strip("\n")
                             for text in all_text if text.strip("\n") != ""]
            else:  # 如果需要排除或选择某字符串开头的文本行
                if choose_mode == 1:  # 选择模式
                    if read_mode == 1:  # 选择模式，从后选取
                        text_list = [text.strip("\n") for text in all_text if text.strip(
                            "\n") != "" and text.strip("\n")[-len(choose):] == str(choose)]
                    else:  # 选择模式，从前选取
                        text_list = [text.strip("\n") for text in all_text if text.strip(
                            "\n") != "" and text.strip("\n")[0:len(choose)] == str(choose)]
                else:  # 排除模式
                    if read_mode == 1:  # 排除模式，从后选取
                        text_list = [text.strip("\n") for text in all_text if text.strip(
                            "\n") != "" and text.strip("\n")[-len(choose):] != str(choose)]
                    else:  # 排除模式，从前选取
                        text_list = [text.strip("\n") for text in all_text if text.strip(
                            "\n") != "" and text.strip("\n")[0:len(choose)] != str(choose)]
        return text_list

    @staticmethod
    def Match_List(list: list, text: str):
        '逐一匹配列表中的值是否包含在字符串中 返回：bool'
        for i in list:  # 逐一匹配列表
            if str(i) in str(text):  # 如果文本在列表中
                return True
        else:
            return False

    def Text_Exists(file_path: str, text_to_write: str = '', encoding: str = 'utf-8'):
        '检查文本文件是否存在，不存在则可创建并写入内容 返回：bool'
        if os.path.isfile("./settings.txt") == True:  # 如果文件存在
            return True
        elif text_to_write != '':  # 如果要写入的内容不为空
            with open(file_path, 'w', encoding=encoding) as file:
                file.write(str(text_to_write))
                return False
        else:  # 文件既不存在也不需要写入内容
            return False


if __name__ == '__main__':  # 代码测试
    import time
    time_start = time.time()
    file_path = './tests/text/test.txt'
    # print(Text_Mgt.Encodeing_Detect(file_path))
    # print(Text_Mgt.List_Read_Text(file_path, choose='#',choose_mode=1, read_mode=0))
    # print(Text_Mgt.Match_List(Text_Mgt.List_Read_Text(file_path),'#测试啊'))
    # Text_Mgt.Text_Exists('./temp.txt', 'hello')
    print(time.time()-time_start)
