import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import json
import numpy as np
from gsheetsdb import connect

siteHeader = st.container()
dataExploration = st.container()
newFeatures = st.container()
modelTraining = st.container()

rc_dataExploration, ls_dataExploration, sf_dataExploration, fn_dataExploration = st.tabs(["Revoke.cash", "LoanShark", "SymphonyFinance", "FantomNames"])

with siteHeader:
  st.title('Welcome to Fantom Round Analysis!')
  st.text('In this project we are going to breakdown analysis of the round contributions and identify possible sybil behaviour')

  df = pd.DataFrame({"one": ['token'], "two": ['id'], "three": ['amount']})
  st.write(df)
  
  gsheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTqCQ3-PFdTVUqEr2bGO4fO88w6zgXdwKLDPz6tarQyDscv6e6FekNiY4uZimyMDxXeocXQ2yZ8nIFr/pub?gid=451420609&single=true&output=csv"
  conn = connect()
  rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
  df_gsheet = pd.DataFrame(rows)
  st.write(df_gsheet)
