import streamlit as st
import pandas as pd
from pathlib import Path

def read_data():
    data_path = Path(__file__).parents[1] / "data"
    df = pd.read_csv(data_path / "supahcoolsoft.csv")
    return df

def number_of_employees(df):
    return df['EmployeeID'].nunique()

def layout():
    df = read_data()
    
    st.title("Info Employes")  
    st.dataframe(df)
    st.write("## Describe")
    st.write(df.describe())
    average_employees = number_of_employees(df)
    st.write(f"Number of employees: {average_employees}")

if __name__ == "__main__":
    layout()
