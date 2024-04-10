#! usr/bin/env python
#  writet: yueji0j1anke

from utils.file import validateurl,validatefile
from module.ipdomain.aiqichaspider import getRigestMoney
from module.ipdomain.aizhanspider import getCompanyname
import colorama
from utils.http import judgeDomainorIP
from module.ipdomain.aizhanspider import ipReverseQuery
from utils.file import IpdomainsaveData



def startFileQuery(filename,output,flag):
    validatefile(filename)
    # 读取文件中的每一行
    company_name_list = []
    domain_list = []
    icp_list = []
    is_cnvd_list = []
    with open(filename, "r") as file:
        for line in file:
            address = line.strip()  # 移除换行符和空格
            result = judgeDomainorIP(address)
            if result == "IP":
                domain = ipReverseQuery(address)
                if domain != None:
                    company_name,icp_name = getCompanyname(domain,flag)
                    if  company_name != None:
                        result,registermoney = getRigestMoney(company_name)
                        if result == 1:
                            domain_list.append(domain)
                            company_name_list.append(company_name)
                            icp_list.append(icp_name)
                            is_cnvd_list.append(registermoney)
                        else:
                            domain_list.append(domain)
                            company_name_list.append(company_name)
                            icp_list.append(icp_name)
                            is_cnvd_list.append(registermoney)
                    else:
                        domain_list.append(domain)
                        company_name_list.append("无")
                        icp_list.append(icp_name)
                        is_cnvd_list.append("无")

            if result == "Domain":
                company_name,icp_name = getCompanyname(address,flag)
                if company_name != None:
                    result ,registermoney = getRigestMoney(company_name)
                    if result == 1:
                        domain_list.append(address)
                        company_name_list.append(company_name)
                        icp_list.append(icp_name)
                        is_cnvd_list.append(registermoney)
                    else:
                        domain_list.append(address)
                        company_name_list.append(company_name)
                        icp_list.append(icp_name)
                        is_cnvd_list.append(registermoney)
                else:
                    domain_list.append(address)
                    company_name_list.append("无")
                    icp_list.append(icp_name)
                    is_cnvd_list.append("无")

    if output != "":

        print(colorama.Fore.GREEN + '[success] 已成功查询所有ip和域名，正在进行保存数据')
        IpdomainsaveData(company_name_list,domain_list,icp_list,is_cnvd_list,output)


def getStartipdomain(url,output,flag):
    address = validateurl(url)
    company_name_list = []
    domain_list = []
    icp_list = []
    is_cnvd_list = []
    result = judgeDomainorIP(address)
    if result == "IP":
        domain = ipReverseQuery(address)
        if domain != None:
            company_name, icp_name = getCompanyname(domain,flag)
            if company_name != None:
                result, registermoney = getRigestMoney(company_name)
                if result == 1:
                    domain_list.append(domain)
                    company_name_list.append(company_name)
                    icp_list.append(icp_name)
                    is_cnvd_list.append(registermoney)
                else:
                    domain_list.append(domain)
                    company_name_list.append(company_name)
                    icp_list.append(icp_name)
                    is_cnvd_list.append(registermoney)
            else:
                domain_list.append(domain)
                company_name_list.append("无")
                icp_list.append(icp_name)
                is_cnvd_list.append("无")

    if result == "Domain":
        company_name ,icp_name = getCompanyname(address,flag)
        if company_name != None:
            result, registermoney = getRigestMoney(company_name)
            if result == 1:
                domain_list.append(address)
                company_name_list.append(company_name)
                icp_list.append(icp_name)
                is_cnvd_list.append(registermoney)
            else:
                domain_list.append(address)
                company_name_list.append(company_name)
                icp_list.append(icp_name)
                is_cnvd_list.append(registermoney)
        else:
            domain_list.append(address)
            company_name_list.append("无")
            icp_list.append(icp_name)
            is_cnvd_list.append("无")

    if output != "":
        print(colorama.Fore.GREEN + '[success] 已成功查询单条ip或域名，正在进行保存数据')
        IpdomainsaveData(company_name_list, domain_list, icp_list, is_cnvd_list, output)



    # startQuery()
    # parser = argparse.ArgumentParser("plugin made by yueji0j1anke")
    # parser.add_argument(
    #     '-o', '--output', required=False,
    #     metavar='', type=str, default='output.csv',
    #     help='目前支持csv文件. eg: -o output.csv'
    # )
    #
    # parser.add_argument(
    #     '-f', '--file', required=False,
    #     metavar='', type=str, default='ip_guns_success.txt',
    #     help='目前支持txt文件. eg: -f ipdomain.txt'
    # )
    # args = parser.parse_args()
    # startFileQuery("1.txt","1.csv")



