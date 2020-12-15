import streamlit as st 

import pandas as pd
from pandas_profiling import ProfileReport
import codecs

import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(
    page_title="Data Mining: Assignment 02",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

@st.cache
def load_data(data_file):
    return pd.read_csv(data_file, error_bad_lines=False)

def main():
    st.sidebar.title('Options')
    menu = ['Home', 'Data Exploration']
    choice = st.sidebar.selectbox("Menu", menu)
    if choice  == 'Data Exploration':
        st.markdown('''
        <h1 style="text-align: center">
        Exploration
        </h1>''', unsafe_allow_html=True)
        # datafile = st.file_uploader('Upload a CSV file.', type=['csv', 'txt'])

        # if datafile is not None:
        #     df = pd.read_csv(datafile, error_bad_lines=False)
        #     # st.dataframe(df.head())
        #     profile = ProfileReport(df)
        #     st_profile_report(profile)
        df = load_data('Assignment2.csv')
        profile = ProfileReport(df)
        st_profile_report(profile)

    else:
        st.markdown('''
        <h1 style="text-align: center">
        PMASDS18: Data Mining
        </h1>''', unsafe_allow_html=True)
        # st.subheader('Assignment 02')
        st.markdown('''
        <div style="text-align: center">

        -----
        ### Submitted By

        Shanto Jourder - 201900101012 \n
        Md. Meftaul Haque Mishu - 201900101040

        ------
        ### Submitted To
        Dr. Md Rezaul Karim

        -----
        #### 15th December 2020

        </div>
        ''', unsafe_allow_html=True)

if __name__ == '__main__':
    main()