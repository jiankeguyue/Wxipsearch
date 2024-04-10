import sys

import colorama

from parse.parseargs import parseArgs
from module.wechatofficial.run import getStartwechat
from parse.title import printTitle
from module.ipdomain.run import getStartipdomain,startFileQuery

def run():
    printTitle()
    argsObj = parseArgs()
    command = argsObj.command
    if command == 'queryWechat':
        company_name = argsObj.companyName
        query_pages = argsObj.page
        output = argsObj.output
        getStartwechat(company_name,query_pages,output)

    elif command == 'queryDomainIp':
        target = argsObj.target
        file = argsObj.file
        output = argsObj.output
        flag = argsObj.repeat
        if target and file:
            print(colorama.Fore.RED + '[error] 参数添加错误，请重试')
            sys.exit()
        if target:
            getStartipdomain(target,output,flag)
        if file:
            startFileQuery(file,output,flag)


if __name__ == '__main__':
    run()