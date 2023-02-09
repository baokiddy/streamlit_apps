import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import json
import numpy as np
import data_flattening

siteHeader = st.container()

with siteHeader:
  st.title('About')
  st.text('Platform to showcase round analysis')
