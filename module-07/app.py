import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

# ── Header ────────────────────────────────────────────────────────────────────
col_title, col_btn = st.columns([9, 1])
with col_title:
    st.title("Dashboard")
with col_btn:
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("+ New Note", use_container_width=True)

# ── Sidebar navigation ────────────────────────────────────────────────────────
page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Notes", "Tasks", "Reports", "Settings"],
    label_visibility="collapsed",
)

# ── Main content ──────────────────────────────────────────────────────────────
if page == "Overview":
    k1, k2, k3 = st.columns(3)
    k1.metric("Total Notes", 128)
    k2.metric("Open Tasks", 42)
    k3.metric("Last Active", "7d")

    st.subheader("Recent items")
    st.divider()

    recent_items = [
        ("Project kickoff notes", "2026-05-30"),
        ("Q2 review summary", "2026-05-28"),
        ("API integration plan", "2026-05-25"),
        ("Team retro action items", "2026-05-22"),
        ("Release checklist v2", "2026-05-20"),
    ]
    for label, value in recent_items:
        left, right = st.columns([5, 1])
        left.write(label)
        right.write(value)

elif page == "Notes":
    st.header("Notes")
    st.info("No notes yet. Click **+ New Note** to create one.")

elif page == "Tasks":
    st.header("Tasks")
    st.info("No tasks yet.")

elif page == "Reports":
    st.header("Reports")
    st.info("No reports available.")

elif page == "Settings":
    st.header("Settings")
    st.info("No settings configured.")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("v1.0.0")
