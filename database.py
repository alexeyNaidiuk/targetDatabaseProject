import asyncio
import sqlite3


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


async def select_from_targets(db_name, limit) -> list:
    if await amount_of_available_ems(db_name) == 0:
        await archive_emails(db_name)
        await delete_sites_from_emails(db_name)
    return await select_from_database_with_limit(db_name, limit)


async def select_from_database_with_limit(db_name, limit) -> list:
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(f'select email from emails where site is NULL limit ?', (limit,))
        if int(limit) == 1:
            result = cursor.fetchone()
        else:
            result = [i[0] for i in cursor.fetchall()]
        return result


async def amount_of_available_ems(db_name):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute('select count(email) from emails where site is NULL')
        return cur.fetchone()[0]


async def update_column(db_name, target):
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(f'update emails set site = ? where email = ?', (target.site, target.email))
        connection.commit()


async def main():
    await create_db('turk.db')


if __name__ == '__main__':
    asyncio.run(main())
