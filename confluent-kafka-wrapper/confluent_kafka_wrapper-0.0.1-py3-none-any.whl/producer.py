import logging
import os

from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer


def _get_config_from_env(username: str, password: str, producer_id: str, acks: int, idempotence: bool):

    return {
        'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS') or "localhost:9092",
        'security.protocol': os.getenv('KAFKA_SECURITY_PROTOCOL') or "PLAINTEXT",
        'sasl.mechanism': os.getenv('SASL_MECHANISMS') or "PLAIN",
        'sasl.username': username,
        'sasl.password': password,
        'acks': acks,
        'enable.idempotence': idempotence,
        'client.id': producer_id
    }


def _get_schema_registry_confing_from_env():
    schema_registry_url = os.getenv('SCHEMA_REGISTRY_URL')
    schema_registry_userinfo = os.getenv('SCHEMA_REGISTRY_USERINFO')

    return {
        'url': schema_registry_url if schema_registry_url is not None else "localhost:9091",
        'basic.auth.user.info': schema_registry_userinfo if schema_registry_userinfo is not None else ""
    }


class KafkaProducer:

    def __init__(self,
                 username: str,
                 password: str,
                 topic: str,
                 producer_id: str = 'DEFAULT_CLIENT',
                 strong_sending: int = 0,
                 use_log: bool = False,
                 ):
        """
        confluent kafka producer 클래스 생성자
        :param username: Kafka 에 접속하기 위한 API username
        :param password: Kafka 에 접속하기 위한 API password
        :param topic: 해당 producer 가 메시지를 송출할 Topic
        :param strong_sending: producer 가 메시지를 보낼 때, 메시지 전송의 안정성을 보장하는 정도입니다.
                               음수일 경우 - acks = 1 (일부 Replica 에만 메시지가 들어감을 보장), enable.idempotence = False (메시지 순서를 보장하지 않습니다)
                               0일 경우 (기본) - acks = all (모든 Replica 에 메시지가 들어감을 보장), enable.idempotence = False
                               양수일 경우 - acks = 1, enable.idempotence = True (메시지 순서 보장)
        :param use_log: 로그 남기기 설정
        """

        if topic is None:
            raise AttributeError("topic 을 지정하지 않았습니다.")

        # set Producer info
        if strong_sending < 0:
            acks, idempotence = 1, False
        elif strong_sending == 0:
            acks, idempotence = 'all', False
        else:
            acks, idempotence = 'all', True
        self._config = _get_config_from_env(username, password, producer_id, acks, idempotence)
        self._config["key.serializer"] = StringSerializer('utf-8')
        self._config["value.serializer"] = StringSerializer('utf-8')
        self.producer = SerializingProducer(self._config)
        self.topic = topic
        self.count = 0

        # if logging setting is True, using _produce_log function to log
        # if not, don't use log function
        self.logging = use_log
        if use_log is True:
            self._produce_logging = KafkaProducer._produce_log
        else:
            self._produce_logging = KafkaProducer._produce_err

    @staticmethod
    def _produce_log(err, msg):
        if err is not None:
            logging.error(f"Failed to deliver message on Topic {msg.topic()}, err : {err}")
        else:
            logging.info(f"Delivered Topic {msg.topic()}, partition {msg.partition()}, offset {msg.offset()}, key {msg.key().decode()}, value {msg.value().decode()}")

    @staticmethod
    def _produce_err(err, msg):
        if err is not None:
            logging.info(f"Failed to deliver message on Topic {msg.topic()}, err : {err}")

    def produce(self, key, value):
        # produce and set callback function (for logging)
        self.producer.produce(self.topic, key=key, value=value, on_delivery=self._produce_logging)
        self.producer.poll(0)
        self.count += 1

    def stop(self):
        # if stop is called, producer will flush
        if self.logging is True:
            logging.info(f"messages were produced to topic {self.topic}, count {self.count}")
        self.producer.flush()
