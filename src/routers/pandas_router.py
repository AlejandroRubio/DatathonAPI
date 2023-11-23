from fastapi import APIRouter
from fastapi.responses import FileResponse

#Liberías peticiones HTTP
import requests

#Librerías cálculo de tendecias 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

router = APIRouter()

from enum import Enum

# class syntax
class DatesetType(Enum):
    empleados = "empleados"
    parados = "parados"
    

@router.get("/apply_correlation_matrix", tags=["Funciones panda"])
def apply_correlation_matrix(dataset: DatesetType):
    
    data =  pd.read_csv ('/mnt/c/Labs/datathon_api/data/dataset_empleados.csv', encoding = "ISO-8859-1")
    if dataset==DatesetType.parados:
        data =  pd.read_csv ('/mnt/c/Labs/datathon_api/data/dataset_desempleados.csv', encoding = "ISO-8859-1")
    
    for col in data.columns:
        print(col)
        
    #corr = pd.corr()
    #sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels = corr.columns.values, cmap='RdYlGm')
    
    corr=data.corr()
    svm = sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels = corr.columns.values, cmap='RdYlGn')
    
    figure = svm.get_figure()   

    outfile_name='heatmap_empleados.png'
    if dataset==DatesetType.parados:
        outfile_name='heatmap_desempleados.png'
    
    figure.savefig(outfile_name, bbox_inches="tight")
    return FileResponse(outfile_name)
    