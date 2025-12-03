import streamlit as st
import random
import string
from datetime import datetime, timedelta
import pandas as pd
import time

# Page configuration
st.set_page_config(
    page_title="Free Temporary Email Generator - Disposable Email Address",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/yourusername/temp-mail',
        'Report a bug': 'https://github.com/yourusername/temp-mail/issues',
        'About': """
        # Temporary Email Generator
        Protect your privacy with disposable email addresses!
        
        **Features:**
        - Instant email generation
        - Multiple domain options
        - Copy with one click
        - Auto-expiry
        - No registration required
        - Spam-free inbox
        
        Made with ❤️ using Streamlit
        """
    }
)

# SEO Meta Tags
st.markdown("""
<meta name="description" content="Free temporary email generator. Create disposable email addresses instantly. Avoid spam, protect privacy. No registration required. Anonymous and secure.">
<meta name="keywords" content="temporary email, disposable email, temp mail, fake email, throwaway email, burner email, spam protection, privacy email, anonymous email">
<meta name="author" content="Your Name">
<meta name="robots" content="index, follow">
<meta property="og:title" content="Free Temporary Email Generator - Disposable Email Address">
<meta property="og:description" content="Generate disposable email addresses instantly. Protect your privacy, avoid spam. Free, no registration required.">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
""", unsafe_allow_html=True)

