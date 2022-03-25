import pickle
import struct
from time import sleep
from qsct.obj_method import Sender
from qsct import functions


class QSCT:
    """QSCT - (Qodex Software Communication Tools) - это класс, представляющий из себя набор инструментов для
    создания API и SDK. Является супер-классом для суб-классов:
    1) QPI (Qodex Programming Interface) - API для ПО разработки компании Qodex,
    2) QDK (Qodex Development Kit) - SDK для взаимодействия с API ПО Qodex.
    QSCT опредлеяет методы передачи и получения данных, а также прочего взаимодействия между этими инструментами.
    """

    def __init__(self, debug=False, name=None, *args, **kwargs):
        """ Принимает атрибуты debug (вкл/выкл вывод в основной поток вывода информации о деятельности программы,
        name - собственное имя """
        self.status_ready = True
        self.debug = debug
        self.name = name
        self.run = Running()

    def send_data_old(self, sock, data, *args, **kwargs):
        """ Отправить сериализированные данные на WServer
        Протокол передачи такой - сначала длинна отправляемых данных, затем сами данные"""
        self.show_print('\nОтправка данных:', data, debug=True)
        self.show_print('\tPickling...', debug=True)
        pickled_data = pickle.dumps(data, pickle.HIGHEST_PROTOCOL)
        data_length = len(pickled_data)
        data_length_packed = struct.pack('>Q', data_length)
        self.show_print('\tОтправка длины...', data_length, debug=True)
        # sock.send(data_length_packed)
        try:
            sock.send(data_length_packed)
            self.show_print('\tОтправка данных...', debug=True)
        except:
            # recreate the socket and reconnect
            self.show_print('\tПотеряно соединение', debug=True)
            return
        # sock.send(pickled_data)
        try:
            sock.send(pickled_data)
            self.show_print('\tДанные были отправлены.', debug=True)
        except:
            # recreate the socket and reconnect
            self.show_print('\tПотеряно соединение', debug=True)

    def get_response(self, sock, *args, **kwargs):
        """Получить, показать и вернуть ответ"""
        response = self.get_data(sock)
        self.show_print('\tПолучен ответ', response, debug=True)
        return response

    def get_data_old(self, sock, *args, **kwargs):
        """Получить данные из сокета. Принимает данные в формате pickle, причем, сначала принимает длину данных,
        а потом сами данные """
        self.show_print('\nОжидаем данные', debug=True)
        try:
            packet = sock.recv(8)
        except:
            self.show_print('\tПотеряно соединене при получении длинны', debug=True)
            packet = b''
        if not packet:
            return
        self.show_print('Got data: {}'.format(packet), debug=True)
        (data_length_unpacked,) = struct.unpack('>Q', packet)
        self.show_print('data length', data_length_unpacked, debug=True)
        data = b''
        # sock.close()
        while len(data) < data_length_unpacked:
            try:
                to_read = data_length_unpacked - len(data)
                data += sock.recv(4096 if to_read > 4096 else to_read)
            except:
                self.show_print('\tПотеряно соединене при получении данных', debug=True)
                return b''
        unpickled_data = pickle.loads(data)
        return unpickled_data

    def show_print(self, *msg, debug=False):
        """ Замена обычному print(), дополнительно получает аргумент debug, и если он положительный - информация msg
        будет выводиться в стандартный поток вывода, только если сам класс вызван с атрибутом debug"""
        msg = functions.make_str_tuple(msg)
        if debug and self.debug:
            print(msg)
        elif not debug:
            print(msg)

    def send_data(self, sock, data, *args, **kwargs):
        """Новая отправка данных по методу стриминга объекта по сокету"""
        # sender = Sender()
        # sender.client(sock, data)
        with ObjectStream(sock) as stream:
            try:
                stream.put_obj(data)
                stream.put_obj(None)
            except:
                self.show_print('\tОтправка данных...', debug=True)
                return
            # print('client:', stream.get_obj())
            # stream.put_obj({1: 2, 3: 4, 5: 6})
            # print('client:', stream.get_obj())

    def get_data(self,  sock, *args, **kwargs):
        """Получение данных путем стриминга объекта по сокету"""
        # sender = Sender()
        # sender.server(sock, conn)
        while self.run.get_run():
            # c, a = s.accept()
            # print('server: connect from', a)
            with ObjectStream(sock) as stream:
                while True:
                    try:
                        obj = stream.get_obj()
                    except:
                        self.show_print('\tПотеряно соединене при получении данных', debug=True)
                        return b''
                    # print('server:', obj)
                    self.show_print('Got data: {}'.format(obj), debug=True)
                    if obj is None:
                        self.run.set_run(False)
                        # s.close()
                        # return obj
                        break
                    return obj
                    # if isinstance(obj, list):
                    #     reverse lists
                    #     stream.put_obj(obj[::-1])
                    #     return obj
                    # elif isinstance(obj, dict):
                    #     # swap key/value in dictionaries
                    #     stream.put_obj({v: k for k, v in obj.items()})
                    #     print(obj)
                    #     return obj
                    # else:
                    #     # otherwise, echo back same object
                    #     stream.put_obj(obj)
                    #     return obj
            print("Передача закончена")
            # print('server: disconnect from', a)

    def get_password_hash(self, password):
        return functions.get_password_hash(password)


class Running:
    def __init__(self):
        self.run = True

    def get_run(self):
        return self.run

    def set_run(self, val):
        self.run = val


class ObjectStream:

    def __init__(self, sock):
        self.sock = sock
        self.writer = sock.makefile('wb')
        self.reader = sock.makefile('rb')

    # Objects are sent/received as a 4-byte big-endian integer of
    # the pickled object data length, followed by the pickled data.

    def get_obj(self):
        header = self.reader.read(4)
        if not header:
            return None
        length = int.from_bytes(header, 'big')
        return pickle.loads(self.reader.read(length))

    def put_obj(self, obj):
        data = pickle.dumps(obj)
        header = len(data).to_bytes(4, 'big')
        self.writer.write(header)
        self.writer.write(data)
        self.writer.flush()  # important!

    def close(self):
        if self.sock is not None:
            self.writer.close()
            self.reader.close()
            self.sock.close()
            self.sock = None
            self.writer = None
            self.reader = None

    # Support for 'with' to close everything.

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    # Support for no more references to ObjectStream

    def __del__(self):
        self.close()
