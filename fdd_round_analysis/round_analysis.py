import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import json
import numpy as np

siteHeader = st.container()

with siteHeader:
  st.title('Welcome to Gitcoin''s Round Analysis platform!')
  st.text('In this project we are going to breakdown analysis of the round contributions and identify possible sybil behaviour')

  col1, col2, col3 = st.columns(3)
  col1.metric("Grant applications", "10")
  col2.metric("Unique contributors", "900")
  col3.metric("Total amount of contributions", "100000", "-10 from yesterday")

  fantom_data = pd.read_csv('data/fantom_data_analysis_by_data_subset.csv') 
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
