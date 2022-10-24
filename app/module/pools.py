from typing import NoReturn

from app.config import TARGETS_FOLDER, PROXIES_FOLDER


class Pool:
    pool: list = []

    def pop(self) -> str:
        ...

    def append(self, value) -> None:
        ...

    def clear(self) -> None:
        ...

    def reload(self) -> None:
        ...

    def __len__(self) -> int:
        ...


class FilePool(Pool):
    path = None

    def __init__(self) -> NoReturn:
        self.reload()

    def append(self, value) -> None:
        self.pool.append(value)

    def reload(self) -> NoReturn:
        with open(self.path) as file:
            self.pool = file.read().split('\n')

    def pop(self) -> str:
        if len(self.pool) == 0:
            self.reload()
        value = self.pool.pop()
        return value

    def clear(self) -> None:
        self.pool.clear()

    def __len__(self):
        return len(self.pool)


class TurkeyTargetFilePool(FilePool):
    path = f'{TARGETS_FOLDER}/all_turk.csv'


class WwmixProxyFilePool(FilePool):
    path = f'{PROXIES_FOLDER}/wwmix.txt'


class Factory:
    pools = {}

    @classmethod
    def get_pool(cls, factory_name) -> Pool:
        return cls.pools[factory_name]()
