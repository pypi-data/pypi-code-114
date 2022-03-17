from multiprocessing import Process, Pool
import os
from datetime import datetime
import copy
import logging
import socket
import traceback
import random

import yaml
import redcap

import dax
from . import dax_tools_utils
from . import DAX_Settings
from .launcher import BUILD_SUFFIX
from . import log
from .errors import AutoProcessorError, DaxError
from . import utilities

# dax manager has 3 main classes: DaxManager has a DaxProjectSettingsManager
# which is a collection of DaxProjectSettings.

# TODO: archive old logs

# TODO: only run launch and update if there are open jobs


DAX_SETTINGS = DAX_Settings()

LOGGER = log.setup_debug_logger('manager', None)


def project_from_settings(settings_file):
    proj = settings_file.split('settings-')[1].split('.yaml')[0]
    return proj


def get_this_instance():
    # build the instance name
    this_host = socket.gethostname().split('.')[0]
    this_user = os.environ['USER']
    return '{}@{}'.format(this_user, this_host)


def check_lockfile(file):
    # Try to read host-PID from lockfile
    try:
        with open(file, 'r') as f:
            line = f.readline()

        host, pid = line.split('-')
        pid = int(pid)

        # Compare host to current host
        this_host = socket.gethostname().split('.')[0]
        if host != this_host:
            LOGGER.debug('different host, cannot check PID:{}', format(file))
        elif pid_exists(pid):
            LOGGER.debug('host matches and PID exists:{}'.format(str(pid)))
        else:
            LOGGER.debug('host matches and PID not running, deleting lockfile')
            os.remove(file)
    except IOError:
        LOGGER.debug('failed to read from lock file:{}'.format(file))
    except ValueError:
        LOGGER.debug('failed to parse lock file:{}'.format(file))


def pid_exists(pid):
    if pid < 0:
        return False   # NOTE: pid == 0 returns True
    try:
        os.kill(pid, 0)
    except ProcessLookupError:   # errno.ESRCH
        return False  # No such process
    except PermissionError:  # errno.EPERM
        return True  # Operation not permitted (i.e., process exists)
    else:
        return True  # no error, we can send a signal to the process


def is_locked(settings_path, lock_dir):
    _prefix = os.path.splitext(os.path.basename(settings_path))[0]
    flagfile = os.path.join(lock_dir, '{}_{}'.format(_prefix, BUILD_SUFFIX))

    LOGGER.debug('checking for flag file:{}'.format(flagfile))
    return os.path.isfile(flagfile)


def make_parents(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)


class DaxManagerError(Exception):
    """Custom exception raised with dax manager."""

    def __init__(self, message):
        Exception.__init__(self, 'Error with dax manager:{}'.format(message))


class DaxProjectSettings(object):
    def __init__(self):
        self.general = {}
        self.processors = []
        self.modules = []
        self.projects = []

    def dump(self):
        return {
            **self.general,
            'modules': self.modules,
            'yamlprocessors': self.processors,
            'projects': self.projects}

    def set_general(self, general):
        # TODO confirm it has required elements
        self.general = general

    def add_processor(self, processor):
        # TODO confirm it has required elements and maintain unique names
        self.processors.append(processor)

    def add_module(self, module):
        # TODO confirm it has required elements and maintain unique names
        self.modules.append(module)

    def add_project(self, project):
        # TODO confirm it has required elements and maintain unique names
        self.projects.append(project)

    def processor_names(self):
        return [x['name'] for x in self.processors]

    def module_names(self):
        return [x['name'] for x in self.modules]

    def module_byname(self, name):
        mod = None
        for m in self.modules:
            if m['name'] == name:
                mod = m
                break

        return mod

    def processor_byname(self, name):
        proc = None
        for p in self.processors:
            if p['name'] == name:
                proc = p
                break

        return proc


