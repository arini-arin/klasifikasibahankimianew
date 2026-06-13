import streamlit as st
from senyawa_data import senyawa_data
import random

st.set_page_config(
    page_title="Klasifikasi 100 Senyawa Kimia",
    page_icon="🧪",
    layout="wide"
)

# ═══════════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

BADGE_COLORS = {
    "korosif":        "#e53e3e",
    "mudah terbakar": "#dd6b20",
    "eksplosif":      "#d53f8c",
    "beracun":        "#6b46c1",
    "toksik":         "#6b46c1",
    "karsinogen":     "#6b46c1",
    "oksidator":      "#2b6cb0",
    "iritasi":        "#d69e2e",
    "tidak berbahaya":"#276749",
    "lingkungan":     "#2c7a7b",
}

SIMBOL_ICONS = {
    "korosif":        "⚠️",
    "mudah terbakar": "🔥",
    "beracun":        "☠️",
    "toksik":         "☠️",
    "karsinogen":     "⚠️",
    "oksidator":      "💥",
    "iritasi":        "❗",
    "tidak berbahaya":"✅",
    "eksplosif":      "💢",
    "lingkungan":     "🌍",
}

CATEGORIES = [
    ("Semua",              ""),
    ("✅ Tidak Berbahaya", "tidak berbahaya"),
    ("☠️ Beracun",         "beracun, toksik, karsinogen"),
    ("⚠️ Korosif",         "korosif"),
    ("🔥 Mudah Terbakar",  "mudah terbakar, eksplosif"),
    ("💥 Oksidator",       "oksidator"),
    ("❗ Iritasi",          "iritasi"),
    ("🌍 Lingkungan",      "lingkungan"),
]

CHIP_PRIORITY = [
    "tidak berbahaya",
    "eksplosif",
    "sangat mudah terbakar",
    "mudah terbakar",
    "beracun, toksik, karsinogen",
    "oksidator",
    "korosif",
    "iritasi",
    "lingkungan",
]

HAZARD_MAP = [
    ("tidak berbahaya",    "Tidak Berbahaya",     "#276749", "✅"),
    ("sangat mudah terbakar","Sgt Mudah Terbakar","#c53030", "🔥"),
    ("mudah terbakar",     "Mudah Terbakar",      "#dd6b20", "🔥"),
    ("karsinogen",         "Karsinogen",          "#6b46c1", "⚠️"),
    ("beracun",            "Beracun",             "#6b46c1", "☠️"),
    ("toksik",             "Toksik",              "#6b46c1", "☠️"),
    ("korosif",            "Korosif",             "#e53e3e", "⚠️"),
    ("oksidator",          "Oksidator",           "#2b6cb0", "💥"),
    ("eksplosif",          "Eksplosif",           "#d53f8c", "💢"),
    ("iritasi",            "Iritasi",             "#d69e2e", "❗"),
    ("lingkungan",         "Lingkungan",          "#2c7a7b", "🌍"),
    ("berbahaya",          "Berbahaya",           "#718096", "⚠️"),
]

# ═══════════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def assign_category(simbol):
    s = simbol.lower()
    for group in CHIP_PRIORITY:
        keywords = [k.strip() for k in group.split(",")]
        for kw in keywords:
            if kw in s:
                for label, _ in CATEGORIES:
                    if label == "Semua":
                        continue
                    if kw in label.lower():
                        return label
                return group
    return "Lainnya"


def parse_hazards(simbol):
    s = simbol.lower()
    found = []
    matched_spans = []
    sorted_map = sorted(HAZARD_MAP, key=lambda x: len(x[0]), reverse=True)
    for keyword, label, color, icon in sorted_map:
        if keyword not in s:
            continue
        start = 0
        while True:
            idx = s.find(keyword, start)
            if idx == -1:
                break
            end = idx + len(keyword)
            already_covered = any(ms <= idx and me >= end for ms, me in matched_spans)
            if not already_covered:
                found.append((label, color, icon))
                matched_spans.append((idx, end))
                break
            start = idx + 1
    if not found:
        found.append((simbol, "#718096", "🏷️"))
    return found


