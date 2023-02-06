import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import json
import numpy as np
import gsheetsdb as gs
from gsheetsdb import connect

siteHeader = st.container()
dataExploration = st.container()
newFeatures = st.container()
modelTraining = st.container()

rc_dataExploration, ls_dataExploration, sf_dataExploration, fn_dataExploration = st.tabs(["Revoke.cash", "LoanShark", "SymphonyFinance", "FantomNames"])

with siteHeader:
  st.title('Welcome to Fantom Round Analysis!')
  st.text('In this project we are going to breakdown analysis of the round contributions and identify possible sybil behaviour')

  df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
  st.write(df)
  
  gsheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTqCQ3-PFdTVUqEr2bGO4fO88w6zgXdwKLDPz6tarQyDscv6e6FekNiY4uZimyMDxXeocXQ2yZ8nIFr/pub?gid=451420609&single=true&output=csv"
  conn = connect()
  rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
  df_gsheet = pd.DataFrame(rows)
  st.write(df_gsheet)
  
  col1, col2, col3 = st.columns(3)
  col1.metric("Grant applications", "10")
  col2.metric("Unique contributors", "900")
  col3.metric("Total amount of contributions", "100000", "-10 from yesterday")

  fantom_data = pd.read_csv(gsheet_url)
  fantom_data['amount_donated'] = fantom_data['amount_donated'].astype('string')

  st.header('Distribution of donations')
  st.text('This data is ...')

  ftm_all_projects =  fantom_data[fantom_data['data_subset'] == 'ftm_all_projects']

  ftm_all_distribution = ftm_all_projects[['amount_donated', 'unique_donations']]
  st.bar_chart(ftm_all_distribution, x='amount_donated', y='unique_donations') 

  st.header('Sum of donations by categories')
  st.text('This data is ...')

  ftm_all_sum = ftm_all_projects[['amount_donated', 'total_amount_donated']]
  st.bar_chart(ftm_all_sum, x='amount_donated', y='total_amount_donated') 

  st.header('Project specific analysis')
  st.text('This data is ...')

with rc_dataExploration:
  st.header('Distribution of all donations')
  st.text('This data is ...')

  revoke_contributions =  fantom_data[fantom_data['data_subset'] == 'revoke_cash']

  revoke_distribution = revoke_contributions[['amount_donated', 'unique_donations']]
  st.bar_chart(revoke_distribution, x='amount_donated', y='unique_donations') 

  st.header('Sum of donations by categories')
  st.text('This data is ...')

  revoke_sum = revoke_contributions[['amount_donated', 'total_amount_donated']]
  st.bar_chart(revoke_sum, x='amount_donated', y='total_amount_donated') 

with ls_dataExploration:
  st.header('Distribution of all donations')
  st.text('This data is ...')

  loan_shark_contributions =  fantom_data[fantom_data['data_subset'] == 'loan_shark']

  loan_shark_distribution = loan_shark_contributions[['amount_donated', 'unique_donations']]
  st.bar_chart(loan_shark_distribution, x='amount_donated', y='unique_donations') 

  st.header('Sum of donations by categories')
  st.text('This data is ...')

  loan_shark_sum = loan_shark_contributions[['amount_donated', 'total_amount_donated']]
  st.bar_chart(loan_shark_sum, x='amount_donated', y='total_amount_donated') 


with sf_dataExploration:
  st.header('Distribution of all donations')
  st.text('This data is ...')

  symphony_finance_contributions =  fantom_data[fantom_data['data_subset'] == 'symphony_finance']

  symphony_financce_distribution = symphony_finance_contributions[['amount_donated', 'unique_donations']]
  st.bar_chart(symphony_financce_distribution, x='amount_donated', y='unique_donations') 

  st.header('Sum of donations by categories')
  st.text('This data is ...')

  symphony_financce_sum = symphony_finance_contributions[['amount_donated', 'total_amount_donated']]
  st.bar_chart(symphony_financce_sum, x='amount_donated', y='total_amount_donated') 


with fn_dataExploration:
  st.header('Distribution of all donations')
  st.text('This data is ...')

  fantom_names_contributions =  fantom_data[fantom_data['data_subset'] == 'fantom_names']

  fantom_names_distribution = fantom_names_contributions[['amount_donated', 'unique_donations']]
  st.bar_chart(fantom_names_distribution, x='amount_donated', y='unique_donations') 

  st.header('Sum of donations by categories')
  st.text('This data is ...')

  fantom_names_sum = fantom_names_contributions[['amount_donated', 'total_amount_donated']]
  st.bar_chart(fantom_names_sum, x='amount_donated', y='total_amount_donated') 
