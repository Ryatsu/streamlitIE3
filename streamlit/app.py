import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import calendar
from datetime import datetime

# Title of the Streamlit app
st.title("Clint Villaflores' random streamlit contents")

# Sidebar with calculator
st.sidebar.header("Calculator")
num1 = st.sidebar.number_input("Enter first number", value=0.0)
num2 = st.sidebar.number_input("Enter second number", value=0.0)
operation = st.sidebar.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

st.sidebar.write("Result:", result)

# Sidebar with calendar as a table
st.sidebar.header("Calendar")

# Initialize session state for month and year if not already done
if "month" not in st.session_state:
    st.session_state.month = datetime.now().month
    st.session_state.year = datetime.now().year

# Button to go to previous month
prev_month = st.sidebar.button("Previous Month")
if prev_month:
    if st.session_state.month == 1:
        st.session_state.month = 12
        st.session_state.year -= 1
    else:
        st.session_state.month -= 1

# Button to go to next month
next_month = st.sidebar.button("Next Month")
if next_month:
    if st.session_state.month == 12:
        st.session_state.month = 1
        st.session_state.year += 1
    else:
        st.session_state.month += 1

# Generate calendar for the current session state month and year
month_calendar = calendar.monthcalendar(st.session_state.year, st.session_state.month)
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Create a DataFrame for the calendar
df_calendar = pd.DataFrame(month_calendar, columns=days_of_week)

st.sidebar.write(f"{calendar.month_name[st.session_state.month]} {st.session_state.year}")
st.sidebar.table(df_calendar)

# File uploader for CSV files
st.header("Upload a CSV File")
uploaded_file = st.file_uploader("Choose a CSV file to table it", type="csv")

if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.text("Click the X to go back to original -------> here ^")
    
    st.subheader("Data from the uploaded file:")
    st.write(df_uploaded)

    # Plot data using Matplotlib
    st.subheader("Matplotlib Plot")
    fig, ax = plt.subplots()
    ax.plot(df_uploaded.index, df_uploaded.iloc[:, 0], 'o-')
    ax.set_xlabel("Index")
    ax.set_ylabel(df_uploaded.columns[0])
    ax.set_title("Matplotlib Plot")
    st.pyplot(fig)

    # Plot data using Plotly
    st.subheader("Plotly Scatter Plot")
    fig = px.scatter(df_uploaded, x=df_uploaded.index, y=df_uploaded.columns[0], title="Plotly Scatter Plot")
    st.plotly_chart(fig)

# Mapping feature
st.header("Map Visualization")
st.text("To find Cebu, Philippines \nLatitude: 10.30° N \nLongitude: 123.91° E")

# Default location to display on the map
latitude = st.number_input("Enter latitude", value=10.3157)
longitude = st.number_input("Enter longitude", value=123.8854)

st.map(pd.DataFrame({'lat': [latitude], 'lon': [longitude]}))

# Main app for manual data input if no file is uploaded
if uploaded_file is None:
    st.header("Input Data for Chart and Table")

    # Input for row and column names
    rows = st.text_area("Enter row names (comma-separated)", "Row1, Row2, Row3")
    cols = st.text_area("Enter column names (comma-separated)", "Col1, Col2, Col3")

    # Convert input into list
    row_list = [r.strip() for r in rows.split(",")]
    col_list = [c.strip() for c in cols.split(",")]

    # Create a dataframe to hold data
    data = np.random.randn(len(row_list), len(col_list))
    df = pd.DataFrame(data, index=row_list, columns=col_list)

    # Display the dataframe as a table
    st.subheader("Table")
    st.write(df)

    # Plot the dataframe as a chart
    st.subheader("Chart")
    st.line_chart(df)

    # Mapping to another content (example: adding a suffix to each cell)
    suffix = st.text_input("Enter suffix to map content", "_mapped")
    df_mapped = df.applymap(lambda x: f"{x}{suffix}")

    st.subheader("Mapped Data")
    st.write(df_mapped)
