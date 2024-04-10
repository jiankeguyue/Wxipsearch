import requests


def GetNewCookieHeaders(global_headers):
    headers = global_headers
    cookie_split = headers["Cookie"].split("; ")
    for item in cookie_split:
        if "SNUID" in item:
            cookie_split.remove(item)
            cookie_split.append("SNUID=%s" % GetSougoCookie(global_headers)["SNUID"])
            break
    headers["Cookie"] = "; ".join(cookie_split)
    return headers

def GetSougoCookie(global_headers):
    # 搜狗视频url，获取新的SNUID
    url = "https://v.sogou.com/?forceredirect=2&ie=utf8"
    rst = requests.get(url=url,
                       headers=global_headers,
                       allow_redirects=False)
    cookies = rst.cookies.get_dict()
    print("Get new cookie SNUID %s" % cookies["SNUID"])
    return {"SNUID":cookies["SNUID"]}