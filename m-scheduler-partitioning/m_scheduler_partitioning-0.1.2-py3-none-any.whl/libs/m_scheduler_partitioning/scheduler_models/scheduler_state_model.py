from datetime import datetime, timedelta

from mobio.libs.m_scheduler_partitioning.scheduler_models.base_model import BaseModel


class SchedulerState:
    BUSY = "busy"
    FREE = "free"


class SchedulerStateModel(BaseModel):
    ID = "_id"
    STATE = "state"
    EXPIRY_TIME = "expiry_time"
    PARTITIONS = "partitions"
    ROOT_NODE = "root_node"

    def __init__(self, url_connection):
        super(SchedulerStateModel, self).__init__(url_connection)
        self.collection = "scheduler_state"

    def register_worker(self, worker_id, partitions, root_node, delay_time):
        return (
            self.get_db()
            .insert_one(
                {
                    self.ID: worker_id,
                    self.STATE: SchedulerState.FREE,
                    self.PARTITIONS: partitions,
                    self.ROOT_NODE: root_node,
                    self.EXPIRY_TIME: datetime.utcnow() + timedelta(seconds=delay_time+15),
                    self.CREATED_TIME: datetime.utcnow(),
                    self.UPDATED_TIME: datetime.utcnow(),
                }
            )
            .inserted_id
        )

    def increase_expiry_time(self, worker_id, delay_time):
        return (
            self.get_db()
            .update_one(
                {self.ID: worker_id},
                {
                    "$set": {
                        self.STATE: SchedulerState.FREE,
                        self.EXPIRY_TIME: datetime.utcnow() + timedelta(seconds=delay_time+15),
                    }
                },
            )
            .matched_count
        )

    def set_busy(self, worker_id):
        return (
            self.get_db()
            .update_one(
                {self.ID: worker_id},
                {"$set": {self.STATE: SchedulerState.BUSY, self.EXPIRY_TIME: datetime.utcnow() + timedelta(days=10)}},
            )
            .matched_count
        )

    def get_free_worker(self, root_node):
        result = self.get_db().find({self.ROOT_NODE: root_node, self.STATE: SchedulerState.FREE})
        return list(result)
