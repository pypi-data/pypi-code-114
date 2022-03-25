# # 指定文件类型
# FILE_TYPE = "excel"

# # SHEET 指定要读取的表, int 指定sheet位置，str 指定表名
# SHEET = 0

# 指定类型
_TYPE = {
    "优先": "PREF",
    "住宅": "HOME",
    "工作": "WORK",
    "单元": "CELL",
    "传真": "FAX",
    "其它": "OTHER",
    "邮寄": "POSTAL",
}


# 输入文件与Vcard对应字典
_VCARD = {
    "前缀": "N_a",
    "后缀": "N_d",
    "姓名": "N",
    "昵称": "NICKNAME",
    "备注": "NOTE",
    "生日": "BDAY",
    "组织": "ORG",
    "职位": "TITLE",
    "电话": "TEL",
    "邮箱": "EMAIL",
    "网址": "URL",
    "地址": "ADR",
}


# 转义字符 \
# , == \,
# ; == \;
# : == \:
# \ == \\
# % == \%


# 名字的长度没有限制？

# BEGIN:VCARD
# VERSION:3.0
# N;CHARSET=UTF-8:后缀;姓名字;;前缀
# NICKNAME: 34567890
# TEL;PREF:13000000000
# TEL;HOME:13111111111
# TEL;FAX:13222222222
# TEL;CELL:13333333333
# TEL:1344444444444
# TEL;OTHER:13555555555
# EMAIL;INTERNET;WORK:333\@qq.com
# EMAIL;INTERNET;HOME:222@qq.com
# EMAIL;INTERNET;OTHER:111@qq.com
# EMAIL;INTERNET:000@qq.com
# URL:http://1133.com
# URL;HOME:http://2233.com
# URL;WORK:http://3333.com
# URL;OTHER:http://4444.com
# ADR:11111\3333,33333
# ADR:22\@2222\;222\\222222\:222\\@222222\;2222222222222\;22222222222
# ADR:名\%字;公寓\大厦;街道\地址;城市;地区;00\,0000;国家
# ADR;WORK:W\ORK;公寓大厦;街道地址;城市;地区;000000;国家
# ADR;OTHER:OT\.HER;公\.寓大厦;街道地址;城市;地区;000000;国家
# ADR;POSTAL:POSTAL;公寓大厦;街道地址;城市;地区;000000;国家
# END:VCARD
