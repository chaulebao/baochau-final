import streamlit as st
import language_tool_python
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import os

# ===== INIT =====
tool = language_tool_python.LanguageTool('en-US')
DATA_FILE = "history.csv"

# ===== FUNCTION: ANALYZE TEXT =====
def analyze_text(text):
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)

    num_errors = len(matches)

    # ===== CLASSIFY ERRORS =====
    error_types = []
    for m in matches:
        msg = m.message.lower()

        if "agreement" in msg:
            error_types.append("Subject-Verb Agreement")
        elif "tense" in msg:
            error_types.append("Verb Tense")
        elif "article" in msg:
            error_types.append("Article")
        else:
            error_types.append("Other")

    error_count = Counter(error_types)

    # ===== SCORE =====
    score = max(0, 10 - num_errors * 0.5)

    return score, matches, corrected, error_count


# ===== SAVE DATA =====
def save_result(score, errors, error_count):
    data = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Score": round(score, 1),
        "Errors": errors,
        "Agreement": error_count.get("Subject-Verb Agreement", 0),
        "Tense": error_count.get("Verb Tense", 0),
        "Article": error_count.get("Article", 0),
        "Other": error_count.get("Other", 0)
    }

    df = pd.DataFrame([data])

    if os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(DATA_FILE, index=False)


# ===== LOAD DATA =====
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame()


# ===== UI =====
st.set_page_config(page_title="Grammar Checker", page_icon="📘")

st.title("📘 Grammar Error Detection System")
st.write("Check your English grammar and get instant feedback.")

# ===== INPUT =====
text = st.text_area("Enter your paragraph:")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        score, errors, corrected, error_count = analyze_text(text)

        # Save data
        save_result(score, len(errors), error_count)

        # ===== RESULT =====
        st.subheader("Score")
        st.write(f"{score:.1f} / 10")

        st.subheader("Grammar Errors")
        if errors:
            for e in errors:
                st.write("-", e.message)
        else:
            st.success("No grammar errors found!")

        st.subheader("Corrected Text")
        st.success(corrected)

        # ===== ERROR TYPES =====
        st.subheader("Error Types")
        if error_count:
            df = pd.DataFrame(error_count.items(), columns=["Type", "Count"])
            st.dataframe(df)

            fig, ax = plt.subplots()
            ax.bar(df["Type"], df["Count"])
            ax.set_title("Error Distribution")
            ax.set_xlabel("Error Type")
            ax.set_ylabel("Count")
            st.pyplot(fig)


# ===== STATISTICS =====
st.subheader("Your History")

df = load_data()

if not df.empty:
    st.dataframe(df)

    st.write("Total essays:", len(df))
    st.write("Average score:", round(df["Score"].mean(), 2))

    # Chart
    fig, ax = plt.subplots()
    ax.plot(df["Score"], marker='o')
    ax.set_title("Score Progress")
    ax.set_xlabel("Attempts")
    ax.set_ylabel("Score")
    st.pyplot(fig)

else:
    st.write("No data yet.")