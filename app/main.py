import uvicorn
from fastapi import FastAPI, Response

from app.config import HOST, PORT
from app.module import TurkeyTargetFilePool, Target, FilePool, RussianTargetFilePool, WwmixProxyFilePool, \
    WestProxyFilePool, RussianDbrTargetFilePool, CheckedProxyFilePool

app = FastAPI()
turkey_target_pool: FilePool = TurkeyTargetFilePool()
russian_target_pool: FilePool = RussianTargetFilePool()
russian_dbr_target_pool: FilePool = RussianDbrTargetFilePool()
wwmix_proxies: FilePool = WwmixProxyFilePool()
west_proxies: FilePool = WestProxyFilePool()
checked_proxies: FilePool = CheckedProxyFilePool()


@app.get('/')
async def index():
    return {'status': 'ok'}


@app.get('/proxies/wwmix')
async def get_proxies():
    return Response(content='\n'.join(wwmix_proxies.pool))


@app.get('/proxies/checked')
async def get_proxies():
    return Response(content='\n'.join(checked_proxies.pool))


@app.get('/proxies/west')
async def get_proxies():
    return Response(content='\n'.join(west_proxies.pool))


@app.delete('/targets/turkey/remove')
async def delete_target_from_pool(target: Target):
    turkey_target_pool.remove(target.email)
    return Response(content=f'{target.email} deleted from pool')


# @app.post('/targets/turkey/append')
# async def append_target_to_pool(target: Target):
#     turkey_target_pool.append(target.email)
#     if turkey_target_pool.is_in_pool(target.email):
#         return Response(content=f'{target.email} added to pool')
#     else:
#         return Response(content=f'{target.email} is not added in pool')


@app.get('/targets/turkey/clear')
async def append_target_to_pool():
    turkey_target_pool.clear()
    return Response(content=f'target pool cleared')


@app.get('/targets/turkey/random')
async def pop_from_target_pool():
    return Response(content=turkey_target_pool.pop())


@app.get('/targets/turkey/amount')
async def get_random_from_target_pool():
    return Response(content=str(len(turkey_target_pool)))


@app.get('/targets/turkey/reload')
async def get_random_from_target_pool():
    turkey_target_pool.reload()
    amount = len(turkey_target_pool)
    return Response(content=f'reloaded! current amount is {amount}')


@app.post('/targets/alotof/append')
async def append_target_to_pool(target: Target):
    russian_target_pool.append(target.email)
    if russian_target_pool.is_in_pool(target.email):
        return Response(content=f'{target.email} added to pool')
    else:
        return Response(content=f'{target.email} is not added in pool')


@app.get('/targets/alotof/clear')
async def append_target_to_pool():
    russian_target_pool.clear()
    return Response(content=f'target pool cleared')


@app.delete('/targets/alotof/remove')
async def delete_target_from_pool(target: Target):
    russian_target_pool.remove(target.email)
    return Response(content=f'{target.email} deleted from pool')


@app.get('/targets/alotof/random')
async def pop_from_target_pool():
    return Response(content=russian_target_pool.pop())


@app.get('/targets/alotof/amount')
async def get_random_from_target_pool():
    return Response(content=str(len(russian_target_pool)))


@app.get('/targets/alotof/reload')
async def get_random_from_target_pool():
    russian_target_pool.reload()
    amount = len(russian_target_pool)
    return Response(content=f'reloaded! current amount is {amount}')


@app.get('/targets/dbru/clear')
async def append_target_to_pool():
    russian_dbr_target_pool.clear()
    return Response(content=f'target pool cleared')


@app.delete('/targets/dbru/remove')
async def delete_target_from_pool(target: Target):
    russian_dbr_target_pool.remove(target.email)
    return Response(content=f'{target.email} deleted from pool')


@app.get('/targets/dbru/random')
async def pop_from_target_pool():
    return Response(content=russian_dbr_target_pool.pop())


@app.get('/targets/dbru/amount')
async def get_random_from_target_pool():
    return Response(content=str(len(russian_dbr_target_pool)))


@app.get('/targets/dbru/reload')
async def get_random_from_target_pool():
    russian_dbr_target_pool.reload()
    amount = len(russian_dbr_target_pool)
    return Response(content=f'reloaded! current amount is {amount}')


if __name__ == '__main__':
    uvicorn.run('app.main:app', host=HOST, port=int(PORT))
