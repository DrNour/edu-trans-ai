# edu_trans_ai.py

import streamlit as st
import pandas as pd
from difflib import SequenceMatcher
import textstat
from collections import Counter

st.set_page_config(page_title="EduTransAI", layout="wide")

st.title("🧠 EduTransAI – Translation Assessment Tool")

uploaded_file = st.file_uploader("📤 Upload a CSV file with student translations", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    for index, row in df.iterrows():
        st.markdown(f"### 🔹 Translation {index+1}")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**📝 Source Text**")
            st.write(row["Source Text"])

        with col2:
            st.markdown("**👨‍🎓 Student Translation**")
            st.write(row["Student Translation"])

        with col3:
            st.markdown("**📘 Reference Translation**")
            st.write(row["Reference Translation"])

        # Simple accuracy score using sequence matcher
        acc = SequenceMatcher(None, row["Student Translation"], row["Reference Translation"]).ratio()

        # Fluency score using textstat
        try:
            fluency = 100 - textstat.flesch_reading_ease(row["Student Translation"])
        except:
            fluency = "N/A"

        # Register / tone (basic keyword match)
        informal_words = ["جداً", "كتير", "عايز", "فيه"]
        tone_penalty = any(word in row["Student Translation"] for word in informal_words)
        tone_score = "Too Informal" if tone_penalty else "Formal Enough"

        st.markdown(f"""
        **🧾 Evaluation**
        - ✅ Accuracy: `{acc:.2f}`
        - ✍️ Fluency Score: `{fluency}`
        - 🎭 Register/Tone: `{tone_score}`
        """)

        st.markdown("---")

    # Glossary extraction
    st.header("📚 Glossary Extractor")
    gloss = []

    for i, row in df.iterrows():
        src_words = row["Source Text"].split()
        tgt_words = row["Student Translation"].split()
        for s, t in zip(src_words, tgt_words):
            gloss.append((s.strip(".,؟"), t.strip(".,؟")))

    glossary_df = pd.DataFrame(gloss, columns=["English", "Arabic"])
    glossary_df = glossary_df.drop_duplicates().value_counts().reset_index(name='Frequency')

    st.dataframe(glossary_df)

    st.download_button("⬇️ Download Glossary", glossary_df.to_csv(index=False), file_name="glossary.csv")

else:
    st.info("Please upload a CSV file to begin.")
