"""" 0. Supahcoolsoft employee executive dashboard
Create a dashboard in streamlit displaying this employee data to the executives. Call it Executive dashboard for coolness sake. It should contain:

* basic statistics on employees (total count, average age, average salary)
* show a table with employee details
* bar chart showing number of employees accross departments
* histogram of salary distribution
* box plot of salaries by department
* histogram of age distribution
* box plot of ages by department
* Style the dashboard to make it more exclusive for executives. """


import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

def read_data():
    data_path = Path(__file__).parents[1] / "data"
    df = pd.read_csv(data_path / "supahcoolsoft.csv")
    return df

def layout():
    df = read_data()
    
    st.title("Executive Dashboard")  
    
    # Show a table with employee details
    st.markdown("### Info Employees")
    st.dataframe(df)
    
    # Basic statistics on employees (total count, average age, average salary)
    st.write("## Employees Details")
    st.write(df.describe())
    
    # Show the total number of employees
    st.write(f"## Number of employees: {df['EmployeeID'].nunique()}")
    
    # Plot employees across departments
    st.write("### Number of Employees per Department")
    dept_df = df.groupby("Department")["EmployeeID"].nunique().reset_index()
    fig = px.bar(dept_df, x="Department", y="EmployeeID")
    st.plotly_chart(fig)

    # Histogram of salary distribution
    st.write("### Salary Distribution")
    fig = px.histogram(df, x='Salary_SEK', nbins=30)
    st.plotly_chart(fig)
   
    #histogram of age distribution
    st.write("### Age Distribution")
    fig = px.histogram(df, x='Age', nbins=30)
    st.plotly_chart(fig)

    # Box plot of salaries by department
    st.write("### Salaries By Department")
    fig = px.box(df, x="Department", y="Salary_SEK")
    st.plotly_chart(fig)

    # Box plot of ages by department
    st.write("### Ages Of Department")
    fig = px.box(df, x="Age", y="Salary_SEK")
    st.plotly_chart(fig)

if __name__ == "__main__":
    layout()



