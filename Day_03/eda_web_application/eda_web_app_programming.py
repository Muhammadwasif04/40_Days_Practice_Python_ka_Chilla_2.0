import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#Ttile of Webapp
st.markdown('''
# **EDA Web Application**
# This is a web application that can be used to perform exploratory data analysis on a dataset.''')

# How to upload a file from your computer

with st.sidebar.header('Upload your Dataset(must be CSV file)'):
    uploaded_file = st.sidebar.file_uploader("Upload your Dataset", type=["csv"])
    df = sns.load_dataset("titanic")
    st.sidebar.markdown('[Example CSV File](df)')

# Profiling report for pandas
if uploaded_file is not none:

    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    profile = ProfileReport(df,explorative=True)
    st.header('**Input of**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report of Pandas**')
    st_profile_report(profile)
else:
    st.info('Awating for your dataset')
    if st.button('Press to use example data'):
        # Example dataset

        def load_data():
            a= pd.DataFrame(np.random.randn(100,5),columns=['A','B','C','D']))
            return a
        df = load_data()
            profile = ProfileReport(df,explorative=True)
        st.header('**Input of**')
        st.write(df)
        st.write('---')
        st.header('**Profiling report of Pandas**')
        st_profile_report(profile)