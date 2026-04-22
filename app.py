import streamlit as st
from PIL import Image

# Page Setup
st.set_page_config(page_title="Buy Sasta - Smart Search", page_icon="🛍️", layout="wide")

# Custom CSS for Small Banner & Highlighted Fixed Search Bar
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #ffffff; }

    /* Chota Hero Banner (Reduced Height) */
    .hero-banner {
        background: linear-gradient(135deg, #2d1b69 0%, #1a1a3d 100%);
        padding: 40px 20px; /* Padding kam kar di height choti karne ke liye */
        text-align: center;
        color: white;
        border-radius: 0 0 30px 30px;
    }
    
    .hero-banner h1 { 
        font-size: 28px; 
        font-weight: 700; 
        color: white !important; 
        margin-bottom: 5px; 
    }
    
    /* Highlighted Search Bar inside the Banner */
    .search-wrapper {
        max-width: 750px;
        margin: 20px auto 0 auto;
        padding: 5px;
        background: rgba(255, 255, 255, 0.1); /* Glass effect */
        border-radius: 50px;
        border: 2px solid #2ecc71; /* Neon Green Highlight */
        box-shadow: 0 0 15px rgba(46, 204, 113, 0.4); /* Glow effect */
    }

    .stTextInput input {
        border-radius: 50px !important;
        padding: 25px 30px !important;
        border: none !important;
        font-size: 16px !important;
        background-color: white !important;
        color: black !important;
    }

    /* Result Cards */
    .deal-card {
        background: #fdfdfd;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #f0f0f0;
        margin-top: 15px;
    }
    .price-green { color: #2ecc71; font-size: 20px; font-weight: bold; }

    /* Hide unnecessary elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 1. Chota Hero Section with Fixed Search Inside
st.markdown("""
    <div class="hero-banner">
        <h1>Find <span style="color:#2ecc71;">Real Deals</span> & Compare Prices</h1>
        <div class="search-wrapper">
    """, unsafe_allow_html=True)

# Search input placed inside the wrapper (visually)
query = st.text_input("", placeholder="🔍 Paste link or search product name...", label_visibility="collapsed")

st.markdown("</div></div>", unsafe_allow_html=True)

# 2. Comparison Logic (Sirf search hone par dikhega)
if query:
    st.markdown(f"<br><h4 style='text-align:center; color:#333;'>Results for '{query}'</h4>", unsafe_allow_html=True)
    
    stores = [
        {"name": "Meesho", "price": "₹ Best Price", "url": f"https://www.meesho.com/search?q={query}"},
        {"name": "Flipkart", "price": "₹ Check Now", "url": f"https://www.flipkart.com/search?q={query}"},
        {"name": "Amazon", "price": "₹ View Deal", "url": f"https://www.amazon.in/s?k={query}"},
        {"name": "Myntra", "price": "₹ Fashion", "url": f"https://www.myntra.com/{query}"},
        {"name": "Ajio", "price": "₹ Brand Sale", "url": f"https://www.ajio.com/search/?text={query}"},
        {"name": "Jiomart", "price": "₹ Savings", "url": f"https://www.jiomart.com/search/{query}"}
    ]

    cols = st.columns(3)
    for i, store in enumerate(stores):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="deal-card">
                    <p style="color:#888; font-size:12px; margin:0;">{store['name']}</p>
                    <p class="price-green">{store['price']}</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Go to {store['name']}", store['url'], use_container_width=True)

# 3. Sidebar for Image Search (Clean & Simple)
with st.sidebar:
    st.markdown("### 📷 AI Photo Search")
    up = st.file_uploader("Product photo", type=['jpg','png','jpeg'])
    if up:
        st.image(Image.open(up))
        st.link_button("Find Similar Products", "https://images.google.com", use_container_width=True)
        
