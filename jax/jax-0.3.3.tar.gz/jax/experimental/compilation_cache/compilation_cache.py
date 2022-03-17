# Copyright 2021 Google LLC
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

import hashlib
import os
import re
import sys
from typing import List, Optional

import jax
from jax.experimental.compilation_cache.file_system_cache import FileSystemCache
import jax._src.lib
from jax._src.lib import xla_client
from absl import logging

_cache = None

def initialize_cache(path, max_cache_size_bytes=32 * 2**30):
  """Creates a global cache object. Should only be called once per process.

     max_cache_sixe defaults to 32GiB.
  """
  global _cache
  assert _cache == None, f"The cache path has already been initialized to {_cache._path}"
  _cache = FileSystemCache(path, max_cache_size_bytes)
  logging.warning("Initialized persistent compilation cache at %s", path)

def get_executable(xla_computation, compile_options, backend) -> Optional[xla_client.Executable]:
  """Returns the cached executable if present, or None otherwise."""
  assert _cache is not None, "initialize_cache must be called before you can call get_executable()"
  cache_key = get_cache_key(xla_computation, compile_options, backend)
  xla_executable_serialized = _cache.get(cache_key)
  if not xla_executable_serialized:
    return None
  xla_executable_deserialized = backend.deserialize_executable(
      xla_executable_serialized,
      compile_options)
  return xla_executable_deserialized

def put_executable(module_name, xla_computation, compile_options,
                   executable: xla_client.Executable, backend):
  """Adds 'executable' to the cache, possibly evicting older entries."""
  assert _cache is not None, "initialize_cache must be called before you can call put_executable()"
  cache_key = get_cache_key(xla_computation, compile_options, backend)
  logging.info('Writing %s to persistent compilation cache with key %s.',
               module_name, cache_key)
  serialized_executable = backend.serialize_executable(executable)
  _cache.put(cache_key, serialized_executable)

def _log_cache_key_hash(hash_obj, last_serialized: str, hashfn):
  if logging.vlog_is_on(1):
    # Log the hash of just this entry
    fresh_hash_obj = hashlib.sha256()
    hashfn(fresh_hash_obj)
    logging.vlog(1, "get_cache_key hash of serialized %s: %s", last_serialized,
                 fresh_hash_obj.digest().hex())
    # Log the cumulative hash
    logging.vlog(1, "get_cache_key hash after serializing %s: %s",
                 last_serialized, hash_obj.digest().hex())

def get_cache_key(xla_computation, compile_options, backend) -> str:
  """Creates a hashed string to use as a key to the compilation cache.

     get_cache_key takes in the xla_computation and compile_options of a program and hashes
     all the components into a uniuqe byte string. This byte string is returned as a regular
     string that is 256 characters long.

     Typical return value example:
      '14ac577cdb2ef6d986078b4054cc9893a9a14a16dbb0d8f37b89167c1f1aacdf'
  """
  entries = [
      ("computation",
       lambda hash_obj: _hash_computation(hash_obj, xla_computation)),
      ("compile_options",
       lambda hash_obj: _hash_compile_options(hash_obj, compile_options)),
      ("jax_lib version",
       lambda hash_obj: hash_obj.update(bytes(jax._src.lib.version_str.encode('utf-8')))),
      ("the backend", lambda hash_obj: _hash_platform(hash_obj, backend)),
      ("XLA flags", _hash_xla_flags),
  ]

  hash_obj = hashlib.sha256()
  for name, hashfn in entries:
    hashfn(hash_obj)
    _log_cache_key_hash(hash_obj, name, hashfn)
  return hash_obj.digest().hex()

def _hash_computation(hash_obj, xla_computation):
  # The HLO op_name metadata sometimes includes Python function pointers,
  # which cause spurious cache misses. Scrub anything that looks like a
  # function pointer. Example op_name metadata:
  #  op_name="jit(s)/custom_jvp_call_jaxpr
  #   [ jvp_jaxpr_thunk=<function _memoize.<locals>.memoized at 0x7f3fa30f0940>\n
  #   num_consts=0 ]"
  # TODO(skye): in theory this could cause us to scrub meaningful binary proto
  # data. Do something more robust.
  if isinstance(xla_computation, str):
    serialized_hlo = xla_computation.encode()  # MLIR module
  else:
    serialized_hlo = xla_computation.as_serialized_hlo_module_proto()
  scrubbed_hlo = re.sub(b" at 0x[a-f0-9]+>", b" at 0x...>", serialized_hlo)
  hash_obj.update(scrubbed_hlo)

