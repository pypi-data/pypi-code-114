import sys
sys.path.append('../src')

from anaplanConnector  import Connection

# anaplan = Connection(email="integration@nightingale.edu",password="MvnYe13!eCcgAUz%NjM&",workspaceId='8a868cd97e5fe85f017eb1b61f7943ed',modelId='C989D3D4D5054619AFB282D98119A88A')
anaplan = Connection(email="integration@nightingale.edu",password="MvnYe13!eCcgAUz%NjM&",workspaceId='8a868cd97e5fe85f017eb1b61f7943ed',modelId='C2BC4368273F4245BAA59AC583987FE0')
anaplan.workspaceId = '8a868cd97e5fe85f017eb1b61f7943ed'
anaplan.modelId = 'C989D3D4D5054619AFB282D98119A88A'

# print(anaplan.modelId)
# print(anaplan.endpoints.modelId)
res = anaplan.getProcessIdByName('Update Data')
# print(res)