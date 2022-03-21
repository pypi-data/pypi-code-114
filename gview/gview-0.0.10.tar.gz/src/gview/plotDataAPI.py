from flask import ( Blueprint,request,url_for,jsonify,render_template )
from .G_VAR import R_PATH
import os
import json

bp = Blueprint('plotDataAPI',__name__,url_prefix='/')

@bp.route('/plotDataAPI')
def plotDataAPI():
    hostname = request.args.get('hostname','')
    timeLength = request.args.get('interval',10)
    rawData=[]
    plotData=[]
    with open (os.path.join(R_PATH,'static/js/HostData.json'),'r') as f:
        rawData = json.load(f)

    rawData = rawData[-int(timeLength):]
    for record in rawData:
        for time in record:
            hosts = record[time]
            for host in hosts:
                if(host['hostname']==hostname):
                    plotData.append({time:host['totalMemUsage']*100})

    return jsonify(plotData)