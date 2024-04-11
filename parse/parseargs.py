import argparse
import time
import sys
from parse.font import blue, bold, red
from utils.validateparse import validateOptions
import os

def parseArgs():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    # 处理公众号查询模块
    parser_queryWechat = subparsers.add_parser('queryWechat', help='query Wechat account')
    parser_queryWechat.add_argument("-n", dest="companyName", required=True, type=str,
                                    help="查询公司名")
    parser_queryWechat.add_argument("-p", dest="page", required=False, type=int, default=1, help="查询公众号总页数")
    parser_queryWechat.add_argument("-o", dest="output", required=False, type=str, default="",help=f"输出文件 (默认不输出  eg：wxsearch.csv,存储在/Result/文件夹下)")

    # 处理域名查询模块
    parser_queryDomainIp = subparsers.add_parser('queryDomainIp', help='query domain or ip')
    parser_queryDomainIp.add_argument("-t", dest="target", required=False, type=str, help="target IP/domain")
    parser_queryDomainIp.add_argument("-f", dest="file", required=False, type=str, default="", help=f"包含目标IP/域名的文件")
    parser_queryDomainIp.add_argument("-o", dest="output", required=False, type=str, default="", help=f"输出文件 (默认输出 ./Result/ipsearch.csv)")
    parser_queryDomainIp.add_argument("-r", dest="repeat", required=False, action="store_true", help=f"使用selenium 进行辅助判断， 默认不开启。 使用后准确率更高")




    argsObj = parser.parse_args()
    validateOptions(argsObj)
    # if not argsObj.target and not argsObj.file:
    #     print(red('\n[x] 用法:python ipInfoSearch.py [-t 目标IP/域名] [-f 含多个目标的文件] [-r 权重最小值] [-icp 备案查询] [-o 输出文件]\n\n[-] 举例:python ipInfoSearch.py -t 127.0.0.1 -r 1 -icp '))
    #     sys.exit()
    # if argsObj.file:
    #     if not os.path.isfile(argsObj.file):
    #         print(printTime()+f"\033[31m[Error] 加载文件[{argsObj.file}]失败\033[0m")
    #         sys.exit()
    # if not argsObj.hidden:
    #     print(printTime()+bold(f"[Info] -t    ：  {argsObj.target}"))
    #     print(printTime()+bold(f"[Info] -f    ：  {argsObj.file}"))
    #     print(printTime()+bold(f"[Info] -r    ：  {argsObj.rank}"))
    #     print(printTime()+bold(f"[Info] -rt   ：  {argsObj.rankTarget}"))
    #     print(printTime()+bold(f"[Info] -showE：  {argsObj.showDominError}"))
    #     print(printTime()+bold(f"[Info] -icp  ：  {argsObj.icp}"))
    #     print(printTime()+bold(f"[Info] -o    ：  ./Result/{argsObj.output}.csv"))
    return argsObj


def printTime():
    return f"[{blue(time.strftime('%H:%M:%S', time.localtime()))}] - "
