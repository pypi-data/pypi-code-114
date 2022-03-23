import os
from abc import abstractmethod
from time import sleep
from kazoo.client import KazooClient
from kazoo.recipe.watchers import DataWatch, ChildrenWatch
import ast
from mobio.libs.m_scheduler_partitioning import generate_nano_id
from mobio.libs.m_scheduler_partitioning.scheduler_models.scheduler_state_model import (
    SchedulerStateModel,
)


class MobioScheduler:
    rebalancing = False
    lst_partitions = []
    # nop = 100
    zk_client = None

    def __init__(
        self,
        root_node="test-scheduler",
        node_id=None,
        nop=100,
        delays=1,
        url_connection=None,
    ):
        if not 10 <= nop <= 1000:
            raise Exception("nop {} not in range 10, 1000".format(nop))

        if delays > 3600:
            raise Exception("delays maximum is 3600 seconds")
        self.root_path = "/mobio-scheduler/{}".format(root_node)
        self.root_node = root_node
        self.nop = nop
        self.delays = delays
        self.url_connection = url_connection
        if not node_id:
            node_id = generate_nano_id(short=True)
        self.node_id = node_id
        self.my_node_path = "{}/{}".format(self.root_path, node_id)

        self.zk_client = KazooClient(
            hosts=os.getenv("ZOOKEEPER_CLUSTER", "localhost:2181")
        )
        self.zk_client.start()
        self.zk_client.ensure_path(self.root_path)
        sleep(1)
        self.zk_client.create(self.my_node_path, ephemeral=True)

        child_watch = ChildrenWatch(
            client=self.zk_client, path=self.root_path, func=self.watch_children
        )
        data_watch_root = DataWatch(
            client=self.zk_client, path=self.root_path, func=self.watch_data_root
        )
        data_watch_child = DataWatch(
            client=self.zk_client, path=self.my_node_path, func=self.watch_data_children
        )
        if self.url_connection:
            result_register_worker = SchedulerStateModel(self.url_connection).register_worker(
                worker_id=self.node_id,
                partitions=self.lst_partitions,
                delay_time=self.delays,
                root_node=self.root_node,
            )
            print("result_register_worker: {}".format(result_register_worker))
        try:
            while True:
                self.process()
                print("still alive after: {} seconds".format(self.delays))
                if self.url_connection:
                    result_increase_expiry_time = SchedulerStateModel(self.url_connection).increase_expiry_time(
                        worker_id=self.node_id, delay_time=self.delays
                    )
                    print("result_increase_expiry_time: {}".format(result_increase_expiry_time))
                sleep(self.delays)
        except RuntimeError as e:
            print("something unexpected happened: {}: {}".format(self.my_node_path, e))
        finally:
            print("consumer is stopped")
            self.zk_client.stop()
            self.zk_client.close()

    @abstractmethod
    def process(self):
        print("in process")
        if self.rebalancing:
            print("in process: rebalancing: {}".format(self.rebalancing))
            self.rebalancing = False
            print("in process: rebalancing: {}".format(self.rebalancing))
        """
        sample code:
        
        limit = 1000
        has_data = True
        sequence_id = 0
        lst_ids = []
        while has_data:
            lst_job = self.get_jobs(
                sequence_id=sequence_id, limit=limit
            )
            if len(lst_job) < limit:
                has_data = False
            for current_job in lst_job:
                if self.rebalancing:
                    if lst_ids:
                        self.save_to_sent_batch(lst_ids=lst_ids)
                        lst_ids = []
                        ConfluentProducerManager().flush_to_topic()
                    has_data = False
                    sys_conf.logger.warning(
                        "rebalancing in row: {}".format(current_msg.get("_id"))
                    )
                    self.rebalancing = False
                    break
    
                try:
                    sequence_id = current_job.get("sequence_id")
                    key = current_job.get("profile_id")
                    ConfluentProducerManager().send_message_to_topic_with_key_without_flush(
                        topic=KafkaTopic.FACTORY_F1_JB_ABANDONED_CART,
                        data=json.dumps(
                            json.loads(JSONEncoder().encode(current_job))
                        ).encode("utf-8"),
                        key=str(key),
                    )
    
                    lst_ids.append(_id)
                    if len(lst_ids) % 20 == 0:
                        self.save_to_sent_batch(lst_ids=lst_ids)
                        lst_ids = []
                        ConfluentProducerManager().flush_to_topic()
                except Exception as er:
                    err_msg = "do_process:: cannot sent data ERROR: {}".format(er)
                    sys_conf.logger.error(err_msg)
            if lst_ids:
                self.save_to_sent_batch(lst_ids=lst_ids)
                lst_ids = []
                ConfluentProducerManager().flush_to_topic()
        """

    # function theo dõi sự thay đổi của các workers.
    # Nếu có worker join hoặc leave parent thì sẽ assign lại partitions cho các workers
    def watch_children(self, lst_children):
        print("Children are now: {}".format(lst_children))
        self.rebalance_current_node()
        num_childs = len(lst_children)
        lst = [x for x in range(self.nop)]
        tmp_lst_partitions = self.split(lst, num_childs)
        for i in range(num_childs):
            value = bytes(str(tmp_lst_partitions[i]), "utf-8")
            self.zk_client.set(
                "{}/{}".format(self.root_path, lst_children[i]), value=value
            )
        print("set data done")

    # function notify số lượng partitions mà worker này sẽ xử lý
    def watch_data_root(self, data, stat):
        print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

    # function notify cho worker là cần rebalance lại partitions
    def watch_data_children(self, data, stat):
        print(
            "watch_data_children:: Version: %s, data: %s"
            % (stat.version, data.decode("utf-8"))
        )
        d = data.decode("utf-8")
        self.rebalancing = True
        self.lst_partitions = []
        if d:
            array = ast.literal_eval(d)
            for p in array:
                self.lst_partitions.append(p)
        print("current partition: {}".format(self.lst_partitions))
        result = SchedulerStateModel(self.url_connection).rebalance_partitions(
            worker_id=self.node_id, partitions=self.lst_partitions
        )
        print("result rebalance: {}".format(result))

    # function reset số lượng partitions cúa worker này.
    def rebalance_current_node(self):
        self.zk_client.set(path=self.my_node_path, value=bytes("", "utf-8"))

    def split(self, a, n):
        k, m = divmod(len(a), n)
        return list(
            a[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n)
        )


if __name__ == "__main__":
    MobioScheduler()
