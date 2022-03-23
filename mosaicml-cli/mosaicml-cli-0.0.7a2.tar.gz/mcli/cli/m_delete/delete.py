""" Delete Secret or Env Variable """
from typing import Optional

from mcli.config import MCLIConfig
from mcli.projects.project_info import get_projects_list
from mcli.utils.utils_interactive import query_yes_no


def delete_environment_variable(variable_name: str, **kwargs) -> int:
    del kwargs
    conf = MCLIConfig.load_config()

    existing_env_variables = conf.environment_variables
    new_env_vars = [x for x in existing_env_variables if x.name != variable_name]
    if len(existing_env_variables) == len(new_env_vars):
        print(f'Unable to find env var with name: {variable_name}.'
              ' To see all env vars run `mcli get env`')
        return 1
    conf.environment_variables = new_env_vars
    conf.save_config()
    return 0


def delete_secret(secret_name: str, **kwargs) -> int:
    del kwargs
    conf = MCLIConfig.load_config()

    existing_secrets = conf.secrets
    new_secrets = [x for x in existing_secrets if x.name != secret_name]
    if len(existing_secrets) == len(new_secrets):
        print(f'Unable to find secret with name: {secret_name}.'
              ' To see all secrets run `mcli get secrets`')
        return 1
    conf.secrets = new_secrets
    conf.save_config()
    return 0


def delete_platform(platform_name: Optional[str] = None, force: bool = False, **kwargs) -> int:
    del kwargs
    if platform_name is None:
        print('You must specify a platform name.'
              ' To see all platforms run `mcli get platforms`')
        return 1

    conf = MCLIConfig.load_config()

    existing_platforms = conf.platforms
    new_platforms = [x for x in existing_platforms if x.name != platform_name]
    if len(existing_platforms) == len(new_platforms):
        print(f'Unable to find platform with name: {platform_name}.'
              ' To see all platforms run `mcli get platforms`')
        return 1
    if not force:
        confirm = query_yes_no(f'Would you like to delete platform {platform_name}?')
        if not confirm:
            print('Canceling deletion.')
            return 1
    conf.platforms = new_platforms
    conf.save_config()
    return 0


def delete_project(project_name: str, **kwargs) -> int:
    del kwargs

    existing_projects = get_projects_list()
    found_projects = [x for x in existing_projects if x.project == project_name]
    if not found_projects:
        print(f'Unable to find project with name: {project_name}.'
              ' To see all projects run `mcli get projects`')
        return 1
    if len(existing_projects) == 1:
        print('Unable to delete the only existing project'
              ' To see all projects run `mcli get projects`')
        return 1
    if found_projects and len(found_projects) == 1:
        found_project = found_projects[0]
        return found_project.delete()

    return 1
