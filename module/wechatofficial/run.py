import sys
import colorama
from colorama import init
from module.wechatofficial.getWechatofficial import GetWechatofficialAccount, GetWechatOfficailInfo
from module.wechatofficial.printResults import printFinallResults
from utils.file import checkDirectoryExist, WechatFilewriter

init()

def getStartwechat(companyName, page, output):
    wechat_official_account,pagenum = GetWechatofficialAccount(companyName,1)
    validatePage(page,pagenum)
    WechatofficailTitleList, WechatofficailInfoList, WechatOfficailVerification = GetWechatOfficailInfo(page, companyName)
    printFinallResults(WechatofficailTitleList, WechatofficailInfoList, WechatOfficailVerification)
    if output != "":
        checkDirectoryExist()
        WechatFilewriter(WechatofficailTitleList, WechatofficailInfoList, WechatOfficailVerification)
        print(colorama.Fore.GREEN + '[success] 请到Result目录下查看对应结果')



def validatePage(page, pagenum):
    if page > pagenum:
        print(colorama.Fore.RED + '[error] 爬取页数超出目标总页数，请重新输入')
        sys.exit()
