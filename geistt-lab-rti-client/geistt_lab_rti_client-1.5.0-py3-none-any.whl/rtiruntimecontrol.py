
# Utility class to simplify sending "start", "stop" messages etc...

from . import proto
from . import constants
from .rticlient import RTIClient

class RTIRuntimeControl:

    def __init__(self, rti: RTIClient, subscribe = True):
        self.rti = rti

        self.subscribed = False
        self.on_reset = None
        self.on_load_scenario = None
        self.on_start = None
        self.on_play = None
        self.on_pause = None
        self.on_end = None
        self.on_stop = None
        self.on_time_scale = None

        self.scenario = None
        self.time_scale = None
        self.current_log = None

        if subscribe: self.subscribe()

    def reset(self):
        message = proto.RuntimeControl()
        message.reset.SetInParent()
        self.publish_and_receive(message)
    
    def load_scenario(self, scenario_name):
        message = proto.RuntimeControl()
        message.load_scenario.name = scenario_name
        self.publish_and_receive(message)

    def start(self):
        message = proto.RuntimeControl()
        message.start.SetInParent()
        self.publish_and_receive(message)

    def play(self):
        message = proto.RuntimeControl()
        message.play.SetInParent()
        self.publish_and_receive(message)

    def pause(self):
        message = proto.RuntimeControl()
        message.pause.SetInParent()
        self.publish_and_receive(message)

    def end(self):
        message = proto.RuntimeControl()
        message.end.SetInParent()
        self.publish_and_receive(message)

    def stop(self):
        message = proto.RuntimeControl()
        message.stop.SetInParent()
        self.publish_and_receive(message)

    def set_time_scale(self, time_scale: float):
        message = proto.RuntimeControl()
        message.set_time_scale.time_scale = time_scale
        self.publish_and_receive(message)

    def seek(self, time: float):
        message = proto.RuntimeControl()
        message.seek.time = time
        self.publish_and_receive(message)

    def subscribe(self):
        if not self.subscribed:
            def on_runtime_control(channel, message):
                self._receive(message)
            self.rti.subscribe(constants.control_channel, proto.RuntimeControl, on_runtime_control)
            self.subscribed = True

    def publish_and_receive(self, message: proto.RuntimeControl):
        self.rti.publish(constants.control_channel, message)
        if not self.rti.connected or not self.subscribed: self._receive(message)

    def _receive(self, message: proto.RuntimeControl):
        if message.HasField("reset"):
            if self.on_reset: self.on_reset()
            self.rti.state = proto.RuntimeState.INITIAL
        elif message.HasField("load_scenario"):
            self.scenario = message.load_scenario.name
            if self.on_load_scenario:
                self.rti.state = proto.RuntimeState.LOADING
                self.on_load_scenario(message.load_scenario.name)
            self.rti.state = proto.RuntimeState.READY
        elif message.HasField("start"):
            if self.on_start: self.on_start()
            self.rti.state = proto.RuntimeState.RUNNING
        elif message.HasField("play"):
            if self.on_play: self.on_play()
            self.rti.state = proto.RuntimeState.PLAYBACK
        elif message.HasField("pause"):
            if self.on_pause: self.on_pause()
            self.rti.state = proto.RuntimeState.PLAYBACK_PAUSED if self.rti.state == proto.RuntimeState.PLAYBACK else proto.RuntimeState.PAUSED
        elif message.HasField("end"):
            if self.on_start: self.on_end()
            self.rti.state = proto.RuntimeState.PLAYBACK_END if self.rti.state == proto.RuntimeState.PLAYBACK else proto.RuntimeState.END
        elif message.HasField("stop"):
            if self.on_start: self.on_stop()
            self.rti.state = proto.RuntimeState.PLAYBACK_STOPPED if self.rti.state == proto.RuntimeState.PLAYBACK else proto.RuntimeState.STOPPED
        elif message.HasField("set_time_scale"):
            self.time_scale = message.set_time_scale.time_scale
            if self.on_time_scale: self.on_time_scale()
        elif message.HasField("time_sync"):
            self.time_scale = message.time_sync.time_scale
        elif message.HasField("current_log"):
            self.current_log = message.current_log
