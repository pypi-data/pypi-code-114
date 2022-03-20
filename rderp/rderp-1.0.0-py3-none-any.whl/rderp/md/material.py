from k3cloud_webapi_sdk.main import K3CloudApiSdk
from rderp.rderp.main import ErpClient
class Material(ErpClient):
    def View(self, Number,CreateOrgId=0,Id=""):
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
if __name__ == '__main__':
    app = Material(acct_id='606ada0b30a9e2', user_name='胡立磊', app_id='224986_TY8p2yGs4vg9Xf0tRfSA3a/N6K3d6OlH',
                       app_secret='e1e0cdc4e8204d178cc383557e64e959', server_url='http://8.133.163.217/k3cloud/')
    data = app.View(Number='01.21.010')
    print(data)