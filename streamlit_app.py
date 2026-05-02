import pandas as pd
import io
import streamlit as st

# ================= CONFIG (WAJIB PALING ATAS) =================
st.set_page_config(
    page_title="Dashboard Transport",
    layout="wide"
)

# ================= SESSION STATE =================
if "menu" not in st.session_state:
    st.session_state.menu = "HOME"

# ================= CUSTOM CSS =================
st.markdown("""
<style>

/* BACKGROUND */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #0a1931 0%, #16213e 100%);
    color: #ffffff;
}

/* HEADER */
.header-container {
    background: linear-gradient(135deg, #0a1931, #1f4068);
    color: #ffd369;
    padding: 2.5rem;
    border-radius: 15px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 30px;
}

/* CARD MENU */
.menu-card {
    background: #112240;
    border-radius: 15px;
    padding: 2rem;
    text-align: left;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    transition: 0.3s;
    border: 1px solid rgba(255, 211, 105, 0.2);
}

.menu-card:hover {
    transform: translateY(-5px);
    background: #1f4068;
    border: 1px solid #ffd369;
}

/* TITLE */
.menu-title {
    font-size: 26px;
    font-weight: bold;
    color: #ffd369;
}

/* SUBTITLE */
.menu-sub {
    color: #dddddd;
    font-size: 14px;
}

/* BUTTON */
.stButton>button {
    background: #ffd369;
    color: #0a1931;
    border-radius: 10px;
    font-weight: bold;
    padding: 0.6rem 1.5rem;
}

</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## 📊 MENU")

    selected_menu = st.radio(
        "",
        ["HOME", "UTILIZATION", "EVALUATION"],
        index=["HOME", "UTILIZATION", "EVALUATION"].index(st.session_state.menu)
    )

    st.session_state.menu = selected_menu

# ================= ROUTING =================
menu = st.session_state.menu

# ================= HOME =================
if menu == "HOME":

    st.markdown("""
    <div class='header-container'>
        DASHBOARD TRANSPORT SYSTEM
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # ===== UTILIZATION =====
    with col1:
        st.markdown("""
        <div class="menu-card">
            <div class="menu-title">UTILIZATION</div>
            <div class="menu-sub">Unit Monitoring & Usage</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Masuk Utilization"):
            st.session_state.menu = "UTILIZATION"
            st.rerun()

    # ===== EVALUATION =====
    with col2:
        st.markdown("""
        <div class="menu-card">
            <div class="menu-title">EVALUATION</div>
            <div class="menu-sub">Performance & Analysis</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Masuk Evaluation"):
            st.session_state.menu = "EVALUATION"
            st.rerun()

# ================= UTILIZATION =================
elif menu == "UTILIZATION":

    st.markdown("""
    <div class='header-container'>
        UTILIZATION DASHBOARD
    </div>
    """, unsafe_allow_html=True)

    st.write("📊 Data Utilization akan ditampilkan di sini")

    if st.button("⬅️ Kembali ke Home"):
        st.session_state.menu = "HOME"
        st.rerun()

# ================= EVALUATION =================
elif menu == "EVALUATION":

    st.markdown("""
    <div class='header-container'>
        EVALUATION DASHBOARD
    </div>
    """, unsafe_allow_html=True)

    st.write("📈 Analisis performa akan ditampilkan di sini")

    if st.button("⬅️ Kembali ke Home"):
        st.session_state.menu = "HOME"
        st.rerun()
