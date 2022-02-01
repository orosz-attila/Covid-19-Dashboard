import streamlit as st
import os
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, timedelta, datetime

PATH = os.path.abspath('')

def get_csv_from_url(): 
    '''This function gets updated COVID-19 data from the OWID website and opens it in a dataframe.'''
    url="https://covid.ourworldindata.org/data/owid-covid-data.csv"
    df=pd.read_csv(url)
    return df


def download_csv():
    """This function downloads updated COVID-19 data from the OWID website (for testing purposes, it will be not used not in the final app)"""
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    r = requests.get(url)
    open(PATH + os.sep + 'data/covid_data.csv', 'wb').write(r.content)
    df = pd.read_csv(PATH + os.sep + 'data/covid_data.csv')
    return df   


def open_local_csv():
    '''This function opens the downloaded csv from local drive. (for testing purposes, it will be not used not in the final app)'''
    df = pd.read_csv(PATH + os.sep + 'data/covid_data.csv')
    return df


def get_owid(df):
    '''This function returns dataframe with aggregated continent or international data starts with 'OWID' in iso-code column.'''
    df_owid = df[df['iso_code'].str.match('OWID')]
    return df_owid    


def drop_owid(df, df_owid):
    '''This function returns a dataframe only with country data, without aggregated continent or international data starts with 'OWID' in iso-code column.'''
    df = df.drop(df_owid.index, axis=0)
    return df


def clean_data(df): 
    '''This function selects and renames data columns, 
    filling Nan values in selected columns with the data from the previous day.'''
    
    df = df[['location', 
         'date', 
         'new_cases', 
         'new_cases_smoothed', 
         'total_cases', 
         'new_cases_per_million', 
         'new_cases_smoothed_per_million', 
         'total_cases_per_million', 
         'new_deaths', 
         'new_deaths_smoothed', 
         'total_deaths', 
         'new_deaths_per_million', 
         'new_deaths_smoothed_per_million', 
         'total_deaths_per_million', 
         'icu_patients', 
         'icu_patients_per_million', 
         'hosp_patients', 
         'hosp_patients_per_million', 
         'stringency_index', 
         'new_tests', 
         'total_tests', 
         'reproduction_rate', 
         'people_fully_vaccinated', 
         'people_fully_vaccinated_per_hundred', 
         'total_boosters_per_hundred']]    
    
    df = df.rename(columns={
        'location': 'country',    

        'new_cases': 'New cases',
        'new_cases_smoothed': 'New cases (Last 7-day average)',
        'total_cases': 'Total cases' , 

        'new_cases_per_million': 'New cases per million',
        'new_cases_smoothed_per_million': 'New cases per million (Last 7-day average)',
        'total_cases_per_million': 'Total cases per million', 

        'new_deaths': 'New deaths',
        'new_deaths_smoothed': 'New deaths (Last 7-day average)', 
        'total_deaths': 'Total deaths', 

        'new_deaths_per_million': 'New deaths per million',
        'new_deaths_smoothed_per_million': 'New deaths per million (Last 7-day average)',
        'total_deaths_per_million': 'Total deaths per million',

        'icu_patients': 'Patients in intensive care',
        'icu_patients_per_million': 'Patients in intensive care per million',
        'hosp_patients': 'Hospitalized patients', 
        'hosp_patients_per_million': 'Hospitalized patients per million', 

        'stringency_index': 'Stringency index', 
        'new_tests': 'New tests', 
        'total_tests': 'Total tests',    
        'reproduction_rate': 'Reproduction rate', 
        'people_fully_vaccinated': 'People fully vaccinated', 
        'people_fully_vaccinated_per_hundred': 'People fully vaccinated (%)',
        'total_boosters_per_hundred': 'Total boosters (%)'})
    
    fillna_columns = [
        'Total cases',  
        'Total cases per million',
        'Total deaths',
        'Total deaths per million', 
        'Patients in intensive care',
        'Patients in intensive care per million', 
        'Hospitalized patients',
        'Hospitalized patients per million',
        'Stringency index',
        'Total tests',
        'Reproduction rate', 
        'People fully vaccinated',
        'People fully vaccinated (%)', 
        'Total boosters (%)']
    
    df[fillna_columns] = df.groupby('country')[fillna_columns].transform(lambda x: x.ffill())
    return df


