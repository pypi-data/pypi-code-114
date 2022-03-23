import copy
import datetime
import json
import logging
import os
import pathlib
import tempfile
import types
from typing import Callable, Dict, Union

import matplotlib
import matplotlib.pyplot as plt
import mlflow
import pandas as pd
from archimedes.configuration import config
from archimedes.utils.environ_context import environ

"""
Any code related to organizing models in MLFlow goes here.
"""

MLFLOW_ARTIFACT_CONFIG = {
    "AWS_ACCESS_KEY_ID": config.mlflow.artifacts_aws_access_key_id,
    "AWS_SECRET_ACCESS_KEY": config.mlflow.artifacts_aws_secret_access_key,
    "MLFLOW_S3_ENDPOINT_URL": config.mlflow.artifacts_s3_endpoint_url,
}


def mlflow_log_artifacts(*args, **kwargs):
    """Call mlflow.log_artifact by temporarily setting environment variables"""
    with environ(MLFLOW_ARTIFACT_CONFIG):
        mlflow.log_artifact(*args, **kwargs)


# Move flatten to utils
def _flatten(df):
    """Flatten the columns in one of our returned dataframes"""
    df_ = copy.deepcopy(df)
    new_columns = ["/".join(list(column)) for column in df_.columns]
    df_.columns = new_columns
    return df_


def _to_long_form(df):
    """Long form one of our returned dataframes"""
    # check if multi index or not, assuming not for now
    df_ = copy.deepcopy(df)
    df_ = _flatten(df_)
    df_.columns = ["value" + c for c in df_.columns]
    df_.columns = [c.replace("/", "_") for c in df_.columns]
    df_ = df_.reset_index()
    l = pd.wide_to_long(
        df_, stubnames="value", i="from_dt", j="series_id", suffix=r"\w+"
    )
    l = l.reset_index()
    return l


def _get_project_name():
    """Get project name from the configuration"""
    project_name = config.project.name
    return project_name


def _get_author():
    """Get author from the configuration"""
    author = config.project.author
    return author


def _get_environment():
    """Get environment from the configuration"""
    environment = config.project.environment
    return environment


# def _get_mlflow_tracking_uri():
#     """Get the MLflow Tracking URI from the configuration"""
#     config = _get_config()
#     mlflow_tracking_uri = config["mlflow"]["tracking_uri"]
#     return mlflow_tracking_uri


def _setup(local_mlflow: bool = False, autolog: bool = True):
    """Setup MLflow for our run

    Args:
        local_mlflow (bool, optional): If True, uses the local MLFlow. Defaults to False.
        autolog (bool, optional): Log extra data from the models. Defaults to True.

    Returns:
        dict: The context of the run
    """
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:\t%(message)s")
    # tracking_uri = os.path.join(_find_root_folder(), "mlruns")
    # mlflow.set_tracking_uri(tracking_uri)
    if local_mlflow:
        tracking_uri = pathlib.Path(
            os.path.join(os.path.expanduser("~"), "mlruns")
        ).as_uri()
    else:
        tracking_uri = config.mlflow.tracking_url
    mlflow.set_tracking_uri(tracking_uri)

    if autolog:
        # As of MLflow v1.12.0, universal auto-logging is supported
        mlflow.autolog()

    return {
        "project_name": _get_project_name(),
        "author": _get_author(),
        "environment": _get_environment(),
    }


def log(message: str):
    """Log a message

    Args:
        message (str): The message to log
    """
    print(message)
    logging.info(message)


