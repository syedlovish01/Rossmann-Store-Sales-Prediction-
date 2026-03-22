import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("rossmann_rf_lag.pkl")

st.title("Rossmann Store Sales Prediction")
st.write("Enter the store details below to predict daily sales.")

store = st.number_input("Store", min_value=1, value=1)
day_of_week = st.selectbox("Day of Week", [1, 2, 3, 4, 5, 6, 7])
open_store = st.selectbox("Open", [0, 1], index=1)
promo = st.selectbox("Promo", [0, 1])
state_holiday = st.selectbox("StateHoliday", [0, 1, 2, 3])
school_holiday = st.selectbox("SchoolHoliday", [0, 1])
store_type = st.selectbox("StoreType", [0, 1, 2, 3])
assortment = st.selectbox("Assortment", [0, 1, 2])
competition_distance = st.number_input("CompetitionDistance", min_value=0.0, value=1000.0)
competition_open_since_month = st.number_input("CompetitionOpenSinceMonth", min_value=0.0, max_value=12.0, value=0.0)
competition_open_since_year = st.number_input("CompetitionOpenSinceYear", min_value=0.0, value=0.0)
promo2 = st.selectbox("Promo2", [0, 1])
promo2_since_week = st.number_input("Promo2SinceWeek", min_value=0.0, max_value=52.0, value=0.0)
promo2_since_year = st.number_input("Promo2SinceYear", min_value=0.0, value=0.0)
promo_interval = st.selectbox("PromoInterval", [0, 1, 2, 3])
month = st.selectbox("Month", list(range(1, 13)))
year = st.number_input("Year", min_value=2013, max_value=2030, value=2015)
day = st.number_input("Day", min_value=1, max_value=31, value=1)
lag_1 = st.number_input("Lag_1 (Previous day sales)", min_value=0.0, value=5000.0)
lag_7 = st.number_input("Lag_7 (Previous week sales)", min_value=0.0, value=5000.0)

if st.button("Predict Sales"):
    input_data = pd.DataFrame([{
        "Store": store,
        "DayOfWeek": day_of_week,
        "Open": open_store,
        "Promo": promo,
        "StateHoliday": state_holiday,
        "SchoolHoliday": school_holiday,
        "StoreType": store_type,
        "Assortment": assortment,
        "CompetitionDistance": competition_distance,
        "CompetitionOpenSinceMonth": competition_open_since_month,
        "CompetitionOpenSinceYear": competition_open_since_year,
        "Promo2": promo2,
        "Promo2SinceWeek": promo2_since_week,
        "Promo2SinceYear": promo2_since_year,
        "PromoInterval": promo_interval,
        "Month": month,
        "Year": year,
        "Day": day,
        "Lag_1": lag_1,
        "Lag_7": lag_7
    }])

    # Force same column order as training
    input_data = input_data[model.feature_names_in_]

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Sales: {prediction:,.2f}")