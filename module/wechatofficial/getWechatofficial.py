import requests
from lxml import etree
import sys
import colorama
from colorama import init
from module.wechatofficial import getCookie
import re
from config import default
from utils.ChineseDecode import Chinese2Url

init()


def GetWechatofficialAccount(keyword,  page):
    keyword = Chinese2Url(keyword)
    url = "https://weixin.sogou.com/weixin?query=" + keyword + "&_sug_type_=&s_from=input&_sug_=y&type=1&ie=utf8&page=" + str(page)
    xpath_get_official_account = "//div[@class='mun']/text()"
    try:
        rep = requests.get(url, headers=default.global_headers)
    except Exception as e:
        print(colorama.Fore.RED + '[error] 请求网址时出现故障：{}'.format(e))

    if "请输入验证码" in rep.text:
        headers = getCookie.GetNewCookieHeaders()
        rep = requests.get(url, headers=default.global_headers)
        #更新全局变量，headers和代理
        global global_headers
        global_headers = headers
        req = requests.get(url, headers=default.global_headers)
    response = rep.text.replace("<em><!--red_beg-->","").replace("<!--red_end--></em>","")
    etree_obj = etree.HTML(response)
    wechat_official_account = etree_obj.xpath(xpath_get_official_account)
    # 将提取的文本转换为字符串
    wechat_official_account_str = ''.join(wechat_official_account)
    # 使用正则表达式匹配数字
    pattern = re.compile(r'\d+')
    wechatofficialAccount = pattern.findall(wechat_official_account_str)
    try:
        wechatofficialAccount = wechatofficialAccount[0]
    except Exception as e:
        print(colorama.Fore.GREEN + "[error] 没有找到相关公众号，请检查cookie，或者更换关键词")
        sys.exit()
    pagenum = int(wechatofficialAccount) / 10 + 1

    # 输出匹配的数字

    if('<img src="/new/pc/images/bg_404_2.png"' in response):
        print(colorama.Fore.GREEN + "[error] 没有找到相关公众号，请检查cookie，或者更换关键词")
        sys.exit()
    print(colorama.Fore.GREEN + "[info] 存在 {} 条公众号".format(wechatofficialAccount))
    return int(wechatofficialAccount), pagenum


def GetWechatOfficailInfo(pagenum, keyword):
    # 容器初始化
    WechatofficailTitleList = []
    WechatofficailInfoList = []
    WechatOfficailVerification = []

    # xpath语法
    WechatOfficailTitleXpath = "//p[@class='tit']/a/text()"
    WechatofficailInfoXpath = "//ul[@class='news-list2']/li/dl[1]/dd/text()"
    WechatOfficalVerificationXpath = "//ul[@class='news-list2']/li/dl[2]/dd/text()"

    keyword = Chinese2Url(keyword)


    for page in range(1, pagenum + 1):
        url = "https://weixin.sogou.com/weixin?query=" + keyword + "&_sug_type_=&s_from=input&_sug_=y&type=1&ie=utf8&page=" + str(
            page)
        try:
            rep = requests.get(url, headers=default.global_headers)
        except Exception as e:
            print(colorama.Fore.RED + '[error] 请求网址时出现故障：{}'.format(e))

        if "请输入验证码" in rep.text:
            headers = getCookie.GetNewCookieHeaders()
            rep = requests.get(url, headers=default.global_headers)
            # 更新全局变量，headers和代理
            global global_headers
            global_headers = headers
            req = requests.get(url, headers=default.global_headers)
        response = rep.text.replace("<em><!--red_beg-->", "").replace("<!--red_end--></em>", "")
        etree_obj = etree.HTML(response)
        try:
            WechatOfficailTitle = etree_obj.xpath(WechatOfficailTitleXpath)
            WechatOfficailInfo = etree_obj.xpath(WechatofficailInfoXpath)
            WechatOfficalVerification = etree_obj.xpath(WechatOfficalVerificationXpath)
            WechatOfficalVerification = list(map(str.strip, filter(str.strip, WechatOfficalVerification)))

            WechatofficailTitleList += WechatOfficailTitle
            WechatofficailInfoList += WechatOfficailInfo
            WechatOfficailVerification += WechatOfficalVerification
        except Exception as e:
            print(colorama.Fore.RED + '[error] 找不到任何公众号相关内容，报错如下: {}'.format(e))

    return WechatofficailTitleList, WechatofficailInfoList, WechatOfficailVerification
