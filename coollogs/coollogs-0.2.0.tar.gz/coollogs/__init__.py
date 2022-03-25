"""Console printing made beautiful

This module is made for more verbouse and eye-catching printing of
information to console.

Example:
    Here is simple example that shows, how to implement basic logging:

        $ from coollogs import log
        $ log.info("That's it!")

Attributes:
    log (Logger): Initialized ``Logger`` object with default arguments,
        that is easy to import and ready to usage.

Todo:
    * Save output to file
    * Deal somehow with super-long arguments
    * Provide more information on logging, with different block prefixes

for further information visit github repo of this project
https://github.com/LeKSuS-04/Cool-logs
"""

__version__ = '0.2.0'
__author__ = 'Alexey Tarasov'

from .logger import Colors, Logger, log_level

# Ready-to-use Logger object
log = Logger()
