# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This module is largely a wrapper around `jaxlib` that performs version
# checking on import.

import platform
import re
import os
import warnings
from typing import Optional, Tuple

__all__ = [
  'cuda_linalg', 'cuda_prng', 'cusolver', 'hip_linalg', 'hip_prng',
  'hipsolver','jaxlib', 'lapack', 'pocketfft', 'pytree',
   'tpu_driver_client', 'version', 'xla_client', 'xla_extension',
]

# Before attempting to import jaxlib, warn about experimental
# machine configurations.
if platform.system() == "Darwin" and platform.machine() == "arm64":
  warnings.warn("JAX on Mac ARM machines is experimental and minimally tested. "
                "Please see https://github.com/google/jax/issues/5501 in the "
                "event of problems.")

try:
  import jaxlib as jaxlib
except ModuleNotFoundError as err:
  raise ModuleNotFoundError(
    'jax requires jaxlib to be installed. See '
    'https://github.com/google/jax#installation for installation instructions.'
    ) from err

import jax.version
from jax.version import _minimum_jaxlib_version as _minimum_jaxlib_version_str
try:
  import jaxlib.version
except Exception as err:
  # jaxlib is too old to have version number.
  msg = f'This version of jax requires jaxlib version >= {_minimum_jaxlib_version_str}.'
  raise ImportError(msg) from err


# Checks the jaxlib version before importing anything else from jaxlib.
# Returns the jaxlib version string.
def check_jaxlib_version(jax_version: str, jaxlib_version: str,
                         minimum_jaxlib_version: str):
  # Regex to match a dotted version prefix 0.1.23.456.789 of a PEP440 version.
  # PEP440 allows a number of non-numeric suffixes, which we allow also.
  # We currently do not allow an epoch.
  version_regex = re.compile(r"[0-9]+(?:\.[0-9]+)*")
  def _parse_version(v: str) -> Tuple[int, ...]:
    m = version_regex.match(v)
    if m is None:
      raise ValueError(f"Unable to parse jaxlib version '{v}'")
    return tuple(int(x) for x in m.group(0).split('.'))

  _jax_version = _parse_version(jax_version)
  _minimum_jaxlib_version = _parse_version(minimum_jaxlib_version)
  _jaxlib_version = _parse_version(jaxlib_version)

  if _jaxlib_version < _minimum_jaxlib_version:
    msg = (f'jaxlib is version {jaxlib_version}, but this version '
           f'of jax requires version >= {minimum_jaxlib_version}.')
    raise RuntimeError(msg)

  if _jaxlib_version > _jax_version:
    msg = (f'jaxlib version {jaxlib_version} is newer than and '
           f'incompatible with jax version {jax_version}. Please '
           'update your jax and/or jaxlib packages.')
    raise RuntimeError(msg)

  return _jaxlib_version

version_str = jaxlib.version.__version__
version = check_jaxlib_version(
  jax_version=jax.version.__version__,
  jaxlib_version=jaxlib.version.__version__,
  minimum_jaxlib_version=jax.version._minimum_jaxlib_version)



# Before importing any C compiled modules from jaxlib, first import the CPU
# feature guard module to verify that jaxlib was compiled in a way that only
# uses instructions that are present on this machine.
import jaxlib.cpu_feature_guard as cpu_feature_guard
cpu_feature_guard.check_cpu_features()

import jaxlib.xla_client as xla_client
import jaxlib.lapack as lapack
import jaxlib.pocketfft as pocketfft

xla_extension = xla_client._xla
pytree = xla_client._xla.pytree
jax_jit = xla_client._xla.jax_jit
pmap_lib = xla_client._xla.pmap_lib

try:
  import jaxlib.cusolver as cusolver  # pytype: disable=import-error
except ImportError:
  cusolver = None

try:
  import jaxlib.hipsolver as hipsolver  # pytype: disable=import-error
except ImportError:
  hipsolver = None

try:
  import jaxlib.cusparse as cusparse  # pytype: disable=import-error
except ImportError:
  cusparse = None

try:
  import jaxlib.hipsparse as hipsparse  # pytype: disable=import-error
except ImportError:
  hipsparse = None

try:
  import jaxlib.cuda_prng as cuda_prng  # pytype: disable=import-error
except ImportError:
  cuda_prng = None

try:
  import jaxlib.hip_prng as hip_prng  # pytype: disable=import-error
except ImportError:
  hip_prng = None

try:
  import jaxlib.cuda_linalg as cuda_linalg  # pytype: disable=import-error
except ImportError:
  cuda_linalg = None

try:
  import jaxlib.hip_linalg as hip_linalg  # pytype: disable=import-error
except ImportError:
  hip_linalg = None

# Jaxlib code is split between the Jax and the Tensorflow repositories.
# Only for the internal usage of the JAX developers, we expose a version
# number that can be used to perform changes without breaking the main
# branch on the Jax github.
xla_extension_version = getattr(xla_client, '_version', 0)

# TODO(phawkins): remove old name
_xla_extension_version = xla_extension_version

# Version number for MLIR:Python APIs, provided by jaxlib.
mlir_api_version = getattr(xla_client, 'mlir_api_version', 0)

try:
  from jaxlib import tpu_client as tpu_driver_client  # pytype: disable=import-error
except:
  tpu_driver_client = None  # type: ignore


# TODO(rocm): check if we need the same for rocm.
cuda_path: Optional[str]
cuda_path = os.path.join(os.path.dirname(jaxlib.__file__), "cuda")
if not os.path.isdir(cuda_path):
  cuda_path = None

if xla_extension_version >= 58:
  transfer_guard_lib = xla_client._xla.transfer_guard_lib
