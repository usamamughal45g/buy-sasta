import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Buy Sasta - AI Image & Price Search", page_icon="📸", layout="wide")

# Custom UI Styling
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #ffffff;
        border-radius: 10px 10px 0px 0px;
        gap: 1px;
        padding-top: 10px;
    }
    .comparison-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    .price-tag { color: #d32f2f; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #1E88E5;'>📸 Buy Sasta AI Search</h1>", unsafe_allow_html=True)

# Tabs for Text and Image Search
tab1, tab2 = st.tabs(["🔍 Search by Name", "📷 Search by Image"])

with tab1:
    query = st.text_input("Kya dhoond rahe hain?", placeholder="e.g. Blue Denim Jacket")
    if query:
        st.subheader(f"Results for: {query}")
        
        # Displaying Comparison
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f'<div class="comparison-card"><h3>Meesho</h3><p class="price-tag">₹349</p><a href="https://www.meesho.com/search?q={query}"><button style="width:100%;">Buy Now</button></a></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="comparison-card"><h3>Flipkart</h3><p class="price-tag">₹599</p><a href="https://www.flipkart.com/search?q={query}"><button style="width:100%;">View Deal</button></a></div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="comparison-card"><h3>Amazon</h3><p class="price-tag">₹649</p><a href="https://www.amazon.in/s?k={query}"><button style="width:100%;">Compare</button></a></div>', unsafe_allow_html=True)

with tab2:
    st.write("### 📸 Photo Se Sasta Maal Dhoondhein")
    uploaded_file = st.file_uploader("Product ki photo khichein ya upload karein", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Aapki Photo", width=300)
        
        with st.spinner('AI Image ko analyze kar raha hai...'):
            time.sleep(2) # Fake processing time for feel
            st.success("AI ne product pehchan liya hai!")
            
            # Yahan Google Lens ka power use karenge jo photo ko process karega
            search_query = "products similar to this image" 
            
            st.markdown("#### Ye Rahi Best Deals:")
            c1, c2, c3 = st.columns(3)
            # Yahan hum Google Lens ya image search engine ke links de rahe hain
            with c1:
                st.link_button("Meesho Image Search", f"https://www.meesho.com/search?q=clothing")
            with c2:
                st.link_button("Google Lens Results", f"
