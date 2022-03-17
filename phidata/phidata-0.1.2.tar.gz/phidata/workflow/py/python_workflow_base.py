from typing import Optional, Any, Callable, Dict

from phidata.workflow import Workflow, WorkflowArgs
from phidata.utils.enums import ExtendedEnum
from phidata.utils.cli_console import print_error, print_info
from phidata.utils.log import logger


class EngineType(ExtendedEnum):
    PANDAS = "PANDAS"
    SPARK = "SPARK"
    DEFAULT = "DEFAULT"


class PythonWorkflowBaseArgs(WorkflowArgs):
    # The compute engine for this python workflow
    # Pandas/Spark are the available options
    engine: EngineType = EngineType.DEFAULT
    # To run a workflow we need to execute a task.
    # For a PythonWorkflowBase this task is a python function
    # For example:
    #     def download_url_to_file(**kwargs) -> bool:
    # The entrypoint_function should accept **kwargs as the arguments
    # and return the run_status as a bool
    # The type for the entrypoint_function is Callable[..., bool].
    # https://stackoverflow.com/a/39624147
    # https://docs.python.org/3/library/typing.html#typing.Callable
    entrypoint: Callable[..., bool]


class PythonWorkflowBase(Workflow):
    """Base Class for Python Workflows"""

    def __init__(self) -> None:
        super().__init__()
        self.args: Optional[PythonWorkflowBaseArgs] = None

    @property
    def engine(self) -> EngineType:
        return self.args.engine if self.args else EngineType.DEFAULT

    @property
    def entrypoint(self) -> Optional[Callable[..., bool]]:
        return self.args.entrypoint if self.args else None

    ######################################################
    ## Run workflow
    ######################################################

    def run_in_local_env(self) -> bool:
        """
        Runs a python workflow in the local environment where phi wf is called from.

        Returns:
            run_status (bool): True if the run was successful
        """
        # Workflow not yet initialized
        if self.args is None:
            return False

        # Important: Validate that PathContext is available
        # This is derived from the current env or passed by the data product
        if self.path_context is None:
            print_error("PathContext not available")
            return False

        dry_run: bool = self.run_context.dry_run if self.run_context else False
        if dry_run:
            print_info("Dry run, returning True")
            return True

        run_status: bool = False
        entrypoint = self.entrypoint
        # TODO: add validation for safe execution
        if self.args is not None and entrypoint is not None:
            run_status = entrypoint(**self.args.dict())
        return run_status

    def run_in_docker_container(
        self, active_container: Any, docker_env: Optional[Dict[str, str]] = None
    ) -> bool:
        """
        Runs a python workflow in a docker container.

        Args:
            active_container: The container to run the workflow in
            docker_env:

        Returns:
            run_status (bool): True if the run was successful

        Notes:
            * This function runs in the local environment where phi wf is called from.
            But executes an `airflow` commands in the docker container to run the workflow
            * For the airflow tasks to be available, they need to be added to the workflow DAG
            using add_airflow_tasks_to_dag()
        """
        # Workflow not yet initialized
        if self.args is None:
            return False

        from pathlib import Path

        from docker.errors import APIError
        from docker.models.containers import Container

        from phidata.utils.cli_console import print_info, print_error
        from phidata.infra.docker.utils.container import execute_command

        if active_container is None or not isinstance(active_container, Container):
            print_error("Invalid Container object")
            return False
        container: Container = active_container

        task_id = self.task_id
        dag_id = self.dag_id
        if task_id is None:
            print_error("Workflow task_id unavailable")
            return False
        if dag_id is None:
            print_error("Workflow dag_id unavailable")
            return False

        run_date: Optional[str] = (
            self.run_context.run_date if self.run_context else None
        )
        dry_run: Optional[bool] = self.run_context.dry_run if self.run_context else None
        af_dry_run_str: str = " -n" if dry_run else ""
        workflow_file_path: Optional[Path] = (
            self.path_context.workflow_file if self.path_context else None
        )
        subdir_str: str = (
            f" -S {str(workflow_file_path.parent)}" if workflow_file_path else ""
        )

        # logger.debug("task_id: {}".format(task_id))
        # logger.debug("dag_id: {}".format(dag_id))
        # logger.debug("run_date: {}".format(run_date))
        # logger.debug("dry_run: {}".format(dry_run))

        run_status: bool = False
        list_tasks_cmd = f"airflow tasks list {dag_id} -t{subdir_str}"
        test_wf_cmd = f"airflow tasks test {dag_id} {task_id} {run_date}{subdir_str}{af_dry_run_str}"
        dry_run_cmd = f"python {workflow_file_path}"
        command_to_run = dry_run_cmd if dry_run else test_wf_cmd
        try:
            # execute_command(cmd=list_tasks, container=container)
            print_info(
                "Running command: {}\nContainer: {}".format(
                    command_to_run, container.name
                )
            )
            run_status = execute_command(
                cmd=command_to_run,
                container=container,
                docker_env=docker_env,
            )
        except APIError as e:
            logger.exception(e)
            raise

        return run_status

    ######################################################
    ## Airflow functions
    ######################################################

    def add_airflow_tasks_to_dag(self, dag: Any) -> bool:
        """
        This function adds the airflow tasks for this workflow to a DAG.
        This function is usually called by the create_airflow_dag()
        and runs on the remote machine where airflow is available.
        Args:
            dag:

        Returns:

        """
        # Workflow not yet initialized
        if self.args is None:
            return False

        # Important: Validate that PathContext is available
        if self.path_context is None:
            return False

        from airflow.models.dag import DAG
        from airflow.operators.python import PythonOperator

        if dag is None or not isinstance(dag, DAG):
            print_error("Invalid DAG")
            return False

        # Build the task_id for the airflow task
        task_id = self.task_id
        print_info(f"Creating airflow task: {task_id}")

        # Function to run
        entrypoint = (
            self.args.entrypoint
            if self.args and isinstance(self.args.entrypoint, Callable)
            else simple_python_function
        )
        # Airflow task
        task = PythonOperator(
            task_id=task_id,
            python_callable=entrypoint,
            op_kwargs=self.args.dict(),
        )
        dag.add_task(task)
        print_info(f"Airflow task created: {task_id}")
        return True


def simple_python_function(**kwargs) -> bool:
    print_error("Invalid entrypoint function")
    print_error("Args: {}".format(kwargs))
    return True
