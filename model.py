import streamlit as st
import xgboost as xgb
import pandas as pd
from PIL import Image

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Calorie Burn Prediction",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Load the XGBoost model as XGBClassifier
try:
    model = xgb.XGBClassifier()  # Use XGBRegressor() if it's a regression model
    model.load_model('Model/my_model.json')
except Exception as e:
    st.error(f"Error loading model: {e}")

# Add custom CSS to include the background image and classic fonts
st.markdown(
    """
    <style>
    /* Background Image */
    .stApp {
        background-image: url('background.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Classic font styling */
    .title-text {
        color: #ffffff;
        font-family: 'Georgia', serif;
        font-size: 55px;
        font-weight: bold;
        text-align: center;
        text-shadow: 3px 3px 6px #000000;
    }
    .subheader {
        color: #ffffff;
        font-family: 'Times New Roman', Times, serif;
        font-size: 25px;
        text-align: center;
        text-shadow: 2px 2px 5px #000000;
    }
    .input-label {
        color: #ffffff;
        font-family: 'Georgia', serif;
        font-size: 18px;
        font-weight: bold;
    }
    .calculate-btn {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 12px;
        font-family: 'Georgia', serif;
    }
    .footer-text {
        color: #ffffff;
        font-family: 'Times New Roman', Times, serif;
        font-size: 18px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section with Customized Title
st.markdown("<h1 class='title-text'>Calorie Burn Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subheader'>Estimate your calories burnt during exercise</h3>", unsafe_allow_html=True)

# Input Section
st.markdown("## Personal Information")
gender = st.selectbox('Select Gender', ['Male', 'Female'], format_func=lambda x: f"👤 {x}")
age = st.slider('Select Age', 18, 100, 30)
height = st.slider('Height (cm)', 100, 250, 170)
weight = st.slider('Weight (kg)', 30, 200, 70)

st.markdown("## Exercise Details")
duration = st.slider('Duration (minutes)', 10, 120, 30)
heart_rate = st.slider('Heart Rate (bpm)', 60, 200, 80)
body_temp = st.slider('Body Temperature (°C)', 35.0, 42.0, 37.0)

# Customize button with classic font
if st.button('🔥 Calculate Calories Burnt 🔥', key='calculate-btn'):
    # Map gender to numerical value
    gender_mapping = {'Male': 0, 'Female': 1}
    
    # Prepare input data for the model
    input_data = pd.DataFrame({
        'Gender': [gender_mapping[gender]],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'Duration': [duration],
        'Heart_Rate': [heart_rate],
        'Body_Temp': [body_temp],
    })

    # Predict calories burnt using the XGBoost model
    try:
        prediction = model.predict(input_data)
        # Display the result in a styled box
        st.success(f"🔥 You have burned approximately **{int(prediction[0])} calories**! 🔥")
    except Exception as e:
        st.error(f"Error making prediction: {e}")
    
    # Optional: Display an image or gif
    st.image("calories_burned.gif", use_column_width=True)

# Footer
st.markdown("---")
st.markdown("""
    <div class='footer-text'>
    <p>Remember, calories burned depend on several factors including intensity and metabolism.</p>
    <p>Stay healthy and keep moving! 💪</p>
    </div>
""", unsafe_allow_html=True)
