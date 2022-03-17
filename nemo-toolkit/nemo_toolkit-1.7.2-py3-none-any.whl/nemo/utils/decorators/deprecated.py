# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__all__ = [
    'deprecated',
]

import functools
import inspect

import wrapt

from nemo.utils import logging

# Remember which deprecation warnings have been printed already.
_PRINTED_WARNING = {}


def deprecated(wrapped=None, version=None, explanation=None):
    """
        Decorator which can be used for indicating that a function/class is deprecated and going to be removed.
        Tracks down which function/class printed the warning and will print it only once per call.

        Args:
          version: Version in which the function/class will be removed (optional).
          explanation: Additional explanation, e.g. "Please, ``use another_function`` instead." (optional).
    """

    if wrapped is None:
        return functools.partial(deprecated, version=version, explanation=explanation)

    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        # Check if we already warned about that function.
        if wrapped.__name__ not in _PRINTED_WARNING.keys():
            # Add to list so we won't print it again.
            _PRINTED_WARNING[wrapped.__name__] = True

            # Prepare the warning message.
            entity_name = "Class" if inspect.isclass(wrapped) else "Function"
            msg = f"{entity_name} ``{wrapped.__name__}`` is deprecated."

            # Optionally, add version and explanation.
            if version is not None:
                msg = f"{msg} It is going to be removed in the {version} version."

            if explanation is not None:
                msg = f"{msg} {explanation}"

            # Display the deprecated warning.
            logging.warning(msg)

        # Call the function.
        return wrapped(*args, **kwargs)

    return wrapper(wrapped)
