from fastapi import APIRouter

#Liberías peticiones HTTP
import requests

#Librerías cálculo de tendecias 
import numpy as np
from sklearn.linear_model import LinearRegression #scikit-learn'

router = APIRouter()


def get_industry_data():
    ine_url="https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/58649?tip=AM&"
    response = requests.get(ine_url)
    #print(response.text)
    first_data_tag=response.json()[0]['Data']
    #print(first_data_tag)
    
    salary_dictionary={}
    
    for anualized_data in first_data_tag:
        year=0
        industry_data=0
        for attribute, value in anualized_data.items():
            if attribute == "NombrePeriodo":
                year=value
                print(attribute, value) 
            if attribute == "Valor":
                industry_data=value
                print(attribute, value) 
            if year !=0 :
                salary_dictionary[year]=industry_data
                
    return salary_dictionary
    
    

@router.get("/get_INE_industry_data", tags=["Datos industriales"])
def get_ine_industry_data_default():
    industry_dictionary=get_industry_data()   
    return industry_dictionary
    


# Añade al endpoint anterior el cálculo de años futuros por regresión lineal
@router.get("/get_INE_industry_data_future", tags=["Datos industriales"])
def get_ine_industry_data_future():
    salary_dictionary=get_industry_data()   
     
    años = np.fromiter(salary_dictionary.keys(), dtype=int)
    valores = np.fromiter(salary_dictionary.values(), dtype=float)
    
    # Ajuste de la regresión lineal
    modelo = LinearRegression().fit(años.reshape(-1, 1), valores)
    
    # Predicciones para los próximos años
    años_futuros = np.array([2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030])  # Puedes ajustar estos años según tus necesidades
    predicciones = modelo.predict(años_futuros.reshape(-1, 1))
    
    # Imprimir resultados
    for año, prediccion in zip(años_futuros, predicciones):
        print(f'Año {año}: {prediccion:.2f}')
        salary_dictionary[str(año)]=round(float(prediccion),2)
    
    return salary_dictionary  