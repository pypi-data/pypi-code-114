from flask import ( Blueprint,request,url_for,jsonify,render_template )
from . import worker

bp = Blueprint('host',__name__,url_prefix='/')

# route to each host page
@bp.route('/host')
def host():
    return render_template('host.html')

# load separate host data
@bp.route('/loadhost')
def loadhost():
    hostname = [request.args.get('hostname','')]
    task = worker.load_gpustat_by_host.apply_async(hostname)
    return jsonify({}), 202, {'url': url_for('host.hostloadstatus',task_id = task.id)}

# hostpage load status check    
@bp.route('/hostloadstatus')
def hostloadstatus():
    task_id = request.args.get('task_id','')
    task = worker.load_gpustat_by_host.AsyncResult(task_id)

    if task.state != 'SUCCESS':
        response = {'state':task.state, 'result': ''}
    else:
        response = {'state':task.state, 'result':task.info.get('result','')}
    return jsonify(response) 