import sys
import threading
import time
from datetime import datetime, timedelta
from enum import Enum, auto
from pathlib import Path
from typing import List, Optional, Dict, Any

import tzlocal
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, \
    EVENT_JOB_ADDED, EVENT_JOB_SUBMITTED, EVENT_JOB_REMOVED, EVENT_JOB_MISSED, EVENT_JOB_MAX_INSTANCES
from apscheduler.events import JobExecutionEvent, JobEvent, JobSubmissionEvent
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.job import Job
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger
from dotenv import load_dotenv
from mysql.connector import Error as mysqlError
from pydantic import BaseModel, constr
from telegram import Bot

from .mysql_basic import *

load_dotenv(Path.cwd() / '.env')

logger = logging.getLogger("rw_scheduler")


class ExecutionStatus(Enum):
    ok = auto()
    error = auto()


class TaskState(Enum):
    new = auto(), '🌱'
    scheduled = auto(), '🪵'
    executing = auto(), '🔥'
    removed = auto(), '☑️'
    canceled = auto(), '❌'
    no_info = 99, '!'

    def __new__(cls, *args, **kwargs):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, _: str, symbol: str):
        self._symbol_ = symbol

    @property
    def symbol(self):
        return self._symbol_


class BotInfo(BaseModel):
    bot_token: str
    chat_ids: List[int]
    info_level: TaskState = TaskState.no_info
    info_on_start: bool = False
    info_on_success: bool = True
    info_on_exception: bool = True
    msg_on_start: str = None
    msg_on_success: str = None
    msg_on_exception: str = None


class AllowedTrigger(Enum):
    date = auto()
    interval = auto()


class JobInfo(BaseModel):
    callback: str  # name of the callback function
    module: str  # name of the module, where to find the callback function
    args: Optional[List] = []  # args to pass to the function
    kwargs: Optional[Dict] = {}  # kwargs to pass to the function
    pydantic_args: Optional[
        List[tuple[str, Any]]] = []  # args tuple of [] will be first parsed by model.parse_obj
    pydantic_kwargs: Optional[Dict[str, tuple[str, Any]]] = {}  # kwargs to pass to the function
    trigger: Optional[AllowedTrigger] = AllowedTrigger.date  # the trigger object that controls the schedule of this job
    trigger_config: dict = dict()  # configuration of the triggers
    coalesce: bool = False  # whether to only run the job once when several run times are due
    misfire_grace_time: Optional[int] = 30  # time (in seconds) how much this job’s execution is allowed to be late
    # (None means “allow the job to run no matter how late it is”)
    max_instances: Optional[int] = 1
    run_in_background: Optional[bool] = False
    bot_info: Optional[List[BotInfo]] = []
    error_msg: Optional[str]  # error msg

    def __str__(self):
        return "JobInfo(module.callback={}, args={}, kwargs={})".format(
            self.module + '.' + self.callback,
            self.args,
            self.kwargs
        )


