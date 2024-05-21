from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api.shared.database.dependencies import get_session


app = FastAPI(tittle="Book Trade")

@app.get("/")
async def read_root(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select("SELECT 'Hello, World!' AS message"))
    message = result.scalar_one()
    return {"message": message}

if __name__ == 'main':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)