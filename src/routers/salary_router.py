from fastapi import APIRouter

#Liberías peticiones HTTP
import requests

#Librerías cálculo de tendecias 
import numpy as np
from sklearn.linear_model import LinearRegression #scikit-learn'

router = APIRouter()


def get_salary_data():
    ine_url="https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/28191?tip=AM&"
    response = requests.get(ine_url)
    #print(response.text)
    first_data_tag=response.json()[0]['Data']
    #print(first_data_tag)
    
    salary_dictionary={}
    
    for anualized_data in first_data_tag:
        year=0
        salary_value=0
        for attribute, value in anualized_data.items():
            if attribute == "Anyo":
                year=value
                print(attribute, value) 
            if attribute == "Valor":
                salary_value=value
                print(attribute, value) 
            if year !=0 :
                salary_dictionary[year]=salary_value
                
    return salary_dictionary
    
    
# Filtra los datos del JSON que nos da el INE
# La salida del método da algo como esto:
#    {
#      "2008": 21883.42,
#      "2009": 22511.47,
#      "2010": 22790.2,
#      "2011": 22899.35,
#      "2012": 22726.44,
#      "2013": 22697.86,
#      "2014": 22858.17,
#      "2015": 23106.3,
#      "2016": 23156.34,
#      "2017": 23646.5,
#      "2018": 24009.12,
#      "2019": 24395.98,
#      "2020": 25165.51,
#      "2021": 25896.82
#    }
@router.get("/get_INE_data", tags=["Datos salariales"])
def get_ine_salary_data_default():
    salary_dictionary=get_salary_data()   
    return salary_dictionary
    

# Añade al endpoint anterior el cálculo de años futuros por regresión lineal
@router.get("/get_INE_data_future", tags=["Datos salariales"])
def get_ine_salary_data_plus_future_data():
    salary_dictionary=get_salary_data()   
     
    #años = np.array([2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008])
    #valores = np.array([25896.82, 25165.51, 24395.98, 24009.12, 23646.50, 23156.34, 23106.30, 22858.17, 22697.86, 22726.44, 22899.35, 22790.20, 22511.47, 21883.42])
    años = np.fromiter(salary_dictionary.keys(), dtype=int)
    valores = np.fromiter(salary_dictionary.values(), dtype=float)
    
    # Ajuste de la regresión lineal
    modelo = LinearRegression().fit(años.reshape(-1, 1), valores)
    
    # Predicciones para los próximos años
    años_futuros = np.array([2022, 2023, 2024, 2025])  # Puedes ajustar estos años según tus necesidades
    predicciones = modelo.predict(años_futuros.reshape(-1, 1))
    
    # Imprimir resultados
    for año, prediccion in zip(años_futuros, predicciones):
        print(f'Año {año}: {prediccion:.2f}')
        salary_dictionary[str(año)]=round(float(prediccion),2)
    
    return salary_dictionary  