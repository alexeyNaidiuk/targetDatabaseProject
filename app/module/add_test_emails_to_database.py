from pathlib import Path

from app.config import TARGETS_FOLDER


def get_database(path: Path | str):
    with open(path, encoding='latin-1') as f:
        return f.read().split('\n')


def save_database(path: Path | str, list_to_save: list):
    with open(path, 'w', encoding='latin-1') as f:
        f.write('\n'.join(list_to_save))


def main():
    file_name = 'rub36'
    suffix = 'rub36'
    original_list = get_database(Path(TARGETS_FOLDER, f'{file_name}.csv'))
    step = 500
    cc = step
    c = 1
    while cc < len(original_list):
        original_list.insert(cc, f'softumwork+{suffix}{c}@gmail.com')
        cc += step
        c += 1
    save_database(Path(TARGETS_FOLDER, f'test_{file_name}.csv'), original_list)


if __name__ == '__main__':
    main()
