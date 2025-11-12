# app/main.py
import streamlit as st
import plotly.express as px
import pandas as pd
from app.utils import load_all

st.set_page_config(layout='wide', page_title='Solar Cross-Country Comparison')
st.title("Solar Cross-Country Comparison")

# Load data (local)
dfs, df_all = load_all()

# Sidebar widgets
country = st.sidebar.multiselect("Select countries", options=list(dfs.keys()), default=list(dfs.keys()))
metric = st.sidebar.selectbox("Metric", ['GHI','DNI','DHI'])

# Filter
df_vis = df_all[df_all['country'].isin(country)].dropna(subset=[metric])

# Boxplot
st.header(f"{metric} — boxplot by country")
fig = px.box(df_vis, x='country', y=metric, points='outliers', color='country', title=f'{metric} distribution by country')
st.plotly_chart(fig, use_container_width=True)

# Summary table
st.header("Summary table (mean, median, std)")
summary = df_vis.groupby('country')[metric].agg(['mean','median','std']).reset_index()
summary.columns = ['country','mean','median','std']
st.dataframe(summary.style.format({'mean':'{:.2f}','median':'{:.2f}','std':'{:.2f}'}))

# Ranking bar chart by mean
st.header("Ranking by average GHI")
ghi_mean = df_all.groupby('country')['GHI'].mean().reset_index().sort_values('GHI', ascending=False)
fig2 = px.bar(ghi_mean, x='country', y='GHI', title='Mean GHI by country')
st.plotly_chart(fig2, use_container_width=True)

# Statistical test section (basic)
st.header("Statistical test (GHI)")
if st.button("Run Kruskal-Wallis for GHI"):
    from scipy.stats import kruskal
    groups = [dfs[c]['GHI'].dropna().values for c in dfs.keys() if c in dfs]
    stat, p = kruskal(*groups)
    st.write("Kruskal-Wallis stat: {:.4f}, p-value: {:.4e}".format(stat, p))
    if p < 0.05:
        st.markdown("**Result:** Significant differences between at least one pair of countries (p < 0.05).")
    else:
        st.markdown("**Result:** No evidence to reject null hypothesis (groups similar).")

st.markdown("**Note:** This app reads local cleaned CSVs in `data/` — keep `data/` in `.gitignore` and do NOT commit data.")
