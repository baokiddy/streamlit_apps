##this is an attempt to pull from googlesheets as data source. Not yet functional.

import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import json
import numpy as np
from gsheetsdb import connect

dataset_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTqCQ3-PFdTVUqEr2bGO4fO88w6zgXdwKLDPz6tarQyDscv6e6FekNiY4uZimyMDxXeocXQ2yZ8nIFr/pub?gid=451420609&single=true&output=csv"

# read csv from a URL
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

st.set_page_config(
    page_title="Fantom Alpha Grants Round Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("Round-Monitoring Dashboard")

job_filter = st.selectbox("Select the Project", pd.unique(df["destination_wallet"]))
df = df[df["destiantion_wallet"] == job_filter]