def render_hazard_diamonds(simbol):
    """Rotated diamond badges — dipakai di detail view"""
    hazards = parse_hazards(simbol)
    parts = []
    for label, color, icon in hazards:
        parts.append(
            f'<div class="haz-diamond" style="background:{color}">'
            f'<div class="haz-inner">'
            f'<span class="haz-icon">{icon}</span>'
            f'<span class="haz-text">{label}</span>'
            f'</div></div>'
        )
    return '<div class="haz-row">' + "".join(parts) + "</div>"


def render_hazard_pills(simbol, max_pills=2):
    """Compact pill badges — dipakai di grid card"""
    hazards = parse_hazards(simbol)
    parts = []
    for label, color, icon in hazards[:max_pills]:
        parts.append(
            f'<span style="background:{color};color:#fff;padding:2px 8px;border-radius:99px;'
            f'font-size:0.6rem;font-weight:700;white-space:nowrap;'
            f'display:inline-flex;align-items:center;gap:3px;line-height:1.6">'
            f'{icon}&nbsp;{label}</span>'
        )
    extra = len(hazards) - max_pills
    if extra > 0:
        parts.append(
            f'<span style="background:#718096;color:#fff;padding:2px 8px;border-radius:99px;'
            f'font-size:0.6rem;font-weight:700">+{extra}</span>'
        )
    return (
        '<div style="display:flex;flex-wrap:wrap;gap:3px;justify-content:center;margin-top:3px">'
        + "".join(parts) + "</div>"
    )


def render_detail_card(label, value, icon, color="#2563eb", delay="0s"):
    st.markdown(
        f"""
        <div class="det-card" style="animation-delay:{delay};border-left:4px solid {color}">
            <div class="det-label">{icon} {label}</div>
            <div class="det-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_compound_detail(name, data):
    """Render header + semua detail card senyawa — dipakai di List & Grid mode"""
    hazard_html = render_hazard_diamonds(data["simbol_bahaya"])
    st.markdown(
        f"""
        <div class="cmp-header">
            <div style="display:flex;justify-content:space-between;align-items:center;
                        flex-wrap:wrap;gap:16px">
                <div>
                    <h2 style="margin:0;font-size:1.55rem;color:#1e3a6e;font-weight:800;
                                letter-spacing:-0.3px">{name}</h2>
                    <div style="font-size:1rem;color:#718096;font-family:'Courier New',monospace;
                                margin-top:5px;font-weight:600">{data['rumus']}</div>
                </div>
                <div>{hazard_html}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        render_detail_card("Wujud",       data["wujud"],       "💧", "#2563eb", "0s")
    with c2:
        render_detail_card("Bau",         data["bau"],         "👃", "#059669", "0.08s")
    with c3:
        render_detail_card("Reaktivitas", data["reaktivitas"], "⚡", "#dc2626", "0.16s")
    c4, c5 = st.columns(2)
    with c4:
        hazards = parse_hazards(data["simbol_bahaya"])
        labels  = ", ".join(h[0] for h in hazards)
        render_detail_card("Simbol Bahaya",      labels,                  "⚠️", "#d97706", "0.24s")
    with c5:
        render_detail_card("Pengelolaan Limbah", data["pengelolaan_limbah"], "♻️", "#7c3aed", "0.32s")


def filter_and_sort(query, category, sort_order):
    if query:
        q = query.lower()
        hasil = {n: d for n, d in senyawa_data.items()
                 if q in n.lower() or q in d["rumus"].lower()}
    else:
        hasil = dict(senyawa_data)

    if category and category != "Semua":
        hasil = {n: d for n, d in hasil.items()
                 if assign_category(d["simbol_bahaya"]) == category}

    items = list(hasil.items())
    items.sort(key=lambda x: x[0].lower(), reverse=(sort_order == "Z-A"))
    return dict(items)


# ═══════════════════════════════════════════════════════════════════════════════
# CSS
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
/* ── Animations ───────────────────────────────────────────────────────── */
@keyframes gradShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes fadeUp {
    from { opacity:0; transform:translateY(14px); }
    to   { opacity:1; transform:translateY(0); }
}
@keyframes fadeIn {
    from { opacity:0; }
    to   { opacity:1; }
}
@keyframes pulse {
    0%,100% { transform:scale(1); }
    50%      { transform:scale(1.08); }
}
@keyframes shimmerSlide {
    0%   { background-position: -200% 0; }
    100% { background-position:  200% 0; }
}

/* ── Global ───────────────────────────────────────────────────────────── */
.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1440px;
}

