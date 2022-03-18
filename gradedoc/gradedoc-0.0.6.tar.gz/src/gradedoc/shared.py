"""Shared values."""


from __future__ import annotations

from pathlib import Path
import re
from typing import Iterator, Tuple

from gradedoc.configs import config

# * -------------------------------------------------------------------------------- * #
# * PATHS

if docx_dir := config.get("docx_dir"):
    docx_dir = Path(docx_dir)
else:
    docx_dir = Path().cwd()

DOCX = r"[!~$]*.docx"  # excludes "~$" prefix temporary files
PATHS = docx_dir.resolve().glob(DOCX)
GRADEBOOK_NAME = "grades.csv"
GRADEBOOK_PATH = Path(docx_dir / GRADEBOOK_NAME)


# * -------------------------------------------------------------------------------- * #
# * COMMENTS
# Patterns here use named groups to be reused during replacement operations.

if headers := config.get("headers"):
    header_names = headers.keys()
    max_scores = headers.values()
else:
    header_names = [
        "abstract",
        "introduction and theory",
        "procedures",
        "results and discussion",
        "conclusion",
    ]
    max_scores = [10, 20, 20, 40, 10]

# For searching document content to insert comments
HEADERS = header_names

# For the actual content of the inserted comments
FULL_HEADERS = HEADERS
MAX_SCORES = max_scores

# The summary to be inserted and its pattern for later updating by regex
SUMMARY_COMMENT = "TOTAL CONTENT: 100\nTOTAL DEDUCTIONS: 0\nGRADE: 100/100"
# We match on "\r" because Microsoft Word implicitly converts "\n" to "\r" on insertion
SUMMARY_COMMENT_PATTERN = re.compile(
    r"(?P<content>TOTAL CONTENT: )-?\d+\r"
    r"(?P<deductions>TOTAL DEDUCTIONS: )-?\d+\r"
    r"(?P<grade>GRADE: )-?\d+"
)

# The header comments to be inserted
HEADER_COMMENTS = [
    f"{header.upper()}: {score}/{score}"
    for header, score in zip(FULL_HEADERS, MAX_SCORES)
]
# The pattern for finding header comments as well as substituting scores within them
HEADER_COMMENT_PATTERNS = [
    re.compile(rf"(?P<header>{header.upper()}: )-?\d+") for header in FULL_HEADERS
]


# * -------------------------------------------------------------------------------- * #
# * SCORING
# Patterns here use named groups to be reused during scoring operations.

# Matches comments with a number at the very start of the comment
CONTENT_POINTS_LOST = r"(?P<value>\d{1,3})"
CONTENT_POINTS_LOST_PATTERN = re.compile(CONTENT_POINTS_LOST)

# Matches comments with "D", then a number, at the very start of the comment
DEDUCTION = r"D(?P<value>\d{1,3})"
DEDUCTION_PATTERN = re.compile(DEDUCTION)

# Matches three types of common deduction patterns, e.g. "D2: G2", "2: A1", or "G12"
COMMON_DEDUCTION_CODE = r"(?P<code>[A-Z]\d{1,3})"
COMMON_DEDUCTION_PATTERNS = [
    re.compile(rf"{CONTENT_POINTS_LOST}:\s?{COMMON_DEDUCTION_CODE}"),
    re.compile(rf"{DEDUCTION}:\s?{COMMON_DEDUCTION_CODE}"),
    re.compile(COMMON_DEDUCTION_CODE),
]

# * -------------------------------------------------------------------------------- * #
# * FUNCTIONS


def get_paths() -> Tuple[Iterator[Path], Path]:
    return PATHS, GRADEBOOK_PATH
