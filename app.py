import streamlit as st

import numpy as np
import pandas as pd
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown("""
            Taxi Fare Website
            """)

# '''
# Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

key='2021-04-15 12:10:20.0000001'
pickup_date = st.date_input('Pickup date', value=datetime.datetime(2021, 10, 6, 12, 10, 20))
pickup_time = st.time_input('Pickup time', value=datetime.datetime(2021, 10, 6, 12, 10, 20))
pickup_datetime = f"{pickup_date} {pickup_time}UTC"
pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
passenger_count = st.number_input('passenger count',min_value=1, max_value=8, step=1, value=1)




# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://container-taxi-fare-two-id6kf6fenq-ew.a.run.app/predict_fare/'

# if url == 'http://taxifare.lewagon.ai/predict_fare/':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')



# 2. Let's build a dictionary containing the parameters for our API...

params = dict(
    key=key,
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count)




# 3. Let's call our API using the `requests` package...

response = requests.get(url, params=params)

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

prediction = response.json()

pred = prediction['prediction']

f'Fare: {pred} $'

## Finally, we can display the prediction to the user

