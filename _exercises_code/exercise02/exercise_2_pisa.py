"""## 2. PISA scores


- basic statistics of the data (number of records, number of locations, subjects, and time periods)
- show a table with sample data
- bar chart showing average PISA scores by location
- plot trends that can be filtered for each country 
  
Bonus:
- more interactive filtering to drill down to specific locations, time period, subjects, ... 
- this filtering should be displayed on a side panel"""


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

@st.cache_data  # Speeds up function
def read_data():
    data_path = Path(__file__).parents[2] / "data"
    df = pd.read_csv(data_path / "pisa_data.csv")
    return df

df = read_data()

st.title("PISA Data Analyze")

def basic_statistics(df):
    num_records = df.shape[0]
    num_locations = df["LOCATION"].nunique()
    num_subjects = df["SUBJECT"].nunique()
    num_time_periods = df["TIME"].nunique()
    
    st.write(f"Number of records: {num_records}")
    st.write(f"Number of locations: {num_locations}")
    st.write(f"Number of subjects: {num_subjects}")
    st.write(f"Number of time periods: {num_time_periods}")

st.header("Basic Statistics")
basic_statistics(df)

st.header("Sample Data")
num_rows = st.slider("Rows", min_value=5, max_value=50)
st.dataframe(df.head(num_rows))

st.header("Average PISA Scores by Location")
all_locations = df["LOCATION"].unique()

selected_locations = st.multiselect(
    "Select Locations (blank = all)", all_locations, default=all_locations
)

def plot_average_scores_by_location(df, locations):
    if locations:
        df = df[df["LOCATION"].isin(locations)]
    
    avg_scores = df.groupby("LOCATION")["Value"].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x="Value", y="LOCATION", hue="LOCATION", data=avg_scores, palette="viridis", dodge=False, legend=False)
    plt.title("Average PISA Scores by Location")
    plt.xlabel("Average PISA Score")
    plt.ylabel("Location")
    st.pyplot(plt)

plot_average_scores_by_location(df, selected_locations)


st.header("PISA Score Trends")
selected_country = st.selectbox("Select a Country", df["LOCATION"].unique())
selected_subject = st.selectbox("Select a Subject", df["SUBJECT"].unique())

def plot_trend(df, location, subject):
    country_data = df[(df["LOCATION"] == location) & (df["SUBJECT"] == subject)]
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="TIME", y="Value", data=country_data, marker="o")
    plt.title(f"PISA Score Trends for {location} ({subject})")
    plt.xlabel("Year")
    plt.ylabel("PISA Score")
    st.pyplot(plt)

plot_trend(df, selected_country, selected_subject)




