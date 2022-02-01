import streamlit as st
import os
PATH = os.path.abspath('')


def page_config():
    '''This function is built-in streamlit function for page configuration'''
    st.set_page_config(
        page_title="Covid-19 Dashboard",
        page_icon=PATH + os.sep + 'data/icon.png'
    )


def container_map():
    '''This function customizes container css if it is in the map view'''
    st.markdown(
        """
    <style>
    .css-1v3fvcr {
        position: static;
        flex-direction: row;
        overflow: visible;
    }
    .reportview-container .main .block-container{
        max-width: 100%;
        padding-top: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        padding-bottom: 0rem;
    }
    .css-12oz5g7 {
        margin-top: -112px;
        margin-bottom: -64px;
    }
    .js-plotly-plot .plotly .modebar{
        position: fixed;
        right: 70px;
        top: 15px;
    }
    .js-plotly-plot .plotly .mapboxgl-ctrl-bottom-right{
        position: fixed;
        }
    .js-plotly-plot .plotly .modebar--hover > :not(.watermark){
        padding-bottom: 8px;
    }
    </style>    
    """,
        unsafe_allow_html=True,
    )


def container_map_continent():
    '''This function customizes container css in the map view and if a continent is selected'''
    st.markdown(
        """
    <style>
    .css-1v3fvcr {
        position: static;
        flex-direction: row;
        overflow: visible;
    }
    .reportview-container .main .block-container{
        max-width: 100%;
        padding-top: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        padding-bottom: 0rem;
    }
    .css-12oz5g7 {
        margin-top: -64px;
        margin-bottom: -64px;
    }
    .js-plotly-plot .plotly .modebar{
        position: fixed;
        right: 70px;
        top: 15px;
    }
    .js-plotly-plot .plotly .mapboxgl-ctrl-bottom-right{
        position: fixed
    }
    .js-plotly-plot .plotly .modebar--hover > :not(.watermark){
        padding-bottom: 8px;
    }
    </style>    
    """,
        unsafe_allow_html=True,
    )


def container_chart():
    '''This function customizes container css in chart view'''
    st.markdown(
        """
    <style>
    .css-1v3fvcr {
        position: relative;
        flex-direction: column;
        overflow: auto;
    }
    .reportview-container .main .block-container{
        max-width: 100%;
        padding-top: 1rem;
        padding-left: 0rem;
        padding-right: 0rem;
        padding-bottom: 0rem;
    }
    .css-12oz5g7 {
        margin-top: -64px;
        margin-bottom: -64px;
    }
    .js-plotly-plot .plotly .modebar{
        position: absolute;
        right: 32px;
        top: 80px;
    }
    </style>    
    """,
        unsafe_allow_html=True,
    )


def sidebar():
    '''This function customizes sidebar css'''
    st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        padding-top: 0rem;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        padding-top: 0rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# if you wanna change sidebar width, just add: width: 450px


