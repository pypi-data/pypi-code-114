#定义接口自动化关键字类
import requests
import json
import sys,os
from commonchi.lib.get_mannjutoken import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class SendRequests():
    """发送请求数据"""
    # 判断请求方式
    def sendRequests(self, s, data,token_1,cookie_2):
        try:
            method = data['method']
            url = data['url']
            reade_mode = data['type']
            #encryption = data['encryption']
            h = data['headers']
            body_1 = data['body']
            par = data['params']
            contain_ch = data['contain_ch']
            ex_type = data['request_data_type']
            file = data['file']
            filename = data['filename']
            filepath = data['filepath']
            filetype = data['filetype']
            file_2 = data['file2']
            filename_2 = data['filename2']
            filepath_2 = data['filepath2']
            filetype_2 = data['filetype2']
            url_token=data['url_token']     #是否需要加token
            cookie_1=data['cookie_1']      #是否需要加cookie
            parametric=data['parametric']   #是否有逻辑关联
            #是否有逻辑关联
            #print(url_token)
            try:
                if parametric=='Yes':   #cxx220208
                    pass
                else:
                    if url_token == 'Yes':
                       # token_1 =data['token']   # Token的值
                        #token_1 = get_mannjutoken(product_name, lobnumber)  # Token的值
                        url = url + '&mannjuToken='+token_1
                        #print(url)
                    else:
                        url = url
                    if cookie_1=='Yes':
                        cookies=cookie_2
                    else:
                        cookies=None

                    if ex_type == 'File':
                        m_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))  # 获取上两级目录
                        filepath = m_path + '\\file\\' + filepath
                        filepath_2 = m_path + '\\file\\' + filepath_2
                        if file_2 != '':

                            files_1 = {file: (filename, open(filepath, 'rb'), filetype),file_2: (filename_2, open(filepath_2, 'rb'), filetype_2)}

                        else:
                            files_1 = {file: (filename, open(filepath, 'rb'), filetype)}

                    else:
                        files_1 = None



                    #body_1 = body.encode("utf-8").decode("latin1")  #12.30
                    # if (body != '' or body != 'No') and contain_ch == 'Yes':   #12.30
                    if (body_1 != '' and body_1 != 'No'):
                        if contain_ch != 'Yes':  # contain_ch请求中是否包含汉字
                            body_1 = body_1.encode("utf-8").decode("latin1")
                            # str转换为dict
                            body_1 = json.loads(body_1)
                            if reade_mode == 'json':
                                # dict转换为json
                                body_1 = json.dumps(body_1)
                            else:
                                pass
                        else:
                            #pass   #12.30
                            try:
                                body_1 = eval(body_1)
                            except:
                                body_1=body_1.encode("utf-8").decode("latin1")
                            if reade_mode == 'json':
                                # dict转换为json
                                body_1 = json.dumps(body_1)
                            else:
                                pass
                    else:
                        pass
                    if h != 'No'and h !='':
                        try:
                            # str转换为dict
                            h = json.loads(h)
                        except:
                            h = None
                    else:
                        h = None
                    if par != 'No'and par != '':
                        try:
                            # str转换为dict
                            par = json.loads(par)
                        except:
                            par = None

                    else:
                        par = None

                    # if files_1 !='':
                    #     files=files_1
                    # else:
                    #     files=None
                    res = s.request(method=method, url=url, headers=h, params=par, data=body_1, files=files_1,cookies=cookies,verify=None,auth=None, timeout=None, allow_redirects=True,proxies=None,hooks=None, stream=None, cert=None, json=None)
                    return res
            except:
                pass

        except:
            #print('api封装有误')
            pass


