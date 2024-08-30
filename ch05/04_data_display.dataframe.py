import streamlit as st
import seaborn as sns
import pandas as pd


@st.cache_data
def load_data():
    df = sns.load_dataset("iris")
    return df

def main():
    st.title("Data Display with st.dataframe()")    
    
    # Add a checkbox for controlling the container width
    st.checkbox("Use Container Width", value=False, key="use_container_width")

    # Load the iris dataset
    iris = load_data()
    
    # Display the dataframe with the option to use container width
    st.dataframe(iris, use_container_width=st.session_state.use_container_width)

    # Display the dataframe with the option to use container width
    st.dataframe(iris.iloc[:5,0:3].style.highlight_max(axis=1))



if __name__ == "__main__":
    main()