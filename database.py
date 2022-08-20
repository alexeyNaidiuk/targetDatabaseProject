import asyncio
import sqlite3
import csv
import config


async def get_index_page():
    databases = {
            'databases': {
                'targets': {
                    'test': {
                        'url': f'http://{config.HOST}:{config.PORT}/dbs/targets/test.db',
                        'available_amount': await amount_of_available_ems('test.db')
                    },
                    'turk': {
                        'url': f'http://{config.HOST}:{config.PORT}/dbs/targets/turk.db',
                        'available_amount': await amount_of_available_ems('turk.db')
                    }
                },
                'proxies': {
                    'wwmix': [],
                    'west_proxy': [],
                    'parsed': []
                },
                'texts': {
                    'turk_with_flame': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  🔥',
                    'turk_text': 'Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!',
                    'ru_spintax': '{Получи|Забери|Используй} 50 {фриспинов|FS|freespins|free spins|spins} за {Регистрацию в клубе|Вход в клуб|Вход в проект|принятие участия в|игру в} Slottica {переходя|перейдя|} по {следующей|этой} ссылке {ниже|} {-|:|} LINK_PUT_HERE {Поспеши|Поторопись|Торопись|Не задерживайся}, время действия {бонуса|приза|подарка} {ограничено|лимитировано}!'
                }
            }
        }
    return databases


async def import_db_from_file(file, db_name):  # todo test
    await create_db(db_name)
    with open(file) as f:
        data = csv.reader(f)
        with sqlite3.connect(db_name) as con:
            cur = con.cursor()
            cur.executemany('insert into emails(email) values(?)', ((i[0] for i in data),))


async def create_db(db_name='test.db'):
    with sqlite3.connect(db_name) as connect:
        cursor = connect.cursor()
        cursor.execute('''
        create table if not exists emails (
        email TEXT not null primary key,
        site  TEXT
        );
        ''')
        cursor.execute('''
        create table if not exists spammed_emails (
        email TEXT,
        site  TEXT
        );
        ''')
        connect.commit()


async def delete_sites_from_emails(db_name):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute('update emails set site = null where site is not null')
        con.commit()


async def archive_emails(db_name):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute('insert into spammed_emails select * from emails;')
        con.commit()


async def select_from_targets(db_name) -> str:
    if await amount_of_available_ems(db_name) == 0:
        await archive_emails(db_name)
        await delete_sites_from_emails(db_name)
    target = await select_from_database_with_limit(db_name)
    await update_column(db_name, {'email': target, 'site': 'busy'})
    return target


async def select_from_database_with_limit(db_name) -> str:
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(f'select email from emails where site is NULL limit 1')
        result = cursor.fetchone()[0]
        return result


async def amount_of_available_ems(db_name) -> int:
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute('select count(email) from emails where site is NULL')
        return cur.fetchone()[0]


async def update_column(db_name, target: dict):
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(f'update emails set site = ? where email = ?', (target['site'], target['email']))
        connection.commit()


async def main():
    await select_from_targets('turk.db')


if __name__ == '__main__':
    asyncio.run(main())