def _hash_compile_options(hash_obj, compile_options_obj):
  assert len(dir(compile_options_obj)) == 31,(f"Unexpected number of CompileOption fields: "
                                              f"{len(dir(compile_options_obj))}. This likely: means that an extra "
                                              f"field was added, and this function needs to be updated.")

  if compile_options_obj.argument_layouts is not None:
    map(lambda shape: hash_obj.update(shape.to_serialized_proto()),
        compile_options_obj.argument_layouts)
  _hash_int(hash_obj, compile_options_obj.parameter_is_tupled_arguments)
  _hash_executable_build_options(hash_obj, compile_options_obj.executable_build_options)
  _hash_bool(hash_obj, compile_options_obj.tuple_arguments)
  _hash_int(hash_obj, compile_options_obj.num_replicas)
  _hash_int(hash_obj, compile_options_obj.num_partitions)
  if compile_options_obj.device_assignment is not None:
    hash_obj.update(compile_options_obj.device_assignment.serialize())

def _hash_executable_build_options(hash_obj, executable_obj):
  if jax._src.lib.xla_extension_version >= 61:
    expected_options = 32
  else:
    expected_options = 31
  assert len(dir(executable_obj)) == expected_options, (
        f"Unexpected number of executable_build_options fields: "
        f"{len(dir(executable_obj))}. This likely means that an extra "
        f"field was added, and this function needs to be updated.")
  if executable_obj.result_layout is not None:
    hash_obj.update(executable_obj.result_layout.to_serialized_proto())
  _hash_int(hash_obj, executable_obj.num_replicas)
  _hash_int(hash_obj, executable_obj.num_partitions)
  _hash_debug_options(hash_obj, executable_obj.debug_options)
  if executable_obj.device_assignment is not None:
    hash_obj.update(executable_obj.device_assignment.serialize())
  _hash_bool(hash_obj, executable_obj.use_spmd_partitioning)
  if jax._src.lib.xla_extension_version >= 61:
    _hash_bool(hash_obj, executable_obj.use_auto_spmd_partitioning)
  _hash_bool(hash_obj, executable_obj.allow_spmd_sharding_propagation_to_output)

def _hash_debug_options(hash_obj, debug_obj):
  _hash_bool(hash_obj, debug_obj.xla_cpu_enable_fast_math)
  _hash_bool(hash_obj, debug_obj.xla_cpu_fast_math_honor_infs)
  _hash_bool(hash_obj, debug_obj.xla_cpu_fast_math_honor_nans)
  _hash_bool(hash_obj, debug_obj.xla_cpu_fast_math_honor_division)
  _hash_bool(hash_obj, debug_obj.xla_cpu_fast_math_honor_functions)
  _hash_bool(hash_obj, debug_obj.xla_gpu_enable_fast_min_max)
  _hash_int(hash_obj, debug_obj.xla_backend_optimization_level)
  _hash_bool(hash_obj, debug_obj.xla_cpu_enable_xprof_traceme)
  _hash_bool(hash_obj, debug_obj.xla_llvm_disable_expensive_passes)
  _hash_bool(hash_obj, debug_obj.xla_test_all_input_layouts)

def _hash_platform(hash_obj, backend):
  _hash_string(hash_obj, backend.platform)
  _hash_string(hash_obj, backend.platform_version)
  _hash_string(hash_obj, backend.runtime_type)

_xla_flags_to_exclude_from_cache_key = [
    "--xla_dump_compress_protos",
    "--xla_dump_module_metadata",
    "--xla_dump_max_hlo_modules",
    "--xla_dump_include_timestamp",
    "--xla_dump_hlo_pass_re",
    "--xla_dump_hlo_module_re",
    "--xla_dump_hlo_snapshots",
    "--xla_dump_fusion_visualization",
    "--xla_dump_hlo_as_url",
    "--xla_dump_hlo_as_proto",
    "--xla_dump_hlo_as_text",
    "--xla_dump_to",
    "--xla_force_host_platform_device_count",
    "--xla_dump_disable_metadata",
    "--xla_dump_hlo_pipeline_re",
]

extra_flag_prefixes_to_include_in_cache_key: List[str] = []

def _hash_xla_flags(hash_obj):
  xla_flags = []

  xla_flags_env_var = os.getenv("XLA_FLAGS")
  if xla_flags_env_var:
    xla_flags.extend(xla_flags_env_var.split())

  for arg in sys.argv:
    if arg.startswith("--xla") or any(
        arg.startswith(p) for p in extra_flag_prefixes_to_include_in_cache_key):
      xla_flags.append(arg)

  # N.B. all XLA flags that take an argument must use '=' and not a space
  # (e.g. --xla_force_host_platform_device_count=8) (I think).
  for flag in xla_flags:
    if flag.split('=')[0] in _xla_flags_to_exclude_from_cache_key:
      logging.vlog(1, "Not including XLA flag in cache key: %s", flag)
      continue
    logging.vlog(1, "Including XLA flag in cache key: %s", flag)
    _hash_string(hash_obj, flag)

def _hash_int(hash_obj, int_var):
  hash_obj.update(int_var.to_bytes(8, byteorder='big'))

def _hash_bool(hash_obj, bool_var):
  hash_obj.update(bool_var.to_bytes(1, byteorder='big'))

def _hash_string(hash_obj, str_var):
  hash_obj.update(str_var.encode('utf-8').strip())

def is_initialized():
  return _cache is not None
