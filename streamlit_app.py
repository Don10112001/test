import pandas as pd
import streamlit as st

# Set page config
st.set_page_config(
    page_title="Pharma Sales",
    page_icon="💊",
    layout="wide"
)

# Load data
@st.cache
def load_data():
    uploaded_file = st.file_uploader("Upload a file", type=["xlsx"])
    if uploaded_file is not None:
        data = pd.read_excel(uploaded_file)
        return data

df = load_data()

if df is not None:
    # Create tabs in the sidebar using radio buttons
    tab_selected = st.sidebar.radio("Navigation", ["Summary", "Dashboard"])

    if tab_selected == "Dashboard":
        st.markdown("# 💊 PHARMA | SALES ANALYSIS")
        st.write("## Dashboard")
        # Add dashboard components here

    elif tab_selected == "Summary":
        st.title("Summary")
        # Summary statistics
        st.write("## Summary Statistics")
        st.write(df.describe())

        # Explanation of product categories
        st.write("## Product Categories:")
        st.write("1. □ **Analgesics**: Medications used to relieve pain.")
        st.write("2. □ **Antibiotics**: Drugs used to treat bacterial infections.")
        st.write("3. □ **Antimalarial**: Medications used to prevent or treat malaria.")
        st.write("4. □ **Antipyretics**: Medications used to reduce fever.")
        st.write("5. □ **Antiseptics**: Substances applied to living tissues to reduce the risk of infection.")
        st.write("6. □ **Mood Stabilizers**: Medications used to treat mood disorders.")
