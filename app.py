import streamlit as st
from PIL import Image

# Page Setup
st.set_page_config(page_title="Buy Sasta - Smart Deal Scanner", page_icon="🛍️", layout="wide")

# Custom CSS to match BuyHatke EXACT layout
st.markdown("""
    <style>
    /* Main App Background */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Top Purple/Blue Banner (BuyHatke Style) */
    .hero-banner {
        background: linear-gradient(135deg, #2d1b69 0%, #1a1a3d 100%);
        padding: 80px 20px;
        text-align: center;
        color: white;
        border-radius: 0 0 30px 30px;
        margin-bottom: -50px; /* Overlap for search bar */
    }
    
    .hero-banner h1 { font-size: 36px; font-weight: 700; color: white !important; }
    .hero-banner p { font-size: 18px; color: #b0b0d0 !important; }

    /* Centered Search Bar like Gemini/BuyHatke */
    .search-container {
        max-width: 700px;
        margin: 0 auto;
        position: relative;
        z-index: 100;
    }
    
    .stTextInput input {
        border-radius: 50px !important;
        padding: 30px 35px !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15) !important;
        font-size: 18px !important;
    }

    /* Comparison Deal Cards */
    .deal-card {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #eee;
        margin-top: 20px;
        transition: 0.3s;
    }
    .deal-card:hover { border-color: #2ecc71; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }

    .site-name { font-weight: 600; color: #555; margin-bottom: 5px; }
    .price-green { color: #2ecc71; font-size: 24px; font-weight: 800; } /* Green for Best Price */
    .price-red { color: #e74c3c; font-size: 24px; font-weight: 800; } /* Red for Other Prices */

    /* Hot Deals Section Header */
    .section-title {
        text-align: center;
        margin-top: 50px;
        color: #333 !important;
        font-weight: 700;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #6366f1 !important;
        border-radius: 25px !important;
        color: white !important;
        width: 100%;
        font-weight: 600;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Top Hero Section
st.markdown("""
    <div class="hero-banner">
        <p style="font-size: 14px; letter-spacing: 2px;">✨ MAGIC TRICK FOR ONLINE SHOPPING</p>
        <h1>Find <span style="color:#2ecc71;">Real Deals</span>, Skip the Fake Ones</h1>
        <p>Track genuine price drops, compare across stores, and shop smarter every day</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Centered Search Bar
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    query = st.text_input("", placeholder="Paste a Flipkart / Myntra link or search product...", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

if query:
    st.markdown(f"<h3 style='text-align:center; color:#333; margin-top:30px;'>Top Comparisons for: {query}</h3>", unsafe_allow_html=True)
    
    # 3x3 Grid for all platforms
    stores = [
        {"name": "Meesho", "price": "₹ Best Price", "color": "green", "url": f"https://www.meesho.com/search?q={query}"},
        {"name": "Amazon", "price": "₹ Check Live", "color": "red", "url": f"https://www.amazon.in/s?k={query}"},
        {"name": "Flipkart", "price": "₹ View Deal", "color": "red", "url": f"https://www.flipkart.com/search?q={query}"},
        {"name": "Myntra", "price": "₹ Fashion", "color": "red", "url": f"https://www.myntra.com/{query}"},
        {"name": "Ajio", "price": "₹ Brand Off", "color": "red", "url": f"https://www.ajio.com/search/?text={query}"},
        {"name": "Jiomart", "price": "₹ Big Savings", "color": "red", "url": f"https://www.jiomart.com/search/{query}"}
    ]

    c = st.columns(3)
    for i, store in enumerate(stores):
        with c[i % 3]:
            st.markdown(f"""
                <div class="deal-card">
                    <p class="site-name">{store['name']}</p>
                    <p class="price-{store['color']}">{store['price']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Buy on {store['name']}", store['url'], use_container_width=True)

else:
    # 3. Hot Deals Section (Landing Page)
    st.markdown("<h2 class='section-title'>Hot Deals</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>✨ Powered by Smart Deal Scanner</p>", unsafe_allow_html=True)
    
    d1, d2 = st.columns(2)
    with d1:
        st.markdown("""<div class="deal-card" style="background: linear-gradient(to right, #fdfbfb 0%, #ebedee 100%);">
            <h4 style="color:#333 !important;">Deals Under</h4>
            <h2 style="color:#6366f1 !important;">₹499</h2>
        </div>""", unsafe_allow_html=True)
    with d2:
        st.markdown("""<div class="deal-card" style="background: linear-gradient(to right, #fdfbfb 0%, #ebedee 100%);">
            <h4 style="color:#333 !important;">Deals Under</h4>
            <h2 style="color:#6366f1 !important;">₹999</h2>
        </div>""", unsafe_allow_html=True)

# 4. Sidebar for Image Search (Gemini Style)
with st.sidebar:
    st.header("📸 Visual Search")
    st.write("Photo se product dhoondhein")
    file = st.file_uploader("", type=['jpg','png','jpeg'])
    if file:
        st.image(Image.open(file))
        st.success("AI analyzing image...")
        st.link_button("Search on Google Lens", "https://images.google.com")
    