def data_category(df):
    '''This function returns a list of the data categories from column labels of the dataframe'''
    df_data_category = df.drop(columns=['country', 'date'])
    list_data_category = df_data_category.columns.values.tolist()
    return list_data_category


def get_update_day(df):
    '''This functions gets the date of the last day from the database, returs it as string.'''
    dates = df['date'].unique()
    dates = sorted(dates, reverse=True)
    update_day = dates[0]
    return update_day


def get_datetime_max(update_day):
    '''This function returns the update day in datetime.date format, which is required for the date_input streamlit element.'''
    datetime_max = datetime.strptime(f'{update_day}', '%Y-%m-%d').date()
    return datetime_max


def get_datetime_min():
    '''This function returns the first day in datetime.date format, which is required for the date_input streamlit element.'''
    datetime_min = datetime.strptime('2020-01-01', '%Y-%m-%d').date()
    return datetime_min


def get_coordinates():
    '''This function loads dataframe with coordinates of country capitals'''
    df_coordinates = pd.read_csv(PATH + os.sep + 'data/coordinates.csv')
    df_coordinates = df_coordinates.drop(columns=['CapitalName', 'CountryCode', 'ContinentName'])
    df_coordinates = df_coordinates.rename(columns={'CountryName': 'country', 'CapitalLatitude': 'latitude', 'CapitalLongitude': 'longitude'})
    return df_coordinates


def merging_dfs(df, df_coordinates):
    '''This function joins coordinates data to the main dataframe'''
    df_merged = df.merge(df_coordinates, left_on = 'country', right_on = 'country', how='left')
    df_merged_isna_coor  = df_merged[df_merged['latitude'].isna()]
    df_merged.drop(df_merged_isna_coor.index, axis=0, inplace=True)
    return df_merged


def df_world(df_owid):
    '''This function returns a dataframe with world data'''
    df_world = df_owid.loc[df_owid['iso_code'] == 'OWID_WRL']

    df_world = df_world[[
        'location', 
        'date', 
        'new_cases', 
        'new_cases_smoothed', 
        'total_cases', 
        'new_cases_per_million', 
        'new_cases_smoothed_per_million', 
        'total_cases_per_million', 
        'new_deaths', 
        'new_deaths_smoothed', 
        'total_deaths', 
        'new_deaths_per_million', 
        'new_deaths_smoothed_per_million', 
        'total_deaths_per_million', 
        'icu_patients', 
        'icu_patients_per_million', 
        'hosp_patients', 
        'hosp_patients_per_million', 
        'stringency_index', 
        'new_tests', 
        'total_tests', 
        'reproduction_rate', 
        'people_fully_vaccinated', 
        'people_fully_vaccinated_per_hundred', 
        'total_boosters_per_hundred']]    
    
    df_world = df_world.rename(columns={
        'location': 'country',    

        'new_cases': 'New cases',
        'new_cases_smoothed': 'New cases (Last 7-day average)',
        'total_cases': 'Total cases' , 

        'new_cases_per_million': 'New cases per million',
        'new_cases_smoothed_per_million': 'New cases per million (Last 7-day average)',
        'total_cases_per_million': 'Total cases per million', 

        'new_deaths': 'New deaths',
        'new_deaths_smoothed': 'New deaths (Last 7-day average)', 
        'total_deaths': 'Total deaths', 

        'new_deaths_per_million': 'New deaths per million',
        'new_deaths_smoothed_per_million': 'New deaths per million (Last 7-day average)',
        'total_deaths_per_million': 'Total deaths per million',

        'icu_patients': 'Patients in intensive care',
        'icu_patients_per_million': 'Patients in intensive care per million',
        'hosp_patients': 'Hospitalized patients', 
        'hosp_patients_per_million': 'Hospitalized patients per million', 

        'stringency_index': 'Stringency index', 
        'new_tests': 'New tests', 
        'total_tests': 'Total tests',    
        'reproduction_rate': 'Reproduction rate',  
        'people_fully_vaccinated': 'People fully vaccinated', 
        'people_fully_vaccinated_per_hundred': 'People fully vaccinated (%)',
        'total_boosters_per_hundred': 'Total boosters (%)'})
    
    fillna_columns = [
        'Total cases',  
        'Total cases per million',
        'Total deaths',
        'Total deaths per million', 
        'Patients in intensive care',
        'Patients in intensive care per million', 
        'Hospitalized patients',
        'Hospitalized patients per million',
        'Stringency index',
        'Total tests',
        'Reproduction rate', 
        'People fully vaccinated',
        'People fully vaccinated (%)', 
        'Total boosters (%)']
    
    df_world[fillna_columns] = df_world.groupby('country')[fillna_columns].transform(lambda x: x.ffill())
    return df_world


