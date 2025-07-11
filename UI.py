import streamlit as st
import requests

BACKEND_URL = "https://calculator-ass1-api.onrender.com"  

st.title("Smart Calculator")

operation = st.selectbox("Choose Operation", [
    "Add", "Subtract", "Multiply", "Divide", "Power", "Modulus", "Square Root", "Logarithm", "Evaluate Expression", "View History"
])

if operation in ["Square Root", "Logarithm"]:
    x = st.number_input("Enter number", value=0.0)
    if st.button("Calculate"):
        url = f"{BACKEND_URL}/{'sqrt' if operation == 'Square Root' else 'log'}"
        try:
            response = requests.post(url, json={"x": x})
            result = response.json().get("result")
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

elif operation == "Evaluate Expression":
    expr = st.text_input("Enter expression")
    if st.button("Evaluate"):
        try:
            response = requests.post(f"{BACKEND_URL}/evaluate", json={"expression": expr})
            result = response.json().get("result")
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

elif operation == "View History":
    if st.button("Fetch History"):
        try:
            response = requests.get(f"{BACKEND_URL}/history")
            history = response.json().get("history", [])
            if not history:
                st.info("No history available.")
            else:
                for item in history:
                    st.write(f"{item['operation']} = {item['result']}")
        except Exception as e:
            st.error(f"Error: {e}")

else:
    a = st.number_input("Enter first number", value=0.0)
    b = st.number_input("Enter second number", value=0.0)
    if st.button("Calculate"):
        url = f"{BACKEND_URL}/{operation.lower()}"
        try:
            response = requests.post(url, json={"a": a, "b": b})
            result = response.json().get("result")
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")
