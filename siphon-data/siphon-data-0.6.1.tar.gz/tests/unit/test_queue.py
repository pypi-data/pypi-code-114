import asyncio
from functools import partial
from unittest.mock import mock_open, patch

import pytest
from pydantic import BaseModel

from siphon import (AioQueue, CollectedError, DiscardOnViolation,
                    RaiseOnViolation, TypedAioQueue, ViolationStrategy,
                    queuecollect)

ahundredints = partial(range, 100)


def test_typed_queue():
    q = TypedAioQueue(model=int)
    q.put_nowait(100)

    assert q.qsize() == 1
    assert q.get_nowait() == 100


def test_typed_queue_violation():
    q = TypedAioQueue(model=int, violations_strategy=RaiseOnViolation)
    with pytest.raises(TypeError):
        q.put_nowait('100')


def test_typed_queue_violation_strat():
    strat = ViolationStrategy()
    with pytest.raises(NotImplementedError):
        strat(1, int)


def test_typed_queue_violation_strat_type_checking():
    strat = ViolationStrategy()
    assert strat._is_item_of_type(1, int) is True
    assert strat._is_item_of_type('1', int) is False


def test_raise_strat():
    strat = RaiseOnViolation()
    assert strat.checks(1, int) == 1
    with pytest.raises(TypeError):
        strat.checks(1, str)


def test_ignore_strat():
    strat = DiscardOnViolation()
    assert strat.checks(1, int) == 1
    assert strat.checks(1, str) is None


def test_queue_plus():
    q = AioQueue()
    [q.put_nowait(i) for i in ahundredints()]
    assert q.collect() == [i for i in ahundredints()]


def test_collect_transform():
    q = AioQueue()
    [q.put_nowait(i) for i in ahundredints()]
    data = q.collect(transform=lambda x: str(x))
    assert all(map(lambda x: isinstance(x, str), data))


def test_iter():
    q = AioQueue()
    [q.put_nowait(i) for i in ahundredints()]

    o = []
    for i in q:
        o.append(i)
    assert o == [i for i in ahundredints()]


@pytest.mark.asyncio
async def test_aiter():
    q = AioQueue()
    [q.put_nowait(i) for i in ahundredints()]

    o = []
    async for i in q:
        o.append(i)
    assert o == [i for i in ahundredints()]


@pytest.mark.asyncio
async def test_queuecollect_errs():
    eq = AioQueue()

    @queuecollect(errors=eq)
    def raiseerr(i: int, err=Exception):
        raise err(f'error with {i}')

    [await raiseerr(i) for i in ahundredints()]
    assert eq.qsize() == 100
    assert all([isinstance(x, CollectedError) for x in eq.collect()])


@pytest.mark.asyncio
async def test_queuecollect_collectederror():
    eq = AioQueue()

    @queuecollect(errors=eq)
    def raiseerr(i: int, **kwargs):
        raise Exception(f'error with {i}')

    await raiseerr(1, test=2)
    err = eq.get_nowait()
    assert err.error_name == 'Exception'
    assert err.func_name == 'raiseerr'
    assert err.args == (1,)
    assert err.kwargs == {'test': 2}
    assert err.func.__name__ == 'raiseerr'


@pytest.mark.asyncio
async def test_queuecollect_collectederror_reraise():
    eq = AioQueue()

    @queuecollect(errors=eq)
    def raiseerr(i: int, **kwargs):
        raise Exception(f'error with {i}')

    await raiseerr(1, test=2)
    with pytest.raises(Exception):
        err = await eq.get()
        err.reraise


@pytest.mark.asyncio
async def test_queuecollect_success():
    eq = AioQueue()

    @queuecollect(errors=eq)
    def raiseerr(i: int):
        return i

    o = [await raiseerr(i) for i in ahundredints()]
    assert len(o) == 100
    assert all([isinstance(x, int) for x in o])


@pytest.mark.asyncio
async def test_queuecollect_successqueue():
    eq = AioQueue()
    sq = AioQueue()

    @queuecollect(errors=eq, success=sq)
    def raiseerr(i: int):
        return i

    [await raiseerr(i) for i in ahundredints()]
    assert sq.qsize() == 100
    assert all([isinstance(x, int) for x in sq])


@pytest.mark.asyncio
@patch('builtins.open', mock_open(read_data='data'))
async def test_csv_export():
    q = AioQueue()
    await q.put({'a': 1})

    q.to_csv('test.csv', cols=['a'])

    await q.put({'a': 1})
    q.to_json('test.json')


@pytest.mark.asyncio
@patch('builtins.open', mock_open(read_data='data'))
async def test_csv_export_with_transform():
    class TestModel(BaseModel):
        a: int = 1

    q = AioQueue()
    await q.put(TestModel())

    q.to_csv('test.csv', cols=['a'], pre_transform=lambda x: x.dict())

    await q.put(TestModel())
    q.to_json('test.json', pre_transform=lambda x: x.dict())


@pytest.mark.asyncio
async def test_consumer_on_queue():
    q = AioQueue()

    found = []
    q.add_consumer(lambda x: found.append(x))

    for i in range(100):
        await q.put(i)

    await q.wait_for_consumer()

    assert len(found) == 100
    assert q.empty()


@pytest.mark.asyncio
async def test_consumer_added():
    q = AioQueue()
    task = q.add_consumer(lambda x: x)
    assert isinstance(task, asyncio.Task)
