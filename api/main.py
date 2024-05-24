from fastapi import FastAPI

from api.modules.users.routers.user_router import router as user_router
from api.modules.users.routers.auth_router import router as auth_router

app = FastAPI(tittle="Book Trade")

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/users")

@app.get("/")
async def read_root():
    return {"message": "Welcome the Web Book Trade"}

if __name__ == 'main':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)