/* ── Header ───────────────────────────────────────────────────────────── */
.main-header {
    background: linear-gradient(-45deg, #0c1f44, #1a3a6e, #2563b8, #1a4a9a, #0c1f44);
    background-size: 400% 400%;
    animation: gradShift 12s ease infinite;
    padding: 26px 34px;
    border-radius: 20px;
    margin-bottom: 22px;
    color: white;
    box-shadow: 0 8px 32px rgba(0,0,0,0.24);
    position: relative;
    overflow: hidden;
}
.main-header::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 80% 50%,
        rgba(100,160,255,0.12) 0%, transparent 65%);
    pointer-events: none;
}
.main-header::before {
    content: '';
    position: absolute;
    top: -60%; left: -60%;
    width: 220%; height: 220%;
    background: radial-gradient(circle, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 26px 26px;
    pointer-events: none;
}
.main-header h1 {
    margin: 0;
    font-size: 1.85rem;
    font-weight: 800;
    position: relative;
    z-index: 1;
    letter-spacing: -0.4px;
    animation: fadeUp 0.5s ease;
}
.main-header p {
    margin: 6px 0 0 0;
    opacity: 0.8;
    font-size: 0.9rem;
    position: relative;
    z-index: 1;
    animation: fadeUp 0.5s ease 0.1s both;
}
.header-badges {
    display: flex;
    gap: 10px;
    margin-top: 14px;
    flex-wrap: wrap;
    position: relative;
    z-index: 1;
    animation: fadeUp 0.5s ease 0.2s both;
}
.hbadge {
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.22);
    border-radius: 8px;
    padding: 5px 13px;
    font-size: 0.78rem;
    font-weight: 600;
    backdrop-filter: blur(4px);
}

/* ── Section label ────────────────────────────────────────────────────── */
.sec-lbl {
    font-size: 0.68rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #a0aec0;
    margin: 16px 0 7px;
    padding-bottom: 5px;
    border-bottom: 1px solid #edf2f7;
}

/* ── Buttons — Primary = BIRU (aktif/terpilih) ────────────────────────── */
div.stButton button[kind="primary"] {
    background: linear-gradient(135deg, #1e40af, #2563eb) !important;
    color: #fff !important;
    border: none !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 12px rgba(37,99,235,0.40) !important;
    transition: all 0.16s ease !important;
}
div.stButton button[kind="primary"]:hover {
    background: linear-gradient(135deg, #1d4ed8, #3b82f6) !important;
    box-shadow: 0 5px 20px rgba(37,99,235,0.55) !important;
    transform: translateY(-1px) !important;
}
div.stButton button[kind="secondary"] {
    background: #fff !important;
    border: 1px solid #e2e8f0 !important;
    color: #4a5568 !important;
    transition: all 0.16s ease !important;
}
div.stButton button[kind="secondary"]:hover {
    border-color: #2563eb !important;
    color: #2563eb !important;
    background: #eff6ff !important;
    transform: translateY(-1px) !important;
}
.stButton button {
    border-radius: 10px !important;
}

/* ── Radio (List mode) ────────────────────────────────────────────────── */
div[data-testid="stRadio"] > label { display: none !important; }
div[data-testid="stRadio"] div[role="radiogroup"] {
    max-height: 460px;
    overflow-y: auto;
    gap: 3px;
    padding-right: 2px;
}
div[data-testid="stRadio"] div[role="radiogroup"]::-webkit-scrollbar { width: 4px; }
div[data-testid="stRadio"] div[role="radiogroup"]::-webkit-scrollbar-track {
    background: transparent;
}
div[data-testid="stRadio"] div[role="radiogroup"]::-webkit-scrollbar-thumb {
    background: #cbd5e0;
    border-radius: 4px;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    background: #fff;
    border: 1px solid #e8edf3;
    border-radius: 10px;
    padding: 8px 12px !important;
    margin: 0;
    transition: all 0.16s ease;
    display: flex !important;
    align-items: center;
    gap: 8px;
    cursor: pointer;
    font-size: 0.88rem;
}
div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    border-color: #2563eb;
    background: #eff6ff;
}
div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
    border-color: #2563eb;
    background: #eff6ff;
    box-shadow: 0 0 0 2px rgba(37,99,235,0.18);
}

