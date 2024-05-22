from fastapi import FastAPI

from api.modules.users.routers.user_router import router as user_router

app = FastAPI(tittle="Book Trade")

app.include_router(user_router, prefix="/users")

@app.get("/")
async def read_root():
    return {"message": "Welcome the Web Book Trade"}

if __name__ == 'main':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)