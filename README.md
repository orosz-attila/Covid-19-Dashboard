# Covid-19 Dashboard

<p align="justify">Interactive dashboard with daily update displaying 23 Covid-19 related data categories on plotly map and charts. According to the user selection criteria, the daily data can be displayed on a scatter world map, the trends of country data in line- and barcharts, with the option of comparing countries in multiple data categories.</p>

<p align="justify">The dashboard is <a href="https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app" target="_blank">deployed with Streamlit</a> and can be found here: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/orosz-attila/covid-19-dashboard])

<p align="justify">The notebook of this dashboard project with detailed comments is also available on <a href="https://colab.research.google.com/drive/1StLDRJ7LVoPS10AULBxVOJo8rDqnt3U8" target="_blank">Jupyter Colab</a>.</p>

## Description 
<ol >
    <li align="justify">streamlit_app.py: contains the codes which runs on Streamlit</li>
    <li align="justify">functions.py: contains the codes of all the functions for data transformation and visualization (except those functions that uses the st.cache(), they can be find in the main file: streamlit_app.py)</li>
    <li align="justify">customize.py: contains the codes for CSS and HTML customization</li>
</ol>

## Requirements 
- streamlit == 1.2.0 
- plotly == 5.3.1
- public token is required for <a href="https://www.mapbox.com/maps/light" target="_blank">mapbox style</a>

## How to use this dashboard?

<ol align="justify">
    <li style='text-align: justify;'>Compare countries on the map. Select a data category, a date and a continent for setting the zoom. Finally, hit Submit. (Hint: select "World" in the continent selector for world view.)</li>
    <li style='text-align: justify;'>Compare countries on line chart. Select one or more data categories and countries. Finally, hit Submit. (Hints: 1. Select the displayed time range on the left corner of the charts or set it with the range selector below. 2. Click on "World" in the legend to display the trace of World data.)</li>
    <li style='text-align: justify;'>Compare countries on bar chart. Select one or more data categories and countries. Finally, hit Submit. (Hint: 1. Set the range of the displayed bars with the range selector below.)</li>
</ol>

Hit Submit once again if you modified the selection criteria.

Hit "Go back to map view" to go back to the main page.

## Data categories
|         | Data Category           | Description  |
| :------------- |:-------------|:-----|
| 1 |`New cases` |  Confirmed cases of COVID-19 on a selected day |
| 2 |`New cases (Last 7-day average)` | The average number of confirmed COVID-19 cases in the last 7 days back from a selected day |
| 3 |`Total cases` | Total confirmed cases of COVID-19 from the beginning of the pandemic until a selected day |
| 4 | `New cases per million`      | Confirmed cases of COVID-19 per 1,000,000 people on a selected day |
| 5 | `New cases per million (Last 7-day average)` | The average of confirmed COVID-19 cases per 1,000,000 people in the last 7 days back from a selected day |
| 6 | `Total cases per million` | Total confirmed cases of COVID-19 per 1,000,000 people from the beginning of the pandemic until a selected day |
| 7 | `New deaths`   | Deaths attributed to COVID-19 on a selected day |
| 8 | `New deaths (Last 7-day average)` | The average number of deaths attributed to COVID-19 in the last 7 days back from a selected day |
| 9 | `Total deaths` | Total deaths attributed to COVID-19 from the beginning of the pandemic until a selected day |
| 10 | `New deaths per million`   | Deaths attributed to COVID-19 per 1,000,000 people on a selected day |
| 11 | `New deaths per million (Last 7-day average)` | The average number of deaths attributed to COVID-19 per 1,000,000 people in the last 7 days back from a selected day |
| 12 | `Total deaths per million` | Total deaths attributed to COVID-19 per 1,000,000 people from the beginning of the pandemic until a selected day|
| 13 | `Patients in intensive care`   | Number of COVID-19 patients in intensive care units (ICUs) on a selected day |
| 14 | `Patients in intensive care per million` | Number of COVID-19 patients in intensive care units (ICUs) per 1,000,000 people on a selected day |
| 15 | `Hospitalized patients` | Number of COVID-19 patients in hospital on a selected day |
| 16 | `Hospitalized patients per million` | Number of COVID-19 patients in hospital per 1,000,000 people on a selected day |
| 17 | `Stringency index`   | Government Response Stringency Index: composite measure based on 9 response indicators including school closures, workplace closures, and travel bans, rescaled to a value from 0 to 100 (100 = strictest response) |
| 18 | `New tests` | Number COVID-19 tests on a selected day |
| 19 | `Total tests` | Total number of COVID-19 tests from the beginning of the pandemic until a selected day 
| 20 | `Reproduction rate` | Real-time estimate of the effective reproduction rate (R) of COVID-19 (<a href="https://github.com/crondonm/TrackingR/tree/main/Estimates-Database" target="_blank">more info</a>) |
| 21 | `People fully vaccinated` | Total number of people who received all doses prescribed by the vaccination protocol |
| 22 | `People fully vaccinated (%)` | Total number of people who received all doses prescribed by the vaccination protocol per 100 people in the total population |
| 23 | `Total boosters (%)` | Total number of COVID-19 vaccination booster doses administered |

