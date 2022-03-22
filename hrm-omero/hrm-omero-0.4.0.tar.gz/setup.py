# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['hrm_omero']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.3.2,<9.0.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'loguru>=0.5.3,<0.6.0',
 'omero-py>=5.9.0,<6.0.0']

entry_points = \
{'console_scripts': ['ome-hrm = hrm_omero.cli:main']}

setup_kwargs = {
    'name': 'hrm-omero',
    'version': '0.4.0',
    'description': 'A connector between the Huygens Remote Manager (HRM) and OMERO.',
    'long_description': '# The HRM-OMERO connector\n\nThis project provides a connector to allow for communication between an [HRM (Huygens\nRemote Manager)][hrm] and an [OMERO server][omero].\n\nIts purpose is to simplify the data transfer by allowing raw images to be downloaded\nfrom OMERO as well as uploading deconvolution results back to OMERO directly from within\nthe HRM web interface.\n\n## Setup\n\n### Installing requirements\n\n**NOTE**: strictly speaking, Java is only required for uploading data from the HRM to\nOMERO, so in case for whatever reason you are planning to use the connector in a\nunidirectional way only you might skip installing the Java packages below. Keep in mind\nthis scenario won\'t be tested by us though.\n\n#### CentOS / RHEL 7 and 8\n\n```bash\n# install the build-time requirements for Python 3.6 and Java 1.8 for Bio-Formats\nsudo yum install \\\n    python36 \\\n    python36-devel \\\n    openssl-devel \\\n    bzip2-devel \\\n    readline-devel \\\n    gcc-c++ \\\n    java-1.8.0-openjdk\n\n# define the target path for the virtual environment:\nHRM_OMERO_VENV="/opt/venvs/hrm-omero"\n\n# create a Python 3.6 virtual environment:\npython3 -m venv $HRM_OMERO_VENV\n\n# upgrade pip, install wheel:\n$HRM_OMERO_VENV/bin/pip install --upgrade pip wheel\n```\n\n#### Ubuntu 20.04\n\n```bash\napt install -y \\\n    python3.8-venv \\\n    openjdk-11-jre-headless\n\n# define the target path for the virtual environment:\nHRM_OMERO_VENV="/opt/venvs/hrm-omero"\n\n# create a Python 3.6 virtual environment:\npython3 -m venv $HRM_OMERO_VENV\n\n# upgrade pip, install wheel:\n$HRM_OMERO_VENV/bin/pip install --upgrade pip wheel\n\n# install the pre-built Ice wheel from the OME project:\n$ICE_WHEEL="zeroc_ice-3.6.5-cp38-cp38-linux_x86_64.whl"\nwget "https://github.com/ome/zeroc-ice-ubuntu2004/releases/download/0.2.0/$ICE_WHEEL"\n$HRM_OMERO_VENV/bin/pip install $ICE_WHEEL\n```\n\n### Installing the HRM-OMERO package\n\n```bash\n# install the connector - please note that it takes quite a while (~15min) as it needs\n# to build (compile) the ZeroC Ice bindings:\n$HRM_OMERO_VENV/bin/pip install hrm-omero\n\n# from now on you can simply call the connector using its full path, there is no need\n# to pre-activate the virtual environment - you could even drop your pyenv completely:\n$HRM_OMERO_VENV/bin/ome-hrm --help\n\n# this is even usable as a drop-in replacement for the legacy `ome_hrm.py` script:\ncd $PATH_TO_YOUR_HRM_INSTALLATION/bin\nmv "ome_hrm.py" "__old__ome_hrm.py"\nln -s "$HRM_OMERO_VENV/bin/ome-hrm" "ome_hrm.py"\n```\n\n### Configuration\n\nAdd the following lines to `/etc/hrm.conf` and fill in the desired values:\n\n```bash\n# Interaction with OMERO (if switched on in hrm/config).\nOMERO_HOSTNAME="omero.example.xy"\n# OMERO_PORT="4064"\nOMERO_CONNECTOR_LOGLEVEL="DEBUG"\n# OMERO_CONNECTOR_LOGFILE_DISABLED="true"\n```\n\nOn top of that it is necessary to explicitly set two environment variables for the\nApache process. By default (at least on recent Ubuntu and CentOS / RHEL versions) the\nsystem user running Apache is not allowed to write to its `$HOME` directory for security\nreasons. Therefore it is required to specify where the OMERO Python bindings and also\nJava may store cache files and preferences. This can be done by running the following\ncommand:\n\n```bash\nsystemctl edit apache2.service  # Debian / Ubuntu\nsystemctl edit httpd.service  # CentOS / RHEL / AlmaLinux\n```\n\nThere, add the following section, adjusting the path if desired:\n\n```systemd\n[Service]\nEnvironment=OMERO_USERDIR=/var/cache/omero\nEnvironment=JAVA_OPTS="-Djava.util.prefs.userRoot=/var/cache/omero/javaUserRoot"\n```\n\nNow make sure the specified directory exists and is writable by the Apache system user:\n```bash\nmkdir -v /var/cache/omero\nchown www-data:www-data /var/cache/omero  # Debian / Ubuntu\nchown apache:apache /var/cache/omero  # CentOS / RHEL / AlmaLinux\n```\n\nFinally, restart *Apache* by running the respective `systemctl` command from above while\nreplacing `edit` for `restart`.\n\n## Debugging\n\nThe connector will try to place log messages in a file in the *directory* specified as\n`$HRM_LOG` in the HRM configuration file **unless** a configuration option named\n`$OMERO_CONNECTOR_LOGFILE_DISABLED` is present and non-empty. In a standard setup this\nwill result in the log file being `/var/log/hrm/omero-connector.log`.\n\nIn addtion, log messages produced by the connector when called by HRM will be sent to\n`stderr`, which usually means they will end up in the web server\'s *error log*.\n\nBy default the connector will be rather silent as otherwise the log files will be\ncluttered up quite a bit on a production system. However, it is possible to increase the\nlog level by specifying `-v`, `-vv` and so on.\n\nSince this is not useful when being operated through the HRM web interface (which is\nthe default) it\'s also possible to set the verbosity level by adjusting the\n`OMERO_CONNECTOR_LOGLEVEL` in `/etc/hrm.conf`.\n\nValid settings are `"SUCCESS"`, `"INFO"`, `"DEBUG"` and `"TRACE"`. If the option is\ncommented out in the configuration file, the level will be set to `WARNING`.\n\n## Example Usage\n\nStore username and password in variables, export the OMERO_PASSWORD variable:\n\n```bash\nread OMERO_USER\nread -s OMERO_PASSWORD\nexport OMERO_PASSWORD   # use \'set --export OMERO_PASSWORD $OMERO_PASSWORD\' for fish\n```\n\n### Verifying Credentials\n\n```bash\nome-hrm \\\n    --user $OMERO_USER \\\n    checkCredentials\n```\n\n### Fetching OMERO tree information\n\nSet the `--id` parameter according to what part of the tree should be retrieved:\n\n```bash\nOMERO_ID="ROOT"                # fetches the base tree view for the current user\nOMERO_ID="G:4:Experimenter:9"  # fetches the projects of user \'9\' in group \'4\'\nOMERO_ID="G:4:Project:12345"   # fetches the datasets of project \'12345\'\nOMERO_ID="G:4:Dataset:65432"   # lists the images of dataset \'65432\'\n```\n\nThen run the actual command to fetch the information, the result will be a JSON tree:\n\n```bash\nome-hrm \\\n    --user $OMERO_USER \\\n    retrieveChildren \\\n    --id "$OMERO_ID"\n```\n\nFor example this could be the output when requesting `"G:4:Dataset:65432"`:\n\n```json\n[\n    {\n        "children": [],\n        "class": "Image",\n        "id": "G:4:Image:1311448",\n        "label": "4321_mko_ctx_77.tif",\n        "owner": "somebody"\n    },\n    {\n        "children": [],\n        "class": "Image",\n        "id": "G:4:Image:1566150",\n        "label": "test-image.tif",\n        "owner": "somebody"\n    }\n]\n```\n\n### Downloading an image from OMERO\n\nThis will fetch the second image from the example tree above and store it in `/tmp/`:\n\n```bash\nome-hrm \\\n    --user $OMERO_USER \\\n    OMEROtoHRM \\\n    --imageid "G:4:Image:1566150" \\\n    --dest /tmp/\n```\n\n### Uploading an image from the local file system to OMERO\n\nThe command below will import a local image file into the example dataset from above:\n\n```bash\nome-hrm \\\n    --user $OMERO_USER \\\n    HRMtoOMERO \\\n    --dset "G:4:Dataset:65432" \\\n    --file test-image.tif\n```\n\n[hrm]: https://huygens-rm.org/\n[omero]: https://www.openmicroscopy.org/omero/\n',
    'author': 'Niko Ehrenfeuchter',
    'author_email': 'nikolaus.ehrenfeuchter@unibas.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/hrm-omero/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
