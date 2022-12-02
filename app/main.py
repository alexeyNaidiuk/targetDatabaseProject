import uvicorn
from fastapi import FastAPI, Response

from app.config import HOST, PORT
from app.module import FilePool, factories

app = FastAPI()


@app.get('/')
async def root():
    return {'status': 'ok'}


@app.get('/{factory}')
async def get_factories(factory: str):
    factory_instance = factories.get(factory)
    if factory_instance:
        return {key: item.info() for key, item in factory_instance.items()}


@app.get('/{factory}/{pool}')
async def get_factory_pools(factory: str, pool: str):
    factory_instance = factories.get(factory)
    if factory_instance:
        target_pool: FilePool = factory_instance[pool]
        info = target_pool.info()
        return info


@app.get('/{factory}/{pool}/pool')
async def get_pool_list(factory: str, pool: str):
    factory_instance = factories.get(factory)
    if factory_instance:
        proxy_pool: FilePool = factory_instance[pool]
        return Response(content='\n'.join(proxy_pool.get_pool()))


@app.get('/{factory}/{pool}/pop')
async def pop_from_pool(factory: str, pool: str):
    factory_instance = factories.get(factory)
    if factory_instance:
        target_pool: FilePool = factory_instance[pool]
        value = target_pool.pop()
        return Response(content=value)


@app.get('/{factory}/{pool}/clear')
async def clear_pool(factory: str, pool: str):
    factory_instance = factories.get(factory)
    if factory_instance:
        target_pool: FilePool = factory_instance[pool]
        target_pool.clear()
        return target_pool.info()


@app.get('/{factory}/{pool}/reload')
async def reload_pool(factory: str, pool: str):
    factory_instance = factories.get(factory)
    if factory_instance:
        target_pool: FilePool = factory_instance[pool]
        target_pool.reload()
        return target_pool.info()


if __name__ == '__main__':
    uvicorn.run('app.main:app', host=HOST, port=int(PORT), reload=True)
