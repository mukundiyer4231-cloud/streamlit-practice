import streamlit as st
from datetime import datetime
import base64
import os
import random

# Import custom messages
from messages import (
    ROSE_DAY, PROPOSE_DAY, CHOCOLATE_DAY, TEDDY_DAY,
    PROMISE_DAY, HUG_DAY, KISS_DAY, VALENTINES_DAY
)

# Page configuration - mobile optimized
st.set_page_config(
    page_title="💕 Aditi_simp.exe 💕",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Day configuration
VALENTINE_DAYS = {
    7: {"name": "Rose Day", "emoji": "🌹", "message": ROSE_DAY, "type": "animated_roses"},
    8: {"name": "Propose Day", "emoji": "💍", "message": PROPOSE_DAY, "type": "propose"},
    9: {"name": "Chocolate Day", "emoji": "🍫", "message": CHOCOLATE_DAY, "type": "image_bg", "image": "chocolate.png"},
    10: {"name": "Teddy Day", "emoji": "🧸", "message": TEDDY_DAY, "type": "image_bg", "image": "teddy.png"},
    11: {"name": "Promise Day", "emoji": "🤞", "message": PROMISE_DAY, "type": "image_bg", "image": "promise.png"},
    12: {"name": "Hug Day", "emoji": "🤗", "message": HUG_DAY, "type": "image_bg", "image": "hug.png"},
    13: {"name": "Kiss Day", "emoji": "💋", "message": KISS_DAY, "type": "image_bg", "image": "kiss.png"},
    14: {"name": "Valentine's Day", "emoji": "❤️", "message": VALENTINES_DAY, "type": "animated_hearts"},
}

def get_base64_image(image_path):
    """Convert image to base64 for embedding"""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

def get_mobile_base_css():
    """Base CSS for mobile-first design"""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@400;600&display=swap');
    
    /* Mobile-first viewport settings */
    html, body, [data-testid="stAppViewContainer"] {
        max-width: 100vw;
        overflow-x: hidden;
    }
    
    .stApp {
        min-height: 100vh;
        padding: 0;
        margin: 0;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mobile card styling */
    .mobile-card {
        background: rgba(255, 255, 255, 0.92);
        border-radius: 24px;
        padding: 30px 24px;
        margin: 20px auto;
        max-width: 380px;
        width: 90%;
        box-shadow: 
            0 10px 40px rgba(0, 0, 0, 0.2),
            0 0 0 1px rgba(255, 255, 255, 0.8) inset;
        position: relative;
        z-index: 10;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
    }
    
    .day-emoji {
        font-size: 4rem;
        text-align: center;
        display: block;
        margin-bottom: 16px;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.15); }
    }
    
    .day-title {
        font-family: 'Dancing Script', cursive;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 8px;
        line-height: 1.2;
    }
    
    .message-text {
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        color: #4a4a4a;
        text-align: center;
        line-height: 1.7;
        padding: 16px;
        background: rgba(255, 255, 255, 0.6);
        border-radius: 16px;
        margin-top: 16px;
    }
    
    /* Floating elements */
    .floating-element {
        position: fixed;
        z-index: 0;
        pointer-events: none;
    }
    
    /* Preview dropdown styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 12px !important;
        border: 2px solid rgba(255, 105, 180, 0.3) !important;
    }
    
    .preview-container {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 16px;
        padding: 16px;
        margin: 16px auto;
        max-width: 380px;
        width: 90%;
        text-align: center;
        backdrop-filter: blur(10px);
        position: relative;
        z-index: 100;
    }
    
    .preview-label {
        font-family: 'Poppins', sans-serif;
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 8px;
    }
    </style>
    """

def get_rose_day_css():
    """Rose Day - Pink with animated roses"""
    return get_mobile_base_css() + """
    <style>
    .stApp {
        background: linear-gradient(135deg, #FFB6C1 0%, #FF69B4 50%, #FFB6C1 100%);
    }
    
    .day-title { color: #FF1493; text-shadow: 2px 2px 4px rgba(255, 20, 147, 0.2); }
    .message-text { background: linear-gradient(135deg, #FFF0F5 0%, #FFE4E1 100%); }
    
    .pixel-rose {
        position: fixed;
        font-size: 28px;
        image-rendering: pixelated;
        animation: floatRose 8s ease-in-out infinite;
        z-index: 0;
        opacity: 0.85;
    }
    
    @keyframes floatRose {
        0%, 100% { transform: translateY(0) rotate(0deg) scale(1); }
        25% { transform: translateY(-25px) rotate(8deg) scale(1.1); }
        50% { transform: translateY(-12px) rotate(-4deg) scale(1.05); }
        75% { transform: translateY(-35px) rotate(12deg) scale(1.12); }
    }
    </style>
    """

def get_valentines_day_css():
    """Valentine's Day - Red with animated hearts"""
    return get_mobile_base_css() + """
    <style>
    .stApp {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF1493 50%, #DC143C 100%);
    }
    
    .day-title { color: #DC143C; text-shadow: 2px 2px 4px rgba(220, 20, 60, 0.2); }
    .message-text { background: linear-gradient(135deg, #FFE4E1 0%, #FFC0CB 100%); }
    
    .pixel-heart {
        position: fixed;
        font-size: 30px;
        image-rendering: pixelated;
        animation: floatHeart 6s ease-in-out infinite;
        z-index: 0;
    }
    
    @keyframes floatHeart {
        0%, 100% { transform: translateY(0) scale(1); opacity: 0.85; }
        50% { transform: translateY(-45px) scale(1.25); opacity: 1; }
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        25% { transform: scale(1.08); }
        50% { transform: scale(1); }
        75% { transform: scale(1.15); }
    }
    
    .day-emoji { animation: heartbeat 1.2s ease-in-out infinite; }
    </style>
    """

def get_propose_day_css():
    """Propose Day - Purple with sparkles"""
    return get_mobile_base_css() + """
    <style>
    .stApp {
        background: linear-gradient(135deg, #E6E6FA 0%, #DDA0DD 50%, #DA70D6 100%);
    }
    
    .day-title { color: #9932CC; text-shadow: 2px 2px 4px rgba(153, 50, 204, 0.2); }
    .message-text { background: linear-gradient(135deg, #F8F0FF 0%, #E8D5F0 100%); }
    
    .sparkle {
        position: fixed;
        font-size: 20px;
        animation: twinkle 3s ease-in-out infinite;
        z-index: 0;
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 0.3; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); }
    }
    
    @keyframes sparkle-rotate {
        0%, 100% { transform: scale(1) rotate(0deg); }
        25% { transform: scale(1.1) rotate(5deg); }
        50% { transform: scale(1.05) rotate(-5deg); }
        75% { transform: scale(1.15) rotate(3deg); }
    }
    
    .day-emoji { animation: sparkle-rotate 2s ease-in-out infinite; }
    
    .yes-result {
        text-align: center;
        padding: 24px;
    }
    
    .yes-result h2 {
        font-family: 'Dancing Script', cursive;
        color: #FF1493;
        font-size: 2rem;
        margin-bottom: 12px;
    }
    
    .yes-result .heart {
        font-size: 4rem;
        animation: heartbeat 1s ease-in-out infinite;
    }
    </style>
    """

def get_image_background_css(image_base64, title_color="#FFFFFF"):
    """CSS for days with PNG background images"""
    if image_base64:
        bg_image = f"url('data:image/png;base64,{image_base64}')"
    else:
        bg_image = "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
    
    return get_mobile_base_css() + f"""
    <style>
    .stApp {{
        background-image: {bg_image};
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* Dark overlay for better text readability */
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.3);
        z-index: 0;
    }}
    
    .day-title {{ 
        color: {title_color}; 
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
    }}
    
    .message-text {{ 
        background: rgba(255, 255, 255, 0.85);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    }}
    
    .mobile-card {{
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3);
    }}
    
    @keyframes float {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-10px); }}
    }}
    
    .day-emoji {{ animation: float 3s ease-in-out infinite; }}
    </style>
    """

def get_waiting_css():
    """Waiting page CSS"""
    return get_mobile_base_css() + """
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .day-title { color: #764ba2; }
    .message-text { background: rgba(255, 255, 255, 0.8); }
    </style>
    """

def generate_floating_elements(element_type, count=12):
    """Generate floating decorative elements"""
    elements_html = ""
    
    if element_type == "roses":
        emoji = "🌹"
        class_name = "pixel-rose"
    elif element_type == "hearts":
        emoji = "❤️"
        class_name = "pixel-heart"
    else:
        emoji = "✨"
        class_name = "sparkle"
    
    for i in range(count):
        left = random.randint(2, 95)
        top = random.randint(5, 85)
        delay = random.uniform(0, 5)
        size = random.randint(18, 36)
        elements_html += f'<div class="{class_name}" style="left: {left}%; top: {top}%; animation-delay: {delay}s; font-size: {size}px;">{emoji}</div>'
    
    return elements_html

def render_card_content(day_info):
    """Render the mobile cardview content"""
    return f"""
    <div class="mobile-card">
        <span class="day-emoji">{day_info['emoji']}</span>
        <div class="message-text">{day_info['message']}</div>
    </div>
    """

def render_propose_day(day_info):
    """Special rendering for Propose Day with buttons inside card that move"""
    st.markdown(get_propose_day_css(), unsafe_allow_html=True)
    st.markdown(generate_floating_elements("sparkles", 15), unsafe_allow_html=True)
    
    # Initialize session state
    if 'said_yes' not in st.session_state:
        st.session_state.said_yes = False
    if 'no_clicks' not in st.session_state:
        st.session_state.no_clicks = 0
    if 'no_position' not in st.session_state:
        st.session_state.no_position = {"x": 0, "y": 0}
    
    if st.session_state.said_yes:
        st.markdown(f"""
        <div class="mobile-card">
            <span class="day-emoji">{day_info['emoji']}</span>
            <div class="message-text">{day_info['message']}</div>
            <div class="yes-result">
                <h2>💕 Yay! I love you! 💕</h2>
                <div class="heart">💖</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Card with message
        st.markdown(f"""
        <div class="mobile-card">
            <span class="day-emoji">{day_info['emoji']}</span>
            <div class="message-text">{day_info['message']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Get current displacement values
        x_offset = st.session_state.no_position["x"]
        y_offset = st.session_state.no_position["y"]
        
        # Button container with dynamic positioning
        st.markdown(f"""
        <style>
        /* YES button styling */
        div[data-testid="stHorizontalBlock"] > div:first-child button {{
            background: linear-gradient(135deg, #FF69B4, #FF1493) !important;
            color: white !important;
            border: none !important;
            padding: 16px 24px !important;
            font-size: 1.2rem !important;
            border-radius: 50px !important;
            width: 100% !important;
            font-weight: 600 !important;
            box-shadow: 0 6px 20px rgba(255, 20, 147, 0.4) !important;
            transition: all 0.2s ease !important;
        }}
        div[data-testid="stHorizontalBlock"] > div:first-child button:hover {{
            transform: scale(1.05) !important;
            box-shadow: 0 8px 25px rgba(255, 20, 147, 0.5) !important;
        }}
        
        /* NO button styling with displacement */
        div[data-testid="stHorizontalBlock"] > div:last-child {{
            transform: translate({x_offset}px, {y_offset}px) !important;
            transition: transform 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
        }}
        div[data-testid="stHorizontalBlock"] > div:last-child button {{
            background: linear-gradient(135deg, #a0a0a0, #808080) !important;
            color: white !important;
            border: none !important;
            padding: 16px 24px !important;
            font-size: 1.2rem !important;
            border-radius: 50px !important;
            width: 100% !important;
            transition: all 0.2s ease !important;
        }}
        </style>
        """, unsafe_allow_html=True)
        
        # Buttons
        st.markdown('<div style="max-width: 380px; margin: 20px auto; padding: 0 20px;">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💕 YES 💕", key="yes_btn", use_container_width=True):
                st.session_state.said_yes = True
                st.rerun()
        
        with col2:
            if st.button("No 😢", key="no_btn", use_container_width=True):
                st.session_state.no_clicks += 1
                # Random displacement - button jumps around
                directions = [
                    {"x": random.randint(-80, 80), "y": random.randint(-60, 60)},
                    {"x": random.randint(-100, 100), "y": random.randint(-80, 80)},
                    {"x": random.randint(-60, 60), "y": random.randint(-100, 100)},
                ]
                st.session_state.no_position = random.choice(directions)
                
                # Fun messages that rotate
                messages = [
                    "Haha! That's not an option! 😜",
                    "Nice try! But no! 💕",
                    "The button ran away! 🏃",
                    "Can't catch it! 😂",
                    "Just say YES already! �",
                ]
                st.toast(random.choice(messages), icon="💕")
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

def render_image_bg_day(day_info):
    """Render days with PNG as background"""
    image_path = f"assets/{day_info['image']}"
    img_base64 = get_base64_image(image_path)
    
    # Title colors for each day
    title_colors = {
        "Chocolate Day": "#8B4513",
        "Teddy Day": "#8B7355",
        "Promise Day": "#1E3A5F",
        "Hug Day": "#C71585",
        "Kiss Day": "#B22222",
    }
    
    st.markdown(get_image_background_css(img_base64, title_colors.get(day_info['name'], "#333333")), unsafe_allow_html=True)
    
    # Show placeholder message if image not found
    if not img_base64:
        st.markdown(f"""
        <div class="mobile-card">
            <span class="day-emoji">{day_info['emoji']}</span>
            <p style="text-align: center; color: #888; padding: 20px;">
                📷 Add your background image:<br>
                <code>assets/{day_info['image']}</code>
            </p>
            <div class="message-text">{day_info['message']}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(render_card_content(day_info), unsafe_allow_html=True)

def render_day(day_num):
    """Render a specific day"""
    day_info = VALENTINE_DAYS.get(day_num)
    if not day_info:
        return
    
    day_type = day_info["type"]
    
    if day_type == "animated_roses":
        st.markdown(get_rose_day_css(), unsafe_allow_html=True)
        st.markdown(generate_floating_elements("roses", 15), unsafe_allow_html=True)
        st.markdown(render_card_content(day_info), unsafe_allow_html=True)
    
    elif day_type == "animated_hearts":
        st.markdown(get_valentines_day_css(), unsafe_allow_html=True)
        st.markdown(generate_floating_elements("hearts", 18), unsafe_allow_html=True)
        st.markdown(render_card_content(day_info), unsafe_allow_html=True)
    
    elif day_type == "propose":
        render_propose_day(day_info)
    
    elif day_type == "image_bg":
        render_image_bg_day(day_info)

def render_waiting():
    """Render waiting page"""
    st.markdown(get_waiting_css(), unsafe_allow_html=True)
    st.markdown("""
    <div class="mobile-card">
        <span class="day-emoji">💝</span>
        <h1 class="day-title" style="color: #764ba2;">Coming Soon!</h1>
        <div class="message-text">
            Something special is being prepared for you...<br><br>
            Come back between February 7-14 for a surprise! 💕
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==================== MAIN APP ====================

def main():
    # Get current date
    today = datetime.now()
    current_day = today.day
    current_month = today.month
    
    # Preview dropdown - always visible at top
    st.markdown("""
    <div class="preview-container">
        <p class="preview-label">🎨 Preview Different Days</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dropdown for day selection
    day_options = {
        0: "📅 Live Mode (Auto-detect date)",
        7: "🌹 Feb 7 - Rose Day",
        8: "💍 Feb 8 - Propose Day",
        9: "🍫 Feb 9 - Chocolate Day",
        10: "🧸 Feb 10 - Teddy Day",
        11: "🤞 Feb 11 - Promise Day",
        12: "🤗 Feb 12 - Hug Day",
        13: "💋 Feb 13 - Kiss Day",
        14: "❤️ Feb 14 - Valentine's Day",
    }
    
    selected_day = st.selectbox(
        "Select a day to preview:",
        options=list(day_options.keys()),
        format_func=lambda x: day_options[x],
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Determine which day to show
    if selected_day == 0:
        # Live mode - check actual date
        if current_month == 2 and 7 <= current_day <= 14:
            render_day(current_day)
        else:
            render_waiting()
    else:
        # Preview mode
        render_day(selected_day)

if __name__ == "__main__":
    main()
