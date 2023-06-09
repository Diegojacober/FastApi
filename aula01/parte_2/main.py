from fastapi import FastAPI

from routes import curso_router
from routes import user_router

app = FastAPI()

app.include_router(curso_router.router, tags=['cursos'])
app.include_router(user_router.router, tags=['usuarios'])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",host='192.168.0.89', port=8000, log_level="info", reload=True) 