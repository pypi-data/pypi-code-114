# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import logging

from .create_plugin_cmd import (
    DatasetNameTransformer,
    LicenceTransformer,
    PluginContext,
    Transformer,
)

LOG = logging.getLogger(__name__)


class DatasetPluginContext(PluginContext):
    kind = "dataset"

    def build_transformers(self):
        Transformer(
            self,
            "plugin_name",
            desc="the plugin name",
            default="my_plugin",
            glob=True,
            help="""The plugin name is used to define:
     - The python package name `import climetlab_{plugin_name} `
     - The pip package name ` pip install climetlab-{plugin-name} `.
  It will also be used to suggest and appropriate URL on github.
  The plugin_name can be the name of the project you are working on,
  but notice that it should be specific enough as only one plugin with
  a given name can be installed. Highly generic names (such as "meteo",
  "domain", "copernicus", "country-name" are not recommended.
  The plugin name cannot be easily modified afterwards.""",
        )
        self.check_output_dir()
        DatasetNameTransformer(
            self,
            "dataset_name",
            desc="the dataset name",
            default="",
            glob=True,
            force_prefix="plugin-name-climetlab-template",
            help="""The dataset name is used as follow:
  A climetlab dataset plugin package can provides one or more
  datasets. This scripts creates a plugin with one dataset.
  The dataset name will be used by the end users to access
  the data through CliMetLab with:
  cml.load_dataset("dataset-name", ...)
  The convention is to make the dataset name start with
  "plugin-name-climetlab-template".
  The dataset name can easily be modified afterwards, without
  regenerating a new plugin, simply by editing the setup.py.""",
        )

        Transformer(
            self,
            "full_name",
            desc="your full name",
            default=self.get_default_full_name(),
            help="""The full name is used in setup.py to define the maintainer of the pip package.""",
        )
        Transformer(
            self,
            "email",
            desc="your email",
            default=self.get_default_email(),
            help="""The email is used in setup.py to define the email maintainer of the pip package.""",
        )
        Transformer(
            self,
            "github_username",
            desc="your Github user name",
            default="ecmwf-lab",
            help="""The github username (or github space name) is used
  to suggest a github repository url.
  The username (ecmwf-lab) should be used if you wish to host your
  repository on the github space "https://github.com/ecmwf-lab/").
  Else, please provide your own github user name.""",
        )
        Transformer(
            self,
            "repo_url",
            desc="the repository url",
            default="github_username_climetlab_template/climetlab-plugin-name-climetlab-template",
            force_prefix="https://github.com/",
            help="""The repository url name is used to define:
      - The package url in the setup.py, i.e. the url published in Pypi for pip.
      - The links in the README file.
  If your do not want to host you repository on github,
  please edit manually the generated setup.py afterwards.""",
        )

        LicenceTransformer(
            self,
            "licence",
            desc="Use the modified APACHE licence with ECMWF additions?",
            help="""The APACHE 2.0 licence is used for the plugin code.
  Most users should answer "n" to use the standard APACHE 2.0 licence.
  ECMWF users should answer "y" to add the appropriate addition to the licence.
  The licence is added in the plugin code:
      - In the header of each python file.
      - In the LICENSE file.
      - In the README.
  If you choose another licence, please modify these files manually afterwards.""",
        )
