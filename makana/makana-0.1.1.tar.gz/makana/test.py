import mlFlow

# Get Framworks
modelFramworks = mlFlow.MLModel.getModelFramworks("https://localhost:44350/")

# Register MakanaModel
makanaModel = mlFlow.MLModel.registerModel("https://localhost:44350/","Test Model Dev1","Test Model Dev1", modelFramworks[0]['id'],
                                 modelFramworks[0]['name'], 1.0 ,"sentiment.h5","Y:\Working\Makana\Models\sentiment.h5")

# Get All MakanaModels
makanaModels = mlFlow.MLModel.getMakanaModels("https://localhost:44350/")

# Get MakanaModel By Id
makanaModel = mlFlow.MLModel.getMakanaModel("https://localhost:44350/", makanaModel['id'])


makanaService = mlFlow.MLService.registerModelService("https://localhost:44350/","Test Service Dev1","Test Service Dev1","makanaModel['id']",
                                 "main.py","requirements.txt","Y:\Working\Makana\Models\main.py","Y:\Working\Makana\Models\requirements.txt",mlFlow.ContainerRunMode.OnDemand,mlFlow.IdleTimeUnit.Day,2)

# Get All MakanaServices
makanaServices = mlFlow.MLService.getMakanaServices("https://localhost:44350/")

# Get MakanaService By Id
makanaService = mlFlow.MLService.getMakanaService("https://localhost:44350/", makanaService['id'])
