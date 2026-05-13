import streamlit as st
import pickle
st.write("enter the values required if youre diabetic or not")
a=st.number_input("enter your pregnancy month")
b=st.number_input("enter your BMI")
c=st.number_input("enter your age")
d=st.number_input("enter your glucose")
if st.button("predict"):
    with open(r"C:\Users\nanda\PycharmProjects\akira\diabetic.pkl", "rb") as file:
        loaded_model = pickle.load(file)
    result=loaded_model.predict([[a,b,c,d]])
    st.write(result)