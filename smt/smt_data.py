import json
import time

# from gevent import monkey

from smt.smt_getsign import get_sign
from smt.get_param import get_prame3, get_prame, get_etag
from smt.smt_goods import get_headers, get_host

# monkey.patch_all()

import requests



base_url = "https://acs.aliexpress.com/h5/mtop.aliexpress.store.products.search.all/1.0/?jsv=2.4.2&appKey=24770048&t={}&sign={}&api=mtop.aliexpress.store.products.search.all&v=1.0&dataType=json&AntiCreep=true&type=originaljson&data={}"

# 获取参数data
def get_data(shop_id, seller_id, num=1):
    data = r'''{{"page":{},"pageSize":20,"locale":"en_US","site":"glo","storeId":"{}","country":"US","currency":"USD","aliMemberId":"{}","sort":"orders_desc"}}'''.format(num,shop_id,seller_id)
    return data

# 获取参数t
def get_t():
    t = int(time.time()*1000)
    return t

# 构造url
def get_url(num=1):
    shop_id = '11111'
    seller_id = '202588862'
    appkey = "24770048"
    t = get_t()
    data = get_data(shop_id, seller_id, num)
    prame3 = get_prame3()
    token = prame3.get("_m_h5_tk").split("_")[0]
    sign = get_sign(t, appkey, data, token)

    url = base_url.format(t, sign, data)
    return url

# 构造headers
def get_header():
    prame = get_prame()
    etag = get_etag()
    prame3 = get_prame3()
    url = get_url()

    cookies_s = "ali_apache_id={}; xman_us_f=x_l=1; acs_usuc_t={}; xman_t={}; xman_f={}; cna={};_m_h5_tk={}; _m_h5_tk_enc={}".format(prame.get("ali_apache_id"), prame.get("acs_usuc_t"), prame.get("xman_t"), prame.get("xman_f"), etag, prame3.get("_m_h5_tk"), prame3.get("_m_h5_tk_enc"))

    headers = get_headers(3)
    headers["Host"] = get_host(url)
    headers["Referer"] = "https://m.aliexpress.com/store/v3/home.html?shopId=11111&sellerId=202588862&pagePath=allProduc.htm"
    headers["Origin"] = "https://m.aliexpress.com"
    headers["Cookie"] = cookies_s

    return headers

# 获取数据
def get_response(num=1):
    prame = get_prame()
    etag = get_etag()
    prame3 = get_prame3()
    url = get_url()

    shop_id= "11111"
    seller_id= "202588862"


    t = int(time.time()*1000)
    appkey = "24770048"
    data = r'''{{"page":{},"pageSize":20,"locale":"en_US","site":"glo","storeId":"{}","country":"US","currency":"USD","aliMemberId":"{}","sort":"orders_desc"}}'''.format(num,shop_id,seller_id)
    # print(data)
    # print(time_str)
    token = prame3.get("_m_h5_tk").split("_")[0]
    sign = get_sign(t,appkey,data,token)
    url4 = "https://acs.aliexpress.com/h5/mtop.aliexpress.store.products.search.all/1.0/?jsv=2.4.2&appKey=24770048&t={}&sign={}&api=mtop.aliexpress.store.products.search.all&v=1.0&dataType=json&AntiCreep=true&type=originaljson&data={}".format(t,sign,data)
    cookies_s = "ali_apache_id={}; xman_us_f=x_l=1; acs_usuc_t={}; xman_t={}; xman_f={}; cna={};_m_h5_tk={}; _m_h5_tk_enc={}".format(prame.get("ali_apache_id"),prame.get("ali_apache_id"),prame.get("ali_apache_id"),prame.get("ali_apache_id"),etag,prame3.get("_m_h5_tk"),prame3.get("_m_h5_tk_enc"))

    headers4 = get_headers(3)
    headers4["Host"] = get_host(url4)
    headers4["Referer"] = url
    headers4["Origin"] = "https://m.aliexpress.com"
    headers4["Cookie"] = cookies_s
    response = requests.get(url=url4,headers=headers4)
    return response

if __name__ == '__main__':
    resp = get_response()
    json_data = json.loads(resp.text)
    data = json_data.get("data")
    totle = data.get("total")
    print(totle)
    num = int(totle / 20) if totle % 20 == 0 else int(totle / 20) + 1
    ret = data.get("ret")
    print(num)
    # for i in ret:
    #     id = i.get("id")
    #     orders = i.get("orders")
    #     print(id, orders)
    # for i in range(2, int(totle / 20)):
    #     req4 = get_response(i)
    #     api_data = json.loads(req4.text)
    #     data = api_data.get("data")
    #     totle = data.get("total")
    #     ret = data.get("ret")
    #     for i in ret:
    #         id = i.get("id")
    #         orders = i.get("orders")
    #         print(id, orders)