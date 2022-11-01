import uvicorn
from fastapi import FastAPI, Response

from app.config import HOST, PORT
from app.module import TurkeyTargetFilePool, Target, FilePool, RussianTargetFilePool, WwmixProxyFilePool

app = FastAPI()
turkey_target_pool: FilePool = TurkeyTargetFilePool()
russian_target_pool: FilePool = RussianTargetFilePool()
wwmix_proxies: FilePool = WwmixProxyFilePool()


@app.get('/')
async def index():
    return {'status': 'ok'}


@app.get('/proxies/wwmix/')
async def get_proxies():
    return Response(content='\n'.join(wwmix_proxies.pool))


@app.delete('/targets/turkey/remove')
async def delete_target_from_pool(target: Target):
    turkey_target_pool.remove(target.email)
    return Response(content=f'{target.email} deleted from pool')


@app.post('/targets/turkey/append')
async def append_target_to_pool(target: Target):
    turkey_target_pool.append(target.email)
    if turkey_target_pool.is_in_pool(target.email):
        return Response(content=f'{target.email} added to pool')
    else:
        return Response(content=f'{target.email} is not added in pool')


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


@app.delete('/targets/russian/remove')
async def delete_target_from_pool(target: Target):
    russian_target_pool.remove(target.email)
    return Response(content=f'{target.email} deleted from pool')


# @app.post('/targets/russian/append')
# async def append_target_to_pool(target: Target):
#     russian_target_pool.append(target.email)
#     if russian_target_pool.is_in_pool(target.email):
#         return Response(content=f'{target.email} added to pool')
#     else:
#         return Response(content=f'{target.email} is not added in pool')


@app.get('/targets/russian/clear')
async def append_target_to_pool():
    russian_target_pool.clear()
    return Response(content=f'target pool cleared')


@app.get('/targets/russian/random')
async def pop_from_target_pool():
    return Response(content=russian_target_pool.pop())


@app.get('/targets/russian/amount')
async def get_random_from_target_pool():
    return Response(content=str(len(russian_target_pool)))


@app.get('/targets/russian/reload')
async def get_random_from_target_pool():
    russian_target_pool.reload()
    amount = len(russian_target_pool)
    return Response(content=f'reloaded! current amount is {amount}')


if __name__ == '__main__':
    uvicorn.run('app.main:app', host=HOST, port=int(PORT))
