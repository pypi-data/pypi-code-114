from battlenet_client.util import localize


def process_extras(function):
    def wrapper(*args, **kwargs):

        kwargs['params'] = {'locale': localize(args[1])}

        print(dict(function.__class__.__self__))
        if 'headers' not in kwargs.keys():
            kwargs['headers'] = {'Battlenet-Namespace': getattr(function.__class__.__self__, f"{args[2]}")}
        else:
            kwargs['headers']['Battlenet-Namespace'] = getattr(function.__class__.__self__, f"{args[2]}")

        if 'fields' in kwargs.keys():
            fields = ','.join([f"{key}={value}" for key, value in kwargs['fields'].items()])
            kwargs['params'].update({'fields': fields})
            kwargs.pop('fields', None)

        return function(*args, **kwargs)
    return wrapper
