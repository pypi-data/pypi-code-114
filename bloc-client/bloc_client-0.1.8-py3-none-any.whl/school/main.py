import asyncio

from bloc_client import BlocClient
from truncate_sentence_function import CutSentence

async def main():
    client_name = "shcool-python"
    bloc_client = BlocClient(name=client_name)

    fake_rabbit_port = 6696
    fake_bloc_server_port = 80
    bloc_client.get_config_builder(
    ).set_server(
		"$bloc_server", fake_bloc_server_port,
    ).set_rabbitMQ(
        user="$user", password='$password',
        host="$host", port=fake_rabbit_port
    ).build_up()

    pyClient_func_group = bloc_client.register_function_group("math")
    pyClient_func_group.add_function(
        "calcu", # name your function node's name
		"receive numbers and do certain math operation to them", # the describe of your function node
		, # your function implement
        "截断器", "一个python client驱动的function节点", CutSentence())

    await bloc_client.run()

if __name__ == "__main__":
    asyncio.run(main())
