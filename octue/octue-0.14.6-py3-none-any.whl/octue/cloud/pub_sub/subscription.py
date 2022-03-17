import logging

import google.api_core.exceptions
from google.cloud.pubsub_v1 import SubscriberClient
from google.protobuf.duration_pb2 import Duration
from google.protobuf.field_mask_pb2 import FieldMask
from google.pubsub_v1.types.pubsub import ExpirationPolicy, RetryPolicy, Subscription as _Subscription


logger = logging.getLogger(__name__)

# Useful time periods in seconds.
SEVEN_DAYS = 7 * 24 * 3600
THIRTY_ONE_DAYS = 31 * 24 * 3600


class Subscription:
    """A candidate subscription to use with Google Pub/Sub. The subscription represented by an instance of this class
    does not necessarily already exist on the Google Pub/Sub servers.

    :param str name: the name of the subscription excluding "projects/<project_name>/subscriptions/<namespace>"
    :param octue.cloud.pub_sub.topic.Topic topic: the topic the subscription is attached to
    :param str project_name: the name of the Google Cloud project that the subscription belongs to
    :param str namespace: a namespace to put before the subscription's name in its path
    :param google.pubsub_v1.services.subscriber.client.SubscriberClient|None subscriber: a Google Pub/Sub subscriber that can be used to create or delete the subscription
    :param int ack_deadline: message acknowledgement deadline in seconds
    :param int message_retention_duration: unacknowledged message retention time in seconds
    :param int|None expiration_time: number of seconds after which the subscription is deleted (infinite time if None)
    :param float minimum_retry_backoff: minimum number of seconds after the acknowledgement deadline has passed to exponentially retry delivering a message to the subscription
    :param float maximum_retry_backoff: maximum number of seconds after the acknowledgement deadline has passed to exponentially retry delivering a message to the subscription
    :return None:
    """

    def __init__(
        self,
        name,
        topic,
        project_name,
        namespace="",
        subscriber=None,
        ack_deadline=60,
        message_retention_duration=SEVEN_DAYS,
        expiration_time=THIRTY_ONE_DAYS,
        minimum_retry_backoff=10,
        maximum_retry_backoff=600,
    ):
        if namespace and not name.startswith(namespace):
            self.name = f"{namespace}.{name}"
        else:
            self.name = name

        self.topic = topic
        self.subscriber = subscriber or SubscriberClient()
        self.path = self.generate_subscription_path(project_name, self.name)
        self.ack_deadline = ack_deadline
        self.message_retention_duration = Duration(seconds=message_retention_duration)

        # If expiration_time is None, the subscription will never expire.
        if expiration_time is None:
            self.expiration_policy = ExpirationPolicy(mapping=None)
        else:
            self.expiration_policy = ExpirationPolicy(mapping=None, ttl=Duration(seconds=expiration_time))

        self.retry_policy = RetryPolicy(
            mapping=None,
            minimum_backoff=Duration(seconds=minimum_retry_backoff),
            maximum_backoff=Duration(seconds=maximum_retry_backoff),
        )

    def __repr__(self):
        """Represent the subscription as a string.

        :return str:
        """
        return f"<{type(self).__name__}({self.name})>"

    def create(self, allow_existing=False):
        """Create a Google Pub/Sub subscription that can be subscribed to.

        :param bool allow_existing: if `False`, raise an error if the subscription already exists; if `True`, do nothing (the existing subscription is not overwritten)
        :return google.pubsub_v1.types.pubsub.Subscription:
        """
        subscription = self._create_proto_message_subscription()

        if not allow_existing:
            subscription = self.subscriber.create_subscription(request=subscription)
            self._log_creation()
            return subscription

        try:
            subscription = self.subscriber.create_subscription(request=subscription)
        except google.api_core.exceptions.AlreadyExists:
            pass

        self._log_creation()
        return subscription

    def update(self):
        """Update an existing subscription with the state of this instance.

        :return None:
        """
        self.subscriber.update_subscription(
            subscription=self._create_proto_message_subscription(),
            update_mask=FieldMask(
                paths=["ack_deadline_seconds", "message_retention_duration", "expiration_policy", "retry_policy"]
            ),
        )

    def delete(self):
        """Delete the subscription from Google Pub/Sub.

        :return None:
        """
        self.subscriber.delete_subscription(subscription=self.path)
        logger.debug("Subscription %r deleted.", self.path)

    @staticmethod
    def generate_subscription_path(project_name, subscription_name):
        """Generate a full subscription path in the format `projects/<project_name>/subscriptions/<subscription_name>`.

        :param str project_name:
        :param str subscription_name:
        :return str:
        """
        return f"projects/{project_name}/subscriptions/{subscription_name}"

    def _log_creation(self):
        """Log the creation of the subscription.

        :return None:
        """
        logger.debug("Subscription %r created.", self.path)

    def _create_proto_message_subscription(self):
        """Create a Proto message subscription from the instance to be sent to the Pub/Sub API.

        :return google.pubsub_v1.types.pubsub.Subscription:
        """
        return _Subscription(
            mapping=None,
            name=self.path,
            topic=self.topic.path,
            ack_deadline_seconds=self.ack_deadline,  # noqa
            message_retention_duration=self.message_retention_duration,  # noqa
            expiration_policy=self.expiration_policy,  # noqa
            retry_policy=self.retry_policy,  # noqa
        )
