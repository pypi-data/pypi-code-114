from huscy.project_design.models import DataAcquisitionMethod, Experiment, Session


def add_data_acquisition_method(session, type, location, order=None):
    if order is None:
        order = DataAcquisitionMethod.objects.filter(session=session).count() + 1

    return DataAcquisitionMethod.objects.create(
        session=session,
        type=type,
        location=location,
        order=order
    )


def create_experiment(project, title='', description='', order=0):
    project_experiment_count = project.experiments.count()

    return Experiment.objects.create(
        description=description,
        order=order or project_experiment_count + 1,
        project=project,
        title=title or f'Experiment {project_experiment_count+1}',
    )


def create_session(experiment, duration, operator, title='', order=0):
    experiment_session_count = experiment.sessions.count()
    project_session_count = Session.objects.filter(experiment__project=experiment.project).count()

    return Session.objects.create(
        duration=duration,
        experiment=experiment,
        operator=operator,
        order=order or experiment_session_count + 1,
        title=title or f'Session {project_session_count + 1}'
    )


def get_data_acquisition_methods(project=None):
    queryset = DataAcquisitionMethod.objects
    if project:
        queryset = queryset.filter(session__experiment__project=project)
    return queryset.order_by('pk')


def get_experiments(project=None):
    queryset = Experiment.objects
    if project:
        queryset = queryset.filter(project=project)
    return queryset.all()


def get_sessions():
    return Session.objects.all()
