from pathlib import Path

from app.config import TARGETS_FOLDER


def get_database(path: Path | str):
    with open(path) as f:
        return f.read().split('\n')


def save_database(path: Path | str, list_to_save: list):
    with open(path, 'w') as f:
        f.write('\n'.join(list_to_save))


def main():
    suffix = 'dadru'
    original_list = get_database(Path(TARGETS_FOLDER, f'{suffix}.csv'))
    step = 362
    c = 1
    while step <= len(original_list):
        original_list.insert(step, f'softumwork+{suffix}{c}@gmail.com')
        step += step
        c += 1
    save_database(Path(TARGETS_FOLDER, f'test_{suffix}.csv'), original_list)


if __name__ == '__main__':
    main()
