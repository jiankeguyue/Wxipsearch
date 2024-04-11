from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.http import judgeDomainorIP
import colorama
import requests
from config.cookie import aizhan_cookie
import time
from lxml import etree
import random


def getCompanyname(domain,flag):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.1311 SLBChan/10',
        'Cookie': aizhan_cookie
    }
    url = 'https://www.aizhan.com/cha/' + domain
    try:
        response = requests.get(url,headers=headers)
    except Exception as e:
        print(colorama.Fore.RED + '[error] 请求爱站公司名时发生错误: {}'.format(e))
    time.sleep(0.25)
    tree = etree.HTML(response.text)
    try:
        print(colorama.Fore.GREEN + "[info] 正在抓取公司名字")
        time.sleep(1)
        company_name = tree.xpath("//span[@id='icp_company']/text()")[0]
        icp_name = tree.xpath("//a[@id='icp_icp']/text()")[0]
    except Exception as e:
        print(colorama.Fore.GREEN + '[error] 获取失败')
        return None,None
    if company_name == '-' and icp_name== '-':
        print(colorama.Fore.GREEN + "[info] 抓取到的相关资源: {}".format(tree.xpath("//span[@id='icp_company']/text()")))
        print(colorama.Fore.GREEN + "[info] 无公司名或icp名， 或者cookie未更新")

        # selenium 进行重新确认
        if flag == True:
            print(colorama.Fore.GREEN + "[info] 重新确认中，请稍等")
            company_name_again, icp_name_again = getCompanynameagain(domain)
            if company_name_again == '-' and icp_name_again == '-':
                return None, None
            else:
                print(colorama.Fore.GREEN + '[info] 成功获取到 {} 的公司名 {}'.format(domain, company_name))
                print(colorama.Fore.GREEN + '[info] 成功获取到 {} 的icp {}'.format(domain, icp_name))
                return company_name_again, icp_name_again
        else: return None, None
    print(colorama.Fore.GREEN + '[info] 成功获取到 {} 的公司名 {}'.format(domain,company_name))
    print(colorama.Fore.GREEN + '[info] 成功获取到 {} 的icp {}'.format(domain, icp_name))
    return company_name, icp_name





def getCompanynameagain(domain):
    geckdriver_path = r'chromedriver.exe'
    options = webdriver.ChromeOptions()
    # options.add_argument("disable-blink-features=AutomationControlled")
    service = webdriver.chrome.service.Service(geckdriver_path)
    # 使用选项创建 webdriver 实例
    drive = webdriver.Chrome(service=service, options=options)
    # drive.add_cookie(aizhan_cookie)
    drive.implicitly_wait(1)
    try:
        drive.get(f"https://www.aizhan.com/cha/{domain}/")
        drive.implicitly_wait(2)
    except Exception as e:
        print(colorama.Fore.RED + '[error] 网络请求失败，原因如下: {}'.format(e))
        return None,None
    drive.maximize_window()
    drive.implicitly_wait(3)
    company_name = drive.find_element(By.ID, "icp_company").text
    icp_name = drive.find_element(By.ID, "icp_icp").text
    if company_name == '-' and icp_name == '-':
        print(colorama.Fore.GREEN + "[info] 确定无公司名或icp名")
        return None, None
    print(colorama.Fore.GREEN + f"[info] 成功重新获取，获取到域名: {domain} 对应ICP备案公司名为: {icp_name}，{company_name}")
    return company_name, icp_name


def ipReverseQuery(ip):
    sleep_time = random.uniform(1,2)
    time.sleep(sleep_time)
    url = 'https://dns.aizhan.com/' + ip +'/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.1311 SLBChan/10',
        'Cookie': aizhan_cookie
    }
    print(colorama.Fore.GREEN + '[info] ip反查中...')
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(colorama.Fore.RED + '[error] ip反查时连接发生错误: {}'.format(e))

    time.sleep(2)
    tree = etree.HTML(response.content)
    try:
        domain = tree.xpath("//td[@class='domain']/a[@rel='nofollow']/text()")[0]
    except Exception as e:
        print(colorama.Fore.RED + '[error] 获取失败，查询不到域名')
        return None
    print(colorama.Fore.GREEN + '[info] 成功反查到 {} 的域名 {}'.format(ip, domain))
    print(colorama.Fore.GREEN + '[info] 正在查询公司')

    return domain
