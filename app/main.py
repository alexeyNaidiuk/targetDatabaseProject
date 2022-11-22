import uvicorn
from fastapi import FastAPI, Response

from app.config import HOST, PORT
from app.module import Target, TargetsFactory, ProxiesFactory, FilePool

app = FastAPI()


@app.get('/')
async def index():
    return {'status': 'ok'}


@app.get('/targets')
async def get_targets_keys():
    return {key: item.info() for key, item in TargetsFactory.pools.items()}


@app.get('/proxies')
async def get_targets_keys():
    return {key: item.info() for key, item in ProxiesFactory.pools.items()}


@app.get('/targets/{pool}')
async def get_pool(pool: str):
    target_pool: FilePool = TargetsFactory.pools[pool]
    info = target_pool.info()
    value = {pool: info}
    return value


@app.get('/proxies/{pool}/pool')
async def get_proxies(pool: str):
    proxy_pool: FilePool = ProxiesFactory.pools[pool]
    return Response(content='\n'.join(proxy_pool.pool))


@app.delete('/targets/{pool}/remove')
async def delete_target_from_pool(pool: str, target: Target):
    target_pool: FilePool = TargetsFactory.pools[pool]
    target_pool.remove(target.email)
    return Response(content=f'{target.email} deleted from pool')


@app.get('/targets/{pool}/clear')
async def clear_pool(pool: str):
    target_pool: FilePool = TargetsFactory.pools[pool]
    target_pool.clear()
    return Response(content=f'target pool cleared')


@app.get('/targets/{pool}/pop')
async def pop_target_from_pool(pool: str):
    target_pool: FilePool = TargetsFactory.pools[pool]
    value = target_pool.pop()
    return Response(content=value)


@app.get('/targets/{pool}/reload')
async def reload_pool(pool: str):
    target_pool: FilePool = TargetsFactory.pools[pool]
    target_pool.reload()
    amount = len(target_pool)
    return Response(content=f'reloaded! current amount is {amount}')


@app.get('/targets/{pool}/length')
async def get_pool_length(pool: str):
    target_pool: FilePool = TargetsFactory.pools[pool]
    amount = len(target_pool)
    return Response(content=str(amount))


if __name__ == '__main__':
    uvicorn.run('app.main:app', host=HOST, port=int(PORT))
