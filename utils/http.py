import re

def judgeDomainorIP(address):
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"  # IP地址的正则表达式模式
    domain_pattern = r"\b[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b"  # 域名的正则表达式模式
    if re.match(ip_pattern, address):
        return "IP"
    elif re.match(domain_pattern, address):
        return "Domain"
    else:
        return "Invalid"