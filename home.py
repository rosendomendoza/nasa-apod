import os
import requests
import streamlit as st

NASA_API_KEY = os.getenv("NASAAPIKEY")

# Prepare API Key and API url
api_key = NASA_API_KEY
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Get the request data as a dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the information
title = data["title"]
url_image = data["url"]
description = data["explanation"]

# Download the image
response2 = requests.get(url_image)
imageOfDay = response2.content

# Make a website
st.set_page_config(page_title=None,
                   page_icon=None,
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

st.title(title)
st.image(imageOfDay)
st.write(description)
