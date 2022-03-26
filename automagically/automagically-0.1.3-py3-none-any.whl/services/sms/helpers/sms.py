class Sms:
    def __init__(self, number: str, message: str) -> None:
        self.to_phone = number
        self.message_body = message

    def get(self) -> dict:
        return {
            "to_phone": self.to_phone,
            "message_body": self.message_body,
        }
