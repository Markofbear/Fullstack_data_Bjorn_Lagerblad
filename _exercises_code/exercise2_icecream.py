"""create a simple app in streamlit that lets the user enter a temperature in celsius and it outputs the revenue prediction. 
You can for example use random forest regression to predict the revenue."""

import streamlit as st
import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the data
def load_data():
    data_path = Path(__file__).parents[1] / "data"
    df = pd.read_csv(data_path / "IceCreamData.csv")
    return df

def train_model(df):
    X = df[["Temperature"]]
    y = df["Revenue"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def main():
    st.title("Temperature to Revenue Prediction")

    df = load_data()

    model = train_model(df)

    temperature = st.slider("Select Temperature (°C)", min_value=int(df["Temperature"].min()), max_value=int(df["Temperature"].max()), value=int(df["Temperature"].mean()))
    
    predicted_revenue = model.predict([[temperature]])[0]
    
    st.write(f"Predicted Revenue for {temperature}°C: ${predicted_revenue:.2f}")

if __name__ == "__main__":
    main()
