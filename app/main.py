import streamlit as st
from pathlib import Path
print("Libraries imported successfully!")
root_dir=Path(__file__).resolve().parents[1]
model_path=root_dir/"models"/"futiq_best_model.joblib"
history_path=(root_dir/"data"/"processed"/"epl_matches_clean.csv")

#page configuration:
st.set_page_config(
    page_title="FutIQ",
    page_icon="⚽︎",
    layout="wide"
)

st.title("⚽︎ FutIQ")
st.subheader("Football Intelligence and Match Prediction")
st.write("Analyze historical football perfromance"
         "and predict English Premire League match outcomes.")
st.divider()
st.header("System Status")
col1, col2= st.columns(2)
with col1:
    if model_path.exists():
        st.success("Prediction model found.")
    else:
        st.error("Prediction model not found.")
with col2:
    if history_path.exists():
        st.success("History match dataset found.")
    else:
        st.error("Historical match dataset not found.")
st.divider()
st.info("FutIQ is being developed."
        "The prediction dashboard will be available in the next stages.")
#run: straemlit run main.py