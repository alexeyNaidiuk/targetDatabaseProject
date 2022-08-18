import uvicorn
from fastapi import FastAPI, Response, Body
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
    return RedirectResponse("/dbs")


@app.get('/dbs')
async def get_list_of_databases():  # todo убрать это куда подальше
    return {
        'databases': {
            'targets': {
                'test': f'http://{HOST}:{PORT}/dbs/targets/test.db',
                'turk': f'http://{HOST}:{PORT}/dbs/targets/turk.db',
            },
            'proxies': {
                'wwmix': [],
                'west_proxy': [],
                'parsed': []
            },
            'texts': {
                'turk_with_flame': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!',
                'turk_text': 'Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!',
                'ru_spintax': '{Получи|Забери|Используй} 50 {фриспинов|FS|freespins|free spins|spins} за {Регистрацию в клубе|Вход в клуб|Вход в проект|принятие участия в|игру в} Slottica {переходя|перейдя|} по {следующей|этой} ссылке {ниже|} {-|:|} LINK_PUT_HERE {Поспеши|Поторопись|Торопись|Не задерживайся}, время действия {бонуса|приза|подарка} {ограничено|лимитировано}!'
            }
        }
    }


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
    return Response(content='\n'.join(emails))


@app.patch('/dbs/targets/{db_name}', status_code=201)
async def update_target(db_name: str, target: Target):
    await update_column(db_name, target)
    return Response(content=f'Updated!')


if __name__ == '__main__':
    uvicorn.run(app='main:app', host=HOST, port=PORT, reload=True)
