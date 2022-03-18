#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import requests
import hashlib
import copy
import time
import envx
"""
返回参数列表：
    名称	类型	必须	描述
    code	int	是	请求结果200表示成功，其他则为失败
    message	string	是	请求结果描述
    data	T	否	请求返回结果集，可空

错误码及说明：
    错误码	说明
    200	成功
    1001	consumerkey非法
    1002	签名校验错误
    1003	请求参数缺失
    1004	timestamp 值非法
    1005	timestamp 过期
    1006	请求参数有重复
    500	系统错误
    404	记录不存在
    405	访问过于频繁，可减少并发调用频次

"""


def make_con_info(
        env_file_name: str = 'reading163.env'
):
    # ---------------- 固定设置 ----------------
    inner_env = envx.read(file_name=env_file_name)
    con_info = {
        "consumerkey": inner_env['consumerkey'],
        "secretkey": inner_env['secretkey'],
    }
    # ---------------- 固定设置 ----------------
    return con_info


def make_sign(
        con_info: dict = None,  # 优先使用
        consumer_key: str = None,  # 从服务商处获取
        secret_key: str = None,  # 从服务商处获取
        data: dict = None,  # 要传的数据
        timestamp: int = int(time.time()*1000)
):
    """
    签名生成方法
    """
    if data is None:
        data = {}
    data['timestamp'] = timestamp  # 增加必填字段
    if con_info is None:
        data['consumerkey'] = consumer_key  # 增加必填字段
        local_secret_key = secret_key
    else:
        data['consumerkey'] = con_info['consumerkey']  # 增加必填字段
        local_secret_key = con_info['secretkey']

    local_data = copy.deepcopy(data)
    local_data['secretkey'] = local_secret_key
    sorted_keys = sorted(local_data.keys())
    key_values = ''
    for key in sorted_keys:
        key_value = '%s=%s' % (key, local_data[key])
        key_values += key_value
    d5 = hashlib.md5()
    d5.update(key_values.encode(encoding='UTF-8'))  # update添加时会进行计算
    sign = d5.hexdigest()

    data['sign'] = sign  # 增加sign

    if 'secretkey' in data:
        data.pop('secretkey')  # 防止多传此值

    return data


def site_list(
        env_file_name: str = 'reading163.env',
        con_info: dict = None
):
    """
    2.1分销站点列表

    入参：
        名称	类型	必须	描述
        consumerkey	long	是	分销商唯一标识
        timestamp	long	是	当前时间戳，取13位毫秒时间戳
        sign	string	是	API输入参数签名结果，使用md5加密,见MD5签名规则

    返回：
        名称	类型	必须	描述
        code	int	是	返回值
        message	string	是	信息描述
        mpId	long	是	站点所属公众号id
        mpName	string	是	站点所属公众号名称
        appID	string	是	公众号开发者的appid
        id	long	是	站点id
        domain	string	是	站点域名
        name	string	是	站点名称
    """
    # ---------------- 固定设置 ----------------
    if con_info is None:
        con_info = make_con_info(env_file_name=env_file_name)
    else:
        pass
    # ---------------- 固定设置 ----------------

    data = make_sign(
        con_info=con_info
    )
    url = 'https://bi.reading.163.com/dist-api/siteList'
    response = requests.request(
        method='GET',
        url=url,
        params=data
    )
    return response.json()


def recharge_list(
        site_id: int,
        start_time: int = None,
        end_time: int = None,
        page: int = 1,
        page_size: int = 20,
        pay_status: int = None,
        env_file_name: str = 'reading163.env',
        con_info: dict = None
):
    """
    2.2分销站点充值信息列表

    入参：
        名称	类型	必须	描述
        consumerkey	long	是	分销商唯一标识
        timestamp	long	是	当前时间戳，取13位毫秒时间戳
        sign	string	是	API输入参数签名结果，使用md5加密,见MD5签名规则
        siteid	long	是	站点id
        starttime	long	否	开始时间，格式yyyyMMddHHmm 包含
        endtime	long	否	结束时间，格式yyyyMMddHHmm 不包含
        pageSize	int	否	默认一页显示20条记录,可以根据自身需求设置，限制10000条
        page	int	否	默认第一页
        paystatus	int	否	订单状态：0-未付款，1-已付款，2-交易关闭，不传默认获取所有记录

    返回：
        名称	类型	必须	描述
        code	int	是	返回值
        message	string	是	信息描述
        totalPage	int	是	总页数
        userId	long	是	用户id
        nickName	string	是	用户昵称
        ip	string	是	充值ip
        userAgent	string	是	充值ua
        userFollowTime	long	是	用户关注时间
        userRegisterTime	long	是	用户注册时间
        wx_originalId	string	是	公众号原始id
        wx_mpName	string	是	公众号名称
        wx_user_openId	string	是	微信用户openid
        rechargeUuid	string	是	订单号
        ewTradeId	string	否	交易号,payStatus=1有值
        payTime	long	否	订单支付时间，payStatus=1有值
        rechargeMethod	int	是	充值渠道：1-微信，2-支付宝
        money	int	是	到账阅点，单位：分
        createTime	long	是	订单生成时间
        updateTime	long	是	订单更新时间
        payStatus	int	是	订单状态：0-未付款，1-已付款， 2-交易关闭
        sourceUuid	string	否	订单关联书籍id
        bookTitle	string	否	订单关联书籍名称
    """
    # ---------------- 固定设置 ----------------
    if con_info is None:
        con_info = make_con_info(env_file_name=env_file_name)
    else:
        pass
    # ---------------- 固定设置 ----------------
    local_data = {
        'siteid': site_id
    }
    if start_time is not None:
        local_data['starttime'] = start_time
    if end_time is not None:
        local_data['endtime'] = end_time
    if page_size is not None:
        local_data['pageSize'] = page_size
    if page is not None:
        local_data['page'] = page
    if pay_status is not None:
        local_data['paystatus'] = pay_status

    data = make_sign(
        con_info=con_info,
        data=local_data
    )
    url = 'https://bi.reading.163.com/dist-api/rechargeList'
    response = requests.request(
        method='GET',
        url=url,
        params=data
    )
    return response.json()
