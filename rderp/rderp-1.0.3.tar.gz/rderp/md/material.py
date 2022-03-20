'''
 * this file is wrapper for K3CloudApiSdk
 * version is 3.0
'''
from k3cloud_webapi_sdk.main import K3CloudApiSdk
'''
 * the follow code show the way to test in local mode
'''
# from rderp.main import ErpClient
'''
* the follow code show the way to refer inner the package.
* check this setting before publish the code into new package.
 
'''
from ..main import ErpClient
'''
* class definition for material object in ERP system
'''
class Material(ErpClient):

    def View(self, Number,CreateOrgId=0,Id=""):
        '''
        * material view / query opration
        :param Number: the number of material
        :param CreateOrgId: the Create orginazation of the material,default is 0
        :param Id: the inner code for material
        :return: the return value is a json formmated data
        '''
        '''
        * to do list:
        * 1. add the function to deal the return value.
        '''
        self.Number = Number
        self.CreateOrgId = CreateOrgId
        self.Id = Id
        '''
        * create the data for material.View opration
        '''
        data = {
    "CreateOrgId": self.CreateOrgId,
    "Number": self.Number,
    "Id": self.Id}
        res = ErpClient.View(self,formid="BD_MATERIAL",data=data)
        return(res)
    def Save(self,FNumber='mtrl_01',FName='demo_01'):
        self.FNumber = FNumber
        self.FName = FName
        data = {"Model": {
            "FCreateOrgId": {"FNumber": 100},
            "FUserOrgId": {"FNumber": 100},
            "FNumber": self.FNumber ,
            "FName": self.FName
        }}
        ErpClient.Save(self,formid="BD_MATERIAL",data=data)
    def Submit(self,Numbers=[],Ids="",SelectedPostId=0,NetworkCtrl="",IgnoreInterationFlag=""):
        '''
        * the material Submit operation just after save.
        :param Numbers: list of material numbers
        :param Ids:   the Ids of material
        :param SelectedPostId: the SelectedPostId of material
        :param NetworkCtrl:  the NetworkCtrl status of material
        :param IgnoreInterationFlag: the Flag of material
        :return: without the return value or the status of Submit after exec.
        '''
        self.Numbers = Numbers
        self.Ids = Ids
        self.SelectedPostId = SelectedPostId
        self.NetworkCtrl = NetworkCtrl
        self.IgnoreInterationFlag = IgnoreInterationFlag
        data = {
            "CreateOrgId": 0,
            "Numbers": self.Numbers,
            "Ids": self.Ids,
            "SelectedPostId": self.SelectedPostId,
            "NetworkCtrl": self.NetworkCtrl,
            "IgnoreInterationFlag": self.IgnoreInterationFlag
        }
        res = ErpClient.Submit(self,formid="BD_MATERIAL",data=data)
        return(res)
if __name__ == '__main__':
    material = Material(acct_id='606ada0b30a9e2', user_name='胡立磊', app_id='224986_TY8p2yGs4vg9Xf0tRfSA3a/N6K3d6OlH',
                       app_secret='e1e0cdc4e8204d178cc383557e64e959', server_url='http://8.133.163.217/k3cloud/')
    data = material.View(Number='01.21.010')
    print(data)
    # material.Save()
    # data2 = material.Submit(Numbers=['mtrl_01'])
    # print(data2)