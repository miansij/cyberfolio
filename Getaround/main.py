## décommentez la 2ème ligne si vous n'êtes pas sur colab ou commentez la si vous êtes sur collab
colab = True
colab = False

## détermination du path
mypath = ''
if colab:
    from sys import path
    from google.colab import drive
    drive.mount('/content/drive')
    path.insert(0,'/content/drive/MyDrive/Getaround/')
    mypath = path[0]
mypath
#! pip install uvicorn
#! pip install joblib
#! pip install fastapi

import pandas as pd
import numpy as np
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import dump, load
import pickle
from typing import Union

description="You are reading the documentation of getaround API. This web page is to give you the prediction price of the input you will give to it. The response is in a json format."
tags_metadata = [
    {"name": " predict",
        "description": """This endpoint accepts POST method for getting predicted prices.\n* Input required:with JSON input data, for exemple:\n* {"model_key":"Citroën","mileage":13929,"engine_power":320,"fuel":"petrol","paint_color":"red","car_type": "convertible",\
"private_parking_available":True,"has_gps":False,"has_air_conditioning":True,"automatic_car":True,"has_getaround_connect":True,"has_speed_regulator":True,"winter_tires":False}.\n* Or a tuple or a list, for exemple:\n* "Citroën",13929,320,"petrol","red","convertible"True,False,True,True,True,True,False\n* Output:The response should be a JSON with one key prediction corresponding to the prediction; for exemple\n* {"prediction":[158,6]}",\n """
    },
    {"name":"compare",
     "description":"You can compare the difference between a price predict and its real value. You have to give an integer query parameter to the endpoint, and you'll get the values for the row (in the dataset) whose index equals the query parameter you gave. It should look like '127.0.0.1:7000/compare/int', where int is the query parameter you gave"
        
    }
]

getaround = FastAPI(title="GETAROUND PRICE PREDICTION API", description=description, version="0.1",openapi_tags=tags_metadata) #, contact={"name": "Ndangani","url": "https:127.0.0.1:7000",})

target_var = 'rental_price_per_day'

## function to prepare data ( from a dict, a the list, or a tuple) as input for a prediction
def func_prepare_iterable(iterable):
    df_cleaned_csv = pd.read_csv('src/get_around_pricing_project_cleaned.csv')
    columns = df_cleaned_csv.drop(target_var,axis=1).columns
    my_iterable = []
    try:
        if type(iterable) == dict:
            my_iterable = list(iterable.values())
        else:
            my_iterable = list(iterable)
    except:
        return "incorrect input"
    else:
        return pd.DataFrame(pd.DataFrame(my_iterable).T.values,columns=columns)

## function to get a prediction
def func_price_pred(iterable,model,preprocessor):
    res=func_prepare_iterable(iterable)
    if type(res)==str:
        return 
    else:
        res = preprocessor.transform(res)
        res = model.predict(res).round(3)
        return res.tolist()
    
def func_preprocessor():
    with open(f'{mypath}src/preprocessor.pkl','rb') as file:
        return load(file)

def func_model():
    with open(f'{mypath}src/predictions.pkl','rb') as file:
        return load(file)
        
@getaround.get("/")
async def root():
    return {"message":"Welcome to the getaround API. for more information go to http://127.0.0.1:7000/docs"}
  
@getaround.get("/compare/{number}",tags=["compare"])
async def compare(number:int):
    """This endpoint gives you the predict price versus the real price of a row in the dataset."""
    preprocessor=func_preprocessor()
    model=func_model()
    X = pd.read_csv("src/get_around_pricing_project_cleaned.csv")
    Y=X.loc[number,[target_var]].to_dict()
    X.drop(target_var,axis=1,inplace=True)
    iterable=X.loc[number,:]
    pred=func_price_pred(iterable,model,preprocessor)
    return{"prediction":{target_var:pred},"real":Y}

    
@getaround.post("/predict/",tags=["predict"])
async def predict(getaround:Union[dict,list,tuple]):
    """This endpoint takes POST method  for getting the predicted price."""
    preprocessor=func_preprocessor()
    model=func_model()
    iterable=getaround
    pred=func_price_pred(iterable,model,preprocessor)
    return{"prediction":pred}
    
    
class Getaround(BaseModel):
    model_key:str
    mileage:int
    engine_power:int
    fuel:str
    paint_color:str
    car_type:str
    private_parking_available:bool
    has_gps:bool
    has_air_conditioning:bool
    automatic_car:bool
    has_getaround_connect:bool
    has_speed_regulator:bool
    winter_tires:bool
    
if __name__=="__main__":
    uvicorn.run(getaround, host="http://127.0.0.1", port=7000)