def run(
    func: Union[Callable, str],
    model_name: str,
    local_mlflow: bool = False,
    args: Dict = None,
):
    """Run a function, without deploying it.

    The first argument can be either a function, the path to a python file or a
    string on the format app:myfunction.

    Example:
        >>> def myfunction():
        >>>     x = 2
        >>>     print(f"The number x is {x}")
        >>> archimedes.run(myfunction, "My first function")
        INFO:	Starting run at 2020-08-20T23:03:53.788115
        INFO:	MLFlow URI: /Users/jo/mlruns
        hello
        INFO:	Ending run at 2020-08-20T23:03:53.794075
        INFO:	The run took 0:00:00.005960

    Args:
        func (Union[Callable, str]): The function to deploy.
        model_name (str): The name of the model you're running.
        local_mlflow (bool, optional): If True, uses the local MLFlow. Defaults to False.
        args (dict, optional): Arguments to pass to the function being run, @TODO: change
    """
    context = _setup(local_mlflow)
    mlflow.set_experiment(context["project_name"])
    mlflow.start_run(
        run_name=model_name,
    )
    mlflow.set_tags(context)
    mlflow.set_tag("run_type", "MANUAL")
    mlflow.set_tag("model_name", model_name)
    run_start = datetime.datetime.utcnow()
    logging.info("Starting run at %s" % run_start.isoformat())
    log("MLFlow URI: %s" % mlflow.get_tracking_uri())
    with environ(MLFLOW_ARTIFACT_CONFIG):
        if args != None:
            func(**args)
        else:
            func()
    mlflow.end_run()
    run_end = datetime.datetime.utcnow()
    run_delta = run_end - run_start
    logging.info("Ending run at %s" % run_end.isoformat())
    logging.info("The run took %s" % run_delta)


def deploy(func: Union[Callable, str], model_name: str, cron: str = None):
    """Deploy a function or script to run on the server

    This is the server equivalent of `archimedes.run`.

    Example:
        >>> my_function = lambda x: x+2
        >>> deploy(my_function, "My First Function", "*10***")

    Args:
        func (Union[Callable, str]): The function to deploy
        model_name (str): The name of the model
        cron (str, optional): A cron string. Defaults to None.

    Returns:
        str: The id of the deployed function
    """
    _configure_prefect_server_endpoint()
    from prefect import Flow, client, task
    from prefect.storage import Docker
    from prefect.executors import DaskExecutor
    from prefect.run_configs import KubernetesRun
    from prefect.schedules import Schedule
    from prefect.schedules.clocks import CronClock

    if cron:
        schedule = Schedule(clocks=[CronClock(cron)])
    else:
        schedule = None

    context = _setup()

    project_name = context["project_name"]
    prefect_client = client.Client(api_server=config.prefect.api_server)
    _create_prefect_project_if_not_exist(prefect_client, project_name)

    # We only deal with functions for now
    if isinstance(func, types.FunctionType):

        def wrapper_func():
            return run(func, model_name, local_mlflow=False)

        only_task = task(wrapper_func, name=model_name)  # name=model_to_run.__name__)

        flow = Flow(name=model_name, tasks=[only_task], schedule=schedule)

        flow.storage = Docker(
            registry_url=config.prefect.docker_registry, dockerfile="Dockerfile"
        )

        flow.run_config = KubernetesRun()
        flow.executor = DaskExecutor()

        print(flow)

        flow.register(project_name=project_name)

    elif ".py" in func:
        raise ValueError("Files not yet implemented")
    elif ":" in func:
        raise ValueError("Function string not yet implemented")
    else:
        raise ValueError("Not yet implemented.")


def _configure_prefect_server_endpoint():
    """Configure prefect to use server endpoint from archimedes configuration

    If prefect server environment is configured in archimedes configuration, it doesn't need to be read from the
    prefect configuration file .prefect/config.yaml
    """
    if config.prefect.server_endpoint:
        os.environ["PREFECT__BACKEND"] = "server"
        os.environ["PREFECT__SERVER__ENDPOINT"] = config.prefect.server_endpoint


def _create_prefect_project_if_not_exist(prefect_client, project_name):
    """Create prefect project if it doesn't already exist

    project_name is mandatory in prefect version 0.13.0 and higher when registering a flow. So, it needs to be created.
    """
    from prefect.utilities.graphql import with_args

    query_project = {
        "query": {
            with_args("project", {"where": {"name": {"_eq": project_name}}}): {
                "id": True
            }
        }
    }
    project = prefect_client.graphql(query_project).data.project
    if not project:
        prefect_client.create_project(project_name)


