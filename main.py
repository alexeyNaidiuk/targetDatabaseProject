from typing import Optional

import uvicorn
from fastapi import FastAPI, Response, Body, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from database import update_column, select_from_targets, amount_of_available_ems, get_index_page
import config

app = FastAPI()


class Target(BaseModel):
    email: str
    site: Optional[str] = None


@app.get('/')
def root_page():
    return RedirectResponse("/dbs")


@app.get('/dbs')
async def get_databases():  # todo убрать это куда подальше
    return get_index_page()


@app.get('/link/{geo}')  # todo return shortlink
async def get_link(geo: str):
    return None


@app.post('/link')  # todo return shortlink
async def add_link(body: dict = Body(...)):
    return None


@app.get('/dbs/proxies/{proxy_name}')  # todo next from cycle
async def get_proxy(proxy_name: str):
    return None


@app.get('/dbs/texts/{text_name}')  # todo можно тут его и крутить
async def get_text(text_name: str, spinned: bool = False):
    return None


@app.get('/dbs/targets/{db_name}')
async def get_targets(db_name, limit: int = 1):
    if db_name == 'favicon.ico':
        return None
    emails = await select_from_targets(db_name, limit)
    print(emails)
    return Response(content='\n'.join(emails))


@app.get('/dbs/targets/{db_name}/available')
async def get_targets(db_name: str):
    res = await amount_of_available_ems(db_name)
    return res


@app.put('/dbs/targets/{db_name}')
async def update_target(db_name: str, target: Target):
    await update_column(db_name, target)
    return Response(content=target.json(), status_code=status.HTTP_202_ACCEPTED)


if __name__ == '__main__':
    uvicorn.run(app='main:app', host=config.HOST, port=config.PORT, reload=True)
