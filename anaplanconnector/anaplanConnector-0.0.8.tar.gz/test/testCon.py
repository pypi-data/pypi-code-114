import sys
sys.path.append('../src')
from anaplanConnector  import Connection

# anaplan = Connection(authType='basic', email="integration@nightingale.edu", password="MvnYe13!eCcgAUz%NjM&", workspaceId='8a868cd97e5fe85f017eb1b61f7943ed', modelId='C2BC4368273F4245BAA59AC583987FE0')
anaplan = Connection(authType='certificate', privateCertPath='./AnaplanPrivateKey.pem', publicCertPath='./AnaplanPublicKey.pem', workspaceId='8a868cd97e5fe85f017eb1b61f7943ed', modelId='C2BC4368273F4245BAA59AC583987FE0')

# print(anaplan.getModels())

# print(anaplan.getFiles())

# print(anaplan.getFileIdByFilename('FactTransactions.csv'))

# print(anaplan.getWorkspaces())

# print(anaplan.getExports())

# print(anaplan.getExportIdByName('integrations.csv'))

# print(anaplan.getProcesses())

# print(anaplan.getProcessIdByName('Import DimSofeRegion'))

# anaplan.getExportIdByName('integrations.csv')
anaplan.export(anaplan.getExportIdByName('integrations.csv'),'./test.csv')