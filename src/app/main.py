import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Enhanced Dashboard", layout="wide")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    selected_option = st.radio("Select an option:", ["Upload & Plot Data", "Sample Data & Plot"])
    st.markdown("---")
    st.markdown("**Customize Theme**")
    theme = st.selectbox("Choose a theme", ["Light", "Dark"])

# Apply theme styling
if theme == "Dark":
    st.markdown("<style>body { background-color: #2B2B2B; color: white; }</style>", unsafe_allow_html=True)
else:
    st.markdown("<style>body { background-color: #FFFFFF; color: black; }</style>", unsafe_allow_html=True)

# Page Title
st.title("Enhanced Streamlit Dashboard")

# Option 1: Upload & Plot Data
if selected_option == "Upload & Plot Data":
    st.header("Option 1: Upload CSV and Plot Data")

    uploaded_file = st.file_uploader("Choose a CSV file to upload", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.subheader("Uploaded Data Preview")
        st.dataframe(data.head())

        # Download Button
        st.download_button(
            label="Download Uploaded Data as CSV",
            data=data.to_csv(index=False).encode('utf-8'),
            file_name="uploaded_data.csv",
            mime="text/csv"
        )

        st.subheader("Interactive Plot of Uploaded Data")
        if data.shape[1] >= 2:
            x_col = st.selectbox("Select X-axis column", data.columns)
            y_col = st.selectbox("Select Y-axis column", data.columns)

            st.line_chart(data[[x_col, y_col]].set_index(x_col))
        else:
            st.warning("Uploaded data must have at least two columns for plotting.")
    else:
        st.warning("Please upload a CSV file to display and plot the data.")

# Option 2: Sample Data & Plot
elif selected_option == "Sample Data & Plot":
    st.header("Option 2: Display Sample Data and Plot")

    sample_data = {
        "Month": ["January", "February", "March", "April", "May", "June"],
        "Sales": [250, 300, 450, 200, 500, 400]
    }
    df = pd.DataFrame(sample_data)

    # Columns for layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sample Data Preview")
        st.dataframe(df)

        # Download Button
        st.download_button(
            label="Download Sample Data as CSV",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name="sample_data.csv",
            mime="text/csv"
        )

    with col2:
        st.subheader("Sample Data Plot")
        st.bar_chart(df.set_index("Month"))

    # Footer
    st.markdown(
        "<h6 style='text-align: center; color: gray;'>Dashboard Development 📊 using Streamlit</h6>",
        unsafe_allow_html=True
    )
