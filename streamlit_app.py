import pandas as pd
import io

st.markdown("""
<style>
/* BASE */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #0a1931 0%, #16213e 100%);
    color: #f5f5f5;
}

/* MAIN CONTAINER */
.main {
    background: rgba(10, 25, 49, 0.9);
    border-radius: 18px;
    padding: 2rem;
}

/* HEADER */
.header-container {
    background: linear-gradient(135deg, #0a1931, #1f4068);
    color: #ffd369;
    padding: 2.5rem;
    border-radius: 18px;
    text-align: center;
    font-weight: bold;
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
    font-size: 28px;
    font-weight: bold;
    color: #ffd369;
}

/* SUBTITLE */
.menu-sub {
    color: #eaeaea;
    font-size: 14px;
}

/* BUTTON */
.stButton>button {
    background: #ffd369;
    color: #0a1931;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

if menu == "HOME":

    st.markdown("""
    <div class='header-container'>
        UNIT ANALYSIS SYSTEM
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # ================= UTILIZATION =================
    with col1:
        st.markdown("""
        <div class="menu-card">
            <div class="menu-title">UTILIZATION</div>
            <div class="menu-sub">Unit Monitoring & Usage</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Masuk Utilization"):
            st.session_state.menu = "UTILIZATION"

    # ================= EVALUATION =================
    with col2:
        st.markdown("""
        <div class="menu-card">
            <div class="menu-title">EVALUATION</div>
            <div class="menu-sub">Performance & Analysis</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Masuk Evaluation"):
            st.session_state.menu = "EVALUATION"
