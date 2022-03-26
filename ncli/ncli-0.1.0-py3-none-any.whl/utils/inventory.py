from httpx import Client, Response

from config import Config, load_config

config: Config = load_config()


def query_sw(query: str, parameters: dict) -> list[dict[str, str | int]]:
    headers = {"Content-Type": "application/json"}
    data = {
        "query": query,
        "parameters": parameters,
    }

    with Client() as client:
        response: Response = client.get(
            f"https://{{config.SW_HOST}}:17778/SolarWinds/InformationService/v3/Json/Query",
            headers=headers,
            auth=(config.SW_USER, config.SW_PASS),
            verify=False,
            json=data,
        )

    if response.status_code != 200:
        return None

    return response["results"]


def search_mac(mac: str) -> list[dict[str, str | int]]:
    query = """SELECT IPNode.IpNodeId as nodeid, IPNode.IPAddress as ip, Subnet.CIDR as cidr, IPNode.MAC as mac, IPNode.DhcpClientName as hostname
                FROM IPAM.IPNode
                INNER JOIN IPAM.Subnet ON IPNode.SubnetId = Subnet.SubnetId 
                WHERE MAC LIKE @m"""
    parameters = {"m": f"%{mac}%"}

    # results = query_sw(query, parameters)

    results = [
        {
            "nodeid": 1,
            "ip": "10.101.10.1",
            "network": "10.101.10.0",
            "cidr": 24,
            "mac": "52-54-00-1D-DA-08",
            "hostname": "PC1011.lab.local",
        }
    ]
