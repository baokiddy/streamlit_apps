import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
from pathlib import Path
import json
import numpy as np

siteHeader = st.container()

with siteHeader:
  st.title('Welcome to Gitcoin''s Round Analysis platform!')
  st.text('In this project we are going to breakdown analysis of the round contributions and identify possible sybil behaviour')

  # col1, col2, col3 = st.columns(3)
  # col1.metric("Grant applications", "10")
  # col2.metric("Unique contributors", "900")
  # col3.metric("Total amount of contributions", "100000", "-10 from yesterday")
  
  # st.text('Overall agreggated insights to be included here')

  
