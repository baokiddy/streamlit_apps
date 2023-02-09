import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import json
import numpy as np
import data_flattening

siteHeader = st.container()

# Gitcoin protocol datasets
file_path_applications = 'data/oss_round_applications.json'
file_path_votes = 'data/oss_round_votes_raw.json'
round_name = 'oss'

votes, apps, complete_dataset = data_flattening.processing(file_path_applications, file_path_votes, round_name)


with siteHeader:
  st.title('Web3 Open Source Software Analysis')
  st.text('In this project we are going to breakdown analysis of the round contributions and identify possible sybil behaviour')

  votes_dai = votes[votes['token'] == 'DAI']
  votes_eth = votes[votes['token'] == 'ETH']

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Grant applications", f"{apps['project_id'].nunique()}")
  col2.metric("Unique contributors", f"{votes['source_wallet'].nunique()}")
  col3.metric("Total contributions (ETH)", str(votes_eth['amount'].sum().round(2)))
  col4.metric("Total contributions (DAI)", str(votes_dai['amount'].sum().round(2)))

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