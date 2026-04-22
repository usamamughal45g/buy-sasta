import streamlit as st
from PIL import Image

st.set_page_config(page_title="Buy Sasta - Smart Comparison", page_icon="🛍️", layout="wide")

# Custom CSS for BuyHatke Style Design
st.markdown("""
    <style>
    /* Main Background and Font */
    .stApp {
        background-color: #0f172a; /* Dark sleek background */
        font-family: 'Inter', sans-serif;
    }
    
    /* Top Banner like BuyHatke */
    .hero-section {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 60px 20px;
        text-align: center;
        border-radius: 0 0 40px 40px;
        margin-bottom: 40px;
    }
    
    .hero-title {
        color: #f8fafc;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        color: #94a3b8;
        font-size: 18px;
    }

    /* BuyHatke Style Search Bar */
    .stTextInput input {
        border-radius: 50px !important;
        padding: 25px 35px !important;
        border: 2px solid #6366f1 !important; /* Purple Border */
        background-color: #1e293b !important;
        color: white !important;
        font-size: 20px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3) !important;
    }

    /* Comparison Cards */
    .deal-card {
        background: #1e293b;
        color: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid #334155;
        transition: 0.3s;
        margin-bottom: 20px;
    }
    
    .deal-card:hover {
        transform: translateY(-10px);
        border-color: #6366f1;
    }

    .store-name { font-size: 14px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; }
    .price-val { font-size: 28px; font-weight: bold; color: #10b981; margin: 10px 0; } /* Green Price */
    
    /* Custom Button */
    .stButton>button {
        background: #6366f1 !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 10px 25px !important;
        border: none !important;
        width: 100%;
        font-weight: bold;
    }

    /* Section Headers */
    h2, h3 { color: #f8fafc !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# Top Hero Section
st.markdown("""
    <div class="hero-section">
        <div class="hero-title">✨ Magic Trick for Online Shopping</div>
        <div class="hero-subtitle">Find Real Deals. Skip the Fake Ones.</div>
    </div>
    """, unsafe_allow_html=True)

# Search Bar Area
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    query = st.text_input("", placeholder="Paste a link or search for products...", label_visibility="collapsed")

if query:
    st.markdown(f"### 🔍 Live Comparison for: {query}")
    
    # 3x3 Grid like professional sites
    stores = [
        {"name": "Amazon", "price": "₹ Live", "tag": "Trusted", "url": f"https://www.amazon.in/s?k={query}"},
        {"name": "Flipkart", "price": "₹ Best", "tag": "Popular", "url": f"https://www.flipkart.com/search?q={query}"},
        {"name": "Meesho", "price": "₹ Low", "tag": "Budget", "url": f"https://www.meesho.com/search?q={query}"},
        {"name": "Myntra", "price": "₹ Trend", "tag": "Fashion", "url": f"https://www.myntra.com/{query}"},
        {"name": "Ajio", "price": "₹ Deal", "tag": "Premium", "url": f"https://www.ajio.com/search/?text={query}"},
        {"name": "Tata CLiQ", "price": "₹ Lux", "tag": "Original", "url": f"https://www.tatacliq.com/search/?text={query}"}
    ]

    c = st.columns(3)
    for i, store in enumerate(stores):
        with c[i % 3]:
            st.markdown(f"""
                <div class="deal-card">
                    <div class="store-name">{store['name']}</div>
                    <div class="price-val">{store['price']}</div>
                    <div style="background:#334155; padding:4px 12px; border-radius:15px; font-size:12px; display:inline-block;">{store['tag']}</div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Grab Deal", store['url'], use_container_width=True)

else:
    # Home Page Content
    st.markdown("<br><h2>🔥 Hot Deals Today</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#94a3b8;'>Powered by Smart Deal Scanner AI</p>", unsafe_allow_html=True)
    
    # Showcase some dummy categories
    cat1, cat2, cat3 = st.columns(3)
    with cat1: st.markdown('<div class="deal-card"><h4>Mobile Deals</h4><p>Under ₹15,000</p></div>', unsafe_allow_html=True)
    with cat2: st.markdown('<div class="deal-card"><h4>Fashion Deals</h4><p>Min 60% Off</p></div>', unsafe_allow_html=True)
    with cat3: st.markdown('<div class="deal-card"><h4>Laptop Deals</h4><p>Extra ₹5000 Off</p></div>', unsafe_allow_html=True)

# Footer/Image Search Simulation
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/google-lens.png", width=50)
    st.header("📸 Visual Search")
    img_file = st.file_uploader("Product photo se search karein", type=['jpg', 'png', 'jpeg'])
    if img_file:
        st.image(img_file)
        st.success("AI Analysis active!")
        