def continent_coordinates():
    '''This function returns a dataframe with continent coordinates used in map_continent() function'''
    data = {'continent': ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania', "World"], 
                         'latitude': [0, 23.98, 50.61, 38.42, -20.77, -20.34, 7.30], 
                         'longitude': [22.41, 89.97, 18.26, -93.20, -63.58, 156.56, 45.85], 
                          'zoom': [2.7, 2.75, 3.35, 3.0, 2.5, 3, 1.58]  
                        }
    df_continents = pd.DataFrame(data)
    return df_continents


def map_initial(df_merged, date, data_category):
    ''''This function returns a map with the selected date and data category'''

    # filtering by the selected date
    date = str(date)
    df_today = df_merged[df_merged['date'] == date]
    df_today = df_today.rename(columns={'date': 'Date',})

    # scaling scatters, setting min and max sizes
    df_today['size_scaled'] = (df_today[data_category]  - df_today[data_category].min()) / (df_today[data_category].max() - df_today[data_category].min())
    df_today['size_scaled'].fillna(0, inplace=True)
    df_today['size_scaled'] = np.where(df_today['size_scaled'] <= 0.012, 0.012, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.012) & (df_today['size_scaled']<=0.02), 0.02, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.02) & (df_today['size_scaled']<=0.03), 0.03, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.03) & (df_today['size_scaled']<=0.04), 0.04, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.04) & (df_today['size_scaled']<=0.05), 0.05, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.05) & (df_today['size_scaled']<=0.1), 0.1, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.1) & (df_today['size_scaled']<=0.2), 0.2, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.2) & (df_today['size_scaled']<=0.3), 0.3, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.3) & (df_today['size_scaled']<=0.4), 0.4, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.4) & (df_today['size_scaled']<=0.5), 0.4, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.5) & (df_today['size_scaled']<=0.6), 0.6, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.6) & (df_today['size_scaled']<=0.7), 0.7, df_today['size_scaled'])
    df_today['size_scaled'] = np.where(df_today['size_scaled'] > 0.7, 0.7, df_today['size_scaled'])

    # making a new column for hover label
    df_today['data_category_fillna'] =  df_today[data_category].fillna(0)

    # creating the map figure 
    fig_map_initial = px.scatter_mapbox(df_today, 
                               lat="latitude", 
                               lon="longitude",
                               color=data_category, 
                               size="size_scaled",
                               size_max=100,
                               color_continuous_scale="Mint", # Teal
                               range_color=(-100000, 0),
                               opacity=0.5,
                               zoom=3.35,
                               center = {"lat": 50.61, "lon": 18.26},
                               height=950,
                               mapbox_style="basic",                              
                               hover_name='country',
                               #title=f'COVID-19 related {data_category} on {date}',
                               custom_data=['country', 'data_category_fillna'],
                              )         
    # updating layout                         
    fig_map_initial.update_layout(mapbox = dict(pitch=10, accesstoken=st.secrets['token'], style= 'mapbox://styles/mapbox/light-v8'))
    fig_map_initial.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) 
    fig_map_initial.update_traces(marker_sizemin = 10, hovertemplate = '<b>%{customdata[0]}</b> <br>' + f'{data_category}' + ': %{customdata[1]:,.0f}<extra></extra>')
    fig_map_initial.update_layout(hoverlabel=dict( font_size=15))
    fig_map_initial.update_layout(hovermode='closest')
    fig_map_initial.update_layout(coloraxis_showscale=False)
    return(fig_map_initial)