class Task(BaseModel):
    id: int
    status: TaskState
    comment: Optional[str]
    target_system: constr(max_length=100)
    ordering_system: Optional[constr(max_length=100)]
    job_info: JobInfo
    return_msg: Optional[str]
    mysql_cnx: Optional[mysql.MySQLConnection]
    executions_instances: int = 0
    job: Optional[Job]

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mysql_cnx = create_connection()
        self.job = None

    def __str__(self):
        return "Task(id={}, module.callback={}, target_system={}, args={}, kwargs={}, status={}, job={})".format(
            self.id,
            self.job_info.module + '.' + self.job_info.callback,
            self.target_system,
            self.job_info.args + self.job_info.pydantic_args,
            {**self.job_info.kwargs, **self.job_info.pydantic_kwargs},
            self.status.name,
            self.job
        )

    def __repr__(self):
        return "id: {}\nstatus: {}\ntarget_system: {}\ncallback: {}\nargs: {} kwargs: {}".format(
            self.id,
            self.status,
            self.target_system,
            self.job_info.module + '.' + self.job_info.callback,
            self.job_info.args + self.job_info.pydantic_args,
            {**self.job_info.kwargs, **self.job_info.pydantic_kwargs},
        )

    @classmethod
    def create(cls, job_info: JobInfo, target_system: str, ordering_system: str, comment: str = None):
        query = f"INSERT INTO db_global.ScheduleJob(job_info,target_system,ordering_system,comment) VALUES(%s,%s,%s,%s)"
        _, cnx = execute_query(query,
                               values=(job_info.json(exclude_unset=True, ensure_ascii=False), target_system,
                                       ordering_system, comment),
                               reuse_cnx=True)
        query = f"SELECT LAST_INSERT_ID()"
        res, _ = select_query(query, cnx=cnx)
        task_id = res[0]['LAST_INSERT_ID()']
        return Task.get_task_from_id(task_id)

    @classmethod
    def get_task_from_id(cls, task_id):
        query = f"SELECT * FROM db_global.ScheduleJob WHERE id=%s"
        res, _ = select_query(query, values=(task_id,))
        if res is not None:
            return Task.parse_from_sql(res[0])
        else:
            raise RuntimeError("Task not found!")

    @classmethod
    def parse_from_sql(cls, sql_result):
        return Task(id=sql_result['id'],
                    target_system=sql_result['target_system'],
                    comment=sql_result['comment'],
                    status=TaskState[sql_result['status']],
                    job_info=JobInfo.parse_raw((sql_result['job_info'])))

    @classmethod
    def update_task(cls, task_id: int, kwarg):
        task = Task.get_task_from_id(task_id)
        task.update(**kwarg)

    @staticmethod
    def send_bot_info(bot_info: BotInfo, msg: str):
        try:
            bot = Bot(bot_info.bot_token)
            for chat_id in bot_info.chat_ids:
                bot.send_message(chat_id, msg, parse_mode='HTML')
        except Exception as err:
            logger.error("could not send info from bot")
            logger.error(f"{type(err).__name__}: {err}")

    def execution_info_start(self, warning: str = None):
        # send bot info
        for bot_info in self.job_info.bot_info:
            if bot_info.info_on_start:
                if bot_info.msg_on_start is None:
                    if warning is not None:
                        msg = f"⚠️ Warning\n<code>{warning}</code>\n\n"
                    else:
                        msg = f"📍 execution started\n"
                    msg += f"<code>{self.__repr__()}</code>"
                else:
                    msg = bot_info.msg_on_start
                self.send_bot_info(bot_info, msg)

    def execution_info_end(self, result: str = None, duration: timedelta = None):
        query = f"INSERT INTO db_global.Executions(task_id, result_msg, duration, execution_status) " \
                f"VALUES (%s,%s,%s,%s)"
        _ = execute_query(query, (self.id, result, str(duration), ExecutionStatus.ok.value))
        for bot_info in self.job_info.bot_info:
            if bot_info.info_on_success:
                if bot_info.msg_on_success is None:
                    msg = f"✅ execution finished\n"
                    msg += f"<code>{self.__repr__()}</code>"
                    msg += f"\n\nresult:\n<code>{result}</code>"
                    msg += f"\n\nduration:\n<code>{duration}</code>"
                else:
                    msg = bot_info.msg_on_success
                self.send_bot_info(bot_info, msg)

    def execution_info_end_with_error(self, error: BaseException, duration: timedelta = None):
        query = f"INSERT INTO db_global.Executions(task_id, result_msg, duration, execution_status) " \
                f"VALUES (%s,%s,%s,%s)"
        error_msg = f"{type(error).__name__}: {error}"
        _ = execute_query(query, (self.id, error_msg, str(duration), ExecutionStatus.error.value))
        for bot_info in self.job_info.bot_info:
            if bot_info.info_on_exception:
                if bot_info.msg_on_exception is None:
                    msg = f"❌ execution finished with error\n"
                    msg += f"<code>{self.__repr__()}</code>"
                    msg += f"\n\nerror:\n<code>{error_msg}</code>"
                else:
                    msg = bot_info.msg_on_exception
                self.send_bot_info(bot_info, msg)

    def update(self, **kwargs):
        if "status" in kwargs and kwargs["status"] != self.status:
            self.status = kwargs["status"]
            query = f'UPDATE db_global.ScheduleJob SET status=%s WHERE id=%s'
            _ = execute_query(query, (self.status.value, self.id))
            # send bot info
            for bot_info in self.job_info.bot_info:
                if self.status.value >= bot_info.info_level.value:
                    msg = f"{self.status.symbol} Task has new status: {self.status.name}\n"
                    msg += f"<code>{self.__repr__()}</code>"
                    self.send_bot_info(bot_info, msg)
        if "job_info" in kwargs:
            self.job_info = kwargs["job_info"]
            query = f'UPDATE db_global.ScheduleJob SET job_info = %s WHERE id = %s'
            _ = execute_query(query, (self.job_info.json(exclude_unset=True), self.id))
        if "job" in kwargs:
            self.job = kwargs["job"]
            if self.job is not None:
                query = f'UPDATE db_global.ScheduleJob SET nextStart=%s WHERE id=%s'
                _ = execute_query(query, (self.job.next_run_time, self.id))
            else:
                query = f'UPDATE db_global.ScheduleJob SET nextStart=%s WHERE id=%s'
                _ = execute_query(query, (None, self.id))


