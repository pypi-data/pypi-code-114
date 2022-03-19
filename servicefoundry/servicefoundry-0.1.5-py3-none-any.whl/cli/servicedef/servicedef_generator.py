from jinja2 import Template

from servicefoundry.build.util import create_file_from_content, read_text


def generate_service_def(service_name, build_type, build_dict, stage_params):
    template = Template(read_text("servicefoundry.j2", name=__name__))
    service_def_str = template.render(
        service_name=service_name,
        build_type=build_type,
        build_dict=build_dict,
        stage_params=stage_params,
    )
    create_file_from_content("servicefoundry.yaml", service_def_str)
