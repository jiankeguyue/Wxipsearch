import colorama


def printFinallResults(WechatofficailTitleList, WechatofficailInfoList, WechatOfficailVerification):
    colorama.init()
    header = '[info] {:<30s} {:<30s} {:<30s}'.format("公众号名称", "公众号认证", "公众号简介")
    print(colorama.Fore.GREEN + header)
    print("-" * len(header))  # 分隔线

    # 数据行
    for title, verification, info in zip(WechatofficailTitleList, WechatOfficailVerification, WechatofficailInfoList):
        row = '{:<30s} {:<30s} {:<30s}'.format(title, verification, info)
        print(colorama.Fore.GREEN + row)