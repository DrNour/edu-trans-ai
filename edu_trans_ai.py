import streamlit as st
import pandas as pd
from difflib import SequenceMatcher

st.title("EduTransAI - Translation Assessment Tool")

# Upload CSV file widget
uploaded_file = st.file_uploader("Upload your translations CSV file", type=["csv"])

if uploaded_file is not None:
    # Try reading the CSV with UTF-8 encoding; fallback to latin1 if error
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(uploaded_file, encoding='latin1')
    
    st.success("CSV file loaded successfully! Here's a preview:")
    st.dataframe(df)

    # Check if required columns exist
    required_columns = ['Student_Translation', 'Reference_Translation']
    if all(col in df.columns for col in required_columns):
        
        st.write("Starting assessment...")

        # Create columns for scores
        df['Similarity'] = 0.0
        df['Accuracy_Score'] = 0
        df['Fluency_Score'] = 0
        df['Register_Score'] = 0
        df['Tone_Score'] = 0

        # For each row, calculate similarity ratio (automated part)
        for i, row in df.iterrows():
            s = row['Student_Translation']
            r = row['Reference_Translation']
            similarity = SequenceMatcher(None, s, r).ratio()
            df.at[i, 'Similarity'] = similarity
        
        # Show the similarity scores for overview
        st.write("Similarity Scores between Student and Reference translations:")
        st.dataframe(df[['Student_Translation', 'Reference_Translation', 'Similarity']])

        st.write("Now, please manually score the following dimensions for each translation:")

        # Create interactive manual scoring for each row
        for i, row in df.iterrows():
            st.markdown(f"### Translation Pair #{i+1}")
            st.write("**Student:**", row['Student_Translation'])
            st.write("**Reference:**", row['Reference_Translation'])
            df.at[i, 'Accuracy_Score'] = st.slider(f"Accuracy Score (1-5) for pair {i+1}", 1, 5, 3, key=f"acc_{i}")
            df.at[i, 'Fluency_Score'] = st.slider(f"Fluency Score (1-5) for pair {i+1}", 1, 5, 3, key=f"flu_{i}")
            df.at[i, 'Register_Score'] = st.slider(f"Register Score (1-5) for pair {i+1}", 1, 5, 3, key=f"reg_{i}")
            df.at[i, 'Tone_Score'] = st.slider(f"Tone Score (1-5) for pair {i+1}", 1, 5, 3, key=f"tone_{i}")

        # Show a summary table of all scores
        st.write("### Summary of Scores")
        st.dataframe(df[['Student_Translation', 'Similarity', 'Accuracy_Score', 'Fluency_Score', 'Register_Score', 'Tone_Score']])

        # Optionally, allow user to download the scores as CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Assessment Results as CSV",
            data=csv,
            file_name='translation_assessment_results.csv',
            mime='text/csv',
        )

    else:
        st.error(f"CSV file must contain the following columns: {required_columns}")

else:
    st.info("Please upload a CSV file containing 'Student_Translation' and 'Reference_Translation' columns.")
