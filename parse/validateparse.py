import sys
import colorama

def validateOptions(argsObj):
    command = argsObj.command
    if command == 'queryWechat':
        company_name = argsObj.companyName
        query_pages = argsObj.page
        output = argsObj.output
        if company_name == "":
            print(colorama.Fore.RED + '[error] 请确定你输入了要查询的公司名')
            sys.exit()

    elif command == 'queryDomainIp':
        target = argsObj.target
        file = argsObj.file
        if target:
            if file:
                print(colorama.Fore.RED + '[error] 请重新检查命令')
                sys.exit()
        if file:
            if target:
                print(colorama.Fore.RED + '[error] 请重新检查命令')
                sys.exit()
