import asyncio
import sqlite3


async def create_db(db_name='test.db'):
    with sqlite3.connect(db_name) as connect:
        cursor = connect.cursor()
        cursor.execute('''
        create table emails (
        email TEXT not null primary key,
        site  TEXT
        );
        ''')
        connect.commit()


async def select_from_database_with_limit(db_name, limit) -> list:
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(f'select email from emails where site is NULL limit {limit}')
        if int(limit) == 1:
            result = cursor.fetchone()
        else:
            result = [i[0] for i in cursor.fetchall()]
        return result


async def get_amount_of_available_ems(db_name):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute('select * from empty_emails')
        return cur.fetchone()[0]


async def update_column(db_name, target):
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(f'update emails set site = ? where email = ?', (target['site'], target["email"]))
        connection.commit()


async def main():
    amount = await get_amount_of_available_ems('test.db')
    print(amount)


if __name__ == '__main__':
    asyncio.run(main())