class ScheduleThread(threading.Thread):
    def __init__(self, target_system: str, time_zone: str = None, sleep_between_checks_sec=0.3):
        super().__init__()
        self.mysql_cnx = create_connection()
        self.cease_continuous_run = threading.Event()
        self.sleep_between_checks_sec = sleep_between_checks_sec
        self.target_system = target_system
        executors = {
            'default': ThreadPoolExecutor(1),
            'background': ThreadPoolExecutor(20),
        }
        self.scheduler = BackgroundScheduler(executors=executors)
        self.scheduler.add_listener(self.listen_job_scheduled, EVENT_JOB_ADDED)
        self.scheduler.add_listener(self.listen_execution_start,
                                    EVENT_JOB_SUBMITTED | EVENT_JOB_MISSED | EVENT_JOB_MAX_INSTANCES)
        self.scheduler.add_listener(self.listen_execution_ends, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
        self.scheduler.add_listener(self.listen_job_removed, EVENT_JOB_REMOVED)
        if time_zone:
            self.time_zone = time_zone
        else:
            self.time_zone = str(tzlocal.get_localzone())
        self.tasks: List[Task] = list()

    def _add_task(self, task: Task):
        self.tasks.append(task)

    def _remove_task(self, task: Task):
        self.tasks.remove(task)

    def _get_task_by_id(self, task_id: int):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task is not None:
            return task
        else:
            return Task.get_task_from_id(task_id)

    def listen_job_scheduled(self, event: JobEvent):
        logger.debug("listen_job_scheduled")
        task = self._get_task_by_id(int(event.job_id))
        job = self.scheduler.get_job(event.job_id)
        task.update(status=TaskState.scheduled, job=job)

    def listen_execution_start(self, event: JobSubmissionEvent):
        logger.debug("listen_execution_start")
        task = self._get_task_by_id(int(event.job_id))
        task.executions_instances += 1
        # job maybe unavailable from the job store, this means it is remove and had its last run
        if event.code == EVENT_JOB_MISSED:
            warning = "job’s execution was missed"
        elif event.code == EVENT_JOB_MAX_INSTANCES:
            warning = "job was not accepted by the executor " \
                      "because its already reached maximum concurrently executing instances"
        else:
            warning = None
        task.execution_info_start(warning=warning)

    def listen_execution_ends(self, event: JobExecutionEvent):
        logger.debug("listen_execution_ends")
        task = self._get_task_by_id(int(event.job_id))
        task.executions_instances -= 1
        job = self.scheduler.get_job(event.job_id)

        # first send info, then change task status to keep the execution state
        if event.exception:
            task.execution_info_end_with_error(event.exception, None)
        else:
            task.execution_info_end(event.retval[0], event.retval[1])

        # task can be removed them job is removed and no more executions left
        if job is None and task.executions_instances == 0:
            task.update(status=TaskState.removed, job=job)
            self._remove_task(task)
        elif job is not None:
            task.update(job=job)

    def listen_job_removed(self, event: JobEvent):
        pass

    def run(self):
        logger.info('Starting up scheduler')
        self.scheduler.start()
        executing_tasks = self.check_for_tasks(TaskState.executing, self.target_system)
        scheduled_tasks = self.check_for_tasks(TaskState.scheduled, self.target_system)
        for task in scheduled_tasks + executing_tasks:
            msg = f"Removing {task} from Scheduler since is was in state {task.status} when starting up."
            logger.warning(msg)
            task.job_info.error_msg = msg
            task.update(status=TaskState.canceled, job_info=task.job_info)

        while not self.cease_continuous_run.is_set():
            # check db for new tasks
            new_tasks = self.check_for_tasks(TaskState.new, self.target_system)

            # put task into the scheduler
            for task in new_tasks or []:
                # append task to this thread
                self._add_task(task)
                # create new task
                logger.debug('got new task: ' + str(task))
                try:
                    _ = self.add_schedule_job(task)
                except Exception as err:
                    task.job_info.error_msg = f"{task} not scheduled\n{type(err).__name__}: {err}"
                    logger.error(task.job_info.error_msg)
                    task.update(status=TaskState.canceled, job_info=task.job_info)
            time.sleep(self.sleep_between_checks_sec)

    @staticmethod
    def check_for_tasks(status: TaskState, target_system: str) -> List[Task]:
        try:
            query = f"SELECT * FROM db_global.ScheduleJob where status = %s AND target_system = %s"
            # get all tasks
            raw_tasks, _ = select_query(query, values=(status.value, target_system))
            tasks = []
            for raw_task in raw_tasks:
                tasks.append(Task.parse_from_sql(raw_task))
        except mysqlError as err:
            logger.error(f'got an error while checking for new tasks:')
            logger.error("{}: {}".format(type(err).__name__, err))
            logger.error('waiting for 20secs to retry checking')
            time.sleep(20.0)
            tasks = []
        else:
            logger.debug(f"got {len(tasks)} tasks")
        return tasks

    def add_schedule_job(self, task: Task) -> Job:
        if task.job_info.trigger == AllowedTrigger.date:
            trigger = DateTrigger(**task.job_info.trigger_config, timezone=self.time_zone)
        elif task.job_info.trigger == AllowedTrigger.interval:
            trigger = IntervalTrigger(**task.job_info.trigger_config, timezone=self.time_zone)
        else:
            raise RuntimeError("Trigger not found!")

        if task.job_info.run_in_background:
            executor = 'background'
        else:
            executor = 'default'
            # ignore user setting and set max instances to 1 per default
            if task.job_info.max_instances != 1:
                logger.warning("setting max instances to 1 since this is not a background job")
                task.job_info.max_instances = 1
        # send bot info
        for bot_info in task.job_info.bot_info:
            if TaskState.new.value >= bot_info.info_level.value:
                msg = f"{task.status.symbol} Task created!\n"
                msg += f"<code>{task.__repr__()}</code>"
                Task.send_bot_info(bot_info, msg)
        scheduler_job = self.scheduler.add_job(id=str(task.id),
                                               func=ScheduleThread.task_template,
                                               args=[task],
                                               executor=executor,
                                               max_instances=task.job_info.max_instances,
                                               misfire_grace_time=task.job_info.misfire_grace_time,
                                               trigger=trigger)
        task.job = scheduler_job
        return scheduler_job

    @staticmethod
    def task_template(task: Task) -> (str, timedelta):
        # update the task
        tic = datetime.now()
        task = Task.get_task_from_id(task.id)
        if task.job_info.pydantic_args is not None:
            for pyd_arg in task.job_info.pydantic_args:
                task.job_info.args.append(getattr(sys.modules[task.job_info.module], pyd_arg[0]).parse_obj(pyd_arg[1]))
        if task.job_info.pydantic_kwargs is not None:
            for key, pyd_kwarg in task.job_info.pydantic_kwargs.items():
                task.job_info.kwargs[key] = getattr(sys.modules[task.job_info.module], pyd_kwarg[0]).parse_obj(
                    pyd_kwarg[1])
        result = getattr(sys.modules[task.job_info.module], task.job_info.callback)(*task.job_info.args,
                                                                                    **task.job_info.kwargs)
        duration = datetime.now() - tic
        if result is None:
            return 'No return value received.', duration
        else:
            try:
                result = str(result)
                return result, duration
            except Exception:
                return "Can not understand the result. But job executed.", duration
