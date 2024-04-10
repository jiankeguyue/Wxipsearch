import requests
from config.cookie import aiqicha_cookie
import time
import colorama


def judgeRegisterMoney(register_money):
    if ',' in register_money:
        register_money = register_money.replace(',','')
    if float(register_money) >= 5000.0:
        print(colorama.Fore.GREEN + '[info] 该公司注册资金：{}万 .... 恭喜，发现大目标'.format(register_money))
        return 1, register_money
    else:
        return 0, register_money

def getRigestMoney(company_name):
    headers = {
        'Cookie': aiqicha_cookie,
        'Referer': 'https://aiqicha.baidu.com/s?q=%E4%B8%AD%E5%9B%BD%E7%89%A9%E8%B5%84%E5%82%A8%E8%BF%90%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&t=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.3.1311 SLBChan/10',
    }

    params = {
        'q': company_name,
        't': '',
        'p': '1',
        's': '10',
        'o': '0',
        'f': '{}',
    }

    url = 'https://aiqicha.baidu.com/s/advanceFilterAjax'
    try:
       response = requests.get(url, params=params, headers=headers)
       time.sleep(1)
    except Exception as e:
        print(colorama.Fore.RED + '[error] 请求爱企查时发生错误: {}'.format(e))
    json_data = response.json()
    try:
       register_money = json_data['data']['resultList'][0]['regCap'].replace('万','')
    except Exception as e:
        return 0, "无"
    if register_money == '-':
        return 0, "无"
    else:
        result, register_money = judgeRegisterMoney(register_money)
        return result, register_money
