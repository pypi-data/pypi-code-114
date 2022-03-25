# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from io import BytesIO

from attr import asdict
from swimlane import Swimlane
from .decorators import log_exception

from .models import (
    User,
    UserLight,
    Role,
    Group,
    Report,
    Package,
    Dashboard
)


class SwimlaneInstance:

    """Creates a connection to a single Swimlane instance
    """

    application_dict = {}
    workflow_dict = {}
    dashboard_dict = {}

    def __init__(self, host='https://sw_web:4443', username=None, password=None, access_token=None,
                 verify_ssl=False, verify_server_version=False, default_timeout=300,
                 resource_cache_size=0, write_to_read_only=False):
        if username and password:
            self.swimlane = Swimlane(
                host=host,
                username=username,
                password=password,
                verify_ssl=verify_ssl,
                verify_server_version=verify_server_version,
                default_timeout=default_timeout,
                resource_cache_size=resource_cache_size,
                write_to_read_only=write_to_read_only
            )
        elif access_token:
            self.swimlane = Swimlane(
                host=host,
                access_token=access_token,
                verify_ssl=verify_ssl,
                verify_server_version=verify_server_version,
                default_timeout=default_timeout,
                resource_cache_size=resource_cache_size,
                write_to_read_only=write_to_read_only
            )
        else:
            raise AttributeError('Please provide either a username and password or a access token!')

        if not self.application_dict:
            self.application_dict = self.__create_application_dict()
        self.plugin_dict = self.__create_plugin_dict()
        self.workflow_dict = self.__create_workflow_dict()
        self.dashboard_dict = self.__create_dashboard_dict()

    def __create_application_dict(self):
        return_dict = {}
        for item in self.get_applications_light():
            if item.get('name') and item['name'] not in return_dict:
                return_dict[item['name']] = item
        return return_dict

    def __create_plugin_dict(self):
        return_dict = {}
        for item in self.get_plugins():
            return_dict[item['id']] = self.get_plugin(item['id']).get('fileId')
        return return_dict

    def __create_dashboard_dict(self):
        return_dict = {}
        for item in self.get_dashboards():
            return_dict[item.uid] = item
        return return_dict

    def __create_workflow_dict(self):
        return_dict = {}
        if not self.application_dict:
            self.application_dict = self.__create_application_dict()
        for workflow in self.get_workflows():
            for name, item in self.application_dict.items():
                if item.get('id') and workflow['applicationId'] == item['id']:
                    return_dict[name] = workflow
        import json
        with open('workflow.json', 'w+') as f:
            json.dump(return_dict, f)
        return return_dict

    @log_exception
    def get_credentials(self):
        return self.swimlane.request('GET', '/credentials').json()

    @log_exception
    def get_credential(self, name):
        try:
            return self.swimlane.request('GET', f"/credentials/{name}").json()
        except:
            return False

    @log_exception
    def add_credential(self, credential):
        return self.swimlane.request('POST', '/credentials', json=credential).json()

    @log_exception
    def get_tasks(self):
        return self.swimlane.request('GET', '/task/list').json()

    @log_exception
    def get_task_by_app_id(self, application_id):
        return self.swimlane.request('GET', f'/task?parentId={application_id}').json()

    @log_exception
    def get_task(self, task_id):
        try:
            return self.swimlane.request('GET', f'/task/{task_id}').json()
        except:
            return False

    @log_exception
    def list_application_tasks(self, application_id):
        return self.swimlane.request('GET', f'/task/list/{application_id}').json()

    @log_exception
    def get_application_tasks(self, application_id):
        return self.swimlane.request('GET', '/task?applicationId={}'.format(application_id)).json()

    @log_exception
    def add_task(self, task):
        return self.swimlane.request('POST', '/task', json=task).json()

    @log_exception
    def update_task(self, task_id, task):
        return self.swimlane.request('PUT', f"/task/{task_id}", json=task).json()

    @log_exception
    def get_plugins(self):
        return self.swimlane.request('GET', '/task/packages').json()

    @log_exception
    def get_plugin(self, name):
        try:
            return self.swimlane.request('GET', f"/task/packages/{name}").json()
        except:
            return False

    @log_exception
    def download_plugin(self, file_id):
        stream = BytesIO()
        response = self.swimlane.request('GET', f'attachment/download/{file_id}', stream=True)
        for chunk in response.iter_content(1024):
            stream.write(chunk) 
        stream.seek(0)
        return stream

    @log_exception
    def upload_plugin(self, filename, stream):
        if not filename.endswith('.swimbundle'):
            filename = filename.split('.')[0] + '.swimbundle'
        return self.swimlane.request(
            'POST', 
            '/task/packages', 
            files={'file': (filename, stream.read())}
        ).json()

    @log_exception
    def upgrade_plugin(self, filename, stream):
        if not filename.endswith('.swimbundle'):
            filename = filename.split('.')[0] + '.swimbundle'
        return self.swimlane.request(
            'POST', 
            '/task/packages/upgrade', 
            files={'file': (filename, stream.read())}
        ).json()

    @log_exception
    def get_pip_packages(self, versions=['Python2_7', 'Python3_6', 'Python3']):
        return_list = []
        for version in versions:
            resp = self.swimlane.request('GET', f"/pip/packages/{version}").json()
            if resp:
                return_list.extend(resp)
        return return_list

    @log_exception
    def install_package(self, package_name, version, python_version='Python3'):
        return self.swimlane.request(
            'POST', 
            '/pip/packages', 
            json={
                "name": package_name, 
                "version": version, 
                "pythonVersion": python_version
            }
        ).json()

    @log_exception
    def install_package_offline(self, filename, stream, data):
        return self.swimlane.request(
            'POST', 
            '/pip/packages/offline', 
            data=data,
            files={"wheel": (filename, stream.read())},
            timeout=120
        )

    @log_exception
    def get_assets(self):
        return self.swimlane.request('GET', '/asset').json()

    @log_exception
    def get_asset(self, asset_id):
        try:
            return self.swimlane.request('GET', f'/asset/{asset_id}').json()
        except:
            return False

    @log_exception
    def add_asset(self, asset):
        return self.swimlane.request('POST', '/asset', json=asset).json()

    @log_exception
    def update_asset(self, asset_id, asset):
        return self.swimlane.request('PUT', f"/asset/{asset_id}", json=asset).json()

    @log_exception
    def get_applications(self):
        return self.swimlane.request('GET', '/app').json()

    @log_exception
    def get_application(self, application_id):
        try:
            return self.swimlane.request('GET', f'/app/{application_id}').json()
        except:
            return False

    @log_exception
    def get_applications_light(self):
        return self.swimlane.request('GET', '/app/light').json()

    @log_exception
    def update_application(self, application):
        return self.swimlane.request('PUT', '/app', json=application).json()

    @log_exception
    def import_application(self, application):
        payload = {
            "modifications": [
                {"field": "name", "type": "create", "value": application['application']['name']},
                {"field": "acronym", "type": "create", "value": application['application']['acronym']}
            ]
        }
        payload['manifest'] = application
        return self.swimlane.request('POST', '/app/import', json=payload).json()

    @log_exception
    def export_application(self, application_id):
        return self.swimlane.request('GET', f"/app/{application_id}/export").json()

    @log_exception
    def add_application(self, application):
        return self.swimlane.request('POST', '/app', json=application).json()

    @log_exception
    def get_default_report_by_application_id(self, application_id):
        try:
            return Report(**self.swimlane.request('GET', f'/reports/app/{application_id}/default').json())
        except:
            return False

    @log_exception
    def get_workspaces(self):
        return self.swimlane.request('GET', '/workspaces').json()

    @log_exception
    def get_workspace(self, workspace_id):
        try:
            return self.swimlane.request('GET', f"/workspaces/{workspace_id}").json()
        except:
            return False

    @log_exception
    def add_workspace(self, workspace):
        return self.swimlane.request('POST', '/workspaces', json=workspace).json()

    @log_exception
    def update_workspace(self, workspace_id, workspace):
        return self.swimlane.request('PUT', f"/workspaces/{workspace_id}", json=workspace).json()

    @log_exception
    def get_dashboards(self):
        return_list = []
        for dashboard in self.swimlane.request('GET', '/dashboard').json():
            if dashboard:
                return_list.append(Dashboard(**dashboard))
        return return_list

    @log_exception
    def get_dashboard(self, dashboard_id):
        try:
            return Dashboard(**self.swimlane.request('GET', f"/dashboard/{dashboard_id}").json())
        except:
            return False

    @log_exception
    def update_dashboard(self, dashboard):
        return Dashboard(**self.swimlane.request('PUT', f"/dashboard/{dashboard.id}", json=asdict(dashboard)).json())

    @log_exception
    def add_dashboard(self, dashboard):
        return Dashboard(**self.swimlane.request('POST', '/dashboard', json=asdict(dashboard)).json())

    @log_exception
    def get_reports(self):
        return_list = []
        for report in self.swimlane.request('GET', '/reports').json():
            return_list.append(Report(**report))
        return return_list

    @log_exception
    def get_report(self, report_id):
        try:
            return Report(**self.swimlane.request('GET', f"/reports/{report_id}").json())
        except:
            return False

    @log_exception
    def get_application_reports(self, application_id):
        return self.swimlane.request('GET', f"/reports/app/{application_id}").json()

    @log_exception
    def add_report(self, report):
        return Report(**self.swimlane.request('POST', '/reports', json=asdict(report)).json())

    @log_exception
    def update_report(self, report_id, report):
        resp = self.swimlane.request('PUT', f"/reports/{report_id}", json=asdict(report))
        if resp.ok:
            return True

    @log_exception
    def update_default_report(self, report):
        return self.swimlane.request('PUT', f"/reports/app/{report.applicationIds[0]}/default", json=asdict(report)).json()

    @log_exception
    def delete_report(self, report_id):
        return self.swimlane.request('DELETE', f"/reports/{report_id}").json()

    @log_exception
    def get_users(self):
        user_list = []
        for user in self.swimlane.request('GET', '/user/light').json():
            user_list.append(UserLight(**user))
        return user_list

    @log_exception
    def get_user(self, user_id):
        #try:
        resp = self.swimlane.request('GET', f'/user/{user_id}').json()
        return User(**resp)
        #except:
        #    return False

    @log_exception
    def search_user(self, query_string):
        try:
            resp = self.swimlane.request('GET', f"/user/search?query={query_string}").json()
            if resp:
                return User(**resp[0])
        except:
            return False

    @log_exception
    def add_user(self, user):
        return User(**self.swimlane.request('POST', '/user', json=asdict(user)).json())

    @log_exception
    def update_user(self, user_id, user):
        return User(**self.swimlane.request('PUT', f"/user/{user_id}", json=asdict(user)).json())

    @log_exception
    def get_groups(self):
        return_list = []
        for item in self.swimlane.request('GET', '/groups').json().get('items'):
            return_list.append(Group(**item))
        return return_list

    @log_exception
    def get_group_by_name(self, group_name):
        return Group(**self.swimlane.request('GET', f'/groups/lookup?name={group_name}').json()[0])

    @log_exception
    def get_group_by_id(self, group_id):
        return Group(**self.swimlane.request('GET', f'/groups/{group_id}').json())

    @log_exception
    def get_formatted_group(self, group_name):
        for group in self.get_group_by_name(group_name=group_name):
            if group.get('name') == group_name:
                return Group(**{
                    'id': group['id'],
                    'name': group['name'],
                    'disabled': group['disabled']
                })

    @log_exception
    def add_group(self, group):
        return Group(**self.swimlane.request('POST', '/groups', json=asdict(group)).json())

    @log_exception
    def update_group(self, group_id, group):
        return Group(**self.swimlane.request('PUT', f'/groups/{group_id}', json=asdict(group)).json())

    @log_exception
    def get_roles(self):
        return_list = []
        for role in self.swimlane.request('GET', '/roles').json().get('items'):
            return_list.append(Role(**role))
        return return_list

    @log_exception
    def get_role(self, role_id):
        try:
            return Role(**self.swimlane.request('GET', f"/roles/{role_id}").json())
        except:
            return False

    @log_exception
    def get_role_by_name(self, role_name):
        try:
            return Role(**self.swimlane.request('GET', f'/roles/?searchFieldName=name&searchValue={role_name}').json())
        except:
            return False

    @log_exception
    def add_role(self, role):
        return self.swimlane.request('POST', '/roles', json=asdict(role)).json()

    @log_exception
    def update_role(self, role_id, role):
        return self.swimlane.request('PUT', f'/roles/{role_id}', json=asdict(role)).json()

    @log_exception
    def get_formatted_role(self, role_name):
        resp = self.get_role_by_name(role_name=role_name)
        if resp:
            for role in resp['items']:
                if role.get('name') == role_name:
                    return {
                        'id': role['id'],
                        'name': role['name'],
                        'disabled': role['disabled']
                    }

    @log_exception
    def get_swimlane_health(self):
        return self.swimlane.request('GET', '/health').json()

    @log_exception
    def get_swimlane_common_usage(self):
        return self.swimlane.request('GET', '/usage/app/common').json()

    @log_exception
    def get_workflows(self):
        return self.swimlane.request('GET', '/workflow/').json()

    @log_exception
    def get_workflow(self, application_id):
        try:
            return self.swimlane.request('GET', f"/workflow/{application_id}").json()
        except:
            return False

    @log_exception
    def add_workflow(self, workflow):
        return self.swimlane.request('POST', '/workflow/', json=workflow).json()

    @log_exception
    def update_workflow(self, workflow):
        return self.swimlane.request('PUT', f"/workflow/{workflow['id']}", json=workflow).json()

    @log_exception
    def save_application(self, name):
        if self.application_dict.get(name):
            app = self.application_dict[name]
            response = self.swimlane.request(
                'PUT',
                f"/app/{app['id']}",
                json=app
            )
            self.application_dict[name] = response.json()
