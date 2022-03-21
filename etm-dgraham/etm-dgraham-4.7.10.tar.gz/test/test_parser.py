#!/usr/bin/env python3
from dateutil import parser
import pendulum
s = "2000-10-03"

def parse(s, dayfirst=False, yearfirst=False):
    pi = parser.parserinfo(
            dayfirst=dayfirst,
            yearfirst=yearfirst
            )
    dt = parser.parse(s, parserinfo=pi)
    print(f"dayfirst: {dayfirst} ", s, ' -> ', dt)

parse(s, dayfirst=True)
parse(s, dayfirst=False)


# yearfirst and dayfirst. Each true or false. Whenever an
# ambiguous date is parsed, the dayfirst and yearfirst
# parameters control how the information is processed.
# Here is the precedence in each case:
#
#   If dayfirst is False and yearfirst is False:
#       MM-DD-YY
#       DD-MM-YY
#       YY-MM-DD
#
#   If dayfirst is True and yearfirst is False:
#       DD-MM-YY
#       MM-DD-YY
#       YY-MM-DD
#
#   If dayfirst is False and yearfirst is True:
#       YY-MM-DD
#       MM-DD-YY
#       DD-MM-YY
#
#   If dayfirst is True and yearfirst is True:
#       YY-MM-DD
#       DD-MM-YY
#       MM-DD-YY
#
