import datetime,random
class Context:
    #pass
    time_1=datetime.datetime.strftime(datetime.datetime.now(), "%m%d%H")
    random_n = ''.join(random.sample('123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRESTUVWXYZ', 3))
    random_num = time_1 + random_n
    time_2=datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
    random_nu = ''.join(random.sample('0123456789',4))
    random_z = ''.join(random.sample('ABCDEFGHIGKLMNOPQRESTUVWXYZ', 4))
    pems_random=time_2+random_nu+random_z