import os
import sys

import pandas as pd
import colorama
import re

def validatefile(filepath):
    # 读取文件中的内容
    checkfileExist(filepath)
    pattern = re.compile(r'(?:https?://)?([\w\.-]+)(?::\d+)?')
    with open(filepath, 'r+') as file:
        # 读取原始文件内容
        lines = file.readlines()
        file.seek(0)  # 将文件指针移动到文件开头

        # 遍历每一行，处理并写入
        for line in lines:
            # 在当前行中查找匹配项
            matches = pattern.findall(line)
            # 如果找到匹配项，则写入到文件
            if matches:
                for match in matches:
                    file.write(match + '\n')
            else:
                file.write(line)

        file.truncate()  # 截断文件，删除原始文件末尾可能存在的多余内容

def validateurl(url):
    if "http" in url:
        return url.split(":")[1]
    if ":" in url:
        return url.split(":")[0]
    else:
        return url


def checkfileExist(file_path):
    if not os.path.exists(file_path):
        print(colorama.Fore.RED + "[error] 文件不存在")
        sys.exit()
    else: return 1

def checkfileExist2(file_path):
    if os.path.exists("Result/" + file_path):
        print(colorama.Fore.RED + "[error] 目标生成文件已存在，请更换文件")
        sys.exit()

def checkDirectoryExist():
    os.mkdir(r"./Result") if not os.path.isdir(r"./Result") else 0


def WechatFilewriter(WechatofficailTitleList, WechatofficailInfoList, WechatOfficailVerification,file_path):
    df = pd.DataFrame(
        {
            '公众号名字': WechatofficailTitleList,
            '公众号简介': WechatofficailInfoList,
            '公众号认证': WechatOfficailVerification,
        }
    )
    if os.path.exists("Result/" + file_path):
        header = False
    else:
        header = True
    df.to_csv("Result/" + file_path, mode="a+", header=header, index=False, encoding='utf_8_sig')

def IpdomainsaveData(company_name_list,domain_list,icp_list, register_money_list,filename):
    # 初始化容器


    df = pd.DataFrame(
        {
            '公司名': company_name_list,
            'domain': domain_list,
            'ICP': icp_list,
            '注册资金': register_money_list,
        }
    )

    # 写入CSV文件
    df.to_csv("Result/" + filename, mode="a+", header=True, index=False, encoding='ANSI')
    print(colorama.Fore.GREEN + "[success] 文件已生成至Result目录下")