class DaxProjectSettingsManager(object):
    RCDATEFORMAT = '%Y-%m-%d %H:%M:%S'

    MOD_PREFIX = 'module_'

    PROC_PREFIX = 'processor_'

    FILE_HEADER = '''# This file generated by dax manager.
# Edits should be made on REDCap.
'''

    # initialize with REDCap url/key
    def __init__(
            self, redcap_url, redcap_key, instance_settings,
            local_dir, general_form='general'):

        self._general_form = general_form
        self._local_dir = local_dir
        self._instance_settings = instance_settings
        self.module_names = []
        self.processor_names = []
        self.rebuild_projects = []
        self.records = {}
        self._redcap = redcap.Project(redcap_url, redcap_key)

        # Initialize by loading from redcap project
        self.load()

    def list_settings_files(self):
        slist = os.listdir(self._local_dir)

        # Make full paths
        slist = [os.path.join(self._local_dir, f) for f in slist]

        # Only yaml files
        slist = [f for f in slist if f.endswith('.yaml') and os.path.isfile(f)]

        return slist

    def _load_metadata(self):
        self.metadata = self._redcap.metadata

    def _load_records(self):
        # Build the list of _complete fields from lists of modules/procesors
        field_list = self._redcap.field_names + ['general_complete']

        p = DaxProjectSettingsManager.PROC_PREFIX
        s = '_complete'
        field_list += [p + f + s for f in self.processor_names]

        p = DaxProjectSettingsManager.MOD_PREFIX
        s = '_complete'
        field_list += [p + f + s for f in self.module_names]

        self.records = self._redcap.export_records(
            fields=field_list, raw_or_label='label')

    def load(self):
        self._load_module_names()
        self._load_processor_names()
        self._load_metadata()
        self._load_records()
        LOGGER.info('loaded {} records'.format(len(self.records)))

    def get_record(self, project):
        # Get the record from the dataframe
        rec = None
        for r in self.records:
            if r['project_name'] == project:
                rec = r
                break

        return rec

    def update_each(self):
        errors = []
        now = datetime.now()

        # First load the settings from our defaults project
        default_settings = self.load_defaults(DaxProjectSettings())

        for name in self.project_names():
            settings = copy.deepcopy(default_settings)

            try:
                LOGGER.info('Loading project: ' + name)
                project = self.load_project(settings, name)
                settings.add_project(project)

                filename = os.path.join(
                    self._local_dir, 'settings-{}.yaml'.format(name))

                if self.settings_match(settings, filename):
                    LOGGER.info('settings unchanged:{}'.format(filename))
                else:
                    # Write project file
                    self.write_settings_file(filename, settings, now)

                    # Append project name to our list of rebuild projects
                    self.rebuild_projects.append(name)

            except DaxManagerError as e:
                err = 'error in project settings:project={}\n{}'.format(
                    project, e)
                LOGGER.info(err)
                errors.append(err)

        return errors

    def settings_match(self, settings, filename):
        if not os.path.exists(filename):
            # No existing file so we it changed
            return False

        # now compare old to new
        new_settings = settings.dump()
        old_settings = self.load_settings_file(filename)
        return (new_settings == old_settings)

    def load_settings_file(self, filename):
        settings = utilities.read_yaml(filename)
        return settings

    def write_settings_file(self, filename, settings, timestamp):
        LOGGER.info('Writing settings to file:' + filename)
        with open(filename, 'w') as f:
            f.write(self.FILE_HEADER)
            f.write('# {}\n'.format(str(timestamp)))
            yaml.dump(
                settings.dump(),
                f,
                sort_keys=False,
                default_flow_style=False,
                explicit_start=True)

    def general_defaults(self):
        rec = {}

        ins = self._instance_settings
        rec['processorlib'] = ins['main_processorlib']
        rec['modulelib'] = ins['main_modulelib']
        rec['singularity_imagedir'] = ins['main_singularityimagedir']
        rec['resdir'] = ins['main_resdir']
        rec['jobtemplate'] = ins['main_jobtemplate']
        rec['admin_email'] = ins['main_adminemail']
        rec['attrs'] = {}
        rec['attrs']['queue_limit'] = int(ins['main_queuelimit'])
        rec['attrs']['job_email_options'] = ins['main_jobemailoptions']
        rec['attrs']['job_rungroup'] = ins['main_rungroup']
        rec['attrs']['xnat_host'] = ins['main_xnathost']

        return rec

    def load_defaults(self, settings):
        # First set the general section
        settings.set_general(self.general_defaults())

        return settings

    def _load_module_names(self):
        p = DaxProjectSettingsManager.MOD_PREFIX
        self.module_names = sorted([
            x.split(p)[1] for x in self._redcap.forms if x.startswith(p)])

    def _load_processor_names(self):
        p = DaxProjectSettingsManager.PROC_PREFIX
        self.processor_names = sorted([
            x.split(p)[1] for x in self._redcap.forms if x.startswith(p)])

    def get_module_keys(self, module):
        _m = self.metadata
        prefix = DaxProjectSettingsManager.MOD_PREFIX
        form = prefix + module

        # Get all the fields for the module's form
        all_list = [f['field_name'] for f in _m if f['form_name'] == form]

        # Find the args key for this module
        args_list = [f for f in all_list if f.endswith('_args')]
        if len(args_list) > 1:
            msg = 'multiple _file keys for module:{}'.format(module)
            raise DaxManagerError(msg)
        elif len(args_list) == 0:
            msg = 'no _file key for module:{}'.format(module)
            raise DaxManagerError(msg)

        args_key = args_list[0]

        # Find the file key for this module
        file_list = [f for f in all_list if f.endswith('_file')]
        if len(file_list) > 1:
            msg = 'multiple _file keys for module:{}'.format(module)
            raise DaxManagerError(msg)
        elif len(file_list) == 0:
            msg = 'no _file key for module:{}'.format(module)
            raise DaxManagerError(msg)

        file_key = file_list[0]

        return (file_key, args_key)

    def get_processor_keys(self, processor):
        _m = self.metadata

        # Get all the fields for the module's form
        prefix = DaxProjectSettingsManager.PROC_PREFIX
        form = prefix + processor
        all_list = [f['field_name'] for f in _m if f['form_name'] == form]

        # Find the args key for this module
        args_list = [f for f in all_list if f.endswith('_args')]
        if len(args_list) > 1:
            msg = 'multiple _file keys for processor:{}'.format(processor)
            raise DaxManagerError(msg)
        elif len(args_list) == 0:
            msg = 'no _file key for processor:{}'.format(processor)
            raise DaxManagerError(msg)

        args_key = args_list[0]

        # Find the file key for this module
        file_list = [f for f in all_list if f.endswith('_file')]
        if len(file_list) > 1:
            msg = 'multiple _file keys for processor:{}'.format(processor)
            raise DaxManagerError(msg)
        elif len(file_list) == 0:
            msg = 'no _file key for processor:{}'.format(processor)
            raise DaxManagerError(msg)

        file_key = file_list[0]

        return (file_key, args_key)

    def load_module_record(self, module, project):
        rc_rec = self.get_record(project)
        dax_rec = {'name': module}

        # Get the _file and _args field name for this module
        file_key, args_key = self.get_module_keys(module)

        # Get the filepath using the file key
        dax_rec['filepath'] = rc_rec[file_key]

        # Parse arguments
        if args_key in rc_rec and len(rc_rec[args_key].strip()) > 0:
            rlist = rc_rec[args_key].strip().split('\r\n')
            rdict = {}
            for arg in rlist:
                key, val = arg.split(':', 1)
                rdict[key] = val.strip()

            dax_rec['arguments'] = rdict

        return dax_rec

    def load_processor_record(self, processor, project):
        rc_rec = self.get_record(project)
        dax_rec = {'name': processor}

        # Get the _file and _args field name for this processor
        file_key, args_key = self.get_processor_keys(processor)

        # Get the filepath
        dax_rec['filepath'] = rc_rec[file_key]

        # Check for arguments
        if args_key in rc_rec and len(rc_rec[args_key].strip()) > 0:
            rlist = rc_rec[args_key].strip().split('\r\n')
            rdict = {}
            for arg in rlist:
                try:
                    key, val = arg.split(':', 1)
                    rdict[key] = val.strip()
                except ValueError as e:
                    msg = 'invalid arguments:{}'.format(e)
                    raise DaxManagerError(msg)

            dax_rec['arguments'] = rdict

        return dax_rec

    def is_enabled_module(self, module, project):
        prefix = DaxProjectSettingsManager.MOD_PREFIX
        form = prefix + module
        rec = self.get_record(project)
        complete = rec[form + '_complete']
        return (complete == 'Complete')

    def is_enabled_processor(self, processor, project):
        prefix = DaxProjectSettingsManager.PROC_PREFIX
        form = prefix + processor
        rec = self.get_record(project)
        try:
            complete = rec[form + '_complete']
            return (complete == 'Complete')
        except KeyError:
            # Probably don't have permissions on instrument
            LOGGER.error(f'Unable to access {form}_complete in REDCap')
            return False
            

    def project_names(self):
        complete_field = self._general_form + '_complete'
        instance_field = 'gen_daxinstance'

        # Filter to only include projects for this instance that are Complete
        this_instance = get_this_instance()
        plist = [
            r['project_name'] for r in self.records if
            r[instance_field] == this_instance and
            r[complete_field] == 'Complete']

        return plist

    def load_project(self, settings, project):
        proj_proc = []
        proj_mod = []

        # Get the project modules
        for name in self.module_names:
            if not self.is_enabled_module(name, project):
                continue

            # Make a new module
            mod = self.load_module_record(name, project)
            mod['name'] = name

            # Add the module to our settings
            settings.add_module(mod)

            # Append it to list for this project
            proj_mod.append(name)

        # Get the project processors
        for name in self.processor_names:
            if not self.is_enabled_processor(name, project):
                continue

            # Make a new custom processor
            proc = self.load_processor_record(name, project)
            proc['name'] = name

            # Add the custom module to our settings
            settings.add_processor(proc)

            # Append it to list for this project
            proj_proc.append(name)

        return {
            'project': project,
            'modules': ','.join(sorted(proj_mod)),
            'yamlprocessors': ','.join(sorted(proj_proc))}

    def delete_disabled(self):
        # Delete disabled project settings files
        enabled_projects = self.project_names()
        for curf in self.list_settings_files():
            curp = project_from_settings(curf)
            if curp not in enabled_projects:
                LOGGER.info('deleting disabled project:{}'.format(curf))
                os.remove(curf)

        return

    def get_last_start_time(self, project):
        rec = self.get_record(project)

        return rec['build_laststarttime']

    def get_last_run(self, project):
        if project in self.rebuild_projects:
            return None

        # Find the record for this project
        rec = self.get_record(project)

        # Get the start/finish times of last complete build
        last_start = rec['build_lastcompletestarttime']
        last_finish = rec['build_lastcompletefinishtime']

        if last_start != '' and last_finish != '' and last_start < last_finish:
            return datetime.strptime(last_start, self.RCDATEFORMAT)
        else:
            return None

    def set_last_build_start(self, project):
        last_start = datetime.strftime(datetime.now(), self.RCDATEFORMAT)

        rec = {
            'project_name': project,
            'build_laststarttime': last_start,
            'build_status_complete': '1'}

        LOGGER.info('set last build start: project={}, {}'.format(
            project,
            last_start))

        try:
            response = self._redcap.import_records([rec])
            assert 'count' in response
        except Exception as e:
            err = 'redcap import failed'
            LOGGER.info(err)
            LOGGER.info(e)
        except AssertionError as e:
            err = 'redcap import failed'
            LOGGER.info(e)
            raise DaxManagerError(err)
        except Exception as e:
            err = 'connection to REDCap interrupted'
            LOGGER.info(e)
            raise DaxManagerError(err)

    def set_last_build_complete(self, project):
        last_finish = datetime.strftime(datetime.now(), self.RCDATEFORMAT)
        last_start = self.get_last_start_time(project)
        last_duration = self.duration(last_start, last_finish)

        rec = {
            'project_name': project,
            'build_lastcompletestarttime': last_start,
            'build_lastcompletefinishtime': last_finish,
            'build_lastcompleteduration': last_duration,
            'build_status_complete': '2'}

        LOGGER.info('set last build: project={}, start={}, finish={}'.format(
            project,
            last_start,
            last_finish))

        try:
            response = self._redcap.import_records([rec])
            assert 'count' in response
        except AssertionError:
            err = 'redcap import failed'
            raise DaxManagerError(err)
        except Exception:
            err = 'connection to REDCap interrupted'
            raise DaxManagerError(err)

    def duration(self, start_time, finish_time):
        try:
            time_delta = (datetime.strptime(finish_time, self.RCDATEFORMAT) -
                          datetime.strptime(start_time, self.RCDATEFORMAT))
            secs = time_delta.total_seconds()
            hours = int(secs // 3600)
            mins = int((secs % 3600) // 60)
            if hours > 0:
                duration = '{} hrs {} mins'.format(hours, mins)
            else:
                duration = '{} mins'.format(mins)
        except Exception as e:
            LOGGER.debug(e)
            duration = None

        return duration


class DaxManager(object):
    FDATEFORMAT = '%Y%m%d-%H%M%S'
    DDATEFORMAT = '%Y%m%d'

    def __init__(self, api_url, api_key_instances, api_key_projects):

        # TODO: test the api keys or catch errors from pycap to
        # handle when redcap is down

        # Load settings for this instance
        instance_settings = self.load_instance_settings(
            api_url, api_key_instances)

        LOGGER.debug(instance_settings)

        self.settings_dir = instance_settings['main_projectsettingsdir']
        self.log_dir = instance_settings['main_logdir']
        self.max_build_count = int(instance_settings['main_buildlimit'])
        self.max_upload_count = int(instance_settings['main_uploadlimit'])
        self.res_dir = instance_settings['main_resdir']
        self.admin_emails = instance_settings['main_adminemail'].split(',')
        self.lock_dir = os.path.join(self.res_dir, 'FlagFiles')
        self.job_template = instance_settings['main_jobtemplate']
        self.smtp_host = instance_settings['main_smtphost']
        self.mode = instance_settings['main_mode']
        self.enabled = (instance_settings['main_complete'] == 'Complete')

        # Create our settings manager and update our settings directory
        self.settings_manager = DaxProjectSettingsManager(
            api_url,
            api_key_projects,
            instance_settings,
            self.settings_dir)

    def is_enabled_instance(self):
        return (self.enabled)

    def is_enabled_build(self):
        return ('build' in self.mode.lower())

    def is_enabled_launch(self):
        return ('launch' in self.mode.lower())

    def is_enabled_upload(self):
        return ('upload' in self.mode.lower())

    def is_enabled_update(self):
        # update is tied to upload here
        return ('upload' in self.mode.lower())

    def load_instance_settings(
            self, redcap_url, redcap_key, main_form='main'):

        self._main_form = main_form

        # Initialize redcap projec
        self._redcap = redcap.Project(redcap_url, redcap_key)

        # get this instance name
        instance_name = get_this_instance()
        LOGGER.debug('instance={}'.format(instance_name))

        # Return the record associated with this instance_name
        fields = self._redcap.field_names + [main_form + '_complete']
        return self._redcap.export_records(
            records=[instance_name], fields=fields, raw_or_label='label')[0]

    def refresh_settings(self):
        # Update settings files, only writing if something changed
        errors = self.settings_manager.update_each()

        # Delete any left over settings files
        self.settings_manager.delete_disabled()

        # Load settings files
        self.settings_list = self.settings_manager.list_settings_files()
        LOGGER.info(self.settings_list)

        return errors

    def log_name(self, runtype, project, timestamp):
        dname = datetime.strftime(timestamp, self.DDATEFORMAT)
        fname = '{}_{}_{}.log'.format(
            runtype, project, datetime.strftime(timestamp, self.FDATEFORMAT))
        log = os.path.join(self.log_dir, project, dname, fname)

        # Make sure the parent dirs exist
        make_parents(log)

        return log

    def queue_builds(self, build_pool):
        # TODO: sort builds by how long we expect them to take,
        # shortest to longest

        # Array to store result accessors
        build_results = [None] * len(self.settings_list)

        # Run each
        for i, settings_path in enumerate(self.settings_list):
            proj = project_from_settings(settings_path)
            log = self.log_name('build', proj, datetime.now())
            last_run = self.get_last_run(proj)

            LOGGER.info('SETTINGS:{}'.format(settings_path))
            LOGGER.info('PROJECT:{}'.format(proj))
            LOGGER.info('LOG:{}'.format(log))
            LOGGER.info('LASTRUN:' + str(last_run))
            build_results[i] = build_pool.apply_async(
                self.run_build, [proj, settings_path, log, last_run])

        return build_results

    def run(self):
        # Refresh project settings
        settings_errors = self.refresh_settings()

        run_errors = settings_errors
        max_build_count = self.max_build_count
        build_pool = None
        build_results = None
        num_build_threads = 0

        if self.is_enabled_build():
            # Build
            lock_list = os.listdir(self.lock_dir)
            lock_list = [x for x in lock_list if x.endswith('_BUILD_RUNNING.txt')]
            cur_build_count = len(lock_list)
            LOGGER.info('count of already running builds:' + str(cur_build_count))

            num_build_threads = max_build_count - cur_build_count
            if num_build_threads < 1:
                LOGGER.info('max builds already:{}'.format(str(cur_build_count)))
            else:
                LOGGER.info('starting {} more builds'.format(
                    str(num_build_threads)))
                build_pool = Pool(processes=num_build_threads)
                build_results = self.queue_builds(build_pool)
                build_pool.close()  # Close the pool, I dunno if this matters

        if self.is_enabled_update():
            # Update
            LOGGER.info('updating')
            for settings_path in self.settings_list:
                try:
                    proj = project_from_settings(settings_path)

                    LOGGER.info('updating jobs:' + proj)
                    log = self.log_name('update', proj, datetime.now())
                    self.run_update(settings_path, log)
                except (AutoProcessorError, DaxError) as e:
                    err = 'error running update:project={}\n{}'.format(proj, e)
                    LOGGER.error(err)
                    run_errors.append(err)

        if self.is_enabled_launch():
            # Launch - report to log if locked
            LOGGER.info('launching')
            # TODO: implement a better sorting method here so that launching
            # is explicitly fair. This random sample is a temporary solution.
            for settings_path in random.sample(
                    self.settings_list, len(self.settings_list)):
                try:
                    proj = project_from_settings(settings_path)

                    LOGGER.info('launching jobs:' + proj)
                    log = self.log_name('launch', proj, datetime.now())
                    self.run_launch(settings_path, log)
                except (AutoProcessorError, DaxError) as e:
                    err = 'error running launch:project={}\n{}'.format(proj, e)
                    LOGGER.error(err)
                    run_errors.append(err)

        if self.is_enabled_upload():
            # Upload - report to log if locked
            log = self.log_name('upload', 'upload', datetime.now())
            upload_process = Process(
                target=self.run_upload,
                args=(log,))
            LOGGER.info('starting upload')
            upload_process.start()
            LOGGER.info('waiting for upload')
            upload_process.join()
            LOGGER.info('upload complete')

        if self.is_enabled_build() and num_build_threads > 0:
            # Wait for builds to finish
            LOGGER.info('waiting for builds to finish')
            build_pool.join()

            # Extract any errors and add to list
            build_errors = [x.get() for x in build_results if x.get()]
            run_errors.extend(build_errors)

        if run_errors:
            LOGGER.info('ERROR:dax manager DONE with errors')
        else:
            LOGGER.info('run DONE with no errors!')

        return run_errors

    def run_build(self, project, settings_file, log_file, lastrun):
        build_error = None

        # Check for existing lock
        if is_locked(settings_file, self.lock_dir):
            LOGGER.warn('cannot build, lock exists:{}'.format(settings_file))
            # TODO: check if it's really running, if not send a notification
        else:
            # dax.bin.build expects a map of project to lastrun
            proj_lastrun = {project: lastrun}

            LOGGER.info('run_build:start:{},{}'.format(project, lastrun))
            self.set_last_build_start(project)
            logging.getLogger('dax').handlers = []
            try:
                dax.bin.build(
                    settings_file, log_file, True, proj_lastrun=proj_lastrun)
                logging.getLogger('dax').handlers = []
            except Exception:
                err = 'error running build:proj={}:err={}'.format(
                    project, traceback.format_exc())
                LOGGER.error(err)
                build_error = err

            self.set_last_build_complete(project)
            LOGGER.info('run_build:done:{}'.format(project))
            return build_error

    def set_last_build_start(self, project):
        self.settings_manager.set_last_build_start(project)

    def set_last_build_complete(self, project):
        self.settings_manager.set_last_build_complete(project)

    def get_last_run(self, project):
        return self.settings_manager.get_last_run(project)

    def run_launch(self, settings_file, log_file):
        logging.getLogger('dax').handlers = []
        dax.bin.launch_jobs(settings_file, log_file, debug=True)
        logging.getLogger('dax').handlers = []

    def run_update(self, settings_file, log_file):
        logging.getLogger('dax').handlers = []
        dax.bin.update_tasks(settings_file, log_file, debug=True)
        logging.getLogger('dax').handlers = []

    def run_upload(self, log_file):
        logging.getLogger('dax').handlers = []
        dax_tools_utils.upload_tasks(log_file, debug=True, resdir=self.res_dir,
                                     num_threads=self.max_upload_count)
        logging.getLogger('dax').handlers = []

    def all_ready(self, results):
        ready = True
        for i, res in enumerate(results):
            if not res.ready():
                LOGGER.debug('not ready:{}'.format(str(i)))
                ready = False

        return ready

    def email_errors(self, errors):
        # email the errors
        _msg = 'ERRORS:\n\n'
        _msg += '\n\n'.join(errors)
        _msg += '\n\n'
        _to = self.admin_emails
        _subj = 'ERROR:dax manager'
        utilities.send_email_netrc(self.smtp_host, _to, _subj, _msg)

    def clean_lockfiles(self):
        lock_list = os.listdir(self.lock_dir)

        # Make full paths
        lock_list = [os.path.join(self.lock_dir, f) for f in lock_list]

        # Check each lock file
        for file in lock_list:
            LOGGER.debug('checking lock file:{}'.format(file))
            check_lockfile(file)


if __name__ == '__main__':
    API_URL = os.environ['API_URL']
    API_KEY_P = os.environ['API_KEY_DAX_PROJECTS']
    API_KEY_I = os.environ['API_KEY_DAX_INSTANCES']

    # Make our dax manager
    manager = DaxManager(API_URL, API_KEY_I, API_KEY_P)

    if manager.is_enabled_instance():
        # Clean up existing lock files
        manager.clean_lockfiles()

        # And run it
        errors = manager.run()

        # Show errors
        if errors:
            msg = 'ERRORS:\n'
            msg += '\n\n'.join(errors)
            msg += '\n\n'
            LOGGER.info(msg)
    else:
        LOGGER.info('this instance is currently disabled in REDCap.')

    LOGGER.info('ALL DONE!')
