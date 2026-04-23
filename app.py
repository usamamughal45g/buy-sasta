import streamlit as st
from PIL import Image

# Page Setup
st.set_page_config(page_title="Buy Sasta - Classic Rounded", page_icon="🛍️", layout="wide")

# Custom CSS for the 2nd Version Look (Rounded + Overlap)
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #ffffff; }

    /* Top Banner (BuyHatke Style) */
    .hero-banner {
        background: linear-gradient(135deg, #2d1b69 0%, #1a1a3d 100%);
        padding: 100px 20px 85px 20px;
        text-align: center;
        color: white;
        border-radius: 0 0 40px 40px;
        position: relative;
    }
    
    .hero-banner h1 { font-size: 42px; font-weight: 800; color: white !important; margin-bottom: 10px; }
    .hero-banner p { font-size: 18px; color: #b0b0d0 !important; }

    /* The Search Bar Box - Overlapping the banner like before */
    .search-box-container {
        max-width: 800px;
        margin: -40px auto 40px auto; /* Overlap effect */
        position: relative;
        z-index: 9999 !important;
        padding: 0 15px;
        overflow: visible !important; /* Isse corners nahi katenge */
    }
    
    /* Rounded Input Box */
    .stTextInput > div > div > input {
        border-radius: 50px !important; /* Proper Rounding */
        padding: 30px 40px !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1) !important;
        font-size: 18px !important;
        background-color: white !important;
        color: black !important;
        height: 65px !important;
    }

    /* Red Glow Highlight on Focus */
    .stTextInput input:focus {
        border-color: #ff4b2b !important;
        box-shadow: 0 0 20px rgba(255, 75, 43, 0.4) !important;
    }

    /* Result Cards */
    .deal-card {
        background: #fdfdfd;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #f0f0f0;
        margin-bottom: 20px;
    }
    .price-green { color: #2ecc71; font-size: 24px; font-weight: bold; }

    /* Hide Streamlit Header/Footer */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 1. Hero Section
st.markdown("""
    <div class="hero-banner">
        <p style="font-size: 14px; letter-spacing: 2px; font-weight: 600; color: #2ecc71;">PREMIUM DEAL FINDER</p>
        <h1>Find <span style="color:#ffffff;">Real Deals</span></h1>
        <p>Compare prices across Meesho, Amazon & Flipkart instantly</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Rounded Search Bar (Back to Version 2 style)
st.markdown('<div class="search-box-container">', unsafe_allow_html=True)
query = st.text_input("", placeholder="🔍 Paste a product link or search here...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# 3. Results Section
if query:
    st.markdown(f"<h3 style='text-align:center; color:#333;'>Search results for '{query}'</h3>", unsafe_allow_html=True)
    
    stores = [
        {"name": "Meesho", "url": f"https://www.meesho.com/search?q={query}"},
        {"name": "Amazon", "url": f"https://www.amazon.in/s?k={query}"},
        {"name": "Flipkart", "url": f"https://www.flipkart.com/search?q={query}"}
    ]

    cols = st.columns(3)
    for i, store in enumerate(stores):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="deal-card">
                    <p style="color:#888; font-size:12px;">{store['name']}</p>
                    <p class="price-green">Check Price</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Go to {store['name']}", store['url'], use_container_width=True)

else:
    st.markdown("<br><p style='text-align:center; color:#ccc;'>Start your smart shopping journey above...</p>", unsafe_allow_html=True)
    
