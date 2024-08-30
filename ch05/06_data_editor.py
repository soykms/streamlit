import streamlit as st
import seaborn as sns
import pandas as pd


@st.cache_data
def load_data():
    df = pd.read_csv("profile.csv", parse_dates=['birthdate']).dropna()
    return df

def main():
    st.title("Data Display st.data_editor()")    
   
    data=load_data()
    st.dataframe(data)


if __name__ == "__main__":
    main()