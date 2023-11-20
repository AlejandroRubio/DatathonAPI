from fastapi import APIRouter
from fastapi.responses import FileResponse

#Liberías peticiones HTTP
import requests

#Librerías cálculo de tendecias 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

router = APIRouter()


@router.get("/apply_correlation_matrix", tags=["Funciones panda"])
def apply_correlation_matrix():
    data =  pd.read_csv ('/mnt/c/Labs/datathon_api/data/dataset.csv', encoding = "ISO-8859-1")
    for col in data.columns:
        print(col)
        
    #corr = pd.corr()
    #sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels = corr.columns.values, cmap='RdYlGm')
    
    corr=data.corr()
    svm = sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels = corr.columns.values, cmap='RdYlGn')
    
    figure = svm.get_figure()    
    figure.savefig('heatmap.png', bbox_inches="tight")
    return FileResponse('heatmap.png')
    