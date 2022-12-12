import abc
import pathlib
from random import shuffle
from typing import NoReturn

from app.config import TARGETS_FOLDER, PROXIES_FOLDER


class Pool(abc.ABC):
    pool: list = []

    def get_pool(self) -> list:
        return self.pool

    @abc.abstractmethod
    def pop(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def info(self) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self.pool)

    @abc.abstractmethod
    def clear(self) -> NoReturn:
        raise NotImplementedError

    @abc.abstractmethod
    def reload(self) -> NoReturn:
        raise NotImplementedError


class FilePool(Pool):
    path = pathlib.Path()

    def pop(self) -> str:
        if len(self.pool) == 0:
            self.reload()
        value = self.pool.pop()
        return value

    def __init__(self):
        if not self.path.exists():
            self.path.write_text('')
        self.reload()

    def reload(self) -> NoReturn:
        with open(self.path, encoding='latin-1') as file:
            self.pool = file.read().split('\n')
            if '' in self.pool:
                self.pool.remove('')

    def clear(self) -> None:
        self.pool.clear()


class TurkeyTarget(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'all_turk.csv')

    def info(self) -> dict:
        return {'lang': 'turkey', 'amount': len(self)}


class DadruTargets(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'test_dadru.csv')

    def info(self) -> dict:
        return {'lang': 'ru', 'amount': len(self)}

    def reload(self) -> NoReturn:
        super().reload()
        shuffle(self.pool)


class MixRuTargets(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'test_mixedru.csv')

    def info(self) -> dict:
        return {'lang': 'russian', 'amount': len(self)}

    def reload(self) -> NoReturn:
        super().reload()
        shuffle(self.pool)


class AlotofTargets(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'alotof.csv')

    def info(self) -> dict:
        return {'lang': 'russian', 'amount': len(self)}

    def reload(self) -> NoReturn:
        super().reload()
        shuffle(self.pool)


class DbrTargets(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'dobro_normalized.csv')

    def info(self) -> dict:
        return {'lang': 'russian', 'amount': len(self)}


class Rub36Targets(FilePool):
    path = pathlib.Path(TARGETS_FOLDER, 'rub36.csv')

    def info(self) -> dict:
        return {'lang': 'russian', 'amount': len(self)}


class WwmixProxy(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'wwmix.txt')

    def info(self) -> dict:
        return {'type': 'http', 'amount': len(self)}


class WestProxy(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'west_proxy.txt')

    def info(self) -> dict:
        return {'type': 'http', 'amount': len(self)}


class VladProxy(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'vlad.txt')

    def info(self) -> dict:
        return {'amount': len(self), 'type': 'vlad kypil'}


class ParsedProxy(FilePool):
    path = pathlib.Path(PROXIES_FOLDER, 'parsed.txt')

    def get_pool(self) -> list:
        self.reload()
        return self.pool

    def info(self) -> dict:
        return {'amount': len(self), 'type': 'parsed'}


factories = {
    'targets': {
        'turkey': TurkeyTarget(),
        'alotof': AlotofTargets(),
        'dbru': DbrTargets(),
        'mixru': MixRuTargets(),
        'dadru': DadruTargets(),
        'rub36': Rub36Targets()
    },
    'proxies': {
        'wwmix': WwmixProxy(),
        'west': WestProxy(),
        'parsed': ParsedProxy(),
        'vlad': VladProxy(),
    }
}
