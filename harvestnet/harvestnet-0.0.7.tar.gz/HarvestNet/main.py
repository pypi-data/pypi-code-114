import requests
from flask import Flask,request,jsonify, make_response
from flask_restful import Resource, Api,reqparse
from flask_cors import cross_origin
from flask_cors import *
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.image import img_to_array
import torch
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from PIL import Image
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .db import DbUser
import json
import base64

app = Flask(__name__)  # 用flask创建app

# def getID():
#     res = request.get_json()
#     ID = res['data']['ID']
#     return ID
#
# limiter = Limiter(app=app,
#                   key_func=getID,
#                   )

#测试
def getID():
    res = request.values
    res = dict(res)
    ID = res['ID']
    return ID

limiter = Limiter(app=app,
                  key_func=getID,
                  )


api = Api(app)  # 用Api来绑定app
parser = reqparse.RequestParser()
parser.add_argument('ID')

transform_valid = transforms.Compose([transforms.Resize(225),
                                           transforms.CenterCrop(224),
                                           transforms.ToTensor(),
                                           transforms.Normalize([0.485, 0.456, 0.406],
                                                             [0.229, 0.224, 0.225])])
#马铃薯模型
model = load_model('D:\potato4.h5')
default_image_size = tuple((256, 256))

#番茄模型
model_tomato = torch.load('D:\ResNet50_SGD.pth')
use_cuda = torch.cuda.is_available()
if use_cuda:
    model_tomato = model_tomato.cuda()

#玉米模型
model_crop = load_model('D:\model-Xception.h5')

classes_tomato = ['番茄细菌斑点病', '番茄早疫病', '健康','番茄晚疫病', '番茄叶霉病', '番茄花叶病毒','番茄斑点病', '番茄黄化卷叶病毒']

# @cross_origin()
# @app.before_request
# def before_request():
#     res = request.get_json()
#     res = dict(res)
#     # print(res)
#     if 'ID' not in res['data']:
#         return {'error': '没有ID，禁止调用'}, 404
#     else:
#         ID = res['data']['ID']
#         ID = DbUser.get_id(ID)
#         if ID == '0':
#             return {'error': 'ID错误'}, 401


#测试
@cross_origin()
@app.before_request
def before_request():
    res = request.values
    # print(res)
    res = dict(res)
    print(res)
    if res['ID'] == '':
        return {'error': '没有ID，禁止调用'}, 404
    else:
        ID = res['ID']
        ID = DbUser.get_id(ID)
        if ID == '0':
            return {'error': 'ID错误'}, 401

class HelloWorld(Resource):
    @cross_origin() #解决跨域
    def get(self):
        return {'text': 'hello world'}

#form-data发送
# class predict(Resource):
#     @cross_origin()
#     def post(self):
#         # args = parser.parse_args()
#         # id= {'ID': args['ID']}
#         # print(id)
#         id = request.get_json()
#         print(id)
#         userid = id['ID']
#         userid = DbStudent.get_student_by_id(userid)
#         if userid == '0':
#             return make_response(jsonify({'error': 'Unauthorized access'}), 401)
#         else:
#             f = request.files['Img']
#             imgname = f.filename
#             basepath = os.path.dirname(__file__)  # 当前文件所在路径
#             src_imgname = "\one.jpg"
#             upload_path = os.path.normpath(os.path.join(basepath, 'static'))
#             print(basepath, upload_path)
#             if os.path.exists(upload_path) == False:
#                 os.makedirs(upload_path)
#             f.save(upload_path + src_imgname)
#             f_img = cv2.imread('static/one.jpg')
#             f_img = cv2.resize(f_img, (256, 256))
#             f_img = img_to_array(f_img)
#             plt.imshow(f_img)
#             img = f_img / 255
#             img = np.expand_dims(img, axis=0)
#             pre = model.predict(img)
#             # pre = predict('D:\\potato\\potato\\static\\one.jpg')
#             pre_1 = pre[:, 0]
#             pre_1 = np.around(pre_1, 2)
#             pre_2 = pre[:, 1]
#             pre_2 = np.around(pre_2, 2)
#             pre_3 = pre[:, 2]
#             pre_3 = np.around(pre_3, 2)
#
#             pre_list = '早疫病:{},晚疫病:{},健康:{}'.format(pre_1, pre_2, pre_3)
#
#             a = pre_list.split(',')
#             b = dict()
#             for i in a:
#                 c = i.split(':')
#                 b[c[0]] = c[1]
#             print(b)
#
#             return b

#json发送
class predict(Resource):
    decorators = [limiter.limit("1000/day"),
                  limiter.limit("5/minute"),
                  limiter.limit("1/second")]

    
    @cross_origin()
    def post(self):
            f = request.files['Img']
            print(f)
            imgname = f.filename
            basepath = os.path.dirname(__file__)  # 当前文件所在路径
            src_imgname = "\one.jpg"
            upload_path = os.path.normpath(os.path.join(basepath, 'static'))
            print(basepath, upload_path)
            if os.path.exists(upload_path) == False:
                os.makedirs(upload_path)
                f.save(upload_path + src_imgname)
            else:
                f.save(upload_path + src_imgname)
            f_img = cv2.imread('static/one.jpg')
            f_img = cv2.resize(f_img, (256, 256))
            f_img = img_to_array(f_img)
            plt.imshow(f_img)
            img = f_img / 255
            img = np.expand_dims(img, axis=0)
            pre = model.predict(img)
                # pre = predict('D:\\potato\\potato\\static\\one.jpg')
            pre_1 = pre[:, 0]
            pre_1 = np.around(pre_1, 2)
            pre_2 = pre[:, 1]
            pre_2 = np.around(pre_2, 2)
            pre_3 = pre[:, 2]
            pre_3 = np.around(pre_3, 2)

            pre_list = '早疫病:{},晚疫病:{},健康:{}'.format(str(pre_1[0]), str(pre_2[0]), str(pre_3[0]))

            a = pre_list.split(',')
            b = dict()
            for i in a:
                c = i.split(':')
                b[c[0]] = c[1]
            print(b)

            return b