def _store_dataframe(df: pd.DataFrame, name: str):
    """Store a dataframe in mlflow

    Example usage:
        df = pd.DataFrame(...)
        _store_dataframe(df, "MySpecialDataFrame")
        >> # The dataframe is stored and stored along with the
        >> # other run data.

    Args:
        df: The dataframe to store
        name: The name to associate with the dataframe
    """
    # name = name.replace("/", "__")
    with tempfile.TemporaryDirectory() as temporary_directory:
        # path = os.path.join(temporary_directory, str(t.timestamp()) + ".csv")
        filename_df = name + ".csv"
        filename_fig = name + ".jpeg"
        path_df = os.path.join(temporary_directory, filename_df)
        path_figure = os.path.join(temporary_directory, filename_fig)

        flat_df = _flatten(df)
        flat_df.index = pd.to_datetime(flat_df.index)

        num_cols = len(flat_df.columns)
        axs = flat_df.plot(
            subplots=True,
            linewidth=0.5,
            layout=(num_cols, 1),
            figsize=(10, 2 * num_cols),
            sharex=True,
            sharey=False,
        )
        # plt.show()
        # print(type(axs))  # <class 'numpy.ndarray'>
        # print(type(axs[0]))  # <class 'numpy.ndarray'>
        # print(type(axs[0][0]))  # <class 'matplotlib.axes._subplots.AxesSubplot'>
        fig = axs[0][0].get_figure()
        fig.savefig(path_figure)

        df.to_csv(path_df)
        mlflow_log_artifacts(path_df)
        log(f"Stored `{filename_df}`")
        mlflow_log_artifacts(path_figure)
        log(f"Stored `{filename_fig}`")


def _store_dict(x, name: str):
    """Store a dict in mlflow.

    Args:
        x ([type]): The dict to store
        name (str): The name of the dict
    """
    json_ = json.dumps(x, indent=4)
    with tempfile.TemporaryDirectory() as temporary_directory:
        filename_dict = name + ".json"
        path_dict = os.path.join(temporary_directory, filename_dict)
        f = open(path_dict, "w+")
        f.write(json_)
        f.close()
        mlflow_log_artifacts(path_dict)
        log(f"Stored `{filename_dict}`")


def _store_list(x, name: str):
    """Store a list in mlflow.

    Args:
        x ([type]): The list to store
        name (str): The name of the list
    """
    json_ = json.dumps(x, indent=4)
    with tempfile.TemporaryDirectory() as temporary_directory:
        filename_list = name + ".json"
        path_dict = os.path.join(temporary_directory, filename_list)
        f = open(path_dict, "w+")
        f.write(json_)
        f.close()
        mlflow_log_artifacts(path_dict)
        log(f"Stored `{filename_list}`")


def _store_metric(x, name: str):
    """Store a metric in mlflow.

    Args:
        x ([type]): The metric to store
        name (str): The name of the metric
    """
    mlflow.log_metric(name, x)


def _store_plot(x, name: str, show: bool = False):
    """Store a plot in MLFlow

    Args:
        x ([type]): The plot to store
        name (str): The name of the plot
        show (bool, optional): If true, also prints the plot to screen. Defaults to False.
    """
    with tempfile.TemporaryDirectory() as temporary_directory:
        filename_fig = name + ".jpeg"
        path_figure = os.path.join(temporary_directory, filename_fig)
        x.savefig(path_figure)
        mlflow_log_artifacts(path_figure)
        log(f"Stored `{filename_fig}`")
    if show:
        plt.show()


def store(x, name, show: bool = False):
    """Store x in mlflow.

    x can either be a dataframe, or a value.

    Args:
        x (): The thing to store
        name (str): The name of the thing
        show (bool, optional): If True, when storing a matplotlib.figure.Figure, prints the plot to screen.
                                Defaults to False.
    """
    if isinstance(x, pd.DataFrame):
        _store_dataframe(x, name)
    elif isinstance(x, matplotlib.figure.Figure):
        _store_plot(x, name, show)
    elif isinstance(x, int):
        _store_metric(x, name)
    elif isinstance(x, float):
        _store_metric(x, name)
    elif isinstance(x, dict):
        _store_dict(x, name)
    elif isinstance(x, list):
        _store_list(x, name)
    else:
        raise TypeError("%s type not implemented yet." % type(x))


def _plot_test_results_scatter(y_true, y_pred, show):
    """Scatter plot of the predicted vs true targets
    Args:
        y_true (pd.Series): The actual target values
        y_pred (pd.Series): The predicted target values
        show (bool, optional): If True, also show the charts on screen. Defaults to False.
    """
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    ax.plot(
        [y_true.min(), y_true.max()], [y_true.min(), y_true.max()], "r--", linewidth=2
    )

    ax.scatter(y_true, y_pred, alpha=0.3)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")

    extra = plt.Rectangle(
        (0, 0), 0, 0, fc="w", fill=False, edgecolor="none", linewidth=0
    )

    store(fig, "Test results scatter", show)


