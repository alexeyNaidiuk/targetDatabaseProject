from typing import NoReturn
from pydantic import BaseModel


class Target(BaseModel):
    email: str


class Pool:
    pool: list = []
    path = None

    def __init__(self) -> NoReturn:
        self.reload()

    def reload(self) -> NoReturn:
        with open(self.path) as file:
            self.pool = list(set(file.read().split('\n')))

    def pop(self) -> str:
        if len(self.pool) == 0:
            self.reload()
        value = self.pool.pop()
        return value

    def __len__(self):
        return len(self.pool)

    def __iter__(self):
        return self.pool


class TargetPool(Pool):

    def append(self, target) -> NoReturn:
        self.pool.append(target)

    def clear(self):
        self.pool.clear()


class TurkeyTargetPool(TargetPool):
    path = 'all_turk.csv'
