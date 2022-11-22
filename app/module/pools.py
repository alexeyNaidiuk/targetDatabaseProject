import abc
import pathlib
from random import shuffle
from typing import NoReturn

from app.config import TARGETS_FOLDER, PROXIES_FOLDER


class Pool:
    pool: list = []

    def __init__(self):
        self.reload()

    def info(self) -> dict:
        return {'amount': len(self)}

    @abc.abstractmethod
    def pop(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self, value: str):
        raise NotImplementedError

    # @abc.abstractmethod
    # def append(self, value: str) -> NoReturn:
    #     raise NotImplementedError

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

    def reload(self) -> NoReturn:
        with open(self.path, encoding='latin-1') as file:
            self.pool = file.read().split('\n')
            if '' in self.pool:
                self.pool.remove('')

    def pop(self) -> str:
        if len(self.pool) == 0:
            self.reload()
        value = self.pool.pop()
        return value

    def clear(self) -> None:
        self.pool.clear()


class TurkeyTargetFilePool(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'all_turk.csv')

    def info(self) -> dict:
        return {'lang': 'turkey', 'amount': len(self)}


class MixRuTargetFilePool(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'test_mixedru.csv')

    def info(self) -> dict:
        return {'lang': 'russian', 'amount': len(self)}

    def reload(self) -> NoReturn:
        with open(self.path, encoding='latin-1') as file:
            self.pool = file.read().split('\n')
            shuffle(self.pool)
            if '' in self.pool:
                self.pool.remove('')


class AlotofTargetFilePool(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'alotof.csv')

    def info(self) -> dict:
        return {'lang': 'russian', 'amount': len(self)}

    def reload(self) -> NoReturn:
        with open(self.path, encoding='latin-1') as file:
            self.pool = file.read().split('\n')
            shuffle(self.pool)
            if '' in self.pool:
                self.pool.remove('')


class RussianDbrTargetFilePool(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'dobro_normalized.csv')

    def info(self) -> dict:
        return {'lang': 'russian', 'amount': len(self)}


class Rub36TargetFilePool(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'rub36.csv')

    def info(self) -> dict:
        return {'lang': 'russian', 'amount': len(self)}


class WwmixProxyFilePool(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'wwmix.txt')

    def info(self) -> dict:
        return {'type': 'http', 'amount': len(self)}


class WestProxyFilePool(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'west_proxy.txt')

    def info(self) -> dict:
        return {'type': 'http', 'amount': len(self)}


class CheckedProxyFilePool(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'checked.txt')

    def info(self) -> dict:
        return {'type': 'http', 'amount': len(self)}


class TargetsFactory:
    pools = {
        'turkey': TurkeyTargetFilePool(),
        'alotof': AlotofTargetFilePool(),
        'dbru': RussianDbrTargetFilePool(),
        'mixru': MixRuTargetFilePool(),
        'rub36': Rub36TargetFilePool()
    }


class ProxiesFactory:
    pools = {
        'wwmix': WwmixProxyFilePool(),
        'west': WestProxyFilePool(),
        'checked': CheckedProxyFilePool()
    }
