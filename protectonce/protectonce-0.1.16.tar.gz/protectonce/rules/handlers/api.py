import os


def get_flask_routes(data):
    try:
        if not data:
            return []
        paths = [data['args'][data['config']['argsIndex']]]
        if(not paths):
            return []
        if("/static/<path:filename>" in paths):  # skipping default path set by flask
            return []
        methods = data['kwargs'].get('methods', None)
        host = os.uname()[1]
        routeData = [{'paths': paths, 'methods': ["GET"]
                      if methods is None else methods, 'host': host}]
        return routeData
    except Exception as e:
        print(
            f'[PROTECTONCE_ERROR] api.get_flask_routes failed with error {e}')
        return []
