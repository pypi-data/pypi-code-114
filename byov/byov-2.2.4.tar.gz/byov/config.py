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
import os
import sys

from byoc import (
    stacks,
    stores,
)

# python2 is not supported
if sys.version_info >= (3,):
    import importlib.util as imputil


class StartingNameMatcher(stacks.SectionMatcher):
    """A sub name section matcher.

    This selects sections starting with a given name with sections sorted
    alphanumerically.
    """

    def __init__(self, store, name):
        super(StartingNameMatcher, self).__init__(store)
        self.name = name

    def get_sections(self):
        """Get all sections starting with ``name`` in the store.

        The most generic sections are described first in the store, then more
        specific ones can be provided for reduced scopes.

        The returned sections are therefore returned in the reversed order so
        the most specific ones can be found first.
        """
        store = self.store
        # Longer sections are more specific, they should be returned first
        for _, section in sorted(
                store.get_sections(), reverse=True,
                # s[1].id or '' is to cope with None as a section id
                key=lambda s: s[1].id or ''):
            if section.id is None:
                # The no-name section is always included if present
                yield store, section
                continue
            if self.name is None:
                # If no name has been defined, no section can match
                continue
            section_name = section.id
            if self.name.startswith(section_name):
                yield store, section


VmMatcher = StartingNameMatcher
VmStore = stores.FileStore
VmCmdLineStore = stores.CommandLineStore


def system_config_dir():
    return '/etc/byov'


def user_config_dir():
    return os.path.expanduser('~/.config/byov')


def config_file_basename():
    return 'byov.conf'


def existing_config_file_basename():
    return 'existing-vms.conf'


def config_files_in(directory, conf_dir='conf.d', suffix='.conf'):
    """Iterate valid config file names in a directory."""
    fulldir = os.path.join(directory, conf_dir)
    if os.path.exists(fulldir):
        for p in sorted(os.listdir(fulldir)):
            # Filter out if not ending with suffix (so README files, for
            # example could be added or renaming can be used to disable config
            # files)
            if p.endswith(suffix):
                yield os.path.join(fulldir, p)


