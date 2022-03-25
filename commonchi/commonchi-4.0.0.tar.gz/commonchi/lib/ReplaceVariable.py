import re
from commonchi.lib.Context import Context

class ReplaceVariable():


    def replace_varibale(params):
        if params.find("{{") != -1:
            list1 =  re.findall("{{(\w+)}}", params)

            # print(list[0])
            if len(list1)==1:
                #params中查找到的值
                i = list1[0]
                #Context中对应i的值
                replace_string = eval("Context.{0}".format(i))
                # print(replace_string)
                #替换后的内容
                params = re.sub("{{(\w+)}}", replace_string, params)
                print(params)
            if len(list1)>1:
                for i in list1:
                    # params中查找到的值
                    #print(i)
                    # Context中对应i的值
                    replace_string = eval("Context.{0}".format(i))
                    # print(replace_string)
                    # 替换后的内容
                    params = re.sub("{{"+i+"}}", replace_string, params)
                    #params = re.sub('{{|}}', '', params)
                    print(params)

            else:
                print('正则搜索为空')
        return params

    def random_1(params):
        if params.find("<<") != -1:
            list1 =  re.findall("<<(\w+)>>", params)
            # print(list1)

            # print(list[0])
            if len(list1)==1:
                #params中查找到的值
                i = list1[0]
                #Context中对应i的值
                replace_string = eval("Context.{0}".format(i))
                # print(replace_string)
                #替换后的内容
                params = re.sub("<<(\w+)>>", replace_string, params)
                print(params)
            if len(list1)>1:
                for i in list1:
                    # params中查找到的值
                    #print(i)
                    # Context中对应i的值
                    replace_string = eval("Context.{0}".format(i))
                    # print(replace_string)
                    # 替换后的内容
                    params = re.sub("<<"+i+">>", replace_string, params)
                    print(params)

            else:
                print('正则搜索为空')
        return params






