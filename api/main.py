import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import FastAPI, status

from api.routers.user_router import router as user_router
from api.routers.auth_router import router as auth_router

app = FastAPI(title="Web Book Trade")

app.include_router(user_router, prefix='/users')
app.include_router(auth_router, prefix='/auth')


@app.get("/", status_code=status.HTTP_200_OK, summary=['main'])
async def main_root():
    return {'message': "Welcome the Web Book Trade"}

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)