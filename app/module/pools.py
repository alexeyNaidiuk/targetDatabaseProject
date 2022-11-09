import abc
import pathlib
from typing import NoReturn

from app.config import TARGETS_FOLDER, PROXIES_FOLDER


class Pool:
    pool: list = []

    def __init__(self):
        self.reload()

    @abc.abstractmethod
    def pop(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self, value: str):
        raise NotImplementedError

    @abc.abstractmethod
    def append(self, value: str) -> NoReturn:
        raise NotImplementedError

    @abc.abstractmethod
    def clear(self) -> NoReturn:
        raise NotImplementedError

    @abc.abstractmethod
    def reload(self) -> NoReturn:
        raise NotImplementedError

    def is_in_pool(self, value: str) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self.pool)


class FilePool(Pool):
    path = None

    def remove(self, value: str):
        self.pool.remove(value)

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


class TurkeyTargetFilePool(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'all_turk.csv')

    def reload(self) -> NoReturn:
        with open(self.path, encoding='latin-1') as file:
            self.pool = file.read().split('\n')


class RussianTargetFilePool(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'alotof.csv')

    def reload(self) -> NoReturn:
        with open(self.path, encoding='latin-1') as file:
            self.pool = file.read().split('\n')


class RussianDbrTargetFilePool(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'dobro_normalized.csv')

    def reload(self) -> NoReturn:
        with open(self.path, encoding='latin-1') as file:
            self.pool = file.read().split('\n')
            self.pool.remove('')


class WwmixProxyFilePool(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'wwmix.txt')


class WestProxyFilePool(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'west_proxy.txt')


class Factory:
    pools = {}

    @classmethod
    def get_pool(cls, factory_name) -> Pool:
        return cls.pools[factory_name]()