/* ── Compound header ──────────────────────────────────────────────────── */
.cmp-header {
    background: #fff;
    border: 1px solid #e8edf3;
    border-radius: 18px;
    padding: 22px 26px;
    margin-bottom: 16px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    animation: fadeUp 0.35s ease;
}

/* ── Detail cards ─────────────────────────────────────────────────────── */
.det-card {
    background: #fff;
    border: 1px solid #e8edf3;
    border-radius: 14px;
    padding: 16px 18px;
    height: 100%;
    box-shadow: 0 1px 6px rgba(0,0,0,0.04);
    animation: fadeUp 0.4s ease both;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.det-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.1) !important;
}
.det-label {
    font-size: 0.68rem;
    color: #718096;
    text-transform: uppercase;
    letter-spacing: 0.7px;
    margin-bottom: 6px;
    font-weight: 700;
}
.det-value {
    font-size: 0.98rem;
    font-weight: 600;
    color: #1a202c;
    word-wrap: break-word;
    line-height: 1.55;
}

/* ── Hazard diamonds ──────────────────────────────────────────────────── */
.haz-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
    justify-content: center;
}
.haz-diamond {
    width: 62px;
    height: 62px;
    transform: rotate(45deg);
    border-radius: 7px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 3px 12px rgba(0,0,0,0.26);
    transition: all 0.22s ease;
    animation: fadeUp 0.4s ease both;
}
.haz-diamond:hover {
    transform: rotate(45deg) scale(1.13);
    box-shadow: 0 6px 22px rgba(0,0,0,0.32);
}
.haz-inner {
    transform: rotate(-45deg);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    line-height: 1.1;
}
.haz-icon { font-size: 1.35rem; }
.haz-text {
    font-size: 0.44rem;
    color: #fff;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin-top: 2px;
    text-align: center;
    max-width: 54px;
    line-height: 1.2;
}

