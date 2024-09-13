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

st.sidebar.title("Filters")

all_locations = df["LOCATION"].unique()
selected_locations = st.sidebar.multiselect(
    "Select Locations", all_locations, default=all_locations
)

all_subjects = df["SUBJECT"].unique()
selected_subjects = st.sidebar.multiselect(
    "Select Subjects", all_subjects, default=all_subjects
)

all_time_periods = df["TIME"].unique()
selected_time_periods = st.sidebar.slider(
    "Select Time Period Range", min_value=int(all_time_periods.min()), max_value=int(all_time_periods.max()),
    value=(int(all_time_periods.min()), int(all_time_periods.max())), step=1
)

st.title("PISA Data Analysis")

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
num_rows = st.slider("Number of Rows to View", min_value=5, max_value=50, value=5)
st.dataframe(df.head(num_rows))

st.header("Average PISA Scores by Location")

filtered_df = df[
    df["LOCATION"].isin(selected_locations) &
    df["SUBJECT"].isin(selected_subjects) &
    df["TIME"].between(*selected_time_periods)
]

def plot_average_scores_by_location(df):
    avg_scores = df.groupby("LOCATION")["Value"].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x="Value", y="LOCATION", hue="LOCATION", data=avg_scores, palette="viridis", dodge=False, legend=False)
    plt.title("Average PISA Scores by Location")
    plt.xlabel("Average PISA Score")
    plt.ylabel("Location")
    st.pyplot(plt)

plot_average_scores_by_location(filtered_df)

st.header("PISA Score Trends")

def plot_trend(df, location, subject):
    country_data = df[(df["LOCATION"] == location) & (df["SUBJECT"] == subject)]
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="TIME", y="Value", data=country_data, marker="o")
    plt.title(f"PISA Score Trends for {location} ({subject})")
    plt.xlabel("Year")
    plt.ylabel("PISA Score")
    st.pyplot(plt)

if selected_locations and selected_subjects:
    plot_trend(filtered_df, selected_locations[0], selected_subjects[0])