<p style='text-align: justify;'>For more information on data collection, please visit the website of Our World in Data (link below at the Data Source section)</p><br> 

Credit to the authors: 

Vaccination dataset: 

    Mathieu, E., Ritchie, H., Ortiz-Ospina, E. et al. A global database of COVID-19 vaccinations. Nat Hum Behav (2021). https://doi.org/10.1038/s41562-021-01122-8

Testing dataset:

    Hasell, J., Mathieu, E., Beltekian, D. et al. A cross-country database of COVID-19 testing. Sci Data 7, 345 (2020). https://doi.org/10.1038/s41597-020-00688-8

<p style='text-align: justify;'>This data has been collected, aggregated, and documented by Cameron Appel, Diana Beltekian, Daniel Gavrilov, Charlie Giattino, Joe Hasell, Bobbie Macdonald, Edouard Mathieu, Esteban Ortiz-Ospina, Hannah Ritchie, Lucas Rodés-Guirao, Max Roser.</p> 

## Data sources
<ul >
    <li style='text-align: justify;'>COVID-19: <a href="https://github.com/owid/covid-19-data/tree/master/public/data" target="_blank">Our World in Data</a></li>
    <li style='text-align: justify;'>Country Coordinates: <a href="https://www.kaggle.com/nikitagrec/world-capitals-gps" target="_blank">Kaggle</a></li>
    <li style='text-align: justify;'>Page Icon: <a href="https://en.wikipedia.org/wiki/File:Coronavirus_icon.svg" target="_blank">Lucbyhet</a></li>
</ul>

## Changelog
19-01-22: v1.0 Uploaded

01-02-22: v1.0 Updates:
<ul>
    <li style='text-align: justify;'>Function for loading the Covid database changed to with 'st.cache(ttl=3600)', so it reruns if the   last update was more than 1 hour ago.</li> 
    <li style='text-align: justify;'>At submit form '1. Compare countries on the map': default data category was set to 'New cases'</li>
    <li style='text-align: justify;'>Map: default data category on initial map changed to 'New cases'</li>
    <li style='text-align: justify;'>Map: hovertemplate corrected, date removed, only country and data category is displayed, numerical data rounded</li>
    <li style='text-align: justify;'>all HTML codes moved to the file 'customize.py'</li>
    <li style='text-align: justify;'>'Back to map view' button:  margin-top corrected</li>
    <li style='text-align: justify;'>Github link: changed to the link of the separate repo (main)</li>
    <li style='text-align: justify;'>Barchart: Height changed to 700</li>
</ul>

## Further developments
<ul >
    <li style='text-align: justify;'>Adding forecasting function in all data categories (ARIMA)</li>
    <li style='text-align: justify;'>Adding automatic interpretation of trends and evaluation of figures (with streamlit function st.metrics())</li>
    <li style='text-align: justify;'>Linking scatter map and charts with mouse click/select event</li>
</ul>

## License 
<p align="justify">Code of this app is created by Attila Orosz and completely open access under the <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons BY license</a>. You have the permission to use, distribute, and reproduce these in any medium, provided the source and authors are credited.</p> 
