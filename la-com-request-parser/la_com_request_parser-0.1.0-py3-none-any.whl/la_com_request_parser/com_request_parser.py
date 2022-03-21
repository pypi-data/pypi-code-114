import zmq
import json
from typing import List
import socket
from threading import Thread
import queue
import subprocess


class ReqParser:
    def __init__(self, client: str, devices: List[str], connect_port=5555, lookup_port=4444):
        """
        :param client: Name of client trying to access the DS
        :param devices: string List (typing) of device names that are meant to be used
        :param connect_port: designated port for 0mq communication; preferably stick to it
        :param lookup_port: int; for automatic identification of available DS; only change if necessary
        """
        self.client = client
        self.ips = list()
        self.ports = list()
        self.lookup_port = lookup_port
        self.devices = devices

        # automatically find ips of device servers
        self.ips = self.__find_server_ips__()

        if type(connect_port) != list:
            self.ports = [str(connect_port)] * len(self.ips)
        elif len(connect_port) == len(self.ips):
            self.ports = str(connect_port)
        else:
            print(f"Passed port {connect_port} does not match input format.")

        # open all 0mq sockets
        sockets, available_devices = list(), list()
        context = zmq.Context()
        for ip, port in zip(self.ips, self.ports):
            # connect
            try:
                sockets.append(context.socket(zmq.REQ))
                sockets[-1].connect(f"tcp://{ip}:{port}")
            except:
                print(f"Error in connection with {ip}:{port}")
                sockets.pop(-1)  # ensures that invalid connections are discarded

            # get available devices
            try:
                sockets[-1].send_json(json.dumps({"client": self.client}))
                message = json.loads(sockets[-1].recv_json())
                available_devices.append(message["devices"])
            except IndexError:
                # caused by exception above, no need for action; exception caught to differentiate errors
                continue
            except:
                print(f"No devices connected from {ip}:{port}.")

        # create dictionary with device string, socket tuple to connect to correct server
        self.connections = dict()
        for dev in devices:
            for s in range(len(sockets)):
                if dev in available_devices[s]:
                    self.connections[dev] = sockets[s]

        assert len(devices) == len(self.connections), f"Could not find all devices for given servers, missing: " \
                                                      f"{[d for d in devices if d not in self.connections.keys()]}"

    def __ping_sweep__(self, q, out_q):
        """Pings hosts in queue"""
        # hiding the ping message
        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = subprocess.SW_HIDE

        while True:
            # get an IP item form queue
            item = q.get()

            args = ['ping', '-n', '1', str(item['ip'])]
            output = subprocess.Popen(args,
                                      stdout=subprocess.PIPE,
                                      startupinfo=info).communicate()[0]

            # only replies from active servers are considered
            if "reply" in output.decode('utf-8').lower():
                out_q.put(item)

            # update queue : this ip is processed
            q.task_done()

    def __port_check__(self, network_ips: list) -> list:
        port_ips = list()
        for ip in network_ips:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((str(ip), self.lookup_port))
                if result == 0:
                    port_ips.append(ip)
                sock.close()
            except socket.gaierror:
                print("IP failed: ", ip)
                continue

        return port_ips

    def __find_server_ips__(self):
        num_threads = 64
        ips_q = queue.Queue()
        out_q = queue.Queue()

        # find all ips of Device Servers in subnet
        # find local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # random IP, does not need to exist; just required to get host IP
        s.connect(("8.8.8.8", 80))
        my_ip = s.getsockname()[0]
        s.close()
        subnet_ip = my_ip.rsplit(".", 1)[0] + "."

        # start the thread pool
        for i in range(num_threads):
            worker = Thread(target=self.__ping_sweep__, args=(ips_q, out_q))
            worker.setDaemon(True)
            worker.start()

        # fill queue; can additionally be filled with parameters (timeout etc.)
        for i in range(0, 256):
            ips_q.put({'ip': subnet_ip + str(i)})

        # wait until worker threads are done to exit
        ips_q.join()

        network_ips = list()
        while True:
            try:
                q_res = out_q.get_nowait()
            except queue.Empty:
                break
            # saving ips of all potential candidates
            network_ips.append(q_res['ip'])

        return self.__port_check__(network_ips)

    def request(self, device: str, action: str, payload=None):
        """
        device: addressed device name as string (defined in Device Server)
        action: requested action as string ("connect", "disconnect", "test", arbitrary)
        payload: values to be passed for arbitrary action

        :return:
        status: True (successful) or False (communication request failed)
        info: string of more detailed information

        """
        if device not in self.devices:
            return False, f"Device {device} unknown to communication manager!"

        if action in ["connect", "disconnect", "test"]:
            message = {"client": self.client,
                       "device": device,
                       "action": action}
        else:
            message = {"client": self.client,
                       "device": device,
                       "action": {action: payload}}
        try:
            self.connections[device].send_json(json.dumps(message))
        except:
            return False, f"Communication request with {device} failed."

        return_message = json.loads(self.connections[device].recv_json())

        return return_message["status"], return_message["info"]
