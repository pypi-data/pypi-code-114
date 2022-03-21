import os
import shutil
import re
from datetime import datetime

from kabaret import flow
from kabaret.flow_entities.entities import Entity, Property

from libreflow.utils.kabaret.flow_entities.entities import EntityView
from libreflow.baseflow.maputils import SimpleCreateAction
from libreflow.baseflow.file import CreateDefaultFilesAction
from libreflow.baseflow.departments import Department
from libreflow.baseflow.users import ToggleBookmarkAction

from .file import FileSystemMap
from .packaging import PackAction


MAX_DELIVERY_COUNT = 1e3


class CreateDepartmentDefaultFilesAction(CreateDefaultFilesAction):

    _department = flow.Parent()

    def get_target_groups(self):
        return [self._department.name()]

    def get_file_map(self):
        return self._department.files


class Department(flow.Object):

    _short_name = flow.Param()

    toggle_bookmark = flow.Child(ToggleBookmarkAction)

    files = flow.Child(FileSystemMap).ui(
        expanded=True,
        action_submenus=True,
        items_action_submenus=True
    )

    create_default_files = flow.Child(CreateDepartmentDefaultFilesAction)

    @classmethod
    def get_source_display(cls, oid):
        split = oid.split('/')
        return f'{split[3]} · {split[5]} · {split[7]} · {split[9]}'
    
    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(
                department=self.name(),
                department_short_name=self._short_name.get() if self._short_name.get() is not None else self.name(),
            )


class CleanDepartment(Department):

    _short_name = flow.Param('cln')


class CompDepartment(Department):

    _short_name = flow.Param('comp')


class MiscDepartment(Department):

    pack = flow.Child(PackAction).ui(label='Create package')

    _short_name = flow.Param('misc')
    _label = flow.Param()

    def _fill_ui(self, ui):
        label = self._label.get()
        if label:
            ui['label'] = label


class ShotDepartments(flow.Object):

    misc        = flow.Child(MiscDepartment)
    clean       = flow.Child(CleanDepartment).ui(label='Clean-up')
    compositing = flow.Child(CompDepartment)


class Shot(Entity):

    ICON = ('icons.flow', 'shot')

    shotgrid_id = Property().ui(label='ShotGrid ID', hidden=True)

    departments = flow.Child(ShotDepartments).ui(expanded=True)

    @classmethod
    def get_source_display(cls, oid):
        split = oid.split('/')
        return f'{split[3]} · {split[5]} · {split[7]}'

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(shot=self.name())


class CreateSGShots(flow.Action):

    ICON = ('icons.flow', 'shotgrid')

    skip_existing = flow.SessionParam(False).ui(editor='bool')

    _shots = flow.Parent()
    _sequence = flow.Parent(2)

    def get_buttons(self):
        return ['Create shots', 'Cancel']
    
    def run(self, button):
        if button == 'Cancel':
            return
        
        skip_existing = self.skip_existing.get()
        shots_data = self.root().project().get_shotgrid_config().get_shots_data(
            self._sequence.shotgrid_id.get()
        )
        for data in shots_data:
            name = data['name'].lower()

            if not self._shots.has_mapped_name(name):
                s = self._shots.add(name)
            elif not skip_existing:
                s = self._shots[name]
            else:
                continue
            
            print(f'Create shot {self._sequence.name()} {data["name"]}')
            s.shotgrid_id.set(data['shotgrid_id'])
        
        self._shots.touch()


class Shots(EntityView):

    ICON = ('icons.flow', 'shot')

    create_shot = flow.Child(SimpleCreateAction)
    create_shots = flow.Child(CreateSGShots)
    
    @classmethod
    def mapped_type(cls):
        return Shot
    
    def collection_name(self):
        mgr = self.root().project().get_entity_manager()
        return mgr.shots.collection_name()
    
    def columns(self):
        return ['Name']
    
    def _fill_row_cells(self, row, item):
        row['Name'] = item.name()


class Sequence(Entity):

    ICON = ('icons.flow', 'sequence')

    shotgrid_id = Property().ui(label='ShotGrid ID', hidden=True)
    shots = flow.Child(Shots).ui(
        expanded=True, 
        show_filter=True
    )

    @classmethod
    def get_source_display(cls, oid):
        split = oid.split('/')
        return f'{split[3]} · {split[5]}'

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(sequence=self.name())


class CreateSGSequences(flow.Action):

    ICON = ('icons.flow', 'shotgrid')

    skip_existing = flow.SessionParam(False).ui(editor='bool')
    create_shots = flow.SessionParam(False).ui(editor='bool')

    _sequences = flow.Parent()

    def get_buttons(self):
        return ['Create sequences', 'Cancel']
    
    def run(self, button):
        if button == 'Cancel':
            return
        
        sequences_data = self.root().project().get_shotgrid_config().get_sequences_data()
        create_shots = self.create_shots.get()
        skip_existing = self.skip_existing.get()

        for data in sequences_data:
            name = data['name'].lower()

            if not self._sequences.has_mapped_name(name):
                s = self._sequences.add(name)
            elif not skip_existing:
                s = self._sequences[name]
            else:
                continue
            
            print(f'Create sequence {data["name"]}')
            s.shotgrid_id.set(data['shotgrid_id'])

            if create_shots:
                s.shots.create_shots.skip_existing.set(skip_existing)
                s.shots.create_shots.run('Create shots')
        
        self._sequences.touch()


