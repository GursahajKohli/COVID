#Imports
import os
import numpy as np
import tensorflow.keras as keras
from tensorflow.keras.models import load_model
import cv2
import pandas as pd
import plotly
import plotly.express as px

# Prediction of x-ray image
def model_prediction(path):
    model = load_model("covid/covid_model.h5")
    img_for_test = cv2.imread(path)
    img_for_test = cv2.resize(img_for_test, (224, 224))
    img_for_test = np.reshape(img_for_test, [1, 224, 224, 3])
    prediction = model.predict(img_for_test)
    if(prediction[0][0] == 0.0):
        prediction = "COVID POSITIVE"
    else:
        prediction = "COVID NEGATIVE"
    return prediction

# Get the three-letter country codes for each country
def get_country_code(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None

def get_plot():
    df = pd.read_csv('covid/covid2.csv')
    ## Drop rows corresponding to the World
    df = df[df.location != 'World']
    ## Sort df by date
    df = df.sort_values(by=['date'])
    fig = px.choropleth(df, locations="2iso_code",
                    color="total_cases",
                    hover_name="location",
                    animation_frame="date",
                    title = "Total COVID cases",
                   color_continuous_scale=px.colors.sequential.PuRd)
    fig["layout"].pop("updatemenus")
    fig.show()
    return 
