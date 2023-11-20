# Para ejecutar en local el API se debe correr el siguiente comando en la ruta raiz del proyecto
# uvicorn src.main:app --reload

#Liberías base FastAPI
from fastapi import FastAPI


from src.routers import default_router, salary_router, industry_router, pandas_router


#Inicialización FastAPI
app = FastAPI()
app.include_router(default_router.router)
app.include_router(salary_router.router)
app.include_router(industry_router.router)
app.include_router(pandas_router.router)