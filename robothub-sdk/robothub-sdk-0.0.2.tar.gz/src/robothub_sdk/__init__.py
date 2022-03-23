import base64
import json
import os
import uuid
import warnings
from datetime import datetime, timedelta
from pathlib import Path
import urllib.request
from urllib.error import HTTPError, URLError

import cv2
import paho_socket as mqtt_client
import numpy as np


class RobotHubPublishException(Exception):
    pass


class RobotHubConnectionException(Exception):
    pass


class Config:
    _rawConfig = {}
    _defaults = {}

    def __getattr__(self, key):
        try:
            return self._rawConfig[key]
        except KeyError:
            return self._defaults.get(key)

    def readConfig(self, raw):
        self._rawConfig = json.loads(raw)

    def addDefaults(self, **kwargs):
        self._defaults = {**self._defaults, **kwargs}


def frameNorm(frame, bbox):
    normVals = np.full(len(bbox), frame.shape[0])
    normVals[::2] = frame.shape[1]
    return (np.clip(np.array(bbox), 0, 1) * normVals).astype(int)


class Detection:
    id = None
    position = None
    first_update = None
    last_update = None
    label = None
    latest_bbox = None
    bboxes = []
    frames = []
    _custom = {}

    def __init__(self, position, label, bbox):
        self.id = str(uuid.uuid4())
        self.label = label
        self.first_update = datetime.now()
        self.update(position, bbox)

    def update(self, position, bbox):
        self.position = position
        self.last_update = datetime.now()
        self.latest_bbox = bbox
        self.bboxes.append(bbox)

    def parse_frame(self, frame):
        bbox = frameNorm(frame, [self.latest_bbox[0], self.latest_bbox[1], self.latest_bbox[2], self.latest_bbox[3]])
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 0, 255), 2)
        self.frames.append(frame)

    def add_field(self, name, data):
        self._custom[name] = data

    def get_payload(self):
        return json.dumps({
            "id": self.id,
            "label": self.label,
            "start": self.first_update.astimezone().replace(microsecond=0).isoformat(),
            "end": self.last_update.astimezone().replace(microsecond=0).isoformat(),
            "frames": [base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode('ascii') for frame in self.frames],
            **self._custom,
        }, ensure_ascii=False)

    @property
    def active(self):
        return datetime.now() - self.last_update < timedelta(seconds=5)

    @property
    def completed(self):
        return datetime.now() - self.first_update > timedelta(seconds=15) or not self.active

    def __str__(self):
        return f"Detection<{self.label} {self.id} - {self.last_update.strftime('%H:%M:%S.%f')} (entries: {len(self.bboxes)})>"

    def __repr__(self):
        return self.__str__()


def dist(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))


def get_pos(entry):
    if hasattr(entry, 'spatialCoordinates'):
        x = entry.spatialCoordinates.x / 1000
        y = entry.spatialCoordinates.y / 1000
        z = entry.spatialCoordinates.z / 1000
    else:
        x = abs(entry.xmax - entry.xmin) / 2
        y = abs(entry.ymax - entry.ymin) / 2
        z = 0
    return [x, y, z]


class DetectionParser:
    #: list: Contains active detections (still detected by NN)
    active = []
    #: list: Contains inactive detections (were not detected by NN for specified period of time and are assumed "lost")
    inactive = []

    def __init__(self, class_whitelist=None, matching_threshold=1.5, confidence_threshold=0.8):
        """
        This class is responsible for extracting detections from NN data and matching the same ones across multiple detections.

        Args:
            class_whitelist (list, Optional): A list of class identifiers, specifying which classes are taken upon consideration while matching
            matching_threshold (float, Optional): Defines the maximum distance between a detection being classified as a new one or matched with the existing one
            confidence_threshold (float, Optional): Defines the minimum confidence the nn result should have to be parsed
        """
        self.matching_threshold = matching_threshold
        self.confidence_threshold = confidence_threshold
        self.class_whitelist = class_whitelist

    def parse(self, data):
        """
        Consumes the NN data and either creates new Detections or updates the existing ones.

        Args:
            data (list): A list containing NN packets produced by device

        """
        for entry in data:
            bbox = [entry.xmin, entry.ymin, entry.xmax, entry.ymax]
            if entry.confidence < self.confidence_threshold:
                continue
            if self.class_whitelist is not None and entry.label in self.class_whitelist:
                continue

            new_position = get_pos(entry)

            for detection in self.active:
                if detection.label == entry.label and dist(detection.position, new_position) < self.matching_threshold:
                    detection.update(new_position, bbox)
                    break
            else:
                self.active.append(Detection(new_position, entry. label, bbox))

        self.active = list(filter(lambda detection: self.inactive.append(detection) if not detection.active else True, self.active))
        print(self.active)

    def feed_frame(self, frame):
        """
        Sends a frame to all active detections for parsing

        Args:
            frame (numpy.ndarray): A frame object

        """
        for detection in self.active:
            detection.parse_frame(frame)

    def has_completed(self):
        """
        Allows checking whether any of the detections are ready to be sent

        Returns:
            bool: True if there is at least one completed detection
        """
        return any(filter(lambda detection: detection.completed, self.active))

    def get_completed(self):
        """
        Returns a list of detections that are ready to be sent

        Returns:
            list: list of detection objects that are completed
        """
        return list(filter(lambda detection: detection.completed, self.active))

    def remove_detection(self, detection):
        """
        Removes a detection from active or inactive list

        Args:
            detection (robothub_sdk.Detection): A detection object to be removed
        """
        if detection in self.active:
            self.active.remove(detection)
        if detection in self.inactive:
            self.inactive.remove(detection)


