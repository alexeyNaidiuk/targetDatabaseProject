import uvicorn
from fastapi import FastAPI, Response, Body, status
from fastapi.responses import RedirectResponse

import config
from database import update_column, select_from_targets, amount_of_available_ems, get_index_page, \
    west_proxies
from models import Target

app = FastAPI()


@app.get('/')
def root_page():
    return RedirectResponse("/dbs")


@app.get('/dbs')
async def get_databases():
    return await get_index_page()


# @app.get('/link/{geo}')  # todo return shortlink
# async def get_link(geo: str):
#     return None


# @app.post('/link')  # todo return shortlink
# async def add_link(body: dict = Body(...)):
#     return None


# @app.get('/dbs/proxies/west_proxy')  # todo next from cycle
# async def get_west_proxy():
#     proxy = next(west_proxies)
#     return Response(content=proxy)


# @app.get('/dbs/texts/{text_name}')  # todo можно тут его и крутить
# async def get_text(text_name: str, spinned: bool = False):
#     return None


@app.get('/dbs/targets/{db_name}')
async def get_target(db_name, site: str = 'busy'):
    if db_name == 'favicon.ico':
        return None
    target = await select_from_targets(db_name)
    await update_column(db_name, {'email': target, 'site': site})
    return Response(content=target)


@app.get('/dbs/targets/{db_name}/available')
async def get_targets_amount(db_name: str):
    res = await amount_of_available_ems(db_name)
    return res


@app.put('/dbs/targets/{db_name}')
async def update_target(db_name: str, target: Target):
    await update_column(db_name, target.dict())
    return Response(content=target.json(), status_code=status.HTTP_202_ACCEPTED)


if __name__ == '__main__':
    uvicorn.run(app='main:app', host=config.HOST, port=config.PORT)