def _plot_test_results_lines(y_true, y_pred, show):
    """Line plot of the predicted vs true targets
    Args:
        y_true (pd.Series): The actual target values
        y_pred (pd.Series): The predicted target values
        show (bool, optional): If True, also show the charts on screen. Defaults to False.
    """
    import matplotlib.pyplot as plt
    from matplotlib.dates import DateFormatter

    fig, ax = plt.subplots()

    ax.plot(y_true, "b-", y_pred, "r--")

    my_fmt = DateFormatter("%d")
    ax.xaxis.set_major_formatter(my_fmt)

    fig.autofmt_xdate()

    store(fig, "Test results lines", show)


def store_test_results(y_true: pd.Series, y_pred: pd.Series, show: bool = False):
    """Store the test results of a model

    Args:
        y_true (pd.Series): The actual target values
        y_pred (pd.Series): The predicted target values
        show (bool, optional): If True, also show the charts on screen. Defaults to False.
    """
    _plot_test_results_scatter(y_true, y_pred, show)
    _plot_test_results_lines(y_true, y_pred, show)


# def load_model(project_name: str = None, model_name: str = None, run_id: str = None):
#     """[summary]

#     @TODO: Load a specific model (eg. after inspecting the results in the dashboard)
#     @TODO: Limit to 'registered models' in MLFlow?

#     Args:
#         project_name (str, optional): [description]. Defaults to None.
#         model_name (str, optional): [description]. Defaults to None.
#         run_id (str, optional): [description]. Defaults to None.
#     """
#     pass


def store_model(model, extra_data: Dict = None):
    mlflow.keras.log_model(model, "model")
    json_ = json.dumps(extra_data)
    mlflow.set_tag("extra_data", json_)


def load_model(model_name: str, stage: str = None, version: int = None):
    import mlflow.pyfunc

    model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{stage}")

    return model


def load_latest_model(project_name: str, model_name: str, local_mlflow: bool = False):
    """Load the latest model for a given project and model

    @TODO: Set a timeout (raise error if no response from MLFlow)

    Args:
        project_name (str): The name of the project
        model_name (str): The name of the model
        local_mlflow (bool, optional): If True, uses the local MLFlow. Defaults to False.
    """
    import mlflow.sklearn

    if local_mlflow:
        tracking_uri = pathlib.Path(
            os.path.join(os.path.expanduser("~"), "mlruns")
        ).as_uri()
    else:
        tracking_uri = config.mlflow.tracking_url
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(project_name)
    df = mlflow.search_runs()
    # df = df[df["tags.mlflow.runName"] == model_name]
    df = df[df["tags.model_name"] == model_name]
    df = df[df["status"] == "FINISHED"]
    try:
        df = df[~df["metrics.training_score"].isna()]
    except KeyError:
        df = df[~df["tags.mlflow.log-model.history"].isna()]
    latest_run_id = df.iloc[0]["run_id"]
    run_res = mlflow.get_run(latest_run_id)

    model_path = os.path.join(run_res.info.artifact_uri.replace("file://", ""), "model")
    extra_data = json.loads(df.iloc[0]["tags.extra_data"])

    # TODO: FIX
    # try:
    #     model = mlflow.sklearn.load_model(model_path)
    # except mlflow.exceptions.MlflowException:
    model = mlflow.keras.load_model(model_path)
    model.extra_data = extra_data
    model.model_version = latest_run_id
    return model


def set_note(note: str, overwrite: bool = False) -> None:
    """Add a note to the current experiment.

    This will add a new note to the project, or overwrite an existing note
    if `overwrite=True`.

    Example:
        >>> set_note(
        >>>    "This is an inital test of the basic model for reservoir levels"
        >>> )

    Args:
        note (str): The text to add.
        overwrite (bool): Whether to overwrite an existing note. Defaults to False.
    """
    mlflow.set_tag("mlflow.note.content", note)


def add_tag(name: str, value: str) -> None:
    """Add a tag to the current experiment.

    All tags have a `name` AND a `value`, eg: "color" "blue".

    Example:
        >>> add_tag("reference", "https://arxiv.org/pdf/2010.99999.pdf")
        >>> # Adds one tag to the current experiment

    Args:
        name (str): The name of the tag to add
        value (str): The value of the tag to add
    """
    mlflow.set_tag(name, value)