class RobotHubClient:
    #: str: unique identifier of the application
    app_id = None
    #: list: Contains device identifiers on which the application can be executed
    device_ids = None
    #: paho_socket.Client: Contains device identifiers on which the application can be executed
    client = None
    #: Config: Contains config supplied by Agent
    config = Config()
    _config_path = None
    _broker_path = None

    def __init__(self, broker_path=None, config_path=None):
        """
        This class is responsible for managing connection between Agent and App.

        Args:
            broker_path (pathlib.Path, Optional): Path to Agent MQTT UNIX socket
            config_path (pathlib.Path, Optional): Path to initial JSON configuration file

        Raises:
            RobotHubConnectionException: If the path to Agent MQTT UNIX socket was not found automatically
        """

        if broker_path is not None:
            parsed = Path(broker_path).resolve().absolute()
            if parsed.exists():
                self._broker_path = parsed
        if config_path is not None:
            parsed = Path(config_path).resolve().absolute()
            if parsed.exists():
                self._config_path = parsed

        if self._config_path is None:
            primary_path = Path('/initial-configuration.json')
            if primary_path.exists():
                self._config_path = primary_path
            else:
                t = "Unable to resolve initial config file location - configuration not loaded. This issue can be solved by providing `config_path` param"
                warnings.warn(t)

        if self._config_path is not None:
            with self._config_path.open() as f:
                self.config.readConfig(json.load(f))

        if self._broker_path is None:
            primary_path = Path('/broker').resolve().absolute()
            secondary_path = (Path(__file__).parent.parent.parent.parent.parent / "dist" / "broker.sock").resolve().absolute()
            if primary_path.exists():
                self._broker_path = primary_path
            elif secondary_path.exists():
                self._broker_path = secondary_path
            else:
                raise RobotHubConnectionException("Unable to resolve broker path. Please provide `broker_path` parameter with socket path")

        self.app_id = os.environ.get('APP_ID', str(uuid.uuid4()))
        self.device_ids = os.environ.get('APP_DEVICES')

    # START MQTT

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.client.on_message = self._on_message
        else:
            raise RobotHubConnectionException(f"Failed to connect - non-zero return code: {rc}", )

    def _on_disconnect(self):
        print("Disconnected to MQTT Broker!")

    def _on_message(self, client, userdata, msg):
        data = msg.payload.decode()
        print(f"Received `{data}` from `{msg.topic}` topic")
        if msg.topic == f'{self.app_id}/configuration':
            self.config.readConfig(data)

    def _send_message(self, topic, msg):
        if self.client is None:
            raise RobotHubPublishException(f"Failed to send message to topic {topic} - client not connected")
        ret = self.client.publish(topic, msg)[0]
        if ret != 0:
            raise RobotHubPublishException(f"Failed to send message to topic {topic} - non-zero return code: {ret}")
        else:
            print(f"Send message to {topic} topic")

    def _send_request(self, url, payload):
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        try:
             urllib.request.urlopen(req, payload.encode('utf-8'))
        except HTTPError as e:
            # do something
            RobotHubPublishException(f"Failed to send message to URL {url} - non-zero return code: {e.code}")
            print('Error code: ', e.code)
        except URLError as e:
            # do something
            RobotHubPublishException(f"Failed to send message to URL {url} - reason: {e.reason}")
            print('Reason: ', e.reason)
        print(f"Send message to {url} topic with payload {payload}")

    def connect(self):
        """
        Starts a connection to the Agent

        Raises:
            RobotHubConnectionException: Raised if a connection was not successful
        """

        self.client = mqtt_client.Client("robothubsdk-luxonis")
        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect
        self.client.sock_connect(str(self._broker_path))
        self.client.loop_start()

    def disconnect(self):
        """
        Terminates a connection to the Agent (if was started)
        """
        if self.client is None:
            warnings.warn("Client not connected - nothing to disconnect!")
        else:
            self.client.loop_stop()

    # END MQTT

    def send_detection(self, detection):
        """
        Sends the :class:`robothub_sdk.Detection` object to the Agent
        """
        payload = detection.get_payload()
        if self.config.detections_url is not None:
            self._send_request(self.config.detections_url, payload)
        else:
            self._send_message("online/detections", payload)

    def send_preview(self, name, frame):
        """
        Sends a preview frame to the Agent

        Args:
            name (str): Name of the preview
            frame (numpy.ndarray): Frame object
        """
        self._send_message(f"online/preview-{name}", cv2.cvtColor(frame, cv2.COLOR_BGR2YUV_I420).tobytes())
