import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Response

from data import TurkeyTargetPool, Target

load_dotenv()
app = FastAPI()
target_pool = TurkeyTargetPool()


@app.get('/')
async def root():
    return {'status': 'ok'}


@app.post('/targets/turkey/append')
async def append_target_to_pool(target: Target):
    target_pool.append(target.email)
    return Response(content=f'{target.email} added to pool')


@app.get('/targets/turkey/clear')
async def append_target_to_pool():
    target_pool.clear()
    return Response(content=f'target pool cleared')


@app.get('/targets/turkey/random')
async def pop_from_target_pool():
    value = target_pool.pop()
    return Response(content=value)


@app.get('/targets/turkey/amount')
async def get_random_from_target_pool():
    value = len(target_pool)
    return Response(content=str(value))


@app.get('/targets/turkey/reload')
async def get_random_from_target_pool():
    target_pool.reload()
    amount = len(target_pool)
    return Response(content=f'reloaded! current amount is {amount}')


if __name__ == '__main__':
    uvicorn.run('main:app', host=os.environ['HOST'], port=int(os.environ['PORT']))
