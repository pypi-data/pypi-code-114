def switch_remote_server():
    from ai_serving.client import AIRedisService
    from ai_serving.client.helper import get_run_args, get_switch_parser
    args = get_run_args(get_switch_parser)
    AIRedisService.switch_server(args)

def show_config():
    from ai_serving.client import AIRedisService
    from ai_serving.client.helper import get_run_args, get_status_parser
    args = get_run_args(get_status_parser)
    AIRedisService.show_config(args)

def terminate():
    from ai_serving.client import AIRedisService
    from ai_serving.client.helper import get_run_args, get_shutdown_parser
    args = get_run_args(get_shutdown_parser)
    AIRedisService.terminate(args)

def idle():
    from ai_serving.client import AIRedisService
    from ai_serving.client.helper import get_run_args, get_shutdown_parser
    args = get_run_args(get_shutdown_parser)
    AIRedisService.idle(args)

def restart_clients():
    from ai_serving.client import AIRedisService
    from ai_serving.client.helper import get_run_args, get_shutdown_parser
    args = get_run_args(get_shutdown_parser)
    AIRedisService.restart_clients(args)
