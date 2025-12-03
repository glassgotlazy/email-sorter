import streamlit as st
import random
import string
from datetime import datetime, timedelta
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Free Temporary Email Generator - Disposable Email Address",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fixed CSS - removed problematic before/after pseudo elements
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
    
    * {
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    
    .main .block-container {
        background: rgba(15, 12, 41, 0.9);
        border-radius: 30px;
        padding: 3rem;
        box-shadow: 0 0 60px rgba(120, 0, 255, 0.3);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(120, 0, 255, 0.3);
    }
    
    .main-title {
        text-align: center;
        background: linear-gradient(135deg, #00f5ff 0%, #7b00ff 50%, #ff006e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem;
        font-weight: 900;
        margin-bottom: 1rem;
        letter-spacing: -3px;
    }
    
    .subtitle {
        text-align: center;
        color: #00f5ff;
        font-size: 1.4rem;
        margin-bottom: 3rem;
        font-weight: 600;
    }
    
    .neon-card {
        background: linear-gradient(135deg, rgba(20, 20, 50, 0.9) 0%, rgba(30, 30, 60, 0.9) 100%);
        border-radius: 25px;
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.3);
        border: 2px solid rgba(0, 245, 255, 0.3);
    }
    
    .email-box {
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.1) 0%, rgba(123, 0, 255, 0.1) 100%);
        border: 3px solid #00f5ff;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.4);
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.8rem;
        color: #00f5ff;
        text-align: center;
        font-weight: 700;
        letter-spacing: 2px;
        word-break: break-all;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #00f5ff 0%, #7b00ff 100%);
        color: #0f0c29;
        border: none;
        border-radius: 15px;
        padding: 1.2rem 2rem;
        font-size: 1.1rem;
        font-weight: 900;
        letter-spacing: 2px;
        text-transform: uppercase;
        transition: all 0.3s;
        box-shadow: 0 10px 30px rgba(0, 245, 255, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 245, 255, 0.6);
        background: linear-gradient(135deg, #7b00ff 0%, #ff006e 100%);
        color: white;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background: rgba(20, 20, 50, 0.5);
        border-radius: 20px;
        padding: 1.2rem;
        border: 1px solid rgba(0, 245, 255, 0.3);
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 15px;
        padding: 16px 32px;
        font-weight: 800;
        color: #00f5ff;
        font-size: 1.1rem;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00f5ff 0%, #7b00ff 100%) !important;
        color: #0f0c29 !important;
        box-shadow: 0 5px 20px rgba(0, 245, 255, 0.4);
    }
    
    .success-box {
        background: linear-gradient(135deg, rgba(0, 255, 150, 0.2) 0%, rgba(0, 245, 255, 0.2) 100%);
        border: 3px solid #00ff96;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        font-size: 1.4rem;
        font-weight: 800;
        color: #00ff96;
        margin: 2rem 0;
        box-shadow: 0 0 30px rgba(0, 255, 150, 0.4);
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00f5ff 0%, #7b00ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    [data-testid="stMetricLabel"] {
        color: #00f5ff !important;
        font-weight: 700;
        text-transform: uppercase;
    }
    
    .stAlert {
        background: rgba(0, 245, 255, 0.1) !important;
        border: 2px solid #00f5ff !important;
        border-radius: 15px !important;
        color: #00f5ff !important;
    }
    
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.1) 0%, rgba(123, 0, 255, 0.1) 100%);
        border: 2px solid #00f5ff;
        border-radius: 15px;
        font-weight: 800;
        font-size: 1.1rem;
        padding: 1.2rem;
        color: #00f5ff;
        text-transform: uppercase;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #00f5ff !important;
    }
    
    p, li {
        color: #a0a0ff !important;
    }
    
    .stSelectbox > div > div {
        background: rgba(20, 20, 50, 0.8);
        border: 2px solid #00f5ff;
        border-radius: 12px;
        color: #00f5ff;
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
                st.code(st.session_state.email, language=None)
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
        
        st.markdown("---")
        st.markdown("#### 📨 Incoming Messages (Demo)")
        
        # Demo messages
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
        st.info("💡 **Note:** This is a demo inbox. In a real implementation, emails would be fetched from an actual mail server.")
    
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
            <h3>Instant Generation</h3>
            <p>Create disposable emails in milliseconds</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <div class="feature-icon">🚫</div>
            <h3>Spam Protection</h3>
            <p>Keep your real inbox clean forever</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">🔒</div>
            <h3>Complete Anonymity</h3>
            <p>No personal information required</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <div class="feature-icon">⏱️</div>
            <h3>Auto-Expiry</h3>
            <p>Emails automatically delete after time</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">🌐</div>
            <h3>Multiple Domains</h3>
            <p>Choose from 10+ domains</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <div class="feature-icon">🆓</div>
            <h3>100% Free</h3>
            <p>No fees, no registration needed</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 💡 Perfect For:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - ✅ Website Signups - Test services
        - ✅ File Downloads - Get resources  
        - ✅ Newsletter Trials - Try before subscribing
        - ✅ Contest Entries - Participate anonymously
        - ✅ Beta Testing - Test apps safely
        """)
    
    with col2:
        st.markdown("""
        - ✅ Form Submissions - Protect real email
        - ✅ Comments & Forums - Browse privately
        - ✅ One-Time Verifications - Quick OTP
        - ✅ Shopping Coupons - Get deals
        - ✅ Privacy Protection - Stay anonymous
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# TAB 4: How It Works
with tab4:
    st.markdown('<div class="neon-card">', unsafe_allow_html=True)
    
    st.markdown("### ❓ How Temporary Email Works")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🔧 Technical Process
        
        1. **Random Generation** - Unique email created
        2. **SMTP Server** - Receives emails
        3. **Temporary Storage** - Limited time storage
        4. **Web Interface** - View emails online
        5. **Auto-Delete** - Automatic cleanup
        """)
    
    with col2:
        st.markdown("""
        #### 🛡️ Privacy Benefits
        
        - **No Registration** - Instant use
        - **No Personal Info** - Zero data collection
        - **Spam Prevention** - Clean inbox
        - **Anti-Tracking** - Stay anonymous
        - **Disposable** - Use and forget
        """)
    
    st.markdown("---")
    
    st.warning("""
    **⚠️ Important Limitations:**
    
    - ❌ Cannot send emails (receive only)
    - ❌ No attachments (text/HTML only)
    - ❌ Not for important accounts
    - ❌ Cannot recover after expiry
    - ❌ Not a primary email replacement
    
    **Best Practice:** Use for temporary, non-critical purposes only!
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; 
background: linear-gradient(135deg, rgba(0, 245, 255, 0.2) 0%, rgba(123, 0, 255, 0.2) 100%); 
border-radius: 20px; 
border: 2px solid rgba(0, 245, 255, 0.3);">
    <div style="font-size: 2rem; font-weight: 900; color: #00f5ff; margin-bottom: 1rem;">
        📧 Temp Mail Generator
    </div>
    <div style="font-size: 1.2rem; color: #00f5ff; font-weight: 700;">
        Made with ❤️ using Streamlit
    </div>
    <div style="font-size: 1rem; color: #a0a0ff; margin-top: 0.5rem;">
        Instant • Anonymous • Secure • 100% Free
    </div>
</div>
""", unsafe_allow_html=True)
