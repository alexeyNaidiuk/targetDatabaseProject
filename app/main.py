import uvicorn
from fastapi import FastAPI, Response

from app.config import HOST, PORT
from app.module import FilePool, factories, Factory

app = FastAPI()


@app.get('/')
async def index():
    return {'status': 'ok'}


@app.get('/{factory}')
async def get_factory_keys(factory: str):
    factory_instance: Factory = factories.get(factory)
    if factory_instance:
        return {key: item.info() for key, item in factory_instance.pools.items()}


@app.get('/{factory}/{pool}')
async def get_targets_pool_info(factory: str, pool: str):
    factory_instance: Factory = factories.get(factory)
    if factory_instance:
        target_pool: FilePool = factory_instance.pools[pool]
        info = target_pool.info()
        return info


@app.get('/{factory}/{pool}/pool')
async def get_proxies(factory: str, pool: str):
    factory_instance: Factory = factories.get(factory)
    if factory_instance:
        proxy_pool: FilePool = factory_instance.pools[pool]
        return Response(content='\n'.join(proxy_pool.get_pool()))


@app.get('/{factory}/{pool}/pop')
async def pop_target_from_pool(factory: str, pool: str):
    factory_instance: Factory = factories.get(factory)
    if factory_instance:
        target_pool: FilePool = factory_instance.pools[pool]
        value = target_pool.pop()
        return Response(content=value)


if __name__ == '__main__':
    uvicorn.run('app.main:app', host=HOST, port=int(PORT), reload=True)
