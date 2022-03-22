
from types import SimpleNamespace
from bs4 import BeautifulSoup


async def remote(hub, **kwargs):
    """
    This is the entrypoint for the async code in your project
    """
    print("inside remote!")
    ctx = SimpleNamespace(acct={})
    repo_list = await hub.exec.request.raw.get(
            ctx,
            url="https://repo.saltproject.io/salt/singlebin/",
    )
    soup = BeautifulSoup(repo_list["ret"], "html.parser")
    links = [node['href'][:-1] for node in soup.find_all('a') if node.get('href') and node["href"].endswith("/") and node["href"] != "../"]
    print("\n".join(sorted(links)))
