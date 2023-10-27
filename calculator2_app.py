# streamlit_calculator.py

import streamlit as st
import math_operation

st.title("Simple Calculator")

x = st.number_input("Enter the first number:")
y = st.number_input("Enter the second number:")

operation = st.selectbox("Select an operation",
                         ("Add", "Subtract", "Multiply", "Divide"))

result = None

if st.button("Calculate"):
    if operation == "Add":
        result = math_operation.add(x, y)
    elif operation == "Subtract":
        result = math_operation.subtract(x, y)
    elif operation == "Multiply":
        result = math_operation.multiply(x, y)
    elif operation == "Divide":
        try:
            result = math_operation.divide(x, y)
        except ZeroDivisionError:
            st.error("Division by zero is not allowed.")

if result is not None:
    st.success(f"Result: {result}")
