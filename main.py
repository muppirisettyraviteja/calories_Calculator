"""
Simple Calorie Calculator - Streamlit App
Run with: streamlit run calorie_calculator_streamlit.py
"""

import streamlit as st


def calculate_bmr(weight_kg, height_cm, age, gender):
    """Mifflin-St Jeor Equation"""
    if gender == "Male":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161


def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        "Sedentary (little or no exercise)": 1.2,
        "Light (exercise 1-3 days/week)": 1.375,
        "Moderate (exercise 3-5 days/week)": 1.55,
        "Active (hard exercise 6-7 days/week)": 1.725,
        "Very Active (very hard exercise & physical job)": 1.9,
    }
    return bmr * activity_multipliers[activity_level]


st.set_page_config(page_title="Calorie Calculator", page_icon="🔥")

st.title("🔥 Calorie Calculator")
st.write("Estimate your daily calorie needs using the Mifflin-St Jeor equation.")

col1, col2 = st.columns(2)

with col1:
    weight_kg = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.5)
    height_cm = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.5)

with col2:
    age = st.number_input("Age (years)", min_value=10, max_value=100, value=25, step=1)
    gender = st.radio("Gender", ["Male", "Female"])

activity = st.selectbox(
    "Activity Level",
    [
        "Sedentary (little or no exercise)",
        "Light (exercise 1-3 days/week)",
        "Moderate (exercise 3-5 days/week)",
        "Active (hard exercise 6-7 days/week)",
        "Very Active (very hard exercise & physical job)",
    ],
)

if st.button("Calculate", type="primary"):
    bmr = calculate_bmr(weight_kg, height_cm, age, gender)
    tdee = calculate_tdee(bmr, activity)

    st.subheader("Results")

    c1, c2 = st.columns(2)
    c1.metric("BMR (at rest)", f"{bmr:.0f} kcal/day")
    c2.metric("TDEE (maintenance)", f"{tdee:.0f} kcal/day")

    st.write("---")
    st.write("**Suggested targets** (~0.5 kg/week change):")
    c3, c4 = st.columns(2)
    c3.metric("Weight Loss", f"{tdee - 500:.0f} kcal/day")
    c4.metric("Weight Gain", f"{tdee + 500:.0f} kcal/day")

    st.caption("Note: These are estimates. Consult a professional for personalized advice.")