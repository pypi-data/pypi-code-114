import json, psutil

def load_config(file_path:str)->dict:
    """
    file_path: file path to load config
    """
    with open(file_path, "r") as f:
        return json.load(f)

def to_json(file_path:str, conf:dict):
    """
    file_path: file path to save config
    """
    with open(file_path, "w") as f:
        json.dump(conf, f)
    
def get_cpu(key:str = None):
    if key == "cpu time":
        return psutil.cpu_times().user
    return psutil.cpu_percent()

def get_mem(key:str = None):
    if key == "percentage":
        return psutil.virtual_memory().percent
    if key == "free":
        return psutil.virtual_memory().free
    if key == "total":
        return psutil.virtual_memory().total
    if key == "active":
        return psutil.virtual_memory().active
    if key == "available":
        return psutil.virtual_memory().available
    return psutil.virtual_memory().used