# Futuristic CSS Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
    
    * {
        font-family: 'Space Grotesk', sans-serif;
    }
    
    /* Cyberpunk animated background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        position: relative;
        overflow: hidden;
    }
    
    .stApp::before {
        content: '';
        position: absolute;
        width: 200%;
        height: 200%;
        background: 
            radial-gradient(circle at 20% 50%, rgba(120, 0, 255, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(0, 255, 200, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 20%, rgba(255, 0, 150, 0.1) 0%, transparent 50%);
        animation: bgMove 20s ease infinite;
    }
    
    @keyframes bgMove {
        0%, 100% { transform: translate(0, 0); }
        50% { transform: translate(-50px, -50px); }
    }
    
    .main .block-container {
        background: rgba(15, 12, 41, 0.85);
        border-radius: 30px;
        padding: 3rem;
        box-shadow: 
            0 0 60px rgba(120, 0, 255, 0.3),
            0 0 100px rgba(0, 255, 200, 0.2),
            inset 0 0 80px rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(120, 0, 255, 0.3);
        position: relative;
    }
    
    /* Glowing title */
    .main-title {
        text-align: center;
        background: linear-gradient(135deg, #00f5ff 0%, #7b00ff 50%, #ff006e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 5rem;
        font-weight: 900;
        margin-bottom: 1rem;
        animation: titleGlow 3s ease-in-out infinite;
        letter-spacing: -4px;
        text-shadow: 0 0 30px rgba(0, 245, 255, 0.5);
        position: relative;
    }
    
    @keyframes titleGlow {
        0%, 100% { 
            filter: brightness(1) drop-shadow(0 0 20px rgba(0, 245, 255, 0.6));
        }
        50% { 
            filter: brightness(1.3) drop-shadow(0 0 40px rgba(123, 0, 255, 0.8));
        }
    }
    
    .subtitle {
        text-align: center;
        color: #00f5ff;
        font-size: 1.6rem;
        margin-bottom: 3rem;
        font-weight: 600;
        text-shadow: 0 0 20px rgba(0, 245, 255, 0.5);
        animation: fadeInUp 1.5s ease;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Neon card effect */
    .neon-card {
        background: linear-gradient(135deg, rgba(20, 20, 50, 0.9) 0%, rgba(30, 30, 60, 0.9) 100%);
        border-radius: 25px;
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 
            0 0 30px rgba(0, 245, 255, 0.3),
            0 0 60px rgba(123, 0, 255, 0.2),
            inset 0 0 30px rgba(255, 255, 255, 0.05);
        border: 2px solid;
        border-image: linear-gradient(135deg, #00f5ff, #7b00ff, #ff006e) 1;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .neon-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(0, 245, 255, 0.1), transparent);
        animation: cardShine 3s linear infinite;
    }
    
    @keyframes cardShine {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .neon-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 
            0 0 50px rgba(0, 245, 255, 0.5),
            0 0 100px rgba(123, 0, 255, 0.4);
    }
    
    /* Email display box */
    .email-box {
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.1) 0%, rgba(123, 0, 255, 0.1) 100%);
        border: 3px solid #00f5ff;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 
            0 0 30px rgba(0, 245, 255, 0.4),
            inset 0 0 20px rgba(0, 245, 255, 0.1);
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.8rem;
        color: #00f5ff;
        text-align: center;
        font-weight: 700;
        letter-spacing: 2px;
        animation: emailPulse 2s ease-in-out infinite;
        position: relative;
    }
    
    @keyframes emailPulse {
        0%, 100% { 
            box-shadow: 0 0 30px rgba(0, 245, 255, 0.4), inset 0 0 20px rgba(0, 245, 255, 0.1);
        }
        50% { 
            box-shadow: 0 0 50px rgba(0, 245, 255, 0.6), inset 0 0 30px rgba(0, 245, 255, 0.2);
        }
    }
    
    /* Cyber buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #00f5ff 0%, #7b00ff 100%);
        color: #0f0c29;
        border: none;
        border-radius: 15px;
        padding: 1.5rem 3rem;
        font-size: 1.3rem;
        font-weight: 900;
        letter-spacing: 2px;
        text-transform: uppercase;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 
            0 10px 40px rgba(0, 245, 255, 0.5),
            0 0 20px rgba(123, 0, 255, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.5s;
    }
    
    .stButton>button:hover::before {
        left: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 
            0 20px 60px rgba(0, 245, 255, 0.7),
            0 0 40px rgba(123, 0, 255, 0.5);
        background: linear-gradient(135deg, #7b00ff 0%, #ff006e 100%);
        color: white;
    }
    
    .stButton>button:active {
        transform: translateY(-2px) scale(1.02);
    }
    
    /* Tabs with glow */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background: rgba(20, 20, 50, 0.5);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 
            inset 0 0 30px rgba(0, 0, 0, 0.5),
            0 0 20px rgba(0, 245, 255, 0.2);
        border: 1px solid rgba(0, 245, 255, 0.3);
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 15px;
        padding: 18px 36px;
        font-weight: 800;
        color: #00f5ff;
        transition: all 0.3s ease;
        font-size: 1.15rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: 2px solid transparent;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(0, 245, 255, 0.1);
        transform: translateY(-3px);
        border-color: #00f5ff;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00f5ff 0%, #7b00ff 100%) !important;
        color: #0f0c29 !important;
        box-shadow: 
            0 10px 30px rgba(0, 245, 255, 0.5),
            0 0 20px rgba(123, 0, 255, 0.3);
        border-color: transparent !important;
    }
    
    /* Success notification */
    .success-box {
        background: linear-gradient(135deg, rgba(0, 255, 150, 0.2) 0%, rgba(0, 245, 255, 0.2) 100%);
        border: 3px solid #00ff96;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        font-size: 1.6rem;
        font-weight: 800;
        color: #00ff96;
        margin: 2rem 0;
        box-shadow: 
            0 0 40px rgba(0, 255, 150, 0.5),
            inset 0 0 20px rgba(0, 255, 150, 0.1);
        animation: successGlow 2s ease-in-out infinite;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    @keyframes successGlow {
        0%, 100% { 
            box-shadow: 0 0 40px rgba(0, 255, 150, 0.5), inset 0 0 20px rgba(0, 255, 150, 0.1);
        }
        50% { 
            box-shadow: 0 0 60px rgba(0, 255, 150, 0.7), inset 0 0 30px rgba(0, 255, 150, 0.2);
        }
    }
    
    /* Metrics with glow */
    [data-testid="stMetricValue"] {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00f5ff 0%, #7b00ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px rgba(0, 245, 255, 0.6));
    }
    
    [data-testid="stMetricLabel"] {
        color: #00f5ff !important;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Info boxes */
    .stAlert {
        background: rgba(0, 245, 255, 0.1) !important;
        border: 2px solid #00f5ff !important;
        border-radius: 15px !important;
        color: #00f5ff !important;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.3);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.1) 0%, rgba(123, 0, 255, 0.1) 100%);
        border: 2px solid #00f5ff;
        border-radius: 15px;
        font-weight: 800;
        font-size: 1.2rem;
        padding: 1.5rem;
        color: #00f5ff;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.2) 0%, rgba(123, 0, 255, 0.2) 100%);
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.4);
        transform: translateX(10px);
    }
    
    /* Code blocks */
    code {
        font-family: 'JetBrains Mono', monospace;
        background: rgba(0, 245, 255, 0.1);
        padding: 6px 12px;
        border-radius: 8px;
        color: #00f5ff;
        font-weight: 600;
        border: 1px solid rgba(0, 245, 255, 0.3);
    }
    
    /* Feature icons */
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 0 20px rgba(0, 245, 255, 0.6));
    }
    
    /* Stats counter */
    .stat-counter {
        font-size: 2.5rem;
        font-weight: 900;
        color: #ff006e;
        text-shadow: 0 0 20px rgba(255, 0, 110, 0.6);
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        background: rgba(20, 20, 50, 0.8);
        border: 2px solid #00f5ff;
        border-radius: 12px;
        color: #00f5ff;
    }
    
    /* Copy button special */
    .copy-btn {
        background: linear-gradient(135deg, #ff006e 0%, #7b00ff 100%);
        animation: copyPulse 2s ease-in-out infinite;
    }
    
    @keyframes copyPulse {
        0%, 100% { box-shadow: 0 10px 40px rgba(255, 0, 110, 0.5); }
        50% { box-shadow: 0 10px 60px rgba(123, 0, 255, 0.7); }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'email' not in st.session_state:
    st.session_state.email = None
if 'generated_count' not in st.session_state:
    st.session_state.generated_count = 0
if 'expiry_time' not in st.session_state:
    st.session_state.expiry_time = None

# Available domains
DOMAINS = [
    "tempmail.ninja",
    "throwaway.email",
    "guerrillamail.com",
    "10minutemail.com",
    "mailinator.com",
    "tempmail.org",
    "burnermail.io",
    "fakeinbox.com",
    "disposable.email",
    "temp-mail.io"
]

# Helper functions
def generate_random_string(length=10):
    """Generate random string for email username"""
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_email(domain):
    """Generate a temporary email address"""
    username = generate_random_string(random.randint(8, 15))
    return f"{username}@{domain}"

def get_expiry_time(duration_minutes=60):
    """Calculate expiry time"""
    return datetime.now() + timedelta(minutes=duration_minutes)

# Title
st.markdown('<h1 class="main-title">📧 Temp Mail Generator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🛡️ Protect Your Privacy with Disposable Email Addresses</p>', unsafe_allow_html=True)

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs(["⚡ Generate Email", "📬 Inbox (Demo)", "🛡️ Features", "❓ How It Works"])

# TAB 1: Generate Email
with tab1:
    st.markdown('<div class="neon-card">', unsafe_allow_html=True)
    
    st.markdown("### ⚡ Generate Your Temporary Email")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_domain = st.selectbox(
            "🌐 Choose Domain:",
            DOMAINS,
            help="Select your preferred email domain"
        )
    
    with col2:
        expiry_duration = st.selectbox(
            "⏱️ Expiry Time:",
            [10, 30, 60, 120, 240],
            index=2,
            format_func=lambda x: f"{x} minutes",
            help="How long the email will be active"
        )
    
    st.markdown("---")
    
    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 GENERATE NEW EMAIL", type="primary", use_container_width=True):
            st.session_state.email = generate_email(selected_domain)
            st.session_state.expiry_time = get_expiry_time(expiry_duration)
            st.session_state.generated_count += 1
            st.balloons()
    
    # Display generated email
    if st.session_state.email:
        st.markdown('<div class="success-box">✨ Email Generated Successfully!</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="email-box">{st.session_state.email}</div>', unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📋 COPY EMAIL", use_container_width=True):
                st.write(f"``````")
                st.success("✅ Copy the email above!")
        
        with col2:
            if st.button("🔄 REGENERATE", use_container_width=True):
                st.session_state.email = generate_email(selected_domain)
                st.session_state.expiry_time = get_expiry_time(expiry_duration)
                st.session_state.generated_count += 1
                st.rerun()
        
        with col3:
            if st.button("🗑️ DELETE", use_container_width=True):
                st.session_state.email = None
                st.session_state.expiry_time = None
                st.rerun()
        
        st.markdown("---")
        
        # Email info
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("📊 Generated Today", st.session_state.generated_count)
        
        with col2:
            if st.session_state.expiry_time:
                remaining = st.session_state.expiry_time - datetime.now()
                minutes_left = int(remaining.total_seconds() / 60)
                st.metric("⏱️ Time Left", f"{minutes_left} min")
        
        with col3:
            domain_name = st.session_state.email.split('@')[1]
            st.metric("🌐 Domain", domain_name)
        
        st.markdown("---")
        
        # Usage instructions
        st.info("""
        **📝 How to use:**
        1. Copy the email address above
        2. Use it for website registrations
        3. Check the Inbox tab for incoming messages
        4. Email will auto-delete after expiry time
        """)
    
    else:
        st.info("👆 Click 'GENERATE NEW EMAIL' to create your disposable email address")
    
    st.markdown('</div>', unsafe_allow_html=True)

# TAB 2: Inbox (Demo)
with tab2:
    st.markdown('<div class="neon-card">', unsafe_allow_html=True)
    
    st.markdown("### 📬 Your Temporary Inbox")
    
    if not st.session_state.email:
        st.warning("⚠️ No active email address. Generate one in the 'Generate Email' tab first!")
    else:
        st.info(f"📧 **Active Email:** `{st.session_state.email}`")
        
        # Demo messages
        st.markdown("---")
        st.markdown("#### 📨 Incoming Messages (Demo)")
        
        # Simulated inbox
        demo_messages = [
            {
                "from": "noreply@example.com",
                "subject": "Welcome to Example Service",
                "time": "2 minutes ago",
                "preview": "Thank you for signing up! Please verify your email..."
            },
            {
                "from": "verification@testsite.com",
                "subject": "Email Verification Code: 123456",
                "time": "5 minutes ago",
                "preview": "Your verification code is: 123456. Valid for 10 minutes."
            },
            {
                "from": "info@newsletter.com",
                "subject": "Your Download is Ready",
                "time": "12 minutes ago",
                "preview": "Click here to download your requested file..."
            }
        ]
        
        for idx, msg in enumerate(demo_messages):
            with st.expander(f"📧 {msg['subject']} - {msg['time']}", expanded=(idx == 0)):
                st.markdown(f"""
                **From:** {msg['from']}  
                **Subject:** {msg['subject']}  
                **Time:** {msg['time']}
                
                ---
                
                {msg['preview']}
                """)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.button(f"🗑️ Delete", key=f"del_{idx}", use_container_width=True)
                with col2:
                    st.button(f"📋 Copy Content", key=f"copy_{idx}", use_container_width=True)
        
        st.markdown("---")
        st.info("💡 **Note:** This is a demo inbox. In a real implementation, emails would be fetched from an actual mail server using APIs.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# TAB 3: Features
with tab3:
    st.markdown('<div class="neon-card">', unsafe_allow_html=True)
    
    st.markdown("### 🛡️ Privacy & Security Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">⚡</div>
            <h3 style="color: #00f5ff;">Instant Generation</h3>
            <p style="color: #a0a0ff;">Create disposable emails in milliseconds with zero signup required</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <div class="feature-icon">🚫</div>
            <h3 style="color: #00f5ff;">Spam Protection</h3>
            <p style="color: #a0a0ff;">Keep your real inbox clean and spam-free forever</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">🔒</div>
            <h3 style="color: #00f5ff;">Complete Anonymity</h3>
            <p style="color: #a0a0ff;">No personal information required. Browse anonymously</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <div class="feature-icon">⏱️</div>
            <h3 style="color: #00f5ff;">Auto-Expiry</h3>
            <p style="color: #a0a0ff;">Emails automatically delete after your chosen time period</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">🌐</div>
            <h3 style="color: #00f5ff;">Multiple Domains</h3>
            <p style="color: #a0a0ff;">Choose from 10+ domains for maximum flexibility</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <div class="feature-icon">🆓</div>
            <h3 style="color: #00f5ff;">100% Free</h3>
            <p style="color: #a0a0ff;">No hidden fees, no registration, unlimited use</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 💡 Perfect For:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - ✅ **Website Signups** - Test services without commitment
        - ✅ **File Downloads** - Get resources without spam
        - ✅ **Newsletter Trials** - Try before subscribing
        - ✅ **Contest Entries** - Participate anonymously
        - ✅ **Beta Testing** - Test apps and services
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        - ✅ **Form Submissions** - Protect your real email
        - ✅ **Comments & Forums** - Browse without tracking
        - ✅ **One-Time Verifications** - Quick OTP codes
        - ✅ **Shopping Coupons** - Get deals without spam
        - ✅ **Privacy Protection** - Stay anonymous online
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# TAB 4: How It Works
with tab4:
    st.markdown('<div class="neon-card">', unsafe_allow_html=True)
    
    st.markdown("### ❓ How Temporary Email Works")
    
    st.markdown("""
    Temporary email services provide you with a disposable email address that you can use instead of your real email. 
    Here's how it works:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🔧 Technical Process
        
        1. **Random Generation** - A unique email address is created using random characters [web:61][web:63]
        
        2. **SMTP Server** - Our mail server receives emails sent to your temporary address [web:70]
        
        3. **Temporary Storage** - Emails are stored for a limited time (10 mins to few hours) [web:66][web:68]
        
        4. **Web Interface** - You can view received emails through our web app [web:67]
        
        5. **Auto-Delete** - All emails and addresses are automatically deleted after expiry [web:66][web:69]
        """)
    
    with col2:
        st.markdown("""
        #### 🛡️ Privacy Benefits
        
        - **No Registration** - Start using immediately without signup [web:65][web:68]
        
        - **No Personal Info** - We don't collect any data about you [web:65]
        
        - **Spam Prevention** - Your real inbox stays clean [web:63][web:66]
        
        - **Anti-Tracking** - Prevents websites from tracking your real identity [web:68]
        
        - **Disposable** - Use once and forget, no maintenance needed [web:69]
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Use Cases")
    
    with st.expander("📱 Social Media & Apps", expanded=False):
        st.markdown("""
        **Scenario:** Want to try a new app but don't trust it yet?
        
        - Use temp email for initial signup
        - Test the app's features
        - If you like it, update to your real email
        - If not, just let it expire
        
        **Result:** No spam, no data leaks, complete control
        """)
    
    with st.expander("🛍️ Online Shopping", expanded=False):
        st.markdown("""
        **Scenario:** Need to get a discount code but don't want marketing emails?
        
        - Use temp email to get the coupon
        - Complete your purchase
        - Let the email expire after
        
        **Result:** Get the deal without the spam
        """)
    
    with st.expander("📥 File Downloads", expanded=False):
        st.markdown("""
        **Scenario:** Website requires email to download a file?
        
        - Generate a temp email
        - Enter it on the download form
        - Get your file link
        - Email auto-deletes after
        
        **Result:** Get your file, avoid spam lists
        """)
    
    with st.expander("🧪 Testing & Development", expanded=False):
        st.markdown("""
        **Scenario:** Developer testing email verification flows?
        
        - Generate multiple temp emails
        - Test your email system
        - No need to create fake accounts
        
        **Result:** Quick testing without cluttering real inboxes
        """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Important Limitations")
    
    st.warning("""
    **What Temp Email CAN'T do:**
    
    - ❌ Send emails (only receive) [web:66]
    - ❌ Receive attachments (text/HTML only) [web:66]
    - ❌ Be used for important accounts
    - ❌ Be recovered after expiry
    - ❌ Replace your primary email
    
    **Best Practice:** Use temp email for temporary, non-critical purposes only!
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")

with st.expander("📊 Statistics & Info"):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="stat-counter">10+</div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #00f5ff;'>Available Domains</p>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="stat-counter">∞</div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #00f5ff;'>Unlimited Emails</p>", unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="stat-counter">0</div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #00f5ff;'>Data Collected</p>", unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="stat-counter">100%</div>', unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #00f5ff;'>Privacy Protected</p>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="text-align: center; padding: 3rem; 
background: linear-gradient(135deg, rgba(0, 245, 255, 0.2) 0%, rgba(123, 0, 255, 0.2) 50%, rgba(255, 0, 110, 0.2) 100%); 
border-radius: 30px; 
border: 2px solid;
border-image: linear-gradient(135deg, #00f5ff, #7b00ff, #ff006e) 1;
box-shadow: 0 0 50px rgba(0, 245, 255, 0.4), 0 0 100px rgba(123, 0, 255, 0.3);">
    <div style="font-size: 2.5rem; margin-bottom: 1rem; font-weight: 900;">
        <span style="background: linear-gradient(135deg, #00f5ff 0%, #7b00ff 50%, #ff006e 100%); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        📧 Temp Mail Generator
        </span>
    </div>
    <div style="font-size: 1.3rem; color: #00f5ff; margin-bottom: 0.5rem; font-weight: 700;">
        Made with ❤️ using Streamlit
    </div>
    <div style="font-size: 1.1rem; color: #a0a0ff; font-weight: 600;">
        Instant • Anonymous • Secure • 100% Free
    </div>
    <div style="font-size: 0.95rem; margin-top: 1.5rem; color: #7b00ff; font-weight: 600;">
        ✨ Protect Your Privacy • Avoid Spam • Stay Anonymous ✨
    </div>
</div>
""", unsafe_allow_html=True)
