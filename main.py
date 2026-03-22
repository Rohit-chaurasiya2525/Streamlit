import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
df = pd.read_csv('startup_clean.csv')
def load_investor(investor):
    st.title(investor)
    last5_df = df[df['Investors Name'].str.contains('North Base Media',na = False)]
    st.subheader('Most recent Investments')
    st.dataframe(last5_df)
    #biggest investments
    col1,col2 = st.columns(2)
    with col1:
        big_investments = df[df['Investors Name'].str.contains(investor, na=False)] \
            .groupby('startup')['amount'] \
            .sum() \
            .sort_values(ascending=False)
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_investments.index, big_investments.values)
        st.pyplot(fig)
        plt.show()

        st.dataframe(big_investments)
    with col2:
        vertical = df[df['Investors Name'].str.contains(investor, na=False)] \
            .groupby('Industry Vertical')['amount'] \
            .sum() \
            .plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
        st.subheader('Sector Investments')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical)
        plt.show(fig1)



option = st.sidebar.selectbox('Select One',['OverAll Analysis','Startup','Investor'])
st.sidebar.title('Startup Funding Analysis')

if option == 'OverAll Analysis':
    st.title('OverAll Analysis')
elif option =='Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup')
else:
    investor_name = st.sidebar.selectbox('Select Investor',sorted(set(df['Investors Name'].dropna().str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor(investor_name)

    st.title('Investor Analysis')
