from pydantic import BaseModel


class BotUser(BaseModel):
    user_id: str
    name: str
