import urllib


def Chinese2Url(chinese_context):
    return urllib.parse.quote(chinese_context)