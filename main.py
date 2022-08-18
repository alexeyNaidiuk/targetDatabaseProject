import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from database import update_column, select_from_targets

PORT = 8000  # todo make as an environmental variable

HOST = '10.107.4.13'  # todo make as an environmental variable
HOST = 'localhost'  # todo make as an environmental variable

app = FastAPI()


class Target(BaseModel):
    email: str
    site: str


@app.get('/')
def root_page():
    return RedirectResponse("/databases")


@app.get('/databases')
async def get_list_of_databases():
    return {
        'databases': {
            'test database url': f'http://{HOST}:{PORT}/databases/test.db',
            # 'targets_available': await get_amount_of_available_ems('test.db')
        }
    }


@app.get('/databases/{db_name}/targets')
async def get_targets(db_name, limit: int = 1):
    if db_name == 'favicon.ico':
        return None
    emails = await select_from_targets(db_name, limit)
    return Response(content='\n'.join(emails))


@app.patch('/databases/{db_name}/targets')
async def update_target(db_name: str, target: Target):
    await update_column(db_name, target)
    return Response(content=f'Updated!')


if __name__ == '__main__':
    uvicorn.run(app='main:app', host=HOST, port=PORT, reload=True)
