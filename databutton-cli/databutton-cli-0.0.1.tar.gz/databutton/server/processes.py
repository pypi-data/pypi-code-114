import asyncio
from fastapi import FastAPI, Response, WebSocket, status
from httpx import AsyncClient
from starlette.background import BackgroundTask
from starlette.responses import StreamingResponse
from websockets import WebSocketClientProtocol, connect

_streamlit_processes = {}


async def start_processes(app: FastAPI, apps: dict, start_port: int = 8501):
    global _streamlit_processes
    for i, (route, fpath) in enumerate(apps.items()):
        p = StreamlitProcess(route, fpath, start_port + i)
        await p.start()
        _streamlit_processes[p.route] = p
        print('Registering route for', route)
        p.add_route_to_app(app)


async def get_proxy_port_from_route(route: str):
    if route in _streamlit_processes:
        return _streamlit_processes.get(route).port
    return None


async def get_proxy(route: str, rest: str = ''):
    # Find correct app
    port = await get_proxy_port_from_route(route)
    if port is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    client = AsyncClient(base_url=f"http://localhost:{port}/")
    req = client.build_request("GET", rest)
    r = await client.send(req, stream=True)
    return StreamingResponse(
        r.aiter_raw(),
        background=BackgroundTask(r.aclose),
        headers=r.headers
    )


class StreamlitProcess:
    def __init__(self, route: str, fpath: str, port: int):
        self.port = port
        self.route = route
        self.fpath = fpath
        self.subprocess = None

    async def start(self):
        cmd = f"streamlit run {self.fpath} --server.port={self.port} --server.headless=true"
        self.subprocess = await asyncio.create_subprocess_shell(cmd,
                                                                stdout=asyncio.subprocess.PIPE,
                                                                stderr=asyncio.subprocess.PIPE)

    def add_route_to_app(self, app_to_add: FastAPI):
        @app_to_add.get(self.route + "/{rest:path}")
        async def _get_app(rest: str):
            return await get_proxy(self.route, rest)

        @app_to_add.websocket(self.route + "/stream")
        async def handle_proxied_websocket(ws_client: WebSocket):
            await ws_client.accept()
            port = await get_proxy_port_from_route(self.route)
            if port is None:
                return Response(status_code=status.HTTP_404_NOT_FOUND)
            async with connect(f"ws://localhost:{port}/stream", max_size=10**20) as ws_server:
                fwd_task = asyncio.create_task(forward(ws_client, ws_server))
                rev_task = asyncio.create_task(reverse(ws_client, ws_server))
                await asyncio.gather(fwd_task, rev_task)


async def forward(ws_client: WebSocket, ws_server: WebSocketClientProtocol):
    try:
        while True:
            data = await ws_client.receive_bytes()
            await ws_server.send(data)
    except Exception as e:
        print('Error when forwarding WS message', e)
        pass


async def reverse(ws_client: WebSocket, ws_server: WebSocketClientProtocol):
    try:
        while True:
            data = await ws_server.recv()
            await ws_client.send_text(data)
    except Exception as e:
        # Swallow error
        print('Error when reversing WS Message', e)
        pass
