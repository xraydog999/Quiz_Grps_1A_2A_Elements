import streamlit as st
import random

st.set_page_config(page_title="Chemistry Quiz", page_icon="🔬")

st.title("🔬 Chemistry Quiz: Group 1A & 2A Elements")

# -----------------------------
# ELEMENT DATA
# -----------------------------
elements = {
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

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "element_order" not in st.session_state:
    st.session_state.element_order = random.sample(list(elements.keys()), len(elements))
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.feedback = ""
    st.session_state.awaiting_input = True

# -----------------------------
# CURRENT QUESTION
# -----------------------------
current_symbol = st.session_state.element_order[st.session_state.index]
st.subheader("Identify the element name (lowercase)")
st.markdown(f"### Symbol: **{current_symbol}**")

# -----------------------------
# ANSWER FORM
# -----------------------------
if st.session_state.awaiting_input:
    with st.form("quiz_form", clear_on_submit=True):
        user_input = st.text_input("Your answer:")
        submitted = st.form_submit_button("Submit Answer")

    if submitted:
        correct = elements[current_symbol]
        st.session_state.total += 1

        if user_input.strip().lower() == correct:
            st.session_state.score += 1
            st.session_state.feedback = f"✅ Correct! **{correct}**"
        else:
            st.session_state.feedback = f"❌ Incorrect. The correct answer was **{correct}**"

        st.session_state.awaiting_input = False

# -----------------------------
# FEEDBACK + NEXT BUTTON
# -----------------------------
if not st.session_state.awaiting_input:
    st.write(st.session_state.feedback)
    if st.button("Next Question"):
        st.session_state.index += 1
        if st.session_state.index >= len(st.session_state.element_order):
            st.session_state.element_order = random.sample(list(elements.keys()), len(elements))
            st.session_state.index = 0
        st.session_state.feedback = ""
        st.session_state.awaiting_input = True

# -----------------------------
# SCOREBOARD
# -----------------------------
st.markdown("---")
st.subheader("📊 Progress")
st.write(f"Score: **{st.session_state.score} / {st.session_state.total}**")

if st.session_state.total > 0:
    accuracy = (st.session_state.score / st.session_state.total) * 100
    st.write(f"Accuracy: **{accuracy:.1f}%**")
