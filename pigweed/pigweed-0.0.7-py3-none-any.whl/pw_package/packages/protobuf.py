# Copyright 2021 The Pigweed Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""Install and check status of Protobuf."""

import pathlib
from typing import Sequence

import pw_package.git_repo
import pw_package.package_manager


class Protobuf(pw_package.git_repo.GitRepo):
    """Install and check status of Protobuf."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         name='protobuf',
                         url="https://github.com/protocolbuffers/protobuf.git",
                         commit='15c40c6cdac2f816a56640d24a5c4c3ec0f84b00',
                         **kwargs)

    def info(self, path: pathlib.Path) -> Sequence[str]:
        return (
            f'{self.name} installed in: {path}',
            "Enable by running 'gn args out' and adding this line:",
            f'  dir_pw_third_party_protobuf = "{path}"',
        )


pw_package.package_manager.register(Protobuf)
