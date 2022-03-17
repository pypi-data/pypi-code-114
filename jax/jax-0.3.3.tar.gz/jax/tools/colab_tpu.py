# Copyright 2020 Google LLC
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

"""Utilities for running JAX on Cloud TPUs via Colab."""

import requests
import os

from jax.config import config

TPU_DRIVER_MODE = 0


def setup_tpu(tpu_driver_version='tpu_driver_nightly'):
  """Sets up Colab to run on TPU.

  Note: make sure the Colab Runtime is set to Accelerator: TPU.

  Args
  ----
  tpu_driver_version : (str) specify the version identifier for the tpu driver.
    Defaults to "tpu_driver_nightly". Occasionally the nightly release contains bugs,
    in which case a workaround is to use a known working version from a previous date,
    for example "tpu_driver-0.1dev20211031".
  """
  global TPU_DRIVER_MODE

  if not TPU_DRIVER_MODE:
    colab_tpu_addr = os.environ['COLAB_TPU_ADDR'].split(':')[0]
    url = f'http://{colab_tpu_addr}:8475/requestversion/{tpu_driver_version}'
    requests.post(url)
    TPU_DRIVER_MODE = 1

  # The following is required to use TPU Driver as JAX's backend.
  config.FLAGS.jax_xla_backend = "tpu_driver"
  config.FLAGS.jax_backend_target = "grpc://" + os.environ['COLAB_TPU_ADDR']