# class predict_tomato(Resource):
#     decorators = [limiter.limit("1000/day"),
#                   limiter.limit("5/minute"),
#                   limiter.limit("1/second")]
#     @cross_origin()
#     def post(self):
#             basepath = os.path.dirname(__file__)  # 当前文件所在路径
#             src_imgname = "\one.jpg"
#             upload_path = os.path.normpath(os.path.join(basepath, 'static'))
#             print(basepath, upload_path)
#             if os.path.exists(upload_path) == False:
#                 os.makedirs(upload_path)
#             f = request.get_json()
#             f = f['data']['Img']
#             img_str = f.encode('ascii')
#             img_byte = base64.b64decode(img_str)
#             img_json = open(upload_path + src_imgname, 'wb')
#             img_json.write(img_byte)
#             img_json.close()
#             # f.save(upload_path + src_imgname)
#             img = Image.open('static/one.jpg').convert('RGB')
#             img_ = transform_valid(img).unsqueeze_(0)  # 拓展维度
#             device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#             img_ = img_.to(device)
#             outputs = model_tomato(img_)
#             # 输出概率最大的类别
#             indices_ = torch.max(outputs, 1)[1]
#             percentage = torch.nn.functional.softmax(outputs, dim=1)[0]
#             percentage = np.round(percentage.detach().numpy(), 5) if not use_cuda else np.round(
#                 percentage.cpu().detach().numpy(), 5)
#             perc = percentage[int(indices_)].item()
#             class_names = list(classes_tomato)
#             result = class_names[indices_]
#             print('predicted:', result)
#             print(percentage)
#
#             return result

#测试
class predict_tomato(Resource):
    decorators = [limiter.limit("1000/day"),
                  limiter.limit("5/minute"),
                  limiter.limit("1/second")]
    @cross_origin()
    def post(self):
            f = request.files['Img']
            imgname = f.filename
            basepath = os.path.dirname(__file__)  # 当前文件所在路径
            src_imgname = "\one.jpg"
            upload_path = os.path.normpath(os.path.join(basepath, 'static'))
            print(basepath, upload_path)
            if os.path.exists(upload_path) == False:
                os.makedirs(upload_path)
                f.save(upload_path + src_imgname)
            else:
                f.save(upload_path + src_imgname)
            img = Image.open('static/one.jpg').convert('RGB')
            img_ = transform_valid(img).unsqueeze_(0)  # 拓展维度
            device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
            img_ = img_.to(device)
            outputs = model_tomato(img_)
            # 输出概率最大的类别
            indices_ = torch.max(outputs, 1)[1]
            percentage = torch.nn.functional.softmax(outputs, dim=1)[0]
            percentage = np.round(percentage.detach().numpy(), 5) if not use_cuda else np.round(
                percentage.cpu().detach().numpy(), 5)
            perc = percentage[int(indices_)].item()
            class_names = list(classes_tomato)
            result = class_names[indices_]
            print('predicted:', result)
            print(percentage)

            return result


class predict_corn(Resource):
    decorators = [limiter.limit("1000/day"),
                  limiter.limit("5/minute"),
                  limiter.limit("1/second")]
    @cross_origin()
    def post(self):
            f = request.files['Img']
            imgname = f.filename
            basepath = os.path.dirname(__file__)  # 当前文件所在路径
            src_imgname = "\one.jpg"
            upload_path = os.path.normpath(os.path.join(basepath, 'static'))
            print(basepath, upload_path)
            if os.path.exists(upload_path) == False:
                os.makedirs(upload_path)
                f.save(upload_path + src_imgname)
            else:
                f.save(upload_path + src_imgname)
            f_img = cv2.imread('static/one.jpg')
            f_img = cv2.resize(f_img, (224, 224))
            f_img = img_to_array(f_img)

            plt.imshow(f_img)
            img = f_img / 255
            img = np.expand_dims(img, axis=0)
            pre = model_crop.predict(img)
                # pre = predict('D:\\potato\\potato\\static\\one.jpg')
            pre_1 = pre[:, 0]
            pre_1 = np.around(pre_1, 2)
            pre_2 = pre[:, 1]
            pre_2 = np.around(pre_2, 2)
            pre_3 = pre[:, 2]
            pre_3 = np.around(pre_3, 2)
            pre_4 = pre[:, 3]
            pre_4 = np.around(pre_4, 2)
            pre_list = '大斑病:{},小斑病:{},褐斑病:{},健康:{}'.format(str(pre_1[0]), str(pre_2[0]), str(pre_3[0]), str(pre_4[0]))

            a = pre_list.split(',')
            b = dict()
            for i in a:
                c = i.split(':')
                b[c[0]] = c[1]
            print(b)

            return b


api.add_resource(HelloWorld, '/api/text')
api.add_resource(predict,'/api/prediction')
api.add_resource(predict_tomato,'/api/prediction_tomato')
api.add_resource(predict_corn,'/api/prediction_corn')


if __name__ == '__main__':
    app.run(debug=True)
