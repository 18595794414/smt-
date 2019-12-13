from smt.header_tool import request_tools
import re




def headers_split(headers_str):
    b = re.sub("(expires=[^,]*),", "\\1，", headers_str, flags=re.I)
    h_list = b.split(",")
    dict_p ={}
    for str_p in h_list:
        parameter = str_p.split(";")[0]
        parameter_l = parameter.split("=",1)
        value_p = ""
        if len(parameter_l) > 1:
            value_p = parameter_l[1].strip()
        name_p = parameter_l[0].strip()
        dict_p[name_p] = value_p
    return dict_p

def get_host(url):
    match = re.search("//(.*?)/|//(.*?)$",url)
    host_new = ""
    if match:
        host_new = match.groups()
    for i in host_new:
        if i:
            return i


def get_headers(type = 1):
    if type == 1:
        headers1 = '''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'''
        headers1 = request_tools.headers_todict(headers1)
        return headers1
    elif type == 2:
        headers2 = '''accept: */*
        accept-encoding: gzip, deflate, br
        accept-language: zh-CN,zh;q=0.9
        upgrade-insecure-requests: 1
        user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'''
        headers2 = request_tools.headers_todict(headers2)
        return headers2
    elif type == 3:
        headers3 = '''Accept: application/json
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1
Content-type: application/x-www-form-urlencoded
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9'''
        headers3 = request_tools.headers_todict(headers3)
        return headers3


# headers3shop_id = "11111"
# seller_id = "202588862"
# url = "https://m.aliexpress.com/store/v3/home.html?shopId={}&sellerId={}&pagePath=allProduct.htm".format(shop_id,seller_id)
# headers=get_headers()
# req = requests.get(url=url,headers=headers)
# set_cookie = req.headers.get("set-cookie")
# prame = headers_split(set_cookie)
# # print(prame)
#
# url2 = "https://log.mmstat.com/eg.js"
# headers2 = get_headers(2)
# headers2["Host"] = get_host(url2)
# headers2["Referer"] = url
# req2 = requests.get(url=url2,headers=headers2)
# etag = req2.headers.get("ETag")
# if etag:
#     etag = etag.replace('"',"")
# print(etag)
#
# time_str = int(time.time()*1000)
# appkey = "24770048"
# data = r'''{{"componentKey":"shopHead","params":"{{\"country\":\"US\",\"site\":\"glo\",\"sellerId\":{},\"backgroundHeight\":\"200\",\"backgroundImage\":\"//ae01.alicdn.com/kf/HTB1WkR_d4TpK1RjSZR0762EwXXaL.png\",\"backgroundWidth\":\"720\",\"language\":\"English\",\"loginUserId\":\"0\",\"locale\":\"en_US\",\"shopSignSelected\":\"logo\"}}"}}'''.format(seller_id)
# print(data)
# print(time_str)
# sign = get_sign(time_str,appkey,data)
# url3 = "https://acs.aliexpress.com/h5/mtop.alibaba.alisite.ae.server.moduleasyncservice/1.0/?jsv=2.4.2&appKey=24770048&t={}&sign={}&api=mtop.alibaba.alisite.ae.server.ModuleAsyncService&v=1.0&dataType=json&type=originaljson&timeout=3000&AntiCreep=true&data={}".format(time_str,sign,data)
# cookies_s = "ali_apache_id={}; xman_us_f=x_l=1; acs_usuc_t={}; xman_t={}; xman_f={}; cna={}".format(prame.get("ali_apache_id"),prame.get("ali_apache_id"),prame.get("ali_apache_id"),prame.get("ali_apache_id"),etag)
# headers3 = get_headers(3)
# headers3["Host"] = get_host(url3)
# headers3["Referer"] = url
# headers3["Origin"] = "https://m.aliexpress.com"
# headers3["Cookie"] = cookies_s
#
# req3 = requests.get(url=url3,headers=headers3)
# print(req3.text)
# set_cookie = req3.headers.get("set-cookie")
# prame3 = headers_split(set_cookie)
# print(prame3)
#
# def goods_id(num,shop_id,seller_id,prame,etag,prame3,url):
#     time_str = int(time.time()*1000)
#     appkey = "24770048"
#     data = r'''{{"page":{},"pageSize":20,"locale":"en_US","site":"glo","storeId":"{}","country":"US","currency":"USD","aliMemberId":"{}","sort":"orders_desc"}}'''.format(num,shop_id,seller_id)
#     # print(data)
#     # print(time_str)
#     token = prame3.get("_m_h5_tk").split("_")[0]
#     sign = get_sign(time_str,appkey,data,token)
#     url4 = "https://acs.aliexpress.com/h5/mtop.aliexpress.store.products.search.all/1.0/?jsv=2.4.2&appKey=24770048&t={}&sign={}&api=mtop.aliexpress.store.products.search.all&v=1.0&dataType=json&AntiCreep=true&type=originaljson&data={}".format(time_str,sign,data)
#     cookies_s = "ali_apache_id={}; xman_us_f=x_l=1; acs_usuc_t={}; xman_t={}; xman_f={}; cna={};_m_h5_tk={}; _m_h5_tk_enc={}".format(prame.get("ali_apache_id"),prame.get("ali_apache_id"),prame.get("ali_apache_id"),prame.get("ali_apache_id"),etag,prame3.get("_m_h5_tk"),prame3.get("_m_h5_tk_enc"))
#
#     headers4 = get_headers(3)
#     headers4["Host"] = get_host(url4)
#     headers4["Referer"] = url
#     headers4["Origin"] = "https://m.aliexpress.com"
#     headers4["Cookie"] = cookies_s
#     req4 = requests.get(url=url4,headers=headers4)
#     return req4
# req4 = goods_id(1,shop_id,seller_id,prame,etag,prame3,url)
# api_data = json.loads(req4.text)
# data = api_data.get("data")
# # print(data)
# totle = data.get("total")
# print(totle)
# num = int(totle/20) if totle%20 else int(totle/20)+1
# ret = data.get("ret")
# for i in ret:
#     id = i.get("id")
#     orders = i.get("orders")
#     print(id,orders)
# for i in range(2,int(totle/20)):
#     req4 = goods_id(i, shop_id, seller_id, prame, etag, prame3, url)
#     api_data = json.loads(req4.text)
#     data = api_data.get("data")
#     totle = data.get("total")
#     ret = data.get("ret")
#     for i in ret:
#         id = i.get("id")
#         orders = i.get("orders")
#         print(id, orders)