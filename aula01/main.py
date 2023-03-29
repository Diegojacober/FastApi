from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return {"msg": "FastApi primeiro contato"}

@app.get('/msg')
async def mensagem():
    return {"msg": "Enviando uma mensagem"}

#rodar uvicorn nomedoarquivo:instancia
#uvicorn main:app --reload

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run("main:app",host='127.0.0.1', port=8000, log_level="info", reload=True) # assim somente seu computador acessa
    uvicorn.run("main:app",host='0.0.0.0', port=8000, log_level="info", reload=True) # assim todos os computadores na rede podem acessar
    #em produção é utilizado o gunicorn
    #gunicorn main:app -w 4 (quantidade de servidores) -k (alto desempenho) uvicorn.workers.UvicornWorker(classes)
    
    