class VmStack(stacks.Stack):
    """Per-vm options."""

    def __init__(self, name):
        """Make a new stack for a given vm.

        :param name: The name of a virtual machine.

        The options are searched in following files for all sections matching
        ``name``. Additionally, defaults can be provided in the no-name
        section, except for ``existing-vms.conf`` which uses only the ``name``
        section.

        * the directory local file: ./byov.conf
        * the directory files in alphanumeric order: byov.conf.d/*.conf.
        * the user file: ~/.config/byov/byov.conf
        * the user files in alphanumeric order: ~/.config/byov/conf.d/*.conf.
        * the system-wide file: /etc/byov.conf
        * the system-wide files in alphanumeric order: /etc/byov/conf.d/*.conf.
        * the existing vms file (for vms already setup):
          ~/.config/byov/existing-vms.conf

        Longer section names are more specific than shorter ones across all
        files.
        """
        self.vm_name = name
        # FIXME: Would life be simpler if the cmdline store was shared ?  Or
        # not ? -- vila 2018-02-12

        # FIXME: Hard-coding a class name is a smell, at the very least make
        # this a class attribute. -- vila 2019-08-13
        self.cmdline_store = VmCmdLineStore()

        section_getters = []

        lpath = os.path.abspath(config_file_basename())
        self.local_store = self.get_shared_store(VmStore(lpath))
        section_getters.append(VmMatcher(self.local_store, name).get_sections)

        for cpath in config_files_in(os.path.abspath('.'), 'byov.conf.d'):
            store = self.get_shared_store(VmStore(cpath))
            section_getters.append(VmMatcher(store, name).get_sections)

        upath = os.path.join(user_config_dir(), config_file_basename())
        self.user_store = self.get_shared_store(VmStore(upath))
        section_getters.append(VmMatcher(self.user_store, name).get_sections)

        for cpath in config_files_in(user_config_dir()):
            store = self.get_shared_store(VmStore(cpath))
            section_getters.append(VmMatcher(store, name).get_sections)

        spath = os.path.join(system_config_dir(), config_file_basename())
        self.system_store = self.get_shared_store(VmStore(spath))
        section_getters.append(VmMatcher(self.system_store, name).get_sections)

        for cpath in config_files_in(system_config_dir()):
            store = self.get_shared_store(VmStore(cpath))
            section_getters.append(VmMatcher(store, name).get_sections)

        epath = os.path.join(user_config_dir(),
                             existing_config_file_basename())
        self.existing_store = self.get_shared_store(VmStore(epath))

        super(VmStack, self).__init__(
            section_getters, self.user_store, mutable_section_id=name)

    def iter_sections(self):
        """Iterate all the defined sections.

        We break the lazy loading from byoc here as we want to ensure that
        section referring to a matching host are matched across
        files. Otherwise, a more specific section in a file is masked by a
        shorter section in a previous file.
        """
        # First the cmdline section
        for store, section in self.cmdline_store.get_sections():
            yield store, section

        host_getters = []
        # Now we break the lazy loading: we need to find all matching sections
        # keeping track of the store rank for later sort.
        for rank, section_getter in enumerate(self.sections_def):
            host_getters.extend([(-rank, store, section)
                                 for store, section in section_getter()])
        # We sort on section name then store rank and reverse the whole.
        # Specific section comes first, ties respect store order
        # t[2].id or '' is to cope with None as a section id
        getters = sorted(host_getters, key=lambda t: (t[2].id or '', t[0]),
                         reverse=True)
        for _, store, section in getters:
            yield store, section

        # Finally the existing vm section
        # We want to match only the existing vm, not any other one
        for store, section in stacks.NameMatcher(self.existing_store,
                                                 self.vm_name).get_sections():
            yield store, section

    # FIXME: This should be a DictOption or a NameSpaceOption
    # -- vila 2018-01-08
    def get_nova_creds(self):
        """Get nova credentials from a config.

        This defines the set of options needed to authenticate against nova in
        a single place.

        :raises: byoc.errors.OptionMandatoryValueError if one of the
            options is not set.
        """
        creds = {}
        for k in ('username', 'password', 'tenant_name',
                  'auth_url', 'region_name'):
            opt_name = 'nova.{}'.format(k)
            creds[opt_name] = self.get(opt_name)
        return creds

    # FIXME: This should be a DictOption or a NameSpaceOption
    # -- vila 2021-12-03
    def get_aws_creds(self):
        """Get aws credentials from a config.

        This defines the set of options needed to authenticate against aws in
        a single place.

        :raises: byoc.errors.OptionMandatoryValueError if one of the
            options is not set.
        """
        creds = {}
        for k in ('key', 'secret', 'token', 'region'):
            opt_name = 'aws.{}'.format(k)
            creds[opt_name] = self.get(opt_name)
        return creds

    # FIXME: This should be a DictOption or a NameSpaceOption
    # -- vila 2021-12-03
    def get_scaleway_creds(self):
        """Get scaleway credentials from a config.

        This defines the set of options needed to authenticate against scaleway
        in a single place.

        :raises: byoc.errors.OptionMandatoryValueError if one of the
            options is not set.

        """
        # In theory the token is region agnostic, in practice you can't use
        # compute without a region (the api host name includes the region
        # name).
        creds = {}
        for k in ('access_key', 'token', 'region_name'):
            opt_name = 'scaleway.{}'.format(k)
            creds[opt_name] = self.get(opt_name)
        return creds


class ExistingVmStack(stacks.Stack):
    """Internal stack for defined vms."""

    def __init__(self, name):
        """Make a new stack for an already setup virtual machine.

        :param name: The name of a virtual machine.

        The options are searched only in the ~/.config/byov/existing-vms.conf
        which contains one section per virtual machine.
        """
        dpath = os.path.join(user_config_dir(),
                             existing_config_file_basename())
        store = self.get_shared_store(VmStore(dpath))
        section_getters = [stacks.NameMatcher(store,
                                              name).get_sections]
        super(ExistingVmStack, self).__init__(
            section_getters, store, mutable_section_id=name)


def import_user_byovs():
    # FIXME: This duplicates VmStack definition somehow, byow will need a
    # better way -- vila 2028-10-18
    for d in (os.path.join('.', 'byov.conf.d'),
              os.path.join(user_config_dir(), 'conf.d'),
              os.path.join(system_config_dir(), 'conf.d')):
        byov_path = os.path.abspath(os.path.join(d, 'byov.py'))
        if os.path.exists(byov_path):
            spec = imputil.spec_from_file_location('byov.config.user',
                                                   byov_path)
            module = imputil.module_from_spec(spec)
            spec.loader.exec_module(module)