/* ── Stats bar ────────────────────────────────────────────────────────── */
.stats-bar {
    background: #fff;
    border: 1px solid #e8edf3;
    border-radius: 10px;
    padding: 8px 14px;
    font-size: 0.8rem;
    color: #718096;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    animation: fadeIn 0.3s ease;
}
.stats-bar strong { color: #1e3a6e; font-weight: 700; }

/* ── Grid placeholder (belum ada pilihan) ─────────────────────────────── */
.grid-placeholder {
    background: linear-gradient(135deg, #f0f4ff 0%, #e8f0fe 100%);
    border: 2px dashed #93c5fd;
    border-radius: 20px;
    padding: 52px 24px;
    text-align: center;
    animation: fadeIn 0.4s ease;
    margin-top: 10px;
}
.gph-icon { font-size: 3.5rem; margin-bottom: 10px; }
.gph-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #2563eb;
    margin-bottom: 6px;
}
.gph-sub { font-size: 0.82rem; color: #93c5fd; }

/* ── Grid detail separator ────────────────────────────────────────────── */
.grid-sep {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 22px 0 16px;
}
.grid-sep::before, .grid-sep::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
}
.grid-sep span {
    font-size: 0.72rem;
    color: #a0aec0;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.7px;
    white-space: nowrap;
}

/* ── Empty states ─────────────────────────────────────────────────────── */
.empty-state {
    text-align: center;
    padding: 52px 20px;
    color: #a0aec0;
    animation: fadeUp 0.4s ease;
}
.es-icon {
    font-size: 3.5rem;
    margin-bottom: 12px;
    display: block;
    animation: pulse 3.5s ease infinite;
}
.es-title { font-size: 1.1rem; font-weight: 700; color: #718096; }
.es-sub   { font-size: 0.84rem; margin-top: 6px; color: #a0aec0; }

/* ── No results ───────────────────────────────────────────────────────── */
.no-results {
    text-align: center;
    padding: 28px 12px;
    color: #a0aec0;
    animation: fadeUp 0.4s ease;
}
.no-results .nr-icon { font-size: 2.8rem; margin-bottom: 8px; display: block; }

/* ── Grid card: style the st.button to look like a card ───────────────── */
div.stButton button {
    white-space: normal !important;
    line-height: 1.4 !important;
    height: auto !important;
    min-height: 52px !important;
    font-size: 0.82rem !important;
}

/* ── Footer ───────────────────────────────────────────────────────────── */
.footer {
    margin-top: 52px;
    padding: 18px 26px;
    background: #f7fafc;
    border-radius: 14px;
    text-align: center;
    color: #718096;
    font-size: 0.82rem;
    border: 1px solid #e8edf3;
    animation: fadeIn 0.6s ease;
}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# SESSION STATE — inisialisasi awal
# ═══════════════════════════════════════════════════════════════════════════════

_defaults = {
    "filter_cat":  "Semua",
    "sort_order":  "A-Z",
    "view_mode":   "List",
    "selected":    list(senyawa_data.keys())[0],
    "prev_query":  "",
}
for _k, _v in _defaults.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v


# ═══════════════════════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="main-header">
    <h1>🧪 Klasifikasi 100 Senyawa Kimia</h1>
    <p>Database keselamatan, sifat fisika, dan penanganan limbah B3 senyawa kimia laboratorium</p>
    <div class="header-badges">
        <div class="hbadge">⚗️ 100 Senyawa</div>
        <div class="hbadge">🗂️ 8 Kategori Bahaya</div>
        <div class="hbadge">📋 5 Parameter</div>
        <div class="hbadge">🔍 Pencarian Real-time</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# LAYOUT  ─  Sidebar (kiri) + Main (kanan)
# ═══════════════════════════════════════════════════════════════════════════════

col_sb, col_main = st.columns([0.30, 0.70], gap="large")

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with col_sb:

    # ── Pencarian ────────────────────────────────────────────────────────────
    st.markdown('<div class="sec-lbl">🔍 Pencarian</div>', unsafe_allow_html=True)
    query = st.text_input(
        "Cari",
        placeholder="Nama atau rumus kimia…",
        label_visibility="collapsed"
    ).strip()

    # Auto-update selection saat query berubah
    if query != st.session_state.prev_query:
        st.session_state.prev_query = query
        _tmp = filter_and_sort(query, st.session_state.filter_cat,
                               st.session_state.sort_order)
        if _tmp:
            if st.session_state.view_mode == "List":
                st.session_state.selected = list(_tmp.keys())[0]
            else:
                # Grid: reset supaya user pilih ulang
                st.session_state.selected = None
        else:
            st.session_state.selected = None

    # ── Filter Kategori ───────────────────────────────────────────────────────
    st.markdown('<div class="sec-lbl">🏷️ Kategori Bahaya</div>', unsafe_allow_html=True)
    chip_cols = st.columns(2)
    for i, (lbl, _) in enumerate(CATEGORIES):
        with chip_cols[i % 2]:
            is_active = st.session_state.filter_cat == lbl
            if st.button(lbl, key=f"chip_{lbl}",
                         use_container_width=True,
                         type="primary" if is_active else "secondary"):
                if st.session_state.filter_cat != lbl:
                    st.session_state.filter_cat = lbl
                    # ── FIX: reset pilihan saat ganti kategori ──
                    # Grid → reset ke None (user harus klik ulang)
                    # List → otomatis pilih item pertama di kategori baru
                    _tmp = filter_and_sort(query, lbl, st.session_state.sort_order)
                    if st.session_state.view_mode == "Grid":
                        st.session_state.selected = None
                    else:
                        st.session_state.selected = list(_tmp.keys())[0] if _tmp else None
                    st.rerun()

    # ── Mode Tampilan ─────────────────────────────────────────────────────────
    st.markdown('<div class="sec-lbl">⚙️ Mode Tampilan</div>', unsafe_allow_html=True)
    vm1, vm2 = st.columns(2)
    with vm1:
        is_list = st.session_state.view_mode == "List"
        if st.button("📋 List", use_container_width=True,
                     type="primary" if is_list else "secondary"):
            if not is_list:
                st.session_state.view_mode = "List"
                # Pastikan ada selection valid untuk list
                _tmp = filter_and_sort(query, st.session_state.filter_cat,
                                       st.session_state.sort_order)
                if _tmp and (not st.session_state.selected
                             or st.session_state.selected not in _tmp):
                    st.session_state.selected = list(_tmp.keys())[0]
                st.rerun()
    with vm2:
        is_grid = st.session_state.view_mode == "Grid"
        if st.button("🗂️ Grid", use_container_width=True,
                     type="primary" if is_grid else "secondary"):
            if not is_grid:
                st.session_state.view_mode = "Grid"
                # ── FIX: reset selection saat masuk grid ──
                st.session_state.selected = None
                st.rerun()

    # ── Opsi Lain ─────────────────────────────────────────────────────────────
    st.markdown('<div class="sec-lbl">🔧 Opsi Lain</div>', unsafe_allow_html=True)
    o1, o2 = st.columns(2)
    with o1:
        sort_lbl = "🔤 A→Z" if st.session_state.sort_order == "A-Z" else "🔤 Z→A"
        if st.button(sort_lbl, use_container_width=True):
            st.session_state.sort_order = (
                "Z-A" if st.session_state.sort_order == "A-Z" else "A-Z"
            )
            st.rerun()
    with o2:
        if st.button("🎲 Acak", use_container_width=True):
            _pick = random.choice(list(senyawa_data.keys()))
            st.session_state.selected = _pick
            # Jika grid, reset filter ke Semua agar item muncul
            if st.session_state.view_mode == "Grid":
                st.session_state.filter_cat = "Semua"
            st.rerun()

    # ── Hitung hasil filter ───────────────────────────────────────────────────
    hasil = filter_and_sort(query, st.session_state.filter_cat, st.session_state.sort_order)

    # ── Daftar senyawa (List mode) ────────────────────────────────────────────
    if st.session_state.view_mode == "List":
        n_txt = (f"{len(hasil)} dari 100"
                 if (query or st.session_state.filter_cat != "Semua")
                 else "100 senyawa")
        st.markdown(
            f'<div class="sec-lbl">📋 Daftar Senyawa '
            f'<span style="font-size:0.7rem;font-weight:400;'
            f'text-transform:none;letter-spacing:0">({n_txt})</span></div>',
            unsafe_allow_html=True
        )

        if not hasil:
            st.markdown("""
            <div class="no-results">
                <span class="nr-icon">🔬</span>
                <div style="font-size:0.95rem;font-weight:700;color:#718096">
                    Tidak ditemukan</div>
                <div style="font-size:0.8rem;margin-top:4px">
                    Coba kata kunci atau filter lain</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            nama_list = list(hasil.keys())
            # Pastikan selection valid di list yang tersaring
            if st.session_state.selected not in nama_list:
                st.session_state.selected = nama_list[0]

            sel = st.radio(
                "Pilih senyawa",
                options=nama_list,
                format_func=lambda x: f"{x}  ({hasil[x]['rumus']})",
                label_visibility="collapsed",
                index=nama_list.index(st.session_state.selected)
            )
            st.session_state.selected = sel

    else:
        # Grid mode: teks hint di sidebar
        n_txt = (f"{len(hasil)} senyawa"
                 if (query or st.session_state.filter_cat != "Semua")
                 else "100 senyawa")
        st.markdown(
            f'<div style="font-size:0.78rem;color:#a0aec0;padding:8px 2px;line-height:1.5">'
            f'📊 <strong style="color:#4a5568">{n_txt}</strong> tersedia<br>'
            f'<span style="font-size:0.72rem">Klik card di sebelah kanan untuk melihat spesifikasi</span>'
            f'</div>',
            unsafe_allow_html=True
        )


# ─────────────────────────────────────────────────────────────────────────────
# MAIN CONTENT
# ─────────────────────────────────────────────────────────────────────────────
with col_main:

    # ══════════════════════ LIST MODE ══════════════════════════════════════════
    if st.session_state.view_mode == "List":
        sel_name = st.session_state.selected
        if sel_name and sel_name in senyawa_data:
            render_compound_detail(sel_name, senyawa_data[sel_name])
        else:
            st.markdown("""
            <div class="empty-state">
                <span class="es-icon">🧪</span>
                <div class="es-title">Pilih senyawa dari daftar</div>
                <div class="es-sub">
                    Gunakan pencarian atau filter kategori<br>untuk menemukan senyawa yang diinginkan
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ══════════════════════ GRID MODE ═════════════════════════════════════════
    else:
        if not hasil:
            st.markdown("""
            <div class="empty-state">
                <span class="es-icon">🔬</span>
                <div class="es-title">Tidak ada senyawa dalam kategori ini</div>
                <div class="es-sub">
                    Pilih kategori berbeda atau hapus teks pencarian
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:
            # Stats bar
            is_filtered = bool(query or st.session_state.filter_cat != "Semua")
            n_show = f"{len(hasil)} dari 100" if is_filtered else "100 senyawa"
            st.markdown(
                f'<div class="stats-bar">'
                f'🗂️ Menampilkan <strong>{n_show}</strong>'
                f'&ensp;·&ensp;Klik card untuk melihat spesifikasi lengkap'
                f'</div>',
                unsafe_allow_html=True
            )

            # ── Grid cards (4 kolom) ──────────────────────────────────────────
            items   = list(hasil.items())
            gcols   = st.columns(4)

            for idx, (nama, data) in enumerate(items):
                with gcols[idx % 4]:
                    is_sel = (st.session_state.selected == nama)
                    label  = f"{nama}\n{data['rumus']}"

                    # ── FIX DOUBLE-CLICK: st.rerun() langsung setelah set ────
                    if st.button(
                        label,
                        key=f"g_{idx}",
                        use_container_width=True,
                        type="primary" if is_sel else "secondary"
                    ):
                        st.session_state.selected = nama
                        st.rerun()   # ← immediate rerun → single click responsif ✓

                    # Hazard pills di bawah setiap card
                    st.markdown(
                        f"<div style='text-align:center;margin-top:-5px;margin-bottom:7px'>"
                        f"{render_hazard_pills(data['simbol_bahaya'])}</div>",
                        unsafe_allow_html=True
                    )

            # ── Detail section ────────────────────────────────────────────────
            # SETELAH loop button, baca selected_name dari session state
            # (mungkin sudah di-update oleh st.rerun, tapi di sini kita baca
            # nilai terkini untuk run ini yang tidak ada click)
            sel_name = st.session_state.selected

            # Tampilkan detail HANYA jika selected ada di hasil saat ini
            # → FIX: ganti kategori tidak menampilkan senyawa dari kategori lama
            if sel_name and sel_name in hasil:
                sel_data = hasil[sel_name]
                st.markdown(
                    f'<div class="grid-sep">'
                    f'<span>📋 Spesifikasi: {sel_name}</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )
                render_compound_detail(sel_name, sel_data)

            else:
                # Placeholder saat belum ada yang dipilih
                st.markdown("""
                <div class="grid-placeholder">
                    <div class="gph-icon">👆</div>
                    <div class="gph-title">Pilih senyawa di atas</div>
                    <div class="gph-sub">
                        Klik salah satu card untuk melihat<br>spesifikasi dan data keselamatan lengkap
                    </div>
                </div>
                """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="footer">
    <div style="font-weight:700;margin-bottom:5px">📚 Sumber Data</div>
    <div>Database karakteristik 100 senyawa kimia laboratorium ·
         Keselamatan, sifat fisika & kimia, penanganan limbah B3</div>
    <div style="margin-top:6px;opacity:0.6;font-size:0.76rem">
        Referensi: MSDS Sigma-Aldrich · Fisher Scientific · NIOSH · GHS/SDS (ISO 11014)
    </div>
    <div style="margin-top:4px;opacity:0.5;font-size:0.74rem">
        © Klasifikasi Senyawa Kimia · Untuk keperluan praktikum kimia dasar
    </div>
</div>
""", unsafe_allow_html=True)
