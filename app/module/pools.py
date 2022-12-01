import abc
import pathlib
from random import shuffle
from typing import NoReturn

from app.config import TARGETS_FOLDER, PROXIES_FOLDER


class Pool(abc.ABC):
    pool: list = []

    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def info(self) -> dict:
        raise NotImplementedError

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
        return value in self.pool

    def __len__(self) -> int:
        return len(self.pool)


class FilePool(Pool):
    path = pathlib.Path()

    def __init__(self):
        if not self.path.exists():
            self.path.write_text('')
        self.reload()

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
        super().reload()
        shuffle(self.pool)


class AlotofTargetFilePool(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'alotof.csv')

    def info(self) -> dict:
        return {'lang': 'russian', 'amount': len(self)}

    def reload(self) -> NoReturn:
        super().reload()
        shuffle(self.pool)


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


class ParsedProxyFilePool(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'parsed.txt')

    def parse_proxies(self):
        ...

    def __init__(self):
        super().__init__()
        self.parse_proxies()

    def info(self) -> dict:
        return {'amount': len(self)}


class VladProxyFilePool(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'vlad.txt')

    def __init__(self):
        super(VladProxyFilePool, self).__init__()
        self.pool = set(self.pool)

    def info(self) -> dict:
        return {'amount': len(self), 'type': 'vlad kypil'}


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
        'checked': CheckedProxyFilePool(),
        # 'parsed': ParsedProxyFilePool(),
        'vlad': VladProxyFilePool()
    }
