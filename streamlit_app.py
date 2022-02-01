import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
import functions as fn #functions
import customize as cust #functions for custom css and html


# loading custom css
cust.page_config()
cust.dropdown()
cust.sidebar()
cust.footer()


# loding database with caching
@st.cache(show_spinner=False, ttl=3600)
def get_csv_from_url(): 
    '''This function downloads updated data from OWID website and returns it in a dataframe'''
    url="https://covid.ourworldindata.org/data/owid-covid-data.csv"
    df=pd.read_csv(url)
    return df
df=get_csv_from_url()
#for testing this function can be called:  df = fn.open_local_csv(), dataframe will be opened from local drive)


#transforming dataframes and data
df_owid = fn.get_owid(df)
df = fn.drop_owid(df, df_owid)
df = fn.clean_data(df)
list_data_category = fn.data_category(df)
df_coordinates = fn.get_coordinates()
df_merged = fn.merging_dfs(df, df_coordinates)
df_continents = fn.continent_coordinates()
list_continents =  df_continents.continent.values.tolist()


#functions by which the output will be cached
@st.cache(show_spinner=False, ttl=3600)
def get_update_day(df):
    '''This function gets the newest day of the dataset and returns it as the update day'''
    dates = df['date'].unique()
    dates = sorted(dates, reverse=True)
    update_day = dates[0]
    return update_day
update_day = get_update_day(df)


@st.cache(show_spinner=False, ttl=3600)
def get_datetime_max():
    '''This function converts update day of the dataset to datetime.date format for the streamlit date_input element in submit form 1.'''
    datetime_max = datetime.strptime(f'{update_day}', '%Y-%m-%d').date()
    return datetime_max
datetime_max = get_datetime_max()


@st.cache(show_spinner=False, ttl=3600)
def get_datetime_min():
    '''This function converts the first day of the dataset ('2020-01-01') to datetime.date format for the streamlit date_input element in submit form 1.'''
    datetime_min = datetime.strptime('2020-01-01', '%Y-%m-%d').date()
    return datetime_min
datetime_min = get_datetime_min() 


@st.cache(show_spinner=False, ttl=3600)
def date_max_min(update_day):
    '''This function calculates min and max dates for the range selector of country chart. date_max is the update day, date_min is 30 days earlier.'''
    date_max = update_day
    update_day = datetime.strptime(update_day, '%Y-%m-%d').date()
    date_min = update_day - timedelta(30)
    date_min = date_min.strftime('%y-%m-%d')
    return date_max, date_min
date_max, date_min = date_max_min(update_day)


#streamlit container element containing the map or charts
container_1 = st.container()


#streamlit sidebar: title, subheader and expander
st.sidebar.title('COVID-19 Dashboard') 
st.sidebar.subheader(f'Last update: {update_day}')
with st.sidebar.expander("How to use this dashboard?"):
    cust.expander_html_1()


#streamlit sidebar: submit form 1. 
st.sidebar.subheader("1. Compare countries on the map")
with st.sidebar.form(key="form_map"):
    data_category_map = st.selectbox('Select a data category', list_data_category, index=0)
    calendar_map = st.date_input('Select a date', value=datetime_max, max_value=datetime_max, min_value=datetime_min)
    continent_map = st.selectbox('Select a continent', list_continents, index=2)
    submit_button_map = st.form_submit_button('Submit')


#streamlit sidebar: submit form 2. 
st.sidebar.subheader('2. Compare countries on line chart')
with st.sidebar.form(key='form_chart'):
    data_category_linechart = st.multiselect('Select data categories', list_data_category, default=[list_data_category[0], list_data_category[21]])
    country_linechart = st.multiselect('Select countries', df_merged['country'].unique(), default=['France', 'Germany', 'Italy', 'Hungary'])    
    submit_button_linechart = st.form_submit_button('Submit')


# streamlit sidebar: submit form 3. 
st.sidebar.subheader('3. Compare countries on bar chart')
with st.sidebar.form(key='form_barchart'):
    data_category_barchart = st.multiselect('Select data categories', list_data_category, default=[list_data_category[4], list_data_category[22]])
    calendar_barchart = st.date_input('Select a date', value=datetime_max, max_value=datetime_max, min_value=datetime_min)
    country_barchart = st.multiselect('Select countries', df_merged['country'].unique(), default=['France', 'Germany', 'Italy', 'Hungary'])
    submit_button_barchart = st.form_submit_button('Submit')


# st.sidebar.subheader('Learn more about this dashboard')
with st.sidebar.expander("Learn more about this dashboard"):
    cust.expander_html_2()


#function for creating initial map (it does not plot it, yet)
map_initial = fn.map_initial(df_merged, update_day, 'New cases')


if submit_button_map:
    del map_initial
    cust.container_map_continent()
    with container_1:
        map_continent = fn.map_continent(df_merged, df_continents, continent_map, calendar_map, data_category_map) 
        st.plotly_chart(map_continent, use_container_width=True)


elif submit_button_linechart:
    del map_initial 
    cust.back_to_map_button()
    cust.container_chart() 
    df_world = fn.df_world(df_owid)
    with container_1:
        back_to_map = st.button('Back to map view') 
        for i in range(len(data_category_linechart)):
            line_chart_user = fn.line_chart(df_merged, df_world, country_linechart, data_category_linechart[i], date_max, date_min) 
            st.plotly_chart(line_chart_user, use_container_width=True)


elif submit_button_barchart:
    del map_initial
    cust.back_to_map_button()
    cust.container_chart()          
    with container_1:
        back_to_map = st.button('Back to map view') 
        for i in range(len(data_category_barchart)):
            bar_chart_user = fn.bar_chart(df_merged, country_barchart, calendar_barchart, data_category_barchart[i])
            st.plotly_chart(bar_chart_user, use_container_width=True)


try:
    with container_1:
        cust.container_map()
        st.plotly_chart(map_initial, use_container_width=True)
except: 
    pass        