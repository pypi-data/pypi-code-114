from pathlib import Path

import pytest
from ape import compilers, project

SOURCE_CODE_DIRECTORY = Path(__name__).parent / "contracts"


@pytest.fixture(params=[p.name for p in SOURCE_CODE_DIRECTORY.iterdir()])
def contract(request):
    yield (SOURCE_CODE_DIRECTORY / request.param).absolute()


def test_compile(contract):
    compilers.compile([contract])
    assert getattr(project, contract.stem)
