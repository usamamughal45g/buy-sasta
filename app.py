import streamlit as st
from PIL import Image

# Page Setup
st.set_page_config(page_title="Buy Sasta - Pro Square UI", page_icon="🛍️", layout="wide")

# Custom CSS for a Clean, Highlighted Square Inbox
st.markdown("""
    <style>
    /* Background and global font */
    .stApp { background-color: #ffffff; }

    /* Modern Banner */
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 100px 20px 110px 20px;
        text-align: center;
        color: white;
        border-radius: 0;
        position: relative;
    }
    
    .hero-banner h1 { font-size: 48px; font-weight: 900; color: white !important; letter-spacing: -1px; }

    /* SEARCH BOX FIX: Preventing 'kata-kata' look */
    .search-box-container {
        max-width: 800px;
        margin: -55px auto 60px auto; 
        position: relative;
        z-index: 9999 !important;
        padding: 10px;
        overflow: visible !important; /* Force visibility */
    }
    
    /* Targeting every layer to ensure Sharp Square edges */
    div[data-baseweb="input"], 
    div[data-baseweb="input"] > div, 
    input {
        border-radius: 0px !important; /* Sharp corners */
    }

    /* Highlighted Inbox Styling */
    .stTextInput > div > div > input {
        border-radius: 0px !important; 
        padding: 35px 30px !important;
        border: 4px solid #ff4b2b !important; /* Bold Red Border */
        background-color: white !important;
        color: #1a1a3d !important;
        font-size: 22px !important;
        height: 80px !important;
        /* Neon Red Glow Effect */
        box-shadow: 0 0 20px rgba(255, 75, 43, 0.4) !important;
        transition: all 0.4s ease;
    }

    /* Focus Highlight: Jab user likhna shuru kare */
    .stTextInput > div > div > input:focus {
        box-shadow: 0 0 40px rgba(255, 75, 43, 0.7) !important;
        border-color: #ff0000 !important;
        transform: translateY(-2px);
    }

    /* Result Cards */
    .deal-card {
        background: #f8fafc;
        padding: 30px;
        border-radius: 0px;
        text-align: center;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .deal-card:hover {
        border-color: #ff4b2b;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    .price-tag { color: #10b981; font-size: 24px; font-weight: bold; }

    /* Removing Streamlit's default clutter */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

# 1. Hero Section
st.markdown("""
    <div class="hero-banner">
        <p style="color: #ff4b2b; font-weight: bold; letter-spacing: 2px;">SMART COMPARISON ENGINE</p>
        <h1>Buy Sasta <span style="color:#ff4b2b;">AI</span></h1>
        <p style="opacity: 0.8;">No Clutter. Just the Lowest Prices.</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Highlighted Square Search Bar
st.markdown('<div class="search-box-container">', unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Paste link or search items...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# 3. Results Section
if query:
    st.markdown(f"<h3 style='text-align:center; color:#0f172a;'>Top Deals for '{query}'</h3>", unsafe_allow_html=True)
    
    # Store List
    stores = [
        {"name": "Meesho", "badge": "Lowest", "url": f"https://www.meesho.com/search?q={query}"},
        {"name": "Amazon", "badge": "Prime", "url": f"https://www.amazon.in/s?k={query}"},
        {"name": "Flipkart", "badge": "Plus", "url": f"https://www.flipkart.com/search?q={query}"}
    ]

    cols = st.columns(3)
    for i, store in enumerate(stores):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="deal-card">
                    <p style="color:#64748b; font-size:12px; text-transform:uppercase;">{store['name']}</p>
                    <p class="price-tag">Check Live</p>
                    <span style="background:#fee2e2; color:#ef4444; padding:3px 12px; font-size:11px; font-weight:bold;">{store['badge']}</span>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Shop on {store['name']}", store['url'], use_container_width=True)
else:
    st.markdown("<br><br><p style='text-align:center; color:#94a3b8; font-size:18px;'>Enter a product name to see the magic...</p>", unsafe_allow_html=True)
    
