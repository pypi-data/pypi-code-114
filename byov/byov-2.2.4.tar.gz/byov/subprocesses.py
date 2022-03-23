# This file is part of Build Your Own Virtual machine.
#
# Copyright 2018 Vincent Ladeuil.
# Copyright 2014-2017 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 3, as published by the
# Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranties of MERCHANTABILITY,
# SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import unicode_literals
import logging
import subprocess


from byov import errors


logger = logging.getLogger(__name__)


def run(args, cmd_input=None, raise_on_error=True):
    """Run the specified command capturing output and errors.

    :param args: A list of a command and its arguments.

    :param cmd_input: A unicode string to feed the command with.

    :param raise_on_error: A boolean controlling whether or not an exception is
        raised if the command fails.

    :return: A tuple of the return code, the output and the errors as unicode
        strings.

    """
    stdin = None
    if cmd_input is not None:
        stdin = subprocess.PIPE
        cmd_input = cmd_input.encode('utf8')
    logger.debug('Running {}'.format(' '.join(args)))
    proc = subprocess.Popen(args,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=stdin)
    out, err = proc.communicate(cmd_input)
    out = out.decode('utf8')
    err = err.decode('utf8')
    if raise_on_error and proc.returncode:
        raise errors.CommandError(args, proc.returncode, out, err)
    logger.debug('Returned: {}'.format(proc.returncode))
    if out:
        logger.debug('stdout: {}'.format(out))
    if err:
        logger.debug('stderr: {}'.format(err))
    return proc.returncode, out, err


def pipe(args):
    """Run the specified command as a pipe.

    The caller is responsible for processing the output and the errors.

    :param args:  A list of a command and its arguments.

    :return: The Popen object.
    """
    proc = subprocess.Popen(args,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc
