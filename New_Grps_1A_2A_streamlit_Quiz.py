import streamlit as st
import random

# --- CONFIG & STYLING ---
st.set_page_config(page_title="Grp 1A & 2A Element Names Quiz")



# --- QUIZ DATA ---
# -----------------------------
quiz_data = {
    "H": "hydrogen",
    "Li": "lithium",
    "Na": "sodium",
    "K": "potassium",
    "Rb": "rubidium",
    "Cs": "cesium",
    "Fr": "francium",
    "Be": "beryllium",
    "Mg": "magnesium",
    "Ca": "calcium",
    "Sr": "strontium",
    "Ba": "barium",
    "Ra": "radium"
}

# --- SESSION STATE INITIALIZATION ---
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_index = 0
    st.session_state.Element_symbols = list(quiz_data.keys())
    random.shuffle(st.session_state.Element_symbols)
    st.session_state.quiz_over = False

import streamlit as st

st.title("Grp 1A & 2A Element Names Quiz")
st.write(f"Score: {st.session_state.score}/{len(quiz_data)}")

if st.session_state.quiz_over:
    st.success("Quiz Over!")
    st.write(f"Final Score: {st.session_state.score}/{len(quiz_data)}")
else:
    current_symbol_index = st.session_state.current_index
    element_symbols = st.session_state.Element_symbols

    if current_symbol_index < len(element_symbols):
        current_symbol = element_symbols[current_symbol_index]
        correct_answer = quiz_data[current_symbol]

        st.write(f"Type the name for '{current_symbol}'?")

        # Use a unique key for st.text_input to ensure it resets when the question changes
        user_answer = st.text_input("Your answer (lowercase):", key=f"question_{current_symbol_index}")

        if user_answer:
            if user_answer.lower() == correct_answer.lower():
                st.success("Correct!")
                st.session_state.score += 1
                st.session_state.current_index += 1
                # Check if all questions have been answered
                if st.session_state.current_index >= len(element_symbols):
                    st.session_state.quiz_over = True
                # Re-run the script to update the question or show the final score
                st.rerun()
            else:
                st.error("Incorrect. Try again.")
    else:
        # This block ensures the quiz_over state is set if all questions were iterated through
        st.session_state.quiz_over = True
        st.rerun()
