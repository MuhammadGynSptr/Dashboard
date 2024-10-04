import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

csv_file_hour = pd.read_csv("hour.csv")
csv_file_day = pd.read_csv("day.csv")

daily_rentals = csv_file_day.groupby('weekday').agg({
    'cnt': 'sum'
}).reset_index()

hourly_rentals = csv_file_hour.groupby('hr').agg({
    'cnt': 'mean'
}).reset_index()

workingday_rentals = csv_file_hour.groupby('workingday').agg({
    'cnt': 'sum'
}).reset_index()

st.header('Dicoding Collection Dashboard :sparkles:')

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    min_date = pd.to_datetime(csv_file_hour['dteday'].min())
    max_date = pd.to_datetime(csv_file_hour['dteday'].max())
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    st.write(f"Data dari {start_date} hingga {end_date}")

st.subheader("Total Bike Rentals per Day of the Week")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=daily_rentals, x='weekday', y='cnt', ax=ax)
ax.set_title('Total Rentals per Day of the Week')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Total Rentals')
st.pyplot(fig)

st.subheader("Average Bike Rentals by Hour of the Day")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=hourly_rentals, x='hr', y='cnt', ax=ax)
ax.set_title('Average Bike Rentals by Hour of the Day')
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Average Rentals')
st.pyplot(fig)

st.subheader("Bike Rentals: Working Days vs Weekends")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=workingday_rentals, x='workingday', y='cnt', ax=ax)
ax.set_title('Total Rentals: Working Days vs Weekends')
ax.set_xlabel('Working Day (1 = Yes, 0 = No)')
ax.set_ylabel('Total Rentals')
ax.set_xticklabels(['Weekend', 'Working Day'])
st.pyplot(fig)