def map_continent(df_merged, df_continents, continent, date, data_category):
    ''''This function returns a map zoomed on a selected continent with 3 user inputs selected in the sidebar form '1. Compare countries on the map': date, data category, continent'''
    
    # filtering by the selected date 
    date = str(date)
    df_today = df_merged[df_merged['date'] == date]
    df_today = df_today.rename(columns={'date': 'Date',})

    # scaling scatters, setting min and max sizes  
    df_today['size_scaled'] = (df_today[data_category]  - df_today[data_category].min()) / (df_today[data_category].max() - df_today[data_category].min())
    df_today['size_scaled'].fillna(0, inplace=True)
    df_today['size_scaled'] = np.where(df_today['size_scaled'] <= 0.012, 0.012, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.012) & (df_today['size_scaled']<=0.02), 0.02, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.02) & (df_today['size_scaled']<=0.03), 0.03, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.03) & (df_today['size_scaled']<=0.04), 0.04, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.04) & (df_today['size_scaled']<=0.05), 0.05, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.05) & (df_today['size_scaled']<=0.1), 0.1, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.1) & (df_today['size_scaled']<=0.2), 0.2, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.2) & (df_today['size_scaled']<=0.3), 0.3, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.3) & (df_today['size_scaled']<=0.4), 0.4, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.4) & (df_today['size_scaled']<=0.5), 0.4, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.5) & (df_today['size_scaled']<=0.6), 0.6, df_today['size_scaled'])
    df_today['size_scaled'] = np.where((df_today['size_scaled']>0.6) & (df_today['size_scaled']<=0.7), 0.7, df_today['size_scaled'])
    df_today['size_scaled'] = np.where(df_today['size_scaled'] > 0.7, 0.7, df_today['size_scaled'])

    # making a new column for hover label
    df_today['data_category_fillna'] =  df_today[data_category].fillna(0)

    # selecting continent, latitude and longitude  
    continent_selected = df_continents.loc[df_continents['continent'] == continent]
    latitude = continent_selected.iloc[0]['latitude']
    longitude = continent_selected.iloc[0]['longitude']
    continent_zoom = continent_selected.iloc[0]['zoom']

    # creating the map figure 
    fig_map_continent = px.scatter_mapbox(df_today, 
                               lat=df_today["latitude"], 
                               lon=df_today["longitude"], 
                               color=data_category,
                               size="size_scaled",
                               size_max=100,
                               color_continuous_scale="Mint",
                               range_color=(-100000, 0),
                               opacity=0.5,
                               zoom=continent_zoom,
                               center = {"lat": latitude, "lon": longitude},
                               height=950,
                               mapbox_style="basic",
                               custom_data=['country', 'data_category_fillna'],
                              )

    # updating layout
    fig_map_continent.update_layout(mapbox = dict(pitch=10, accesstoken=st.secrets['token'], style= 'mapbox://styles/mapbox/light-v8'))
    fig_map_continent.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig_map_continent.update_traces(marker_sizemin = 10, hovertemplate = '<b>%{customdata[0]}</b> <br>' + f'{data_category}' + ': %{customdata[1]:,.0f}<extra></extra>')       
    fig_map_continent.update_layout(hovermode='closest')
    fig_map_continent.update_layout(coloraxis_showscale=False)
    return(fig_map_continent)

   
