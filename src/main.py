# Para ejecutar en local el API se debe correr el siguiente comando en la ruta raiz del proyecto
# uvicorn src.main:app --reload

from typing import Union
from fastapi import FastAPI
import requests


app = FastAPI()


@app.get("/")
def root():
    return {"The API is up and running"}

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
@app.get("/get_INE_data")
def get_ine_data():
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
                print(attribute, value) # example usage
            if attribute == "Valor":
                salary_value=value
                print(attribute, value) # example usage
            if year !=0 :
                salary_dictionary[year]=salary_value

        
    return salary_dictionary