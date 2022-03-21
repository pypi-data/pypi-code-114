try:
    # System imports.
    from typing import Tuple, Any, Union, Optional

    import asyncio
    import os
    import sanic
    import aiohttp
    import requests

    
except ModuleNotFoundError as e:
    print(f'Error: {e}\nAttempting to install packages now (this may take a while).')

    for module in (
        'sanic==21.6.2',
        'aiohttp',
        'requests'
    ):
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

    os.system('clear')

    print('Installed packages, restarting script.')

    python = sys.executable




sanic_app = sanic.Sanic(__name__)
server = None




@sanic_app.route('/', methods=['GET'])
async def root(request: sanic.request.Request) -> None:
    if 'Accept' in request.headers and request.headers['Accept'] == 'application/json':
        return sanic.response.json(
            {
                "status": "online"
            }
        )

    return sanic.response.html(
         """
<!DOCTYPE html>
<html>
  <head>
    <body scroll="no" style="overflow: hidden">
<img src="https://img1.picmix.com/output/stamp/normal/1/5/1/8/128151_83449.gif" alt="troll face" class="stamp" width="800" height="400">
  </body>
</html>
        """
    )

sanic_app.run(host="0.0.0.0", port=80)