import makana

# Get Framworks
modelFramworks = makana.MLModel.getModelFramworks("https://localhost:44350/")

# Register MakanaModel
# makanaModel = makana.MLModel.registerModel("https://localhost:44350/","Test Model Dev1","Test Model Dev1", modelFramworks[0]['id'],
#                                  modelFramworks[0]['name'], 1.0 ,"sentiment.h5","Y:\Working\Makana\Models\sentiment.h5")

# Get All MakanaModels
# makanaModels = makana.MLModel.getMakanaModels("https://localhost:44350/")

# Get MakanaModel By Id
# makanaModel = makana.MLModel.getMakanaModel("https://localhost:44350/", makanaModel['id'])


# makanaService = makana.MLService.registerModelService("https://localhost:44350/","Test Service Dev1","Test Service Dev1","makanaModel['id']",
#                                  "main.py","requirements.txt","Y:\Working\Makana\Models\main.py","Y:\Working\Makana\Models\requirements.txt",makana.ContainerRunMode.OnDemand,makana.IdleTimeUnit.Day,2)

# Get All MakanaServices
# makanaServices = makana.MLService.getMakanaServices("https://localhost:44350/")

# Get MakanaService By Id
# makanaService = makana.MLService.getMakanaService("https://localhost:44350/", makanaService['id'])
