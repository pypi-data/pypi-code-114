import logging
import os
import threading
from queue import Queue
from typing import Tuple

from confluent_kafka import Consumer, Message, TopicPartition


class StoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


def _get_config_from_env(username: str, password: str, group_id: str, consumer_id: str, offset: str, auto_commit: bool):

    return {
        'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS') or "localhost:9092",
        'security.protocol': os.getenv('KAFKA_SECURITY_PROTOCOL') or "PLAINTEXT",
        'sasl.mechanism': os.getenv('SASL_MECHANISMS') or "PLAIN",
        'sasl.username': username,
        'sasl.password': password,
        'enable.auto.commit': auto_commit,
        'group.id': group_id,
        'auto.offset.reset': offset,
        'client.id': consumer_id
    }


class KafkaConsumer(StoppableThread):

    def __init__(self,
                 username: str,
                 password: str,
                 topic: str,
                 callback_function,
                 auto_start: bool = True,
                 strong_receiving: bool = True,
                 strong_receiving_fail_retry_count: int = 3,
                 strong_receiving_fail_callback=None,
                 group_id: str = 'DEFAULT_GROUP',
                 consumer_id: str = 'DEFAULT_CLIENT',
                 offset='earliest'):
        """
        Kafka consumer 를 생성하는 클래스입니다.
        :param username: Kafka 에 접속하기 위한 API username
        :param password: Kafka 에 접속하기 위한 API password
        :param topic: consume 할 Topic 이름입니다.
        :param callback_function: Consumer 로부터 받아들인 값을 처리할 callback function 을 입력받습니다.
                                  callback function 은 입력으로 (key: str, value: str) 를 받아야 합니다.
        :param auto_start: consumer 의 메시지 consume 을 기본적으로 시작할 지 설정하는 파라미터입니다.
                           기본 True 이고, False 일 시 Consumer 를 수동으로 시작해줘야 합니다.
        :param strong_receiving: Consumer 의 receiving 정책을 결정합니다.
                                 True 일 경우, 한 번에 하나의 메시지만을 받고, 해당 메시지에 대해 비즈니스 로직이 수행된 이후에 commit 을 수행해 다음 메시지를 가져오도록 설정합니다.
                                    비즈니스 로직 시행 중 실패시 최대 strong_receiving_fail_retry_count 까지 시도하고, 끝까지 실패한다면 fail_callback 을 실행합니다.
                                 False 일 경우, 계속 메시지를 받고, 비즈니스 로직의 실패를 고려하지 않습니다.
        :param strong_receiving_fail_retry_count : strong_receiving 수행 중, 몇 번을 실패해야 알람을 보낼 것인지를 설정합니다.
                                                   다만, consume_queue 방식을 사용할 경우 비활성화됩니다.
                                                   기본값은 3으로, 메시지 consume 실패시 최대 3번까지, 비즈니스 로직 수행시 최대 3번까지 시도합니다.
        :param strong_receiving_fail_callback : strong_receiving 수행 중, 실패 횟수가 지정 상한을 넘었을 때 실행할 callback function 을 설정합니다.
        :param group_id: 해당 consumer의 group_id 입니다. 기본값은 'DEFALUT GROUP' 로 설정됩니다.
        :param consumer_id: 해당 consumer 의 이름입니다. 기본값은 'DEFAULT CLIENT' 로 설정됩니다.
        :param offset: 해당 group_id 의 offset 설정 정책입니다. 기본값은 'earliest' 입니다.
        """
        super().__init__()

        if topic is None:
            raise AttributeError('[KafkaConsumer] Kafka Topic 이 제공되지 않음')
        elif type(topic) == str:
            self.topics = [topic]
        else:
            raise AttributeError('[KafkaConsumer] Kafka Topic 으로 잘못된 값을 지정함')

        # set consume policy
        if strong_receiving:
            self._consume = self._consume_with_strong_receiving
            auto_commit = False
        else:
            self._consume = self._consume_with_weak_receiving
            auto_commit = True

        self._callback_function = callback_function
        self._consumer_config = _get_config_from_env(username, password, group_id, consumer_id, offset, auto_commit)
        self._consumer = Consumer(self._consumer_config)
        self._consumer.subscribe(self.topics)
        self.consume_queue = Queue()
        self._logger = logging.getLogger("KafkaConsumer")
        self._fail_retry_count = strong_receiving_fail_retry_count
        self._fail_callback = strong_receiving_fail_callback

        # start consumer
        if auto_start:
            self.start()

        self._logger.info("[KafkaConsumer] init complete!")

    def run(self):
        try:
            while not self.stopped():
                self._consume()
        except KeyboardInterrupt:
            pass
        finally:
            # if thread is stopped, consumer will be closed and print closed log
            self._consumer.close()
        self._logger.info(f"Consume stopped on topics : {self.topics}")

    def _use_callback(self, key: str, value: str) -> Tuple[bool, Exception]:
        count = 0
        cur_exception = None
        while count < self._fail_retry_count:
            try:
                self._callback_function(key=key, value=value)
                break
            except Exception as e:
                count += 1
                cur_exception = e
                continue
        if count == self._fail_retry_count:
            return False, cur_exception
        else:
            return True, cur_exception

    def _consume_message_with_fail_count(self) -> Tuple[bool, Message]:
        for i in range(self._fail_retry_count):
            message: Message = self._consumer.consume(num_messages=1, timeout=-1)[0]
            if message.error():
                topic_partition = TopicPartition(message.topic(), message.partition())
                topic_partition.offset = message.offset()
                self._consumer.seek(topic_partition)
            else:
                return True, message
        return False, message

    def _consume_with_strong_receiving(self) -> Message:
        is_normal, message = self._consume_message_with_fail_count()
        if is_normal is False:
            self._fail_callback(message=message)
        else:
            key: str = message.key().decode()
            value: str = message.value().decode()
            is_normal, exception = self._use_callback(key, value)
            if is_normal is False:
                self._fail_callback(message=message, exception=exception)
            self._consumer.commit(message=message)
        return message

    def _consume_with_weak_receiving(self) -> bool:
        message: Message = self._consumer.poll(1.0)

        # if message is received, check error. if error is True, logging and continue receiving again
        if message is None:
            return False
        if message.error():
            self._logger.error(f"Error occured while consuming message on topic : {self.topics}")
            return False

        # retain message values
        key: str = message.key().decode()
        value: str = message.value().decode()
        self._use_callback(key, value)
