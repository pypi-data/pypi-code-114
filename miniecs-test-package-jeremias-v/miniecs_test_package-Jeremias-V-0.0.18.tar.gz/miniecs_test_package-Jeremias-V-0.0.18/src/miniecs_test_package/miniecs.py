import socket
from xmlrpc.client import Boolean

class MiniECS:
    """
    A class used to define the methods of the mini elastic
    container service project for Operating Systems course.
    """

    def __init__(self, address = 'localhost', port = 65535) -> None:
        self.address = address
        self.port = port
        self.sock = socket.create_connection((self.address, self.port))
        self.containers_info = {}

    def stop(self):

        response = (False, "None")
        try:
            command = 'X!STOP'
            message = name.encode()
            print('sending {!r}'.format(message))
            self.sock.sendall(message)

            amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {!r}'.format(data))

        finally:
            response = (True, "Success, the signal to stop the connection was sent.".format(name))

        self.sock.close()

        return response
        

    def create_container(self, name: str):

        response = (False, "None")

        if name not in self.containers_info:

            self.containers_info[name] = True

            try:
                name = 'C!' + name
                message = name.encode()
                print('sending {!r}'.format(message))
                self.sock.sendall(message)

                amount_received = 0
                amount_expected = len(message)
                while amount_received < amount_expected:
                    data = self.sock.recv(16)
                    amount_received += len(data)
                    print('received {!r}'.format(data))

            finally:
                response = (True, "Success, the container with name '{}' was created.".format(name))
        
        else:

            response = (False, "Error, the container with name '{}' already exists.".format(name))
        
        return response
    
    def list_containers(self) -> str:
        ans = ""
        for key, val in self.containers_info.items():
            ans += "{0: <30} {1}\n".format(key, 'RUNNING' if val else 'STOPPED')
        return ans.strip()

    def resume_container(self, name: str):
        response = (False, "None")

        if name in self.containers_info:

            self.containers_info[name] = True

            try:
                name = 'R!' + name
                message = name.encode()
                print('sending {!r}'.format(message))
                self.sock.sendall(message)

                amount_received = 0
                amount_expected = len(message)
                while amount_received < amount_expected:
                    data = self.sock.recv(16)
                    amount_received += len(data)
                    print('received {!r}'.format(data))

            finally:
                response = (True, "Success, the signal to resume the container '{}' was sent.".format(name))
        
        else:

            response = (False, "Error, the container with name '{}' doesn't exist.".format(name))
        
        return response

    def stop_container(self, name: str):
        response = (False, "None")

        if name in self.containers_info:

            self.containers_info[name] = False

            try:
                name = 'S!' + name
                message = name.encode()
                print('sending {!r}'.format(message))
                self.sock.sendall(message)

                amount_received = 0
                amount_expected = len(message)
                while amount_received < amount_expected:
                    data = self.sock.recv(16)
                    amount_received += len(data)
                    print('received {!r}'.format(data))

            finally:
                response = (True, "Success, the signal to stop the container '{}' was sent.".format(name))
        
        else:

            response = (False, "Error, the container with name '{}' doesn't exist.".format(name))
        
        return response

    def delete_instance(self, name: str):
        response = (False, "None")

        if name in self.containers_info:

            del self.containers_info[name]

            try:
                name = 'D!' + name
                message = name.encode()
                print('sending {!r}'.format(message))
                self.sock.sendall(message)

                amount_received = 0
                amount_expected = len(message)
                while amount_received < amount_expected:
                    data = self.sock.recv(16)
                    amount_received += len(data)
                    print('received {!r}'.format(data))

            finally:
                response = (True, "Success, the signal to delete the instance '{}' was sent.".format(name))
        
        else:

            response = (False, "Error, the container with name '{}' doesn't exist.".format(name))
        
        return response
