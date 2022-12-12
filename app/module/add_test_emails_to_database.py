from pathlib import Path


def get_database(path: Path | str):
    with open(path) as f:
        return f.read().split('\n')


def save_database(path: Path | str, list_to_save: list):
    with open(path, 'w') as f:
        f.write('\n'.join(list_to_save))


def main():
    original_list = get_database(Path(r'C:\Users\Administrator\Desktop\targetDatabaseProject\targets\dadru.csv'))

    suffix = 'dadru'
    step = 362
    c = 1
    while step <= len(original_list):
        original_list.insert(step, f'softumwork+{suffix}{c}@gmail.com')
        step += step
        c += 1

    save_database(r'C:\Users\Administrator\Desktop\targetDatabaseProject\targets\test_dadru.csv', original_list)
    print('softumwork+dadru1@gmail.com' in original_list)


if __name__ == '__main__':
    main()
