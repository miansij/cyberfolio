import streamlit as st 
import time  
import numpy as np
import pandas as pd 
import plotly.express as px 
from datetime import datetime

st.set_page_config(
    page_title="KAYAK",
    page_icon="✅",
    layout="wide",
)

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


df_towns_enriched = pd.read_csv(f"{mypath}src/towns_enriched.csv")
df_best_destinations = pd.read_csv(f"{mypath}src/best_destinations.csv")
df_best_hotels = pd.read_csv(f"{mypath}src/best_hotels.csv")

# return a csv file
@st.experimental_memo
@st.cache
def get_data() -> pd.DataFrame:
    # read a csv file
    df_towns_enriched = pd.read_csv(f"{mypath}src/towns_enriched.csv")
    return df

def func_filter(cat_column,selectbox):
    res = df[cat_column] == selectbox
    if selectbox == 'all':
        res = True

## function that return a citeria to sort the dataframe with the the weather criteria
## 2 seasons are defined
def current_period(df):
    ## A nice weather for me depends on the current period.
    ## From march to october a nice weather is defined by max 'apparent_temperature_max','apparent_temperature_min'
    ## and min 'rain_sum','snowfall_sum','windspeed_10m_max'.
    sun_by = ['dates','apparent_temperature_max','apparent_temperature_min','rain_sum','snowfall_sum','windspeed_10m_max']
    sun_sort = [True,False,False,True,True,True]

    ## From november to february a nice weather is defined by max 'snowfall_sum' and min 'apparent_temperature_max',
    ## 'apparent_temperature_min','rain_sum','windspeed_10m_max'
    snow_by = ['dates','snowfall_sum','apparent_temperature_max','apparent_temperature_min','rain_sum','windspeed_10m_max']
    snow_sort = [True,False,True,True,True,True]    
    ## the 2 seasons
    period = datetime.now().date()
    sunny_period = period >= datetime.strptime('01-03-2022',"%d-%m-%Y").date() and period < datetime.strptime('01-11-2022',"%d-%m-%Y").date()
    snow_period = period >= datetime.strptime('01-11-2022',"%d-%m-%Y").date() and period < datetime.strptime('01-03-2022',"%d-%m-%Y").date()
    if sunny_period:
        criteria = [sun_by,sun_sort]
    else:
        criteria = [snow_by,snow_sort]    
    return criteria
## How to sort the dataframe
sorting=current_period(df_towns_enriched)


## Function to plot a map of the 5 best destinations per day
def plot_5destinations(df):
    #liste = get_best_destinations(df)
    #df = pd.concat([destination for destination in liste],ignore_index=True)
    mapbox_style=["open-street-map", "carto-positron", "carto-darkmatter", "stamen-terrain", "stamen-toner","stamen-watercolor"]
    date_first=min(df['dates'].unique())
    date_last=max(df['dates'].unique())
    fig = px.scatter_mapbox(df,
                            lat='latitude',
                            lon='longitude',
                            hover_name='ville',
                            color= sorting[0][1],
                            size= sorting[0][2],
                            opacity=0.8,
                            title= f'the 5 best touristic destination per day from {date_first} to {date_last}',
                            animation_frame="dates",
                            height=1000,
                            zoom=4,
                            mapbox_style=mapbox_style[1],
                            center={'lat':47,'lon':12})
    fig.show()

## Function to plot a map of the 20 best hotels per best destination per day
def plot_20hotels(df):
    #liste = get_best_hotels(df)
    #df = pd.concat([destination for destination in liste],ignore_index=True)
    mapbox_style=["open-street-map", "carto-positron", "carto-darkmatter", "stamen-terrain", "stamen-toner","stamen-watercolor"]
    date_first=min(df['dates'].unique())
    date_last=max(df['dates'].unique())
    fig = px.scatter_mapbox(df,
                            lat='latitude',
                            lon='longitude',
                            hover_name='hotel',
                            color= 'ville',
                            size= sorting[0][2],
                            opacity=0.5,
                            title= f'the 20 best hotels in the best touristic destination per day from {date_first} to {date_last}',
                            animation_frame="dates",
                            height=1000,
                            zoom=4,
                            mapbox_style=mapbox_style[1],
                            center={'lat':47,'lon':12})
    fig.show() 

st.title("Kayak project")
    
    ### Side bar 
st.sidebar.header("Filtering the maps")

st.sidebar.markdown("""
    *[Map with streamlit](#map-with-streamlit)
    * [the 5 best destinations with streamlit](#the-5-best-destinations-with-streamlit)
    * [the 20 best hotels in an area with streamlit](#the-20-best-hotels-in-an-area-with-streamlit)
    """)
    #*[Map with plotly](#map-with-plotly)
    #* [the 5 best destinations with plotly](#the-5-best-destinations-with-plotly)
    #* [the 20 best hotels in an area with plotly](#the-20-best-hotels-in-an-area-with-plotly)

day_filter = st.sidebar.selectbox("Select a day to plot",df_best_hotels['dates'].unique(),index=0)
st.sidebar.write("Made for the certification by Ndangani :sunglasses:")
  
# creating a single-element container
streamlitholder = st.empty()
plotyholder = st.empty()

st.map(df_best_destinations[df_best_destinations['dates']==day_filter])
with streamlitholder.container():
    st.subheader('Map with streamlit')
    st.subheader('The 5 best destinations with streamlit')
    ## To see the 5 best destinations   
    st.map(df_best_destinations[df_best_destinations['dates']==day_filter],zoom=4)
    
    st.subheader('The 20 best hotels in an area with streamlit')
    st.write("zoom to see the 20 hotels")
    ## To see the 20 best hotels in an area, you need to zoom
    st.map(df_best_hotels[df_best_hotels['dates']==day_filter],zoom=4)
    
    
with plotyholder.container():
    #st.subheader('Map with plotly')
    #st.subheader('The 5 best destinations with plotly')
    ## To see the 5 best destinations   
    #plot_5destinations(df_best_destinations)
    
    #st.subheader('The 20 best hotels in an area with plotly')
    #st.write("zoom to see the 20 hotels")
    ## To see the 20 best hotels in an area, you need to zoom
    #plot_20hotels(df_best_hotels)
    
    #count=0
    ## Run the below code if the check is checked
    #if st.checkbst.line_chart(ox(label='Detailed Data View',key=f"raw_data{count}"):
    #    st.markdown("### Detailed Data View")
    #    #st.write(df_source)
    #    st.dataframe(df_source)
    #    count +=1
    st.write("Made for the certification by Ndangani :sunglasses:")
