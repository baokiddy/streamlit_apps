import streamlit as st
import pandas as pd
from pandas.io.json import json_normalize
import json
import numpy as np

siteHeader = st.container()

# Gitcoin protocol datasets
votes = pd.read_csv('data/ethereum_grant_votes.csv')
apps = pd.read_csv('data/ethereum_grant_applications.csv')
complete_dataset = pd.read_csv('data/ethereum_joined_dataset.csv')

complete_dataset = complete_dataset[['id','token','amount',	'source_wallet', 'project_wallet', 'created_at_x',	'project_id','title', 'project_github',	'project_twitter', 'previous_funding', 'team_size',	'verified_twitter_or_github', 'links_to_github_or_org']]
main_df = complete_dataset.tail()

with siteHeader:
    st.title('Ethereum Infrastructure Analysis')
    st.text('In this project we are going to breakdown analysis of the round contributions and identify possible sybil behaviour')

    votes_dai = votes[votes['token'] == 'DAI']
    votes_eth = votes[votes['token'] == 'ETH']

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Grant applications", f"{apps['project_id'].nunique()}")
    col2.metric("Unique contributors", f"{votes['source_wallet'].nunique()}")
    col3.metric("Total contributions (ETH)", str(votes_eth['amount'].sum().round(2)))
    col4.metric("Total contributions (DAI)", str(votes_dai['amount'].sum().round(2)))

    
    gb = GridOptionsBuilder.from_dataframe(main_df)
   
    gb.configure_column("amount", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=2, aggFunc='sum')
    gb.configure_column("created_at_x", type=["dateColumnFilter","customDateTimeFormat"], custom_format_string='yyyy-MM-dd HH:mm zzz', pivot=True)

    #configures last row to use custom styles based on cell's value, injecting JsCode on components front end
    cellsytle_jscode = JsCode("""
    function(params) {
        if ((params.value !== undefined) && (params.value !== null)) {
            return {
                'color': 'black',
                'backgroundColor': 'white'
            }
        } else {
            return {
                'color': 'white',
                'backgroundColor': 'darkred'
            }
        }
    };
    """)

    gb.configure_column("previous_funding", cellStyle=cellsytle_jscode)

    gb.configure_selection('multiple')
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren=True, groupSelectsFiltered=True)

    gb.configure_grid_options(domLayout='normal')
    gridOptions = gb.build()


    grid_height = 300
    return_mode_value = 'FILTERED'
    update_mode_value = 'GRID_CHANGED'

    grid_response = AgGrid(
        complete_dataset, 
        gridOptions=gridOptions,
        height=grid_height, 
        width='100%',
        data_return_mode=return_mode_value, 
        update_mode=update_mode_value,
        allow_unsafe_jscode=True #Set it to True to allow jsfunction to be injected
        )

    df = grid_response['data']
    selected = grid_response['selected_rows']
    selected_df = pd.DataFrame(selected).apply(pd.to_numeric, errors='coerce')


    with st.spinner("Displaying results..."):
        #displays the chart
        df['created_at_x'] = pd.to_datetime(df['created_at_x'])
        chart_data = df.loc[:,['created_at_x','amount']].assign(source='total')

        if not selected_df.empty :
            selected_data = selected_df.loc[:,['created_at_x','amount']].assign(source='selection')
            chart_data = pd.concat([chart_data, selected_data])

        # chart_data = pd.melt(chart_data, id_vars=['source'], var_name="date", value_name="quantity")
        #st.dataframe(chart_data)
        chart = alt.Chart(data=chart_data).mark_bar().encode(
            x=alt.X("week(checked_at_x):O"),
            y=alt.Y("sum(amount):Q"),
            color=alt.Color('source:N', scale=alt.Scale(domain=['total','selection'])),
        )


        # alt.Chart(df).mark_line().encode(
        #     x=alt.X('Date', axis=alt.Axis(format='%e %b, %Y')),
        #     y=alt.Y('Values', scale=alt.Scale(zero=False)),
        #     color='Key') 

        # chart = alt.Chart(data=chart_data).mark_bar().encode(
        #     x=alt.X('checked_at_x:N', title=None),
        #     y=alt.Y('amount:Q', scale=alt.Scale(domain=(0, 12000000))),
        #     color=alt.Color('source:N', scale=alt.Scale(domain=['total','selection']))
        # ).properties(
        #     width=600
        # ).transform_calculate(
        #     "source", alt.expr.if_(alt.datum.source == 1, "total", "selection")
        # ).configure_facet(
        #     spacing=8
        # )

        st.header("Amount donated over time")
        st.markdown("""
        This chart is built with data returned from the grid. The rows that are selected are identified as shown in the legend.
        """)

        st.altair_chart(chart, use_container_width=True)