def footer():
    '''This function customizes footer css''' 
    st.markdown("""
    <style>
    footer {
        visibility: hidden;
    }
    .css-12gp8ed {
        max-width: 0rem;
        padding: 0rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def back_to_map_button():
    '''This function customizes back_to_map button css'''
    st.markdown("""
        <style>
        .css-ns78wr {
            margin-top: 18px;
            margin-left: 64px;
            border-color: rgb(255, 75, 75);
            background-color: rgb(255, 75, 75);
            color: white;
        }
        .css-ns78wr:hover {
            background-color: white;
            color: rgb(255, 75, 75);
        }
        </style>    
        """,
        unsafe_allow_html=True,
)


def dropdown():
    '''This function customizes dropdown menu css'''
    st.markdown(
        """
    <style>
    .css-1d0tddh {
        text-overflow: clip;
        overflow: revert;
         white-space: nowrap;
    }
    </style>    
    """,
        unsafe_allow_html=True,
    )


# def streamlit_menu():
#    '''This function customizes menu button css'''
#     st.markdown(
#         """
#     <style>
#     .css-d1b1ld {
#         margin-top: 48px;
#     }
#     </style>    
#     """,
#         unsafe_allow_html=True,
#     )

def expander_html_1():
    st.write("""
        <p style='text-align: justify;'><b>Welcome to my Dashboard!</b></p>
        
        <p style='text-align: justify;'>Select from 23 daily updated COVID-19 related data categories to visualize trends of the pandemic in different countries or continents and the world.</p>

        <p style='text-align: justify;'><b>1. Compare countries on the map.</b> Select a data category, a date and a continent for setting the zoom. Finally, hit Submit. (Hint: select "World" in the continent selector for world view.)</p>
        
        <p style='text-align: justify;'><b>2. Compare countries on line chart.</b> Select one or more data categories and countries. Finally, hit Submit. (Hints: 1. Select the displayed time range on the left corner of the charts or set it with the range selector below. 2. Click on "World" in the legend to display the trace of World data.)</p>
        
        <p style='text-align: justify;'><b>3. Compare countries on bar chart.</b> Select one or more data categories and countries. Finally, hit Submit. (Hint: 1. Set the range of the displayed bars with the range selector below.)</p>

        <p style='text-align: justify;'>Hit Submit once again if you modified the selection criteria.</p>
        
        <p style='text-align: justify;'>Hit "Go back to map view" to go back to the main page.</p>
        """, 
        unsafe_allow_html=True,
        )

def expander_html_2():
    st.write("""
        <p><b>1. Sources:</b></p> 
        <ul style= 'margin-bottom: 16px;'>
            <li>COVID-19: <a href="https://github.com/owid/covid-19-data/tree/master/public/data" target="_blank">Our World in Data</a>, License: <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">“CC BY-ND 4.0”</a></li>
            <li>Country Coordinates: <a href="https://www.kaggle.com/nikitagrec/world-capitals-gps" target="_blank">Kaggle</a></li>
            <li>Page Icon: <a href="https://en.wikipedia.org/wiki/File:Coronavirus_icon.svg" target="_blank">Lucbyhet</a>,<br>License: <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">“CC BY-ND 4.0”</a></li>
        </ul> 
        <p><b>2. COVID-19 data categories:</b></p>
        <ol style= 'margin-bottom: 16px;'>
            <li>New cases</li>
            <li>New cases (Last 7-day average)</li>
            <li>Total cases</li>
            <li>New cases per million</li>
            <li>New cases per million (Last 7-day average)</li>
            <li>Total cases per million</li>
            <li>New deaths</li>
            <li>New deaths (Last 7-day average)</li>
            <li>Total deaths</li>
            <li>New deaths per million</li>
            <li>New deaths per million (Last 7-day average)</li>
            <li>Total deaths per million</li>
            <li>Patients in intensive care</li>
            <li>Patients in intensive care per million</li>
            <li>Hospitalized patients</li>
            <li>Hospitalized patients per million</li>
            <li>Stringency index</li>
            <li>New tests</li>
            <li>Total tests</li>
            <li>Reproduction rate</li>
            <li>People fully vaccinated</li>
            <li>People fully vaccinated (%)</li>
            <li>Total boosters (%)</li>
        </ol>
        <p style='text-align: justify;'>For more information on the data categories, please visit the Github repository (link below)</p>


        <p><b>3. Further developments:<b></p>
        <ul style= 'margin-bottom: 16px;'>
            <li>Adding forecasting function in all data categories (ARIMA)</li>
            <li>Automatic interpretation of trends and evaluation of figures</li>
            <li>Linking scatter map and charts with mouse click/select event</li>
        </ul>

        <p><b>4. Created by Attila Orosz: <a href="https://github.com/orosz-attila/Covid-19-Dashboard" target="_blank">Github</a><b></p>
        """, 
        unsafe_allow_html=True,
        )