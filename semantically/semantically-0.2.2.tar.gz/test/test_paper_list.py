"""Testing semanticallys custom paper list"""

import pytest
from semantically import datastructures, paper_list

AUTHOR1 = datastructures.Author("1", "Test Guy 1")
AUTHOR2 = datastructures.Author("2", "Test Guy 2")
AUTHOR3 = datastructures.Author("3", "Test Guy 3")

PAPER1 = datastructures.Paper(
    "1",
    {"testId": 1},
    "www.test.com",
    "First test paper",
    "Abstract of first test paper.",
    "Test Journal",
    1990,
    14,
    55,
    1,
    False,
    ["Test Science"],
    [AUTHOR1, AUTHOR2],
)

PAPER2 = datastructures.Paper(
    paperId="2",
    externalIds={"testId": 2},
    title="First test paper",
    venue="Test Journal",
    year=2010,
    referenceCount=1,
    citationCount=2,
    isOpenAccess=True,
    authors=[AUTHOR3],
)

PAPER3 = datastructures.Paper(
    paperId="3",
    externalIds={"testId": 3},
    url="www.test.com",
    title="Third test paper",
    abstract="Abstract of third paper",
    venue="Test Journal",
    year=2020,
    referenceCount=10,
    citationCount=20,
    influentialCitationCount=4,
    isOpenAccess=True,
    fieldsOfStudy=["Test Science", "Assert Science"],
    authors=[AUTHOR3],
)

PAPER4 = datastructures.Paper(
    paperId="4",
)


def test_missing_all_data():
    test_list = paper_list.PaperList([PAPER1, PAPER3])
