import toml

from captif_db.db.models import (
    Project, Section, Station, Basecourse, Subbase, Subgrade, Surface,
)

from . import schema


__all__ = [
    "ProjectConfigLoader",
]


class UploadError(Exception):
    pass


class ConfigError(Exception):
    pass


class ProjectConfigLoader:
    def __init__(self, session, config_file):
        self.session = session
        self.config = self.load_config(config_file)
        self.project = self.get_project()

    def get_project(self):
        """Retrieve the project details held in the database."""
        return (
            self.session.query(Project)
            .filter(Project.id == self.config["project"]["id"])
            .first()
        )

    def update(self):
        if self.project is None:
            try:
                self.project = self.upload_project(self.session, self.config)

                for section_config in self.config["section"]:
                    self.upload_section(self.session, self.project, section_config,)

                self.session.commit()

            except Exception:
                self.session.rollback()

            return None

        # TODO: Allow changes to project config file
        print(
            "There is currently no ability to update the database using the project "
            "config file. This needs to be done manually."
        )

    @classmethod
    def upload_project(cls, session, config):
        project = Project(**config["project"])
        session.add(project)
        session.flush()
        return project

    @classmethod
    def upload_section(cls, session, project, section_config):
        info = section_config["info"]

        section = Section(project_obj=project, section_id=info["section_id"])
        session.add(section)

        session.add_all((
            Station(section_obj=section, station_no=station_no)
            for station_no in cls.stations(info["start_station"], info["end_station"])
        ))
        session.add_all((
            Basecourse(section_obj=section, **basecourse_info)
            for basecourse_info in section_config["basecourse"]
        ))
        session.add_all((
            Subbase(section_obj=section, **subbase_info)
            for subbase_info in section_config["subbase"]
        ))
        session.add_all((
            Subgrade(section_obj=section, **subgrade_info)
            for subgrade_info in section_config["subgrade"]
        ))
        session.add_all((
            Surface(section_obj=section, **surface_info)
            for surface_info in section_config["surface"]
        ))

        session.flush()

    @staticmethod
    def load_config(config_file):
        return schema.project_config_schema.validate(toml.load(config_file))

    @staticmethod
    def stations(start_station, end_station):
        for ii in range(start_station, end_station + 1):
            yield ii % 60