def line_chart(df, df_world, country_list, data_category, date_max, date_min):
    '''This function returns a plotly charth with 2 user inputs selected in the sidebar form '2. Browse in country data': country, data category.
    date_max, date_min are for range selector to display 1 month range as default on x axis. 
    date_max is the update day, date_min is 1 month earlier.
    Optional trace is World data that the user can display in the chart by clicking on it in the legend'''

    df_world = df_world.sort_values('date', ascending=False)
    df = df[df['country'].isin(country_list)].sort_values('date', ascending=False)

    fig = go.Figure()
    
    for i in range(len(country_list)):
        df_country = df.loc[df['country'] == country_list[i]]
        fig.add_trace(go.Scatter(
                            x=df_country['date'],
                            y=df_country[data_category],
                            name=country_list[i],
                            hovertemplate = f'{country_list[i]}'+': %{y:,.0f}<extra></extra>',
                            mode="lines")
                        )
    #formatting chart  
    if len(country_list) == 1:
        fig.update_layout(title = f'{data_category} in the selected country:')
    else:
        fig.update_layout(title = f'{data_category} in the selected countries:')
    fig.update_layout(xaxis_title="Date",
                      yaxis_title=data_category,
                      height=600,
                      margin=dict(l=100, r=150, b=50, t=150, pad=4),
                      hovermode="x",
                     )
    # adding range slider and buttons for setting date range 
    fig.update_layout(xaxis=dict(
                                rangeselector=dict(
                                    buttons=list([
                                        dict(step="all", label="From the beginning"), 
                                        dict(count=1, label="Last 12 months", step="year", stepmode="backward"),
                                        dict(count=6, label="Last 6 months", step="month", stepmode="backward"),
                                        dict(count=3, label="Last 3 months", step="month", stepmode="backward"),
                                        dict(count=1, label="Last month", step="month", stepmode="backward"),
                                        dict(count=7, label="Last week", step="day", stepmode="backward")]
                                    )
                                ),
                                range=[date_min, date_max],
                                rangeslider=dict(visible=True), type="date"),
                        yaxis=dict(autorange= True, fixedrange= False)
    )

    # adding World trace
    fig.add_trace(go.Scatter(x=df_world['date'], 
        y=df_world[data_category],
        mode="lines",
        line=dict(color="#3D3D3D", dash="dash"),
        name = "World", #<br> 
        visible="legendonly", 
        hovertemplate = 'World: %{y}<extra></extra>'
        )
    )
    fig.update_traces(connectgaps=True)
    # setting spikes
    fig.update_xaxes(showspikes=True, spikecolor='grey', spikesnap="cursor", spikemode="across", spikedash='dot')
    fig.update_yaxes(showspikes=True, spikedash='dot')
    fig.update_layout(spikedistance=1000, hoverdistance=100)
    return fig


def bar_chart(df_merged, country_list, date, data_category):
    '''This function returns a barchart sorting countries by descending order in the selected data category 
    on the update day. The countries selected in the user-submit form have red color'''

    # setting color for selected countries
    all_countries_list = df_merged['country'].tolist()
    color_list = []
    for country in all_countries_list:
        if country in country_list:
            color_list.append('#FF4B4B')
        else:
            color_list.append('#636EFA')
    df_merged['bar_colors'] = color_list

    # dropping countries with nan 
    date = str(date)  
    df_date = df_merged[(df_merged['date'] == date)].sort_values(data_category, ascending=True)
    df_isna  = df_date[df_date[data_category].isna()]
    df_date.drop(df_isna.index, axis=0, inplace=True)

    # setting the default displayed range, number of bars     
    xmax = len(df_date.index)
    xmin = xmax-30.5

    # creating the chart figure      
    fig = go.Figure(go.Bar(
                  x=df_date['country'], 
                  y=df_date[data_category],
                  marker={'color' : df_date['bar_colors']},
                  hovertemplate = '%{x}'+': %{y:,.0f}<extra></extra>')
    )

    # updating layout
    fig.update_layout(title = f'{data_category} sorted by descending order on {date}.')
    fig.update_layout(xaxis_title="Countries",
                      yaxis_title=data_category,
                      height=700,
                      margin=dict(l=100, r=150, b=50, t=150, pad=4)),
    fig.update_layout(hovermode='x')
    fig.update_layout(clickmode='select')
    fig.update_layout(xaxis=dict(range=[xmin, xmax]))
    fig.update_layout(yaxis=dict(fixedrange= False))
    fig.update_xaxes(tickangle=45)
    fig.update_xaxes(rangeslider_yaxis_rangemode='match')
    fig.update_xaxes(rangeslider=dict(autorange=True))

    # setting spikes
    fig.update_xaxes(showspikes=True, spikecolor='grey', spikemode="across", spikedash='dot')
    fig.update_yaxes(showspikes=True, spikedash='dot')
    fig.update_layout(spikedistance=1000, hoverdistance=100)
    return fig


if __name__ == "__main__":
    pass  



