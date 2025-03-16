



import streamlit as st

# Title of the application
st.title("Unit Converter")

# Sidebar for selecting the type of conversion
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Temperature", "Length"])

if conversion_type == "Temperature":
    st.header("Temperature Conversion")
    
    # Input temperature
    input_temp = st.number_input("Enter the Temperature", value=0.0)
    
    # Select the original unit
    original_unit = st.selectbox("Select the original unit", ["Celsius", "Fahrenheit"])
    
    # Select the target unit
    target_unit = st.selectbox("Select the target unit", ["Celsius", "Fahrenheit"])
    
    # Conversion logic
    if original_unit == "Celsius" and target_unit == "Fahrenheit":
        converted_temp = (input_temp * 1.8) + 32
        st.success(f"Converted temperature: {converted_temp}°F")
    elif original_unit == "Fahrenheit" and target_unit == "Celsius":
        converted_temp = (input_temp - 32) / 1.8
        st.success(f"Converted temperature: {converted_temp}°C")
    elif original_unit == target_unit:
        st.success(f"Converted temperature: {input_temp}°{original_unit[0]}")
    else:
        st.error("Invalid conversion selected")

elif conversion_type == "Length":
    st.header("Length Conversion")
    
    # Input length
    input_length = st.number_input("Enter the Length", value=0.0)
    
    # Select the original unit
    original_unit = st.selectbox("Select the original unit", ["Meters", "Feet"])
    
    # Select the target unit
    target_unit = st.selectbox("Select the target unit", ["Meters", "Feet"])
    
    # Conversion logic
    if original_unit == "Meters" and target_unit == "Feet":
        converted_length = input_length * 3.28084
        st.success(f"Converted length: {converted_length} feet")
    elif original_unit == "Feet" and target_unit == "Meters":
        converted_length = input_length / 3.28084
        st.success(f"Converted length: {converted_length} meters")
    elif original_unit == target_unit:
        st.success(f"Converted length: {input_length} {original_unit.lower()}")
    else:
        st.error("Invalid conversion selected")