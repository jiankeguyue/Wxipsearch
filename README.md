# Wxipsearch

## 0x1 介绍

市面上没有太好的公众号查询工具，所以自制了一款小工具，结合了其它功能，后续还会增加更多模块功能，敬请期待

```
支持ip反查
支持域名seo综合查询
支持注册资金获取
支持icp获取
支持公司公众号相关获取
支持selenium精准确认
```



开发环境

```
google 123.x 最新版
python3.9
```



测试环境

```
google 123.x 最新版
python3.8-python3.10
```



## 0x2 使用

```
pip3 install -r requirements.txt
```

再config下填入cookie信息

搜狗的cookie，这里需要登陆页面

```
https://weixin.sogou.com/
```

搜索出相关信息之后才能填入cookie

在相关页面搜索往往会回显如下

![image-20240410115946111](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240410115946111.png)

把param的type值改为1后，往往会有回显内容（如果不行就重复来几次，即可刷新）

![image-20240410115935928](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240410115935928.png)

以下为改为1后结果

![image-20240410120034915](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240410120034915.png)

在配置文件中填入cookie后即可进行使用



**ip反查和domain查询模块**

```
python .\wxipsearch.py queryDomainIp -t example.com/ip
python .\wxipsearch.py queryDomainIp -f xx.txt -o xx.csv
```

![image-20240410113052222](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240410113052222.png)

![image-20240410113453228](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240410113453228.png)

![image-20240410120229104](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240410120229104.png)

-r参数默认不开启，但开启后查询会更加精确，同时也需要在目录下放入google浏览器对应版本的selenium，我这里提供了最新123.x版本的内核。

```
python .\wxipsearch.py queryDomainIp -f 1.txt -o 1.csv -r
```

![image-20240410122117574](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240410122117574.png)



关于如何寻找对应版本，参考文章

```
https://blog.csdn.net/m0_45447650/article/details/134241434
```





**公众号查询模块**

```
python .\wxipsearch.py queryWechat -n companyName
python .\wxipsearch.py queryWechat -n companyName -o xx.csv
```

![image-20240410113841853](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240410113841853.png)

![image-20240410114059119](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240410114059119.png)

因存在cookie很快失效问题，故不支持大批量查询

![image-20240410120442216](https://gitee.com/yuejinjianke/tuchuang/raw/master/image/image-20240410120442216.png)



## 0x3 更新

持续中



## 0x4 免责声明

 本工具仅能在取得足够合法授权的企业安全建设中使用，在使用本工具过程中，您应确保自己所有行为符合当地的法律法规。 如您在使用本工具的过程中存在任何非法行为，您将自行承担所有后果，本工具所有开发者和所有贡献者不承担任何法律及连带责任。 除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要安装并使用本工具。 您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
