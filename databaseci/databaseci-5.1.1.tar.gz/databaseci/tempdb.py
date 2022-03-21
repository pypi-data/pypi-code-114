import socket
import time
from contextlib import contextmanager

import docker
import sqlalchemy
from pendulum import now
from psycopg2 import OperationalError

# from sqlbag import S

client = docker.from_env()


from .database import db


def try_connect(db_url, timeout=3.0, should_raise=True):
    start = now()

    while True:
        # try:
        try:
            with db(db_url).t() as t:
                t.q("select 1")
                return True
        except OperationalError as e:
            pass

        current = now()
        elapsed = current - start

        if elapsed.total_seconds() > timeout:
            if should_raise:
                raise RuntimeError("cannot connect")
            return False


def wait_open(port, host="localhost", timeout=3.0, should_raise=True):
    PAUSE = 0.1

    start = now()

    while True:

        try:
            s = socket.create_connection((host, port), timeout)
            s.close()
            return True
        except socket.error:
            pass

        elapsed = (now() - start).total_seconds()

        if elapsed > timeout:
            if should_raise:
                raise RuntimeError("timeout waiting for port")

            return False

        time.sleep(PAUSE)


def stop_container(container, wait=1):
    try:
        container.stop(timeout=wait)
    except docker.errors.NotFound:
        pass


def stop_containers(prefix, wait=1):
    for c in client.containers.list(ignore_removed=True):
        if c.name.startswith(prefix):
            stop_container(c, wait=wait)


@contextmanager
def temporary_docker_db():
    c = client.containers.run(
        "databaseci/tempdb-pg",
        name=f"tempdb-pg-{int(time.time())}",
        detach=True,
        remove=True,
        ports={"5432/tcp": None},
    )
    try:
        c.reload()

        port = c.ports["5432/tcp"][0]["HostPort"]
        db_url = f"postgresql://docker:pw@localhost:{port}/docker"

        wait_open(port, timeout=10)

        try_connect(db_url)
        yield db(db_url)

    finally:
        stop_container(c)


def pull_temporary_docker_db_image():
    print("pulling databaseci/tempdb-pg docker image...")
    client.images.pull("databaseci/tempdb-pg")


def cleanup_temporary_docker_db_containers():
    stop_containers("tempdb-pg-")
