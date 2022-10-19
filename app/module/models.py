from pydantic import BaseModel


class Target(BaseModel):
    email: str
