# -*- coding: utf-8 -*-
# python 3.x
# author：huangxiaoyan
# data:"2022/3/17 19:16"
from base.mysql_handle import MysqlHandle


class HealthManagement(MysqlHandle):
    def __init__(self):
        super(HealthManagement, self).db()


class HealthSync(MysqlHandle):
    def __init__(self):
        super(HealthSync, self).db(dbName='health_sync')


class PlatformHealthHospitalAdmin(MysqlHandle):
    def __init__(self):
        super(PlatformHealthHospitalAdmin, self).db(dbName='platform_health_hospital_admin')


class PlatformHealthMessage(MysqlHandle):
    def __init__(self):
        super(PlatformHealthMessage, self).db(dbName='platform_health_message')


class PlatformHealthOperateAdmin(MysqlHandle):
    def __init__(self):
        super(PlatformHealthOperateAdmin, self).db(dbName='platform_health_operate_admin')


class PlatformHealthPayment(MysqlHandle):
    def __init__(self):
        super(PlatformHealthPayment, self).db(dbName='platform_health_payment')


class PlatformHealthUser(MysqlHandle):
    def __init__(self):
        super(PlatformHealthUser, self).db(dbName='platform_health_user')


class FamilyXxlJob(MysqlHandle):
    def __init__(self):
        super(FamilyXxlJob, self).db(dbName='family_xxl_job')


if __name__ == "__main__":
    print(HealthManagement().get_one("SELECT *  FROM  `msg_content` "))
