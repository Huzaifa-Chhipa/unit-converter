import streamlit as st

st.title("Simple Unit Converter")

value = st.number_input("Enter value", value=1.0)

from_unit = st.selectbox("From", ["meter", "kilometer", "centimeter"])
to_unit = st.selectbox("To", ["meter", "kilometer", "centimeter"])

if from_unit == "meter":
    converted_value = value
elif from_unit == "kilometer":
    converted_value = value * 1000 
elif from_unit == "centimeter":
    converted_value = value / 100 

if to_unit == "meter":
    result = converted_value
elif to_unit == "kilometer":
    result = converted_value / 1000 
elif to_unit == "centimeter":
    result = converted_value * 100
    
st.write(f"**Result:** {result:.2f} {to_unit}")