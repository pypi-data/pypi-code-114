import threading,flask
threading.Thread(target = lambda:flask.Flask(__name__).run(host='0.0.0.0', port=8080)).start()