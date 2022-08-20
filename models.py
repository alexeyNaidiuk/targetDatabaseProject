from typing import Optional

from pydantic.main import BaseModel


class Target(BaseModel):
    email: str
    site: Optional[str] = None
