import streamlit as st  # 🎈 data web app development
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.express as px  # interactive charts

st.set_page_config(
    page_title="Getaround delay analysis",
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

# return a csv file
#@st.experimental_memo
#@st.cache
def get_data() -> pd.DataFrame:
    # read a csv file
    df_source = pd.read_csv(f"{mypath}src/getaround_delay_filled.csv")
    df=df_source.drop(['rental_id','car_id','previous_ended_rental_id'],axis=1)
    return df

def func_filter(cat_column,selectbox):
    res = df[cat_column] == selectbox
    if selectbox == 'all':
        res = True

df = get_data()
df_source = pd.read_csv(f"{mypath}src/getaround_delay_filled.csv")
df_source_exc = pd.read_csv(f"{mypath}src/get_around_pricing_project_cleaned.csv")
price_per_minute = round(df_source_exc['rental_price_per_day'].mean()/24/60,4)



# dashboard title
st.title("Getaround delay analysis")

### Side bar 
st.sidebar.header("Menu")
col1,_ = st.sidebar.columns(2)
with col1:
    st.sidebar.markdown("""
    * [Drivers Key indicators](#drivers-key-indicators)
    * [Time Key indicators](#time-key-indicators)
    * [Checkin type Key indicators](#checkin-type-key-indicators)
    * [cost Key indicators](#cost-key-indicators)
""")
## top-level filters
#col3,col4 = st.columns(2)
#state_filter = st.sidebar.selectbox("Select the state type", ['all',*pd.unique(df["state"])],index=0)
#checkin_filter = st.sidebar.selectbox("Select the checkin type", ['all',*pd.unique(df["checkin_type"])],index=0)
#delay_slider = st.sidebar.slider("Select the delay at checkout",min_value=-15000, max_value=15000, value=0, step=1)
#count_slider = st.sidebar.slider("Select the number of operation",min_value=0,max_value=21310, value=0, step=1)

st.sidebar.empty()
st.sidebar.write("Made for the certification by Ndangani :sunglasses:")

# creating a single-element container
placeholder = st.empty()
chartholder = st.empty()

# dataframe filter
#df_state_filter = df[df["state"] == state_filter]
#df_delay_slider = df[df["delay_at_checkout_in_minutes"] == delay_slider]
#df_checkin_filter = df[df["checkin_type"] == checkin_filter]
#df_time_delta_slider = df[df["time_delta_with_previous_rental_in_minutes"] == time_delta_slider]


   ## there are negative 'delay_at_checkout_in_minutes', I presume it is for those who arrive ahead of time
negative_delay = df[df['delay_at_checkout_in_minutes']<0]['delay_at_checkout_in_minutes']
positive_delay = df[df['delay_at_checkout_in_minutes']>0]['delay_at_checkout_in_minutes']
no_delay = df[df['delay_at_checkout_in_minutes']==0]['delay_at_checkout_in_minutes']

## count the checkout
early_checkout = negative_delay.count()
late_checkout = positive_delay.count()
inTime_checkout = no_delay.count()
total_checkout = early_checkout+late_checkout+inTime_checkout

## part checkout
part_early_checkout = early_checkout /total_checkout
part_late_checkout = late_checkout/total_checkout
part_inTime_checkout = inTime_checkout/total_checkout

## sum the minutes
early_minutes = negative_delay.sum()
late_minutes = positive_delay.sum()

## always 0
inTime_minutes = no_delay.sum()
total_minutes = abs(early_minutes)+late_minutes+inTime_minutes

## Absolute minutes Average
meanA_early_minutes = negative_delay.sum()/total_checkout
meanA_late_minutes = positive_delay.sum()/total_checkout
## always 0
meanA_inTime_minutes = no_delay.sum()/total_checkout
mean_total_minutes = (early_minutes+late_minutes)/total_checkout

## Relative minutes Average
meanR_early_minutes = negative_delay.sum()/early_checkout
meanR_late_minutes = positive_delay.sum()/late_checkout        
## always 0
meanR_InTime_minutes = no_delay.sum()/total_checkout
meanR_total_minutes=meanR_late_minutes+meanR_early_minutes

## Percentage of time
percentage_early_minutes = 100*negative_delay.sum()/total_minutes
percentage_late_minutes = 100*positive_delay.sum()/total_minutes
## always 0
percentage_inTime_minutes = 100*no_delay.sum()/total_minutes

## Numbers about the checkin type
delay_checkin_type = df[df['delay_at_checkout_in_minutes']>0]['checkin_type']
nb_checkin_type=df['checkin_type']

## The revenue affected by the delay is:
mean_cost_of_delay = round(price_per_minute*mean_total_minutes,3)

## the drivers delay


## function to calculate the nb of drivers late at checkout over the threshold given
def func_nb_drivers_late(thresh):
    if thresh <=0:
        thresh = 0
    return df[df['delay_at_checkout_in_minutes']>=thresh]['delay_at_checkout_in_minutes'].count()


## function to calculate the cost of the drivers late at checkout over the threshold given
def func_cost_thresh(thresh):
    cost = round(func_nb_drivers_late(thresh)*price_per_minute*mean_total_minutes,2)
    return cost

with placeholder.container():
    st.subheader('Key performance indicators')
    st.subheader('drivers Key indicators')
    desc,left,center,right = st.columns([1,1,1,1])

    desc.metric(label=" drivers en avance",value=early_checkout)
    left.metric(label=" drivers en retard",value=late_checkout)
    center.metric(label=" drivers à l'heure",value=inTime_checkout)
    right.metric(label="total  drivers",value=total_checkout)

    desc2,left2,center2,right2 = st.columns([1,1,1,1])
    desc2.metric(label="% des drivers en avance",value=f"{round(100*part_early_checkout,2)} %")
    left2.metric(label="%  drivers en retard",value=f"{round(100*part_late_checkout,2)} %")
    center2.metric(label="% des  drivers à l'heure",value=f"{round(100*part_inTime_checkout,2)} %")

    st.markdown("###### delay_at_checkout_in_minutes")
    st.line_chart(data=df['delay_at_checkout_in_minutes'])

    st.subheader("Time Key indicators")
    desc3,left3,center3,right3 = st.columns([1,1,1,1])
    desc3.metric(label="total de minutes d'avance",value=early_minutes)
    left3.metric(label="total de minutes de retard",value=late_minutes)

    #center.metric(label="total de minutes à temps",value=inTime_minutes)
    right3.metric(label="total minutes",value=total_minutes)

    fig_col31, fig_col32 = st.columns(2)
    with fig_col31:
        st.markdown("###### negative_delay")
        st.line_chart(negative_delay)
    with fig_col32:
        st.markdown("###### positive_delay")
        st.line_chart(positive_delay)

    left4,center4,right4 = st.columns([1,1,1])
    left4.metric(label="moyenne absolue de minutes d'avance",value=round(meanA_early_minutes,2))
    center4.metric(label="moyenne absolue de minutes de retard",value=round(meanA_late_minutes,2))
    right4.metric(label="moyenne absolue totale de temps",value=round(mean_total_minutes,2))

    left4.metric(label="% de minutes d'avance",value=f"{round(percentage_early_minutes,2)} %")
    center4.metric(label="% de minutes de retard",value=f"{round(percentage_late_minutes,2)} %")

    left4.metric(label="moyenne relative de minutes d'avance",value=round(meanR_early_minutes,2))
    center4.metric(label="moyenne relative de minutes de retard",value=round(meanR_late_minutes,2))        
    right4.metric(label="moyenne relative totale de temps",value=round(meanR_total_minutes,2))

    left4.metric(label="% relatif de minutes d'avance",value=f"{round(100*meanR_early_minutes/(abs(meanR_early_minutes)+meanR_late_minutes),2)} %")
    center4.metric(label="% relatif de minutes de retard",value=f"{round(100*meanR_late_minutes/(abs(meanR_early_minutes)+meanR_late_minutes),2)} %")

    fig_col21,fig_col22=st.columns(2)       
    with fig_col21:
        st.markdown("###### canceled state, checkin_type and delay_at_checkout_in_minutes")
        st.line_chart(data=df.loc[df['state']=='canceled',:],x="checkin_type",y="delay_at_checkout_in_minutes")

    with fig_col22:
        st.markdown("###### ended state, checkin_type and delay_at_checkout_in_minutes")
        st.line_chart(data=df.loc[df['state']=='ended',:],x="checkin_type",y="delay_at_checkout_in_minutes")

    st.subheader("Checkin type Key indicators")
    desc5,left5,center5,right5 = st.columns([1,1,1,1])
    #desc.metric(label=f"checkin type",label_visibility='hidden',value="")
    desc5.write("global checkin type")
    left5.metric(label=f"{nb_checkin_type.value_counts().index[0]} checkin type",value=nb_checkin_type.value_counts()[0])
    center5.metric(label=f"{nb_checkin_type.value_counts().index[1]} checkin type",value=nb_checkin_type.value_counts()[1])
    desc5.metric(label=f"checkin type",label_visibility='hidden',value="")
    desc5.write("checkin type in delay")
    left5.metric(label=f"{delay_checkin_type.value_counts().index[0]} in delay",value=delay_checkin_type.value_counts()[0])
    center5.metric(label=f"{delay_checkin_type.value_counts().index[1]} in delay",value=delay_checkin_type.value_counts()[1])

    fig_col1,fig_col2=st.columns(2)
    with fig_col1:
        st.markdown("###### checkin_type and delay_at_checkout_in_minutes")
        st.bar_chart(data=df,x="state",y="delay_at_checkout_in_minutes")
    with fig_col2:
        st.markdown("###### checkin_type and delay_at_checkout_in_minutes")
        st.bar_chart(data=df,x="checkin_type",y="delay_at_checkout_in_minutes")

    st.subheader("cost Key indicators")
    desc6,left6,center6,right6 = st.columns([1,1,1,1])
    desc6.metric(label="price location per minute",value=f"{price_per_minute} $")
    left6.metric(label="average cost of minutes late",value=f"{round(price_per_minute*mean_total_minutes,2)} $")
    center6.metric(label="threshold: average minutes late",value=f"{round(mean_total_minutes,2)}")
    left6.metric(label="nb de drivers concernés",value=func_nb_drivers_late(mean_total_minutes))
    center6.metric(label="cost of those drivers",value=f"{func_cost_thresh(mean_total_minutes)} $")

