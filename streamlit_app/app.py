import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

st.set_page_config(layout='wide', page_title='Solar Week0 Dashboard')
st.title("Solar Data Discovery - Week 0")

DATA_DIR = Path(__file__).parents[1] / 'data'
files = {'Benin':'benin_clean.csv','SierraLeone':'sierraleone_clean.csv','Togo':'togo_clean.csv'}

country = st.sidebar.selectbox("Country", list(files.keys()))
fn = files[country]
path = DATA_DIR / fn
if not path.exists():
    st.warning(f"Place cleaned CSV at {path}")
else:
    df = pd.read_csv(path, parse_dates=['Timestamp'])
    st.dataframe(df.head())
    if 'GHI' in df.columns:
        df['date'] = pd.to_datetime(df['Timestamp']).dt.date
        daily = df.groupby('date').mean().reset_index()
        fig = px.line(daily, x='date', y='GHI', title=f'Daily mean GHI - {country}')
        st.plotly_chart(fig, use_container_width=True)
