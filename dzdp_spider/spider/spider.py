# -*- coding: UTF-8 -*-
import requests
import re
import random
from bs4 import BeautifulSoup
from retrying import retry
import os
from dzdp_spider.spider.models import Shop


def get_proxy():  # 使用阿布云的代理接口
    # 要访问的目标页面
    targetUrl = "http://test.abuyun.com"

    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "HS9039NV974Y34KD"
    proxyPass = "B5687CE5E8CFD090"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }
    return proxies


def get_ua():  # 构建ua池
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Opera/8.0 (Windows NT 5.1; U; en)',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
    ]
    user_agent = random.choice(user_agents)  # random.choice(),从列表中随机抽取一个对象
    return user_agent


def get_ref():  # 构建referer池
    referers = ['http://www.dianping.com/chengdu/ch10/r7949',
                'http://www.dianping.com/chengdu/ch10/r1577',
                'http://www.dianping.com/chengdu/ch10/r7767',
                'http://www.dianping.com/chengdu/ch10/r5894',
                'http://www.dianping.com/chengdu/ch10/r1592',
                'http://www.dianping.com/chengdu/ch10/r1601',
                'http://www.dianping.com/chengdu/ch10/r70146',
                'http://www.dianping.com/chengdu/ch10/r7764',
                'http://www.dianping.com/chengdu/ch10/r7771',
                'http://www.dianping.com/chengdu/ch10/r7769',
                'http://www.dianping.com/chengdu/ch10/r1597',
                'http://www.dianping.com/chengdu/ch10/r7768',
                'http://www.dianping.com/chengdu/ch10/r1974',
                'http://www.dianping.com/chengdu/ch10/r1578',
                'http://www.dianping.com/chengdu/ch10/r1604',
                'http://www.dianping.com/chengdu/ch10/r1579'
                ]
    referer = random.choice(referers)
    return referer


@retry  # 利用retry装饰器，异常重试
def UseBeautifulSoup(url):  # 使用beautifulsoup处理
    ua = get_ua()  # 获得随机的User-Agent
    referer = get_ref()  # 获得随机的Referer
    proxy = get_proxy()  # 获得代理
    cookie = r'showNav=#nav-tab|0|0; navCtgScroll=0; cy=8; cye=chengdu; _lxsdk_cuid=168028405d7c8-03b66fc34109d1-b78173e-144000-168028405d7c8; _lxsdk=168028405d7c8-03b66fc34109d1-b78173e-144000-168028405d7c8; _hc.v="\"3e6deb85-b6e2-49f4-aaa5-125749448165.1546230434\""; s_ViewType=10; ua=dpuser_6109551570; ctu=db26d6b72b3e4ff035bf16f42e66e6cc96fb4c17096a262eb3a198333aa1fce9; _lxsdk_s=168221578c5-08b-7d5-a79%7C%7C43'
    headers = {"Host": "www.dianping.com",
               "User-Agent": ua,
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Referer": referer,
               "Connection": "close",
               "Cookie": cookie,
               # 加r防止转义
               "Upgrade-Insecure-Requests": "1"
               }  # 这里需要加个header，否则直接给返回个403
    res = requests.get(url, headers=headers, proxies=proxy)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


def getRegion():  # 返回要爬取的区域的链接,返回一个数组
    href = []  # 用来存储每个区域的链接
    url = "http://www.dianping.com/chengdu/ch10/r1579"
    try:
        soup = UseBeautifulSoup(url)
        s = soup.find_all(id="bussi-nav")[0]  # 注意到区域的div的id是bussi-nav,find_all方法筛选到

        for m in s.select('a'):
            href.append(re.findall(r"href=\"(.+?)\"", str(m))[0])  # 正则找到链接，存储到href数组中,注意这里re.fnidall返回的是一个数组,取第一项
        print('爬取地区链接成功')
        return href
    except:
        print('爬取地区链接失败')
        print(soup)
        os._exit()


def retry_if_result_none(result):
    return result is None


@retry(retry_on_result=retry_if_result_none)  # 当出现错误时，进行异常重试
def getValue(url):  # 获取这个区域的前五面的店名，以及他的id，链接，星级，返回一个字典
    name_And_value = {}
    value = {'id': '', 'href': '', 'star': ''}
    count = 0
    try:
        soup = UseBeautifulSoup(url)
        star = get_Star(soup)  # 获得这面的star
        # print(star)
        if len(star) == 0:  # 没有爬到，返回个None

            return None
        shoplist = soup.find_all('a', attrs={
            "data-click-name": "shop_title_click"})  # 注意这里有些tag属性是不能用来搜索的，例如HTML5中的data-*属性，我们需要用attrs方法
        for i in shoplist:
            temp = value.copy()  # 这里我遇到一个坑点，在字典1中添加字典2其指向的应该是被添加字典2的地址，并没有新建一个对象，所以在循环汇总改变字典2的值，有点类似深浅拷贝，也会改变字典1里面的值具体参考：https://blog.csdn.net/sinat_21302587/article/details/72356431
            name = re.findall(r"title=\"(.+?)\"", str(i))[0]  # 正则寻找店名及
            temp['href'] = re.findall(r"href=\"(.+?)\"", str(i))[0]  # 链接存储
            temp['id'] = re.findall(r"http://www.dianping.com/shop/(.+)", str(temp['href']))[0]  # 获取每个店铺的id值
            temp['star'] = star[count]  # 存入对应的星级
            name_And_value[name] = temp
            count += 1

        print("爬取区域店铺成功")
        return name_And_value
    except:
        print('爬取区域店铺失败')
        print(soup)
        os._exit()
        return 1


def get_Star(soup):  # 获取商户的星级
    star = []
    comment = soup.find_all('div', class_='comment')  # 先找到comment标签
    for i in comment:
        star.append(re.findall(r"title=\"(.+?)\"", str(i))[0])  # 正则在comment标签中获取星级，
    '''
    if len(star)==0:
        print('爬取到的是：')
        print(soup)
        os._exit()
    '''
    return star


def main():
    n = {}  # n用来储存结果，key是店名，value是个字典包括id,链接，星级
    href = getRegion()  # 获得各个区域的链接
    # print(href)
    print('区域数量为' + str(len(href)))
    for i in range(len(href)):
        for index in range(1, 5):  # 取1到5面的内容
            if index == 1:
                realurl = href[i]
            else:
                realurl = href[i] + 'p' + str(index)  # 注意到每面的链接就是在第一面的基础上加上p+页数

            # print(realurl)
            t = getValue(realurl)
            if t != 1:
                n = {**n, **t}  # 进行字典的合并，如果有key值重复第二项会将第一项进行覆盖，这里将获得的“店名：链接”字典进行合并
    for key, value in n.items():
        args = {}
        args['id'] = value['id']
        args['name'] = key
        args['href'] = value['href']
        args['star'] = value['star']
        shop = Shop()
        shop.save(args)
