import streamlit as st
import random
import base64

st.set_page_config(page_title="Chemistry Group 1A & 2A Quiz", page_icon="🔬")

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
# SOUND LOADING
# -----------------------------
def load_sound(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

correct_sound = load_sound("correct.mp3")
incorrect_sound = load_sound("incorrect.mp3")

def play_sound(sound_b64):
    if not sound_b64:
        return
    sound_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{sound_b64}" type="audio/mp3">
        </audio>
    """
    st.markdown(sound_html, unsafe_allow_html=True)

# -----------------------------
# SESSION STATE INITIALIZATION
# -----------------------------
if "element_order" not in st.session_state:
    st.session_state.element_order = random.sample(list(elements.keys()), len(elements))
    st.session_state.index = 0
    st.session_state.symbol = st.session_state.element_order[0]
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.feedback = ""
    st.session_state.answer = ""

# -----------------------------
# QUESTION DISPLAY
# -----------------------------
st.subheader("Identify the element name (lowercase)")
st.markdown(f"### Symbol: **{st.session_state.symbol}**")

answer = st.text_input("Type your answer and press Enter:", value=st.session_state.answer, key="answer_input")

# -----------------------------
# ANSWER CHECKING
# -----------------------------
if answer and answer != st.session_state.answer:
    correct = elements[st.session_state.symbol]
    st.session_state.total += 1

    if answer.strip().lower() == correct:
        st.session_state.score += 1
        st.session_state.feedback = f"✅ Correct! **{correct}**."
        play_sound(correct_sound)
    else:
        st.session_state.feedback = f"❌ Incorrect. The correct answer is **{correct}**."
        play_sound(incorrect_sound)

    st.session_state.answer = ""  # Clear input
    st.session_state.index += 1
    if st.session_state.index >= len(st.session_state.element_order):
        st.session_state.element_order = random.sample(list(elements.keys()), len(elements))
        st.session_state.index = 0
    st.session_state.symbol = st.session_state.element_order[st.session_state.index]
    st.experimental_set_query_params()  # Triggers rerun to refresh input field

# -----------------------------
# FEEDBACK + SCOREBOARD
# -----------------------------
st.write(st.session_state.feedback)

st.markdown("---")
st.subheader("📊 Progress")
st.write(f"Score: **{st.session_state.score} / {st.session_state.total}**")

if st.session_state.total > 0:
    accuracy = (st.session_state.score / st.session_state.total) * 100
    st.write(f"Accuracy: **{accuracy:.1f}%**")
