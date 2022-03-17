import pytest

import coredis
from coredis.exceptions import ConnectionError, TimeoutError
from coredis.sentinel import (
    MasterNotFoundError,
    Sentinel,
    SentinelConnectionPool,
    SlaveNotFoundError,
)


class SentinelTestClient:
    def __init__(self, cluster, id):
        self.cluster = cluster
        self.id = id

    async def sentinel_masters(self):
        self.cluster.connection_error_if_down(self)
        self.cluster.timeout_if_down(self)

        return {self.cluster.service_name: self.cluster.master}

    async def sentinel_slaves(self, master_name):
        self.cluster.connection_error_if_down(self)
        self.cluster.timeout_if_down(self)

        if master_name != self.cluster.service_name:
            return []

        return self.cluster.slaves


class SentinelTestCluster:
    def __init__(
        self, service_name="localhost-redis-sentinel", ip="127.0.0.1", port=6379
    ):
        self.clients = {}
        self.master = {
            "ip": ip,
            "port": port,
            "is_master": True,
            "is_sdown": False,
            "is_odown": False,
            "num_other_sentinels": 0,
        }
        self.service_name = service_name
        self.slaves = []
        self.nodes_down = set()
        self.nodes_timeout = set()

    def connection_error_if_down(self, node):
        if node.id in self.nodes_down:
            raise ConnectionError

    def timeout_if_down(self, node):
        if node.id in self.nodes_timeout:
            raise TimeoutError

    def client(self, host, port, **kwargs):
        return SentinelTestClient(self, (host, port))


@pytest.fixture()
def cluster(request):
    def teardown():
        coredis.sentinel.Redis = saved_Redis

    cluster = SentinelTestCluster()
    saved_Redis = coredis.sentinel.Redis
    coredis.sentinel.Redis = cluster.client
    request.addfinalizer(teardown)

    return cluster


@pytest.fixture()
def sentinel(request, cluster, event_loop):
    return Sentinel([("foo", 26379), ("bar", 26379)], loop=event_loop)


@pytest.mark.asyncio()
async def test_discover_master(sentinel):
    address = await sentinel.discover_master("localhost-redis-sentinel")
    assert address == ("127.0.0.1", 6379)


@pytest.mark.asyncio()
async def test_discover_master_error(sentinel):
    with pytest.raises(MasterNotFoundError):
        await sentinel.discover_master("xxx")


@pytest.mark.asyncio()
async def test_discover_master_sentinel_down(cluster, sentinel):
    # Put first sentinel 'foo' down
    cluster.nodes_down.add(("foo", 26379))
    address = await sentinel.discover_master("localhost-redis-sentinel")
    assert address == ("127.0.0.1", 6379)
    # 'bar' is now first sentinel
    assert sentinel.sentinels[0].id == ("bar", 26379)


@pytest.mark.asyncio()
async def test_discover_master_sentinel_timeout(cluster, sentinel):
    # Put first sentinel 'foo' down
    cluster.nodes_timeout.add(("foo", 26379))
    address = await sentinel.discover_master("localhost-redis-sentinel")
    assert address == ("127.0.0.1", 6379)
    # 'bar' is now first sentinel
    assert sentinel.sentinels[0].id == ("bar", 26379)


@pytest.mark.asyncio()
async def test_master_min_other_sentinels(cluster):
    sentinel = Sentinel([("foo", 26379)], min_other_sentinels=1)
    # min_other_sentinels
    with pytest.raises(MasterNotFoundError):
        await sentinel.discover_master("localhost-redis-sentinel")
    cluster.master["num_other_sentinels"] = 2
    address = await sentinel.discover_master("localhost-redis-sentinel")
    assert address == ("127.0.0.1", 6379)


@pytest.mark.asyncio()
async def test_master_odown(cluster, sentinel):
    cluster.master["is_odown"] = True
    with pytest.raises(MasterNotFoundError):
        await sentinel.discover_master("localhost-redis-sentinel")


@pytest.mark.asyncio()
async def test_master_sdown(cluster, sentinel):
    cluster.master["is_sdown"] = True
    with pytest.raises(MasterNotFoundError):
        await sentinel.discover_master("localhost-redis-sentinel")


@pytest.mark.asyncio()
async def test_discover_slaves(cluster, sentinel):
    assert await sentinel.discover_slaves("localhost-redis-sentinel") == []

    cluster.slaves = [
        {"ip": "slave0", "port": 1234, "is_odown": False, "is_sdown": False},
        {"ip": "slave1", "port": 1234, "is_odown": False, "is_sdown": False},
    ]
    assert await sentinel.discover_slaves("localhost-redis-sentinel") == [
        ("slave0", 1234),
        ("slave1", 1234),
    ]

    # slave0 -> ODOWN
    cluster.slaves[0]["is_odown"] = True
    assert await sentinel.discover_slaves("localhost-redis-sentinel") == [
        ("slave1", 1234)
    ]

    # slave1 -> SDOWN
    cluster.slaves[1]["is_sdown"] = True
    assert await sentinel.discover_slaves("localhost-redis-sentinel") == []

    cluster.slaves[0]["is_odown"] = False
    cluster.slaves[1]["is_sdown"] = False

    # node0 -> DOWN
    cluster.nodes_down.add(("foo", 26379))
    assert await sentinel.discover_slaves("localhost-redis-sentinel") == [
        ("slave0", 1234),
        ("slave1", 1234),
    ]
    cluster.nodes_down.clear()

    # node0 -> TIMEOUT
    cluster.nodes_timeout.add(("foo", 26379))
    assert await sentinel.discover_slaves("localhost-redis-sentinel") == [
        ("slave0", 1234),
        ("slave1", 1234),
    ]


@pytest.mark.asyncio()
async def test_master_for(redis_sentinel, host_ip):
    master = redis_sentinel.master_for("localhost-redis-sentinel")
    assert await master.ping()
    assert master.connection_pool.master_address == (host_ip, 6380)

    # Use internal connection check
    master = redis_sentinel.master_for(
        "localhost-redis-sentinel", check_connection=True
    )
    assert await master.ping()


@pytest.mark.asyncio()
async def test_slave_for(redis_sentinel):
    slave = redis_sentinel.slave_for("localhost-redis-sentinel")
    assert await slave.ping()


@pytest.mark.asyncio()
async def test_slave_for_slave_not_found_error(cluster, sentinel):
    cluster.master["is_odown"] = True
    slave = sentinel.slave_for("localhost-redis-sentinel", db=9)
    with pytest.raises(SlaveNotFoundError):
        await slave.ping()


@pytest.mark.asyncio()
async def test_slave_round_robin(cluster, sentinel):
    cluster.slaves = [
        {"ip": "slave0", "port": 6379, "is_odown": False, "is_sdown": False},
        {"ip": "slave1", "port": 6379, "is_odown": False, "is_sdown": False},
    ]
    pool = SentinelConnectionPool("localhost-redis-sentinel", sentinel)
    rotator = await pool.rotate_slaves()
    assert set(rotator) == {("slave0", 6379), ("slave1", 6379)}
