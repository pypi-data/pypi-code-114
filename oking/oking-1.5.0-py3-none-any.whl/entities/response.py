from typing import List

class CatalogoResponse:
    def __init__(self, Status: int, Message: str, codigo_erp: str = '', protocolo: str = '', loja: str = '') -> None:
        self.codigo_erp = codigo_erp
        self.status = Status
        self.message = Message
        self.protocolo = protocolo
        self.loja = loja


class PriceResponse:
    def __init__(self, codigo_erp, Status: int, Message: str, protocolo: str, loja: str):
        self.codigo_erp = codigo_erp
        self.status = Status
        self.message = Message
        self.protocolo = protocolo


class InvoiceResponse:
    def __init__(self, Status: int, Message: str):
        self.status = Status
        self.message = Message


class TrackingResponse:
    def __init__(self, Status: int, Message: str):
        self.status = Status
        self.message = Message


class StockResponse:
    def __init__(self, Identifiers, Status, Message, Protocolo):
        self.identifiers: List[str] = Identifiers
        self.status: str = Status
        self.message: str = Message
        self.protocol: str = Protocolo
