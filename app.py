import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def load_data(path):
    df = pd.read_csv(path, parse_dates=['date'])
    return df

# Load and clean data
df = load_data('data/owid-covid-data.csv')
countries = st.sidebar.multiselect('Select Countries', df['location'].unique(), ['United States', 'India', 'Kenya'])
start_date = st.sidebar.date_input('Start Date', df['date'].min())
end_date = st.sidebar.date_input('End Date', df['date'].max())
df = df[df['location'].isin(countries) & (df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

st.title('COVID-19 Global Data Tracker')

# Line Chart: Total Cases
st.subheader('Total Cases Over Time')
fig1 = px.line(df, x='date', y='total_cases', color='location')
st.plotly_chart(fig1)

# Line Chart: Total Deaths
st.subheader('Total Deaths Over Time')
fig2 = px.line(df, x='date', y='total_deaths', color='location')
st.plotly_chart(fig2)

# Vaccination Progress
if 'total_vaccinations' in df:
    st.subheader('Vaccination Progress')
    fig3 = px.line(df, x='date', y='total_vaccinations', color='location')
    st.plotly_chart(fig3)

# Choropleth Map
st.subheader('Global Cases Map')
latest = df.groupby('iso_code').apply(lambda x: x.loc[x['date'].idxmax()])[['iso_code','total_cases']].reset_index(drop=True)
fig4 = px.choropleth(latest, locations='iso_code', color='total_cases', hover_name='iso_code', color_continuous_scale='Viridis')
st.plotly_chart(fig4)