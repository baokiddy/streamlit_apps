import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import json
import numpy as np


st.set_page_config(
    page_title="Fantom Round Dashboard",
    page_icon="📊",
    layout="wide",
)

fantom_data = pd.read_csv('data/fantom_data_analysis_by_data_subset.csv') 

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return fantom_data

df = get_data()

st.title("demo of rounds dashboard")

projects = [str(row["destination_wallet"] for row in fantom_data])]
donations = [float(row["amount"] for row in fantom_data])]
n_projects = np.unique(projects)
avg_donation = np.mean(donations)
    
print("# of Projects", n_projects)
print("Avg Donation", avg_donation)

# top-level filters
#project_filter = st.selectbox("Select the Project", pd.unique(df["destination_wallet"]))

# creating a single-element container
#placeholder = st.empty()

# dataframe filter
#df = df[df["destination_wallet"] == project_filter]

# creating KPIs
#avg_donation = int(np.round(np.mean(df["amount"])))
#count_donors = int(
#    df[(df["source_wallet"] == "source_wallet")]["source_wallet"].count()
#)
#projects = np.sum(df["amount"])

#with placeholder.container():

        # create three columns
#    kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
 #   kpi1.metric(
 #       label="Age ⏳",
 #       value=round(avg_donation),
 #       delta=round(avg_donation) - 10,
 #   )
        
 #   kpi2.metric(
 #       label="Married Count 💍",
 #       value=int(avg_donation),
 #       delta=-10 + avg_donation,
 #   )
        
 #   kpi3.metric(
 #       label="A/C Balance ＄",
 #       value=f"$ {round(avg_donation,2)} ",
 #       delta=-round(avg_donation / 1) * 100,
 #   )

        # create two columns for charts
 #   fig_col1, fig_col2 = st.columns(2)
 #   with fig_col1:
 #       st.markdown("### First Chart")
 #       fig = px.density_heatmap(
 #           data_frame=df, y="amount", x="source_wallet"
 #       )
 #       st.write(fig)
            
 #   with fig_col2:
 #       st.markdown("### Second Chart")
 #       fig2 = px.histogram(data_frame=df, x="created_at")
 #       st.write(fig2)

 #   st.markdown("### Detailed Data View")
 #   st.dataframe(df)
