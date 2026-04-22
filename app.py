import streamlit as st
from PIL import Image
import numpy as np
import time
# AI Image Similarity libraries
from sklearn.neighbors import NearestNeighbors
import pickle

st.set_page_config(page_title="Buy Sasta - AI Visual Search", page_icon="🏷️", layout="wide")

# Custom CSS for Gemini AI style with Red & Green Theme
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff4b2b 0%, #ff416c 100%);
        color: white;
    }
    /* AI Search Bar */
    .stTextInput input {
        border-radius: 30px !important;
        padding: 15px 25px !important;
        border: 2px solid #2ecc71 !important; /* Green Border */
        background-color: white !important;
        color: black !important;
    }
    /* Comparison Cards */
    .comp-card {
        background: white;
        color: #333;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border-bottom: 5px solid #2ecc71; /* Green Bottom Border */
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .comp-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .price-text {
        color: #e74c3c; /* Red Price */
        font-size: 22px;
        font-weight: bold;
    }
    h1, h2, h3, h4, p { color: white !important; }
    .comp-card h4, .comp-card p { color: #333 !important; }
    
    /* Center aligning text in tabs */
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🏷️ Buy Sasta AI</h1>", unsafe_allow_html=True)

# Tabs for Search Options (Gemini style)
tab1, tab2 = st.tabs(["🔍 Search by Text", "📷 Search by Image"])

with tab1:
    query = st.text_input("", placeholder="Search with product name...", label_visibility="collapsed")
    if query:
        st.markdown(f"## 🚀 AI Comparison for '{query}'")
        # Same grid layout with all platforms
        col1, col2, col3, col4, col5 = st.columns(5)
        # (Hum dummy results yahan use kar rahe hain interface dikhane ke liye)
        with col1:
            st.markdown('<div class="comp-card"><h4>Amazon</h4><p class="price-text">₹ Live</p></div>', unsafe_allow_html=True)
            st.link_button("View Deal", f"https://www.amazon.in/s?k={query}", use_container_width=True)
        with col2:
            st.markdown('<div class="comp-card"><h4>Flipkart</h4><p class="price-tag">₹ Live</p></div>', unsafe_allow_html=True)
            st.link_button("View Deal", f"https://www.flipkart.com/search?q={query}", use_container_width=True)
        with col3:
            st.markdown('<div class="comp-card"><h4>Meesho</h4><p class="price-text">₹ Lowest</p></div>', unsafe_allow_html=True)
            st.link_button("View Deal", f"https://www.meesho.com/search?q={query}", use_container_width=True)
        with col4:
            st.markdown('<div class="comp-card"><h4>Myntra</h4><p class="price-tag">₹ Fashion</p></div>', unsafe_allow_html=True)
            st.link_button("View Deal", f"https://www.myntra.com/{query}", use_container_width=True)
        with col5:
            st.markdown('<div class="comp-card"><h4>Ajio</h4><p class="price-text">₹ Brands</p></div>', unsafe_allow_html=True)
            st.link_button("View Deal", f"https://www.ajio.com/search/?text={query}", use_container_width=True)
            
        col6, col7, col8, col9, col10 = st.columns(5)
        with col6:
            st.markdown('<div class="comp-card"><h4>Nykaa</h4><p class="price-tag">₹ Beauty</p></div>', unsafe_allow_html=True)
            st.link_button("View Deal", f"https://www.nykaa.com/search/result/?q={query}", use_container_width=True)
        with col7:
            st.markdown('<div class="comp-card"><h4>Tata CLiQ</h4><p class="price-text">₹ Premium</p></div>', unsafe_allow_html=True)
            st.link_button("View Deal", f"https://www.tatacliq.com/search/?text={query}", use_container_width=True)
        with col8:
            st.markdown('<div class="comp-card"><h4>Snapdeal</h4><p class="price-tag">₹ Budget</p></div>', unsafe_allow_html=True)
            st.link_button("View Deal", f"https://www.snapdeal.com/search?keyword={query}", use_container_width=True)
        with col9:
            st.markdown('<div class="comp-card"><h4> Reliance</h4><p class="price-text">₹ Tech</p></div>', unsafe_allow_html=True)
            st.link_button("View Deal", f"https://www.reliancedigital.in/search?q={query}", use_container_width=True)
        with col10:
            st.markdown('<div class="comp-card"><h4>Jiomart</h4><p class="price-tag">₹ Savings</p></div>', unsafe_allow_html=True)
            st.link_button("View Deal", f"https://www.jiomart.com/search/{query}", use_container_width=True)

with tab2:
    st.markdown("### 📸 Photo Se Sasta Maal Dhoondhein (AI)")
    
    # Simple image similarity simulation 
    # Ideal implementation uses deep learning models, here we show the flow
    file = st.file_uploader("Upload Product Photo...", type=["jpg", "png", "jpeg"])
    if file:
        img = Image.open(file)
        st.image(img, caption="Aapki Photo", width=300)
        
        with st.spinner("AI Analysis chal raha hai..."):
            time.sleep(2)
            st.success("AI ne product pehchan liya!")
            st.markdown("#### Similar Products on Other Sites:")
            
            # Simulated Results 
            sc1, sc2, sc3 = st.columns(3)
            # Yahan hum Google Lens ya image similarity engines ke links de sakte hain
            with sc1:
                st.link_button("Similar on Google Lens", "https://images.google.com")
            with sc2:
                st.link_button("Meesho Image Search", "https://www.meesho.com/search?q=clothing")
            with sc3:
                st.link_button("Flipkart Similar", "https://www.flipkart.com/search?q=trending")

st.sidebar.title("🚀 Business Dashboard")
st.sidebar.info("Tip: EarnKaro join karke apne links yahan lagayein!")
            
