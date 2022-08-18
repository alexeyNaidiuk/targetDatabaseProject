import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

from database import select_from_database_with_limit, update_column, get_amount_of_available_ems

PORT = 8000

HOST = '10.107.4.13'

app = FastAPI()


@app.get('/')
def root_page():
    return RedirectResponse("/listofdatabases")


@app.get('/listofdatabases')
async def get_list_of_databases():
    return {
        'targets': {
            'test': f'http://{HOST}:{PORT}/targets/test',
            'available_emails': await get_amount_of_available_ems('test.db')
        }
    }


@app.get('/targets/{db_name}')
async def get_from_targets_db(db_name, limit=1):
    if db_name == 'favicon.ico':
        return None
    ems = await get_amount_of_available_ems(db_name+'.db')
    if ems == 0:
        return None
    emails = await select_from_database_with_limit(db_name + '.db', limit)
    return Response(content='\n'.join(emails))


@app.put('/targets/{db_name}')
async def update_targets_row(db_name, target: dict):
    await update_column(db_name + '.db', target)
    return Response(content=f'Updated!')


if __name__ == '__main__':
    uvicorn.run(app='main:app', host=HOST, port=PORT, reload=True)
