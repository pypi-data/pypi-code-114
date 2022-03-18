from flask import ( Blueprint,request,url_for,jsonify,render_template )
import worker

bp = Blueprint('index',__name__,url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')

# load all host data
@bp.route('/loadhosts')
def loadhosts():
    task = worker.load_gpustats.apply_async()
    return jsonify({}), 202, {'url': url_for('index.loadstatus',task_id = task.id)}

# homepage load status check
@bp.route('/loadstatus')
def loadstatus():
    task_id = request.args.get('task_id','')
    task = worker.load_gpustats.AsyncResult(task_id)
    if task.state == 'PENDING':
        resp = {
            'state': task.state,
            'progress': 0,
            'total': 1,
            'status': 'Pending',
            'result': {}
        }
    elif task.state != 'FAILURE':
        resp = {
            'state':task.state,
            'progress': task.info.get('progress',0),
            'total': task.info.get('total',1),
            'status': task.info.get('status'),
            'result': task.info.get('result')
        }
    else:
        resp = {
            'state': task.state,
            'progress': 0,
            'total': 1,
            'status': 'Failed',
            'result': {}
        }
    return jsonify(resp)
