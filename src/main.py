# Para ejecutar en local el API se debe correr el siguiente comando en la ruta raiz del proyecto
# uvicorn src.main:app --reload

#Liberías base FastAPI
from fastapi import FastAPI


from src.routers import default_router, salary_router, industry_router, pandas_router


#Inicialización FastAPI
app = FastAPI(
    title="Datathon CID API",
    description="API desarrollada para la extracción de datos del INE y su procesamiento",
    version="0.0.1",
    contact={
        "name": "DataMasters Team - GDG Datathon 2023",
        "url": "http://x-force.example.com/contact/",
        "email": "alejandro.rubio@web.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(default_router.router)
app.include_router(salary_router.router)
app.include_router(industry_router.router)
app.include_router(pandas_router.router)