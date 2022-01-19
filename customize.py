import streamlit as st
import os
PATH = os.path.abspath('')


# setting page config
def page_config():
    st.set_page_config(
        page_title="Covid-19 Dashboard",
        page_icon=PATH + os.sep + 'data/icon.png',
        #  menu_items={
        #      'Get Help': 'https://www.extremelycoolapp.com/help',
        #      'Report a bug': "https://www.extremelycoolapp.com/bug",
        #      'About': "# This is a header. This is an *extremely* cool app!"
        #  }
    )


# setting container css
def container_map():
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
    </style>    
    """,
        unsafe_allow_html=True,
    )

# .main {
#         position: fixed;
#     }
#  .element-container {
#         flex-direction: row;
#     }

def container_map_continent():
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
    </style>    
    """,
        unsafe_allow_html=True,
    )


def container_chart():
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



# setting sidebar css
def sidebar():
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

#if you wanna change sidebar width, just add: 
#width: 450px

def footer(): 
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
    st.markdown("""
        <style>
        .css-ns78wr {
            margin-top: 28px;
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


# def streamlit_menu():
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


def dropdown():
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
