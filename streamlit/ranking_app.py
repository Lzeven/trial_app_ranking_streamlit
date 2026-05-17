import streamlit as st
import joblib
import sklearn
import pickle
import numpy as np
import os 

st.title('Ranking prediction App for N-gage')
try:
        
        model = joblib.load('student_gamifi_ranking_model.pkl')
except FileNotFoundError:
        st.error("file not found, make sure the file is in the same folder. ")

Past_Sem1_Total = st.number_input("Past 1st Semester total points :", min_value=0, max_value=2000, value=10, key="Past_Sem1_Total")
Past_Sem1_Ev1 = st.number_input("Past 1st Semester Event 1 points :", min_value=0, max_value=2000, value=10, key="Past_Sem1_Ev1")
Past_Sem1_Ev2 = st.number_input("Past 1st Semester Event 2 points :", min_value=0, max_value=2000, value=10, key="Past_Sem1_Ev2")
Past_Sem1_Ev3 = st.number_input("Past 1st Semester Event 3 points :", min_value=0, max_value=2000, value=10, key="Past_Sem1_Ev3")
Past_Sem1_Rank = st.number_input("Past 1st Semester Rank :", min_value=0, max_value=2000, value=10, key="Past_Sem1_Rank")
Past_Sem2_Total = st.number_input("Past 2nd Semester total points :", min_value=0, max_value=2000, value=10, key="Past_Sem2_Total")
Past_Sem2_Ev1 = st.number_input("Past 2nd Semester Event 1 points :", min_value=0, max_value=2000, value=10, key="Past_Sem2_Ev1")
Past_Sem2_Ev2 = st.number_input("Past 2nd Semester Event 2 points :", min_value=0, max_value=2000, value=10, key="Past_Sem2_Ev2")
Past_Sem2_Ev3 = st.number_input("Past 2nd Semester Event 3 points :", min_value=0, max_value=2000, value=10, key="Past_Sem2_Ev3")
Past_Sem2_Rank = st.number_input("Past 2nd semester rank:",min_value=0, max_value=2000, value=10, key="Past_Sem2_Rank")
Current_Sem_Total = st.number_input("Current Semester Total points :",min_value=0, max_value=2000, value=10, key="Current_Sem_Total")
Current_Ev1 = st.number_input("Current Semester Event 1 points :",min_value=0, max_value=2000, value=10, key="Current_Ev1")
Current_Ev2 = st.number_input("Current Semester Event 2 points :",min_value=0, max_value=2000, value=10, key="Current_Ev2")

if st.button("predict this semester's Rank"):
        input_data = np.array([[Past_Sem1_Total,
                                Past_Sem1_Ev1,
                                Past_Sem1_Ev2,
                                Past_Sem1_Ev3,
                                Past_Sem1_Rank,
                                Past_Sem2_Total,
                                Past_Sem2_Ev1,
                                Past_Sem2_Ev2,
                                Past_Sem2_Ev3,
                                Past_Sem2_Rank,
                                Current_Sem_Total,
                                Current_Ev1,
                                Current_Ev2]])
        
        prediction = model.predict(input_data)

        st.success (f"Predicted Rank:{prediction[0]:.2f}")
