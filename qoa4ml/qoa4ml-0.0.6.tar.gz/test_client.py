from qoa4ml.reports import Qoa_Client
import qoa4ml.utils as utils
import time, psutil

client_conf = utils.load_config("./qoa4ml/conf/client.json")
connetor_conf = utils.load_config("./qoa4ml/conf/connector.json")
metric_conf = utils.load_config("./qoa4ml/conf/metrics.json")
client = Qoa_Client(client_conf,connetor_conf,metric_conf)
metrics = client.get_metric()
while True:
    time.sleep(1)
    metrics['Accuracy'].inc()
    metrics['CPU'].set(psutil.cpu_times().user)
    metrics['Mem'].set(psutil.virtual_memory().used)
    client.report()
    print("sending report...")


