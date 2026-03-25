import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('bodyfat_test.pkl','rb'))

st.write("""
# Body Fat Percent Measurement App
""")

st.write("## Enter your data below:")

Density = st.number_input('Density (determined from underwater weighing)', 0.0000, 1.2000, 0.0000 , format="%.4f")
Age = st.number_input('age', 0, 100, 0)
Weight_kg = st.number_input('Weight(kg)', 0.00, 300.00, 0.00)
Height_cm = st.number_input('Height (cm)', 0.00, 300.00, 0.00)
Neck = st.number_input('Neck circumference (cm)', 0.0, 60.0, 0.0 , format="%.1f")
Chest = st.number_input('Chest circumference (cm)', 0.0, 150.0, 0.0 , format="%.1f")
Abdomen = st.number_input('Abdomen 2 circumference (cm)', 0.0, 180.0, 0.0 , format="%.1f")
Hip = st.number_input('Hip circumference (cm)', 0.0, 160.0, 0.0 , format="%.1f")
Thigh = st.number_input('Thigh circumference (cm)', 0.0, 100.0, 0.0 , format="%.1f")
Knee = st.number_input('Knee circumference (cm)', 0.0, 70.0, 0.0 , format="%.1f")
Ankle = st.number_input('Ankle circumference (cm)', 0.0, 50.0, 0.0 , format="%.1f")
Biceps = st.number_input('Biceps (extended) circumference (cm)', 0.0, 60.0, 0.0 , format="%.1f")
Forearm = st.number_input('Forearm circumference (cm)', 0.0, 50.0, 0.0 , format="%.1f")
Wrist = st.number_input('Wrist circumference (cm)', 0.0, 40.0, 0.0 , format="%.1f")
    
Weight = Weight_kg * 2.2046
Height = Height_cm * 0.3937

if st.button("Predict Body fat"):

    input_data = pd.DataFrame([[Density , Age , Weight , Height , Neck , Chest , Abdomen , Hip , Thigh , Knee , Ankle , Biceps , Forearm , Wrist]], columns=["Denity" , "Age" , "Weight" , "Height" , "Neck" , "Chest" , "Abdomen" , "Hip" , "Thigh" , "Knee" , "Ankle" , "Biceps" , "Forearm" , "Wrist"])
    
    predicted_BodyFat = model.predict(input_data)[0]
    
    st.write(f"Estimated Body Fat: {predicted_BodyFat:,.2f} %")