class Sequences(EntityView):

    ICON = ('icons.flow', 'sequence')

    create_sequence = flow.Child(SimpleCreateAction)
    create_sequences = flow.Child(CreateSGSequences)
    
    @classmethod
    def mapped_type(cls):
        return Sequence
    
    def collection_name(self):
        mgr = self.root().project().get_entity_manager()
        return mgr.sequences.collection_name()
    
    def columns(self):
        return ['Name']
    
    def _fill_row_cells(self, row, item):
        row['Name'] = item.name()


class CreateShotPackagesAction(flow.Action):
    '''
    This action allows to package folders into existing shots.

    It uses the following parameters in the current site:
      - `package_source_dir`: location of the folders to pack
      - `package_target_dir`: location where each folder will
      be moved after packing

    A folder is packed as a tracked folder. The target shot
    name is extracted performing a match between the folder
    name and the regular expression `shot_name_regex`. Thus,
    only folders with names matching this parameter will be
    available for packing.

    Each package is requested toward all sites whose names are
    provided in the `target_sites` param of the current site.
    '''

    ICON = ('icons.gui', 'package')

    shot_name_regex = flow.Param('^TS_(c\d{3})_(s\d{3})').ui(editable=False, hidden=True) # Used to validate ShotGrid shot names
    source_dir_name_pattern = flow.Param('^TS_{sequence_name}_{shot_name}.*').ui(editable=False, hidden=True) # Used to find shot source folders

    target_sg_task    = flow.DictParam(dict(name='Pre-Comp', status='rs'))
    target_kitsu_task = flow.DictParam(dict(name='Compositing', status='INV'))

    _film = flow.Parent()

    def __init__(self, parent, name):
        super(CreateShotPackagesAction, self).__init__(parent, name)
        self._shots_data = None

    def get_buttons(self):
        return ['Create packages', 'Cancel']
    
    def get_shots_data(self, refresh=False):
        if self._shots_data is None or refresh:
            self._shots_data = []
            site = self.root().project().get_current_site()
            sg_config = self.root().project().get_shotgrid_config()
            
            regex = self.shot_name_regex.get()
            layout_src_dir = site.package_layout_dir.get()
            clean_src_dir = site.package_clean_dir.get()

            for sg_shot in sg_config.get_shots('Pre-Comp', 'send'):
                sg_shot_name = sg_shot['name']
                m = re.search(regex, sg_shot_name, re.IGNORECASE)

                if m is not None:
                    sg_shot_id = sg_shot['id']
                    sequence_name = m.group(1).lower()
                    shot_name = m.group(2).lower()

                    layout_src_path = self.find_shot_source_dir(sequence_name, shot_name, layout_src_dir)
                    color_src_path = self.find_shot_source_dir(sequence_name, shot_name, clean_src_dir)
                    layout_status = sg_config.get_shot_task_status(sg_shot_id, 'Layout')
                    color_status = sg_config.get_shot_task_status(sg_shot_id, 'Color Ink & Paint')

                    status = 'warning'
                    if layout_src_path is None or (color_status != 'na' and color_src_path is None):
                        status = 'error'
                    elif layout_status == 'apr' and (color_status == 'apr' or color_status == 'na'):
                        status = 'valid'

                    self._shots_data.append({
                        'shotgrid_id': sg_shot_id,
                        'sequence': m.group(1).lower(),
                        'shot': m.group(2).lower(),
                        'sg_name': sg_shot_name,
                        'publish_comment': None,
                        'status': status,
                        'available': layout_status != 'na',
                        'layout_src_path': layout_src_path,
                        'layout_sg_status': layout_status,
                        'color_src_path': color_src_path,
                        'color_sg_status': color_status,
                    })
        
        return self._shots_data
    
    def _ensure_package_revision(self, sequence_name, shot_name, dept_name, package_name):
        revision = None

        try:
            file_map = self.root().get_object(
                f'{self._film.oid()}/sequences/{sequence_name}/shots/{shot_name}/departments/{dept_name}/files'
            )
        except:
            print(f'Packages :: TS_{sequence_name}_{shot_name} :: Shot does not exist in the project')
        else:
            if not file_map.has_folder(package_name):
                f = file_map.add_folder(package_name, tracked=True)
            else:
                f = file_map[package_name]
            
            revision = f.add_revision()
        
        return revision
    
    def _submit_upload(self, revision, do_upload=False):
        current_site = self.root().project().get_current_site()
        sites = self.root().project().get_working_sites()

        # Request revision for upload toward source site
        source_site = sites[revision.site.get()]
        
        if revision.get_sync_status(exchange=True) != 'Available':
            job = source_site.get_queue().submit_job(
                job_type='Upload',
                init_status='WAITING',
                emitter_oid=revision.oid(),
                user=self.root().project().get_user_name(),
                studio=source_site.name(),
            )

        # Request revision for download toward target sites
        for site_name in current_site.target_sites.get():
            try:
                site = sites[site_name]
            except flow.exceptions.MappedNameError:
                continue
            else:
                if revision.get_sync_status(site_name=site_name) != 'Available':
                    site.get_queue().submit_job(
                        job_type='Download',
                        init_status='WAITING',
                        emitter_oid=revision.oid(),
                        user=self.root().project().get_user_name(),
                        studio=site_name,
                    )
                    revision.set_sync_status('Requested', site_name=site_name)

        if do_upload and current_site.name() == source_site.name():
            self.root().project().get_sync_manager().process(job)
    
    def find_shot_source_dir(self, sequence_name, shot_name, sources_dir):
        src_dir = None

        if os.path.exists(sources_dir):
            regex = self.source_dir_name_pattern.get().format(
                sequence_name=sequence_name,
                shot_name=shot_name
            )

            for dir_name in next(os.walk(sources_dir))[1]:
                if re.search(regex, dir_name, re.IGNORECASE) is not None:
                    src_dir = os.path.join(sources_dir, dir_name)
                    break
        
        return src_dir
    
    def _create_shot_package(self, shot_data, dept_name, package_name, source_path, do_upload, dst_dir):
        sg_shot_name = shot_data['sg_name']
        
        if source_path is None:
            print(f'Packages :: {sg_shot_name}: Source files not found for package {dept_name}/{package_name}')
            return False
        
        sequence_name = shot_data['sequence']
        shot_name = shot_data['shot']

        # Create new revision for package
        r = self._ensure_package_revision(sequence_name, shot_name, dept_name, package_name)

        if r is not None:
            target_path = r.get_path()

            if os.path.exists(target_path):
                shutil.rmtree(target_path)
            
            # Copy source files in package revision
            shutil.copytree(source_path, target_path)
            print(f'Packages :: {sg_shot_name}: Package created: {target_path}')
            
            # Submit revision upload
            self._submit_upload(r, do_upload)
            print(f'Packages :: {sg_shot_name}: Package uploaded')

            # Copy sources to destination folder
            if dst_dir is not None:
                dst_path = os.path.join(dst_dir, os.path.basename(source_path))

                if not os.path.exists(dst_path):
                    shutil.copytree(source_path, dst_path)
                    print(f'Packages :: {sg_shot_name}: Source folder copied into {dst_path}')
                else:
                    print(f'Packages :: {sg_shot_name}: Source folder already present in {dst_dir}')
            
            return True
        else:
            return False

    def create_shot_packages(self, shot_data, do_upload, dst_dir):
        layout_sent = self._create_shot_package(shot_data, 'misc', 'sources', shot_data['layout_src_path'], do_upload, dst_dir)
        self._create_shot_package(shot_data, 'clean', 'sources', shot_data['color_src_path'], do_upload, dst_dir)
        
        if layout_sent:
            # Update SG status: ready to start
            sg_config = self.root().project().get_shotgrid_config()
            target_task = self.target_sg_task.get()
            sg_config.set_shot_task_status(shot_data['shotgrid_id'], target_task['name'], target_task['status'])

            # Update Kitsu status: inventory
            kitsu_config = self.root().project().kitsu_api()
            target_task = self.target_kitsu_task.get()
            kitsu_config.set_shot_task_status(shot_data['sequence'], shot_data['shot'], target_task['name'], target_task['status'])
    
    def create_packages(self, shots_data, do_upload=False):
        site = self.root().project().get_current_site()
        pkg_layout_dir = site.package_layout_dir.get()
        pkg_clean_dir = site.package_clean_dir.get()
        dst_dir = os.path.join(
            site.package_target_dir.get(),
            datetime.now().strftime('%y%m%d')
        )

        if os.path.exists(dst_dir):
            i = 2
            while os.path.exists(f'{dst_dir}-{i}') and i <= MAX_DELIVERY_COUNT:
                i += 1
            
            dst_dir = f'{dst_dir}-{i}'

        if pkg_layout_dir is None or pkg_clean_dir is None:
            print((
                'Packages :: Layout and clean package directories '
                'must be specified in the current site settings'
            ))
            return

        for shot_data in shots_data:
            self.create_shot_packages(shot_data, do_upload, dst_dir)
    
    def _fill_ui(self, ui):
        ui['custom_page'] = 'libreflow.pianoplayer.ui.packaging.CreateShotPackagesWidget'


class Film(Entity):

    ICON = ('icons.flow', 'film')

    sequences = flow.Child(Sequences).ui(
        expanded=True,
        show_filter=True
    )
    create_packages = flow.Child(CreateShotPackagesAction)
    
    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(film=self.name())


class Films(EntityView):

    ICON = ('icons.flow', 'film')

    create_film = flow.Child(SimpleCreateAction)

    @classmethod
    def mapped_type(cls):
        return Film
    
    def collection_name(self):
        return self.root().project().get_entity_manager().films.collection_name()
