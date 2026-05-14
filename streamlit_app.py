import pandas as pd
import io
import streamlit as st

# ================= CONFIG =================
st.set_page_config(
    page_title="Dashboard Transport",
    page_icon="wingbox.jpg",  
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
    st.markdown("## 🚛 MENU")

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

    from datetime import datetime

    # =====================================================
    # HEADER
    # =====================================================
    st.markdown("""
    <div class='header-container'>
        UTILIZATION DASHBOARD
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # TITLE
    # =====================================================
    st.markdown("""
    <h3 style="
        margin-bottom:0;
        color:#0F172A;
        font-weight:700;
    ">
        📂 Upload Data
    </h3>

    <p style="
        margin-top:4px;
        font-size:13px;
        color:#64748B;
    ">
        Silakan unggah file data unit Inside, Outside, dan Locked
        dalam format Excel (.xlsx)
    </p>
    """, unsafe_allow_html=True)

    # =====================================================
    # CUSTOM CSS
    # =====================================================
    st.markdown("""
    <style>

    /* MULTISELECT TAG */
    .stMultiSelect [data-baseweb="tag"]{
        background-color:#0F172A !important;
        color:white !important;
        border-radius:8px !important;
        border:none !important;
        padding:2px 6px !important;
    }

    .stMultiSelect [data-baseweb="tag"] span{
        color:white !important;
        font-size:12px !important;
    }

    /* BUTTON */
    .stButton > button{
        border-radius:10px !important;
        border:1px solid #E2E8F0 !important;
        background-color:white !important;
        color:#0F172A !important;
        font-weight:600 !important;
        padding:10px 18px !important;
        transition:0.3s;
    }

    .stButton > button:hover{
        background-color:#0F172A !important;
        color:white !important;
        border:1px solid #0F172A !important;
    }

    /* INFO BOX */
    div[data-baseweb="notification"]{
        border-radius:10px !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # =====================================================
    # FILE UPLOADER
    # =====================================================
    uploaded_files = st.file_uploader(
        "Upload file Excel",
        type=["xlsx"],
        accept_multiple_files=True
    )

    # =====================================================
    # VALIDASI FILE
    # =====================================================
    if uploaded_files:

        # =====================================================
        # VALIDASI JUMLAH FILE
        # =====================================================
        if len(uploaded_files) > 3:

            st.warning(
                "⚠️ Maksimal upload 3 file."
            )

        else:

            # =====================================================
            # VALIDASI SIZE
            # =====================================================
            total_size_mb = sum(
                file.size for file in uploaded_files
            ) / (1024 * 1024)

            if total_size_mb > 10:

                st.warning(
                    "⚠️ Total ukuran file maksimal 10 MB."
                )

            else:

                df_list = []

                # =====================================================
                # BACA FILE
                # =====================================================
                for file in uploaded_files:

                    try:

                        df = pd.read_excel(file)
                        df_list.append(df)

                    except Exception:

                        st.error(
                            f"Gagal membaca file: {file.name}"
                        )

                        st.stop()

                # =====================================================
                # GABUNG FILE
                # =====================================================
                df_all = pd.concat(
                    df_list,
                    ignore_index=True
                )

                st.success(
                    "✅ File berhasil digabungkan."
                )

                # =====================================================
                # BUTTON DATA PREPARATION
                # =====================================================
                st.markdown(
                    "<br>",
                    unsafe_allow_html=True
                )

                if st.button(
                    "📊 Data Preparation"
                ):

                    st.session_state[
                        "show_preparation"
                    ] = True

                # =====================================================
                # SHOW PREPARATION
                # =====================================================
                if st.session_state.get(
                    "show_preparation",
                    False
                ):

                    # =====================================================
                    # FILTER KOLOM
                    # =====================================================
                    st.markdown("""
                    <h3 style="
                        margin-top:25px;
                        margin-bottom:5px;
                        color:#0F172A;
                        font-weight:700;
                    ">
                        🧩 Filter Kolom
                    </h3>

                    <p style="
                        font-size:13px;
                        color:#64748B;
                        margin-top:0;
                    ">
                        Pilih kolom yang digunakan
                    </p>
                    """, unsafe_allow_html=True)

                    all_columns = (
                        df_all.columns.tolist()
                    )

                    # =====================================================
                    # DEFAULT KOLOM
                    # =====================================================
                    default_cols = [
                        'LICENSE NUMBER',
                        'SHIPMENT NUMBER',
                        'SHIPMENT STATUS',
                        'DRIVER 1',
                        'DRIVER 2',
                        'CURRENT STATUS',
                        'COMPLETE PLAN',
                        'OWNERSHIP UNIT',
                        'LIVE LOCATION',
                        'LAST DROP LOCATION'
                    ]

                    default_existing = [
                        col for col in default_cols
                        if col in all_columns
                    ]

                    # =====================================================
                    # MULTISELECT
                    # =====================================================
                    selected_columns = st.multiselect(
                        "Pilih kolom",
                        all_columns,
                        default=default_existing,
                        label_visibility="collapsed"
                    )

                    st.info(
                        f"{len(default_existing)} kolom dipilih secara default."
                    )

                    # =====================================================
                    # BUTTON SHOW PREPARATION
                    # =====================================================
                    st.markdown(
                        "<br>",
                        unsafe_allow_html=True
                    )

                    if st.button(
                        "📋 Preview Data"
                    ):

                        st.session_state[
                            "show_result_preparation"
                        ] = True

                    # =====================================================
                    # SHOW RESULT PREPARATION
                    # =====================================================
                    if (
                        st.session_state.get(
                            "show_result_preparation",
                            False
                        )
                        and selected_columns
                    ):

                        df_selected = (
                            df_all[selected_columns]
                            .copy()
                        )

                        st.markdown("""
                        <h3 style="
                            margin-top:25px;
                            margin-bottom:10px;
                            color:#0F172A;
                            font-weight:700;
                        ">
                            📋 Data Preparation Results
                        </h3>
                        """, unsafe_allow_html=True)

                        st.dataframe(
                            df_selected,
                            use_container_width=True
                        )

                        # =====================================================
                        # INPUT TANGGAL ANALISA
                        # =====================================================
                        st.markdown("""
                        <h3 style="
                            margin-top:25px;
                            margin-bottom:10px;
                            color:#0F172A;
                            font-weight:700;
                        ">
                            📅 Analysis Date
                        </h3>
                        """, unsafe_allow_html=True)

                        tanggal_analisa = st.date_input(
                            "Pilih tanggal analisa",
                            value=datetime.today(),
                            label_visibility="collapsed"
                        )

                        # =====================================================
                        # BUTTON ANALISA
                        # =====================================================
                        if st.button(
                            "🔍 Utilization Analysis"
                        ):

                            # =====================================================
                            # VALIDASI KOLOM WAJIB
                            # =====================================================
                            required_cols = [
                                'LICENSE NUMBER',
                                'SHIPMENT STATUS'
                            ]

                            missing_cols = [
                                col for col in required_cols
                                if col not in df_selected.columns
                            ]

                            if missing_cols:

                                st.warning(
                                    "⚠️ Kolom wajib tidak ditemukan: "
                                    + ", ".join(missing_cols)
                                )

                            else:

                                # =====================================================
                                # INSERT REMARKS
                                # =====================================================
                                idx = (
                                    df_selected.columns.get_loc(
                                        'LICENSE NUMBER'
                                    )
                                )

                                df_selected.insert(
                                    idx + 1,
                                    'REMARKS',
                                    ''
                                )

                                # =====================================================
                                # LOGIC 1
                                # SHIPMENT STATUS
                                # =====================================================
                                df_selected['is_ongoing'] = (
                                    df_selected[
                                        'SHIPMENT STATUS'
                                    ]
                                    .astype(str)
                                    .str.contains(
                                        'Onprogress',
                                        case=False,
                                        na=False
                                    )
                                )

                                df_selected['is_ready'] = (
                                    df_selected[
                                        'SHIPMENT STATUS'
                                    ]
                                    .astype(str)
                                    .str.contains(
                                        'Ready',
                                        case=False,
                                        na=False
                                    )
                                )

                                # =====================================================
                                # GROUPING NOPOL
                                # =====================================================
                                status_nopol = (
                                    df_selected
                                    .groupby(
                                        'LICENSE NUMBER'
                                    )
                                    .agg({
                                        'is_ongoing': 'max',
                                        'is_ready': 'max'
                                    })
                                )

                                # =====================================================
                                # REMARKS LOGIC 1
                                # =====================================================
                                df_selected['REMARKS'] = (
                                    df_selected[
                                        'LICENSE NUMBER'
                                    ]
                                    .map(
                                        lambda x:
                                            'ON ROAD'
                                            if (
                                                status_nopol.loc[
                                                    x,
                                                    'is_ongoing'
                                                ]
                                                and
                                                status_nopol.loc[
                                                    x,
                                                    'is_ready'
                                                ]
                                            )
                                            else ''
                                    )
                                )

                                # =====================================================
                                # LOGIC 2
                                # CURRENT STATUS OTW
                                # =====================================================
                                mask_kosong = (
                                    df_selected['REMARKS']
                                    .astype(str)
                                    .str.strip() == ''
                                )

                                if (
                                    'CURRENT STATUS'
                                    in df_selected.columns
                                ):

                                    mask_otw = (
                                        df_selected[
                                            'CURRENT STATUS'
                                        ]
                                        .astype(str)
                                        .str.contains(
                                            'OTW',
                                            case=False,
                                            na=False
                                        )
                                    )

                                    df_selected.loc[
                                        mask_kosong & mask_otw,
                                        'REMARKS'
                                    ] = 'ON ROAD'

                                # =====================================================
                                # LOGIC 3
                                # COMPLETE PLAN
                                # =====================================================
                                if (
                                    'COMPLETE PLAN'
                                    in df_selected.columns
                                ):

                                    # ===== UPDATE MASK =====
                                    mask_kosong = (
                                        df_selected['REMARKS']
                                        .astype(str)
                                        .str.strip() == ''
                                    )

                                    # ===== CONVERT DATE =====
                                    df_selected[
                                        'COMPLETE PLAN'
                                    ] = pd.to_datetime(
                                        df_selected[
                                            'COMPLETE PLAN'
                                        ],
                                        errors='coerce'
                                    )

                                    # ===== TANGGAL ANALISA =====
                                    tanggal_analisa_fix = (
                                        pd.to_datetime(
                                            tanggal_analisa
                                        ).normalize()
                                    )

                                    # ===== ON ROAD =====
                                    mask_onroad = (
                                        df_selected[
                                            'COMPLETE PLAN'
                                        ]
                                        >= tanggal_analisa_fix
                                    )

                                    # ===== AVAILABLE =====
                                    mask_available = (
                                        df_selected[
                                            'COMPLETE PLAN'
                                        ]
                                        < tanggal_analisa_fix
                                    )

                                    # ===== APPLY =====
                                    df_selected.loc[
                                        mask_kosong & mask_onroad,
                                        'REMARKS'
                                    ] = 'ON ROAD'

                                    df_selected.loc[
                                        mask_kosong & mask_available,
                                        'REMARKS'
                                    ] = 'AVAILABLE'

                                # =====================================================
                                # DROP TEMP COLUMN
                                # =====================================================
                                df_selected.drop(
                                    columns=[
                                        'is_ongoing',
                                        'is_ready'
                                    ],
                                    inplace=True
                                )

                                # =====================================================
                                # CEK REMARKS KOSONG
                                # =====================================================
                                jumlah_kosong = (
                                    df_selected[
                                        'REMARKS'
                                    ]
                                    .astype(str)
                                    .str.strip()
                                    .eq('')
                                    .sum()
                                )

                                # =====================================================
                                # SUMMARY
                                # =====================================================
                                total_onroad = (
                                    df_selected[
                                        'REMARKS'
                                    ]
                                    == 'ON ROAD'
                                ).sum()

                                total_available = (
                                    df_selected[
                                        'REMARKS'
                                    ]
                                    == 'AVAILABLE'
                                ).sum()

                                # =====================================================
                                # HASIL ANALISA
                                # =====================================================
                                st.success(
                                    "✅ Analisa berhasil dilakukan."
                                )

                                col1, col2, col3 = st.columns(3)

                                with col1:
                                    st.metric(
                                        "ON ROAD",
                                        total_onroad
                                    )

                                with col2:
                                    st.metric(
                                        "AVAILABLE",
                                        total_available
                                    )

                                with col3:
                                    st.metric(
                                        "REMARKS KOSONG",
                                        jumlah_kosong
                                    )

                                # =====================================================
                                # DATA HASIL
                                # =====================================================
                                st.markdown("""
                                <h3 style="
                                    margin-top:25px;
                                    margin-bottom:10px;
                                    color:#0F172A;
                                    font-weight:700;
                                ">
                                    📊 Analysis Results
                                </h3>
                                """, unsafe_allow_html=True)

                                st.dataframe(
                                    df_selected,
                                    use_container_width=True
                                )

                                # =====================================================
                                # FILTER AVAILABLE
                                # =====================================================
                                df_available = (
                                    df_selected[
                                        df_selected[
                                            'REMARKS'
                                        ]
                                        == 'AVAILABLE'
                                    ]
                                )

                                with st.expander(
                                    "📋 View Available Units"
                                ):

                                    st.dataframe(
                                        df_available,
                                        use_container_width=True
                                    )

                                # =====================================================
                                # DOWNLOAD
                                # =====================================================
                                to_excel = io.BytesIO()

                                with pd.ExcelWriter(
                                    to_excel,
                                    engine='openpyxl'
                                ) as writer:

                                    df_selected.to_excel(
                                        writer,
                                        index=False
                                    )

                                st.download_button(
                                    label="⬇️ Export Analysis",
                                    data=to_excel.getvalue(),
                                    file_name="hasil_utilization.xlsx",
                                    mime=(
                                        "application/"
                                        "vnd.openxmlformats-officedocument."
                                        "spreadsheetml.sheet"
                                    )
                                )

    else:

        st.info(
            "Silakan upload file terlebih dahulu."
        )
        
    # ===== BUTTON BACK =====
    if st.button("⬅️ Back to Home"):
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
