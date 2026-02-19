import streamlit as st
import time
import random
import re
from datetime import datetime
import os
import sys
import subprocess

# Auto-restart with Streamlit if run directly with Python
# Auto-restart with Streamlit if run directly with Python
if __name__ == "__main__" and "STREAMLIT_RUN" not in os.environ:
    os.environ["STREAMLIT_RUN"] = "yes"
    # Using sys.executable to ensure we use the same environment
    # Using -m streamlit to avoid PATH issues
    cmd = [sys.executable, "-m", "streamlit", "run", sys.argv[0]]
    print("🚀 Launching Phish-Shield: Neon Ops...")
    try:
        sys.exit(subprocess.call(cmd))
    except KeyboardInterrupt:
        print("\n🛑 Mission Aborted. Shutting down Neon Ops...")
        sys.exit(0)


# -----------------------------------------------------------------------------
# 1. CONFIGURATION & VISUAL IDENTITY
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Phish-Shield Master-Hub",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Custom CSS for "Tactical HUD"
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&family=JetBrains+Mono:wght@400;700&display=swap');

    /* BASE ATMOSPHERE */
    .stApp {
        background-color: #050505;
        background-image: 
            linear-gradient(rgba(0, 229, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 229, 255, 0.03) 1px, transparent 1px);
        background-size: 30px 30px;
        color: #e0e0e0;
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* SCANLINE ANIMATION */
    @keyframes scanline {
        0% { top: -10%; opacity: 0; }
        50% { opacity: 0.5; }
        100% { top: 110%; opacity: 0; }
    }
    .stApp::before {
        content: "";
        position: fixed;
        left: 0;
        width: 100vw; height: 2px;
        background: #00E5FF;
        box-shadow: 0 0 10px #00E5FF;
        animation: scanline 6s linear infinite;
        z-index: 9999;
        pointer-events: none;
    }

    /* TYPOGRAPHY */
    h1, h2, h3 {
        font-family: 'Rajdhani', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .neon-title {
        color: #00E5FF;
        text-shadow: 0 0 10px rgba(0, 229, 255, 0.7), 0 0 20px rgba(0, 229, 255, 0.5);
        animation: flicker 3s infinite;
    }
    
    @keyframes flicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% { opacity: 1; }
        20%, 24%, 55% { opacity: 0.5; }
    }

    /* TACTICAL CONTAINERS */
    .tactical-card {
        background: rgba(10, 15, 25, 0.85);
        border: 1px solid #00E5FF;
        /* Slanted Corners (Hex) */
        clip-path: polygon(
            20px 0, 100% 0, 
            100% calc(100% - 20px), calc(100% - 20px) 100%, 
            0 100%, 0 20px
        );
        padding: 25px;
        margin-top: 20px;
        position: relative;
        backdrop-filter: blur(5px);
    }
    
    /* Decoration on Card */
    .tactical-card::after {
        content: "SYSTEM_READY";
        position: absolute;
        bottom: 5px; right: 10px;
        font-size: 10px;
        color: rgba(0, 229, 255, 0.4);
        letter-spacing: 1px;
    }

    /* INPUTS */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: rgba(0, 0, 0, 0.5) !important;
        border: 1px solid #333 !important;
        border-left: 3px solid #00E5FF !important;
        color: #00FF41 !important;
        font-family: 'JetBrains Mono', monospace;
    }
    .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
        background-color: rgba(0, 229, 255, 0.1) !important;
        box-shadow: 0 0 15px rgba(0, 229, 255, 0.2);
    }

    /* BUTTONS - SCI-FI TRIGGERS */
    div.stButton > button {
        background: transparent;
        border: 1px solid #00E5FF;
        color: #00E5FF;
        padding: 10px 20px;
        font-family: 'Rajdhani', sans-serif;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        clip-path: polygon(10px 0, 100% 0, 100% calc(100% - 10px), calc(100% - 10px) 100%, 0 100%, 0 10px);
        transition: all 0.2s ease;
        margin: 5px 0;
        width: 100%;
    }
    div.stButton > button:hover {
        background: rgba(0, 229, 255, 0.2);
        box-shadow: 0 0 20px rgba(0, 229, 255, 0.6);
        color: #fff;
        text-shadow: 0 0 5px #fff;
        border-color: #fff;
    }
    
    /* LIVE SIGNAL */
    .live-signal {
        display: inline-block;
        width: 10px; height: 10px;
        background: #00FF41;
        border-radius: 50%;
        margin-right: 10px;
        box-shadow: 0 0 10px #00FF41;
        animation: pulse-green 2s infinite;
    }
    @keyframes pulse-green {
        0% { opacity: 0.5; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); }
        100% { opacity: 0.5; transform: scale(0.8); }
    }
    
    /* Hide Default Elements */
    [data-testid="stSidebar"] { display: none; }
    header, footer { visibility: hidden; }

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. CORE LOGIC: INTELLIGENCE & GAMIFICATION
# -----------------------------------------------------------------------------

# XP & Rank System
if 'xp' not in st.session_state:
    st.session_state['xp'] = 0

def update_xp(amount):
    st.session_state['xp'] += amount

def get_rank():
    xp = st.session_state['xp']
    if xp < 100:
        return "JUNIOR ANALYST", "#00FF41" # Matrix Green
    elif xp < 500:
        return "SENIOR FORENSIC LEAD", "#00E5FF" # Cyan
    else:
        return "ELITE DEFENDER", "#FF0099" # Magenta

def analyze_url(url):
    risk_score = 0
    flags = []
    
    # --- HIGH RISK (40 PTS) ---
    # 1. Punycode / Homoglyph Detection
    if "xn--" in url or any(ord(c) > 127 for c in url):
        risk_score += 40
        flags.append("HIGH: Visual Homoglyph / Punycode Detected (Possible Spoofing)")
    
    # 2. IP Address Usage
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    if re.search(ip_pattern, url):
        risk_score += 40
        flags.append("HIGH: Direct IP Address Usage (Avoids DNS)")

    # 3. Critical TLDs
    critical_tlds = ['.xyz', '.top', '.zip', '.bit', '.monster', '.gq', '.tk']
    for tld in critical_tlds:
        if url.endswith(tld) or tld + '/' in url:
            risk_score += 40
            flags.append(f"HIGH: Suspicious TLD detected ({tld})")
            
    # --- MEDIUM RISK (20 PTS) ---
    # 4. Open Redirects
    redirect_params = ['url=', 'redirect=', 'next=', 'target=', 'dest=']
    for param in redirect_params:
        if param in url.lower():
            risk_score += 20
            flags.append(f"MED: Open Redirect Parameter Detected ('{param}')")
            break

    # 5. Keywords
    suspicious_keywords = ['login', 'verify', 'bank', 'secure', 'account', 'update', 'confirm']
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            risk_score += 20
            flags.append(f"MED: Sensitive keyword detected ('{keyword}')")
            break
            
    # --- LOW RISK (10 PTS) ---
    # 6. Protocol & Structure
    if url.startswith("http://"):
        risk_score += 10
        flags.append("LOW: Unsecured HTTP Protocol")
        
    if url.count('.') > 3:
        risk_score += 10
        flags.append("LOW: Excessive subdomains")
        
    if '@' in url:
        risk_score += 10
        flags.append("LOW: URL contains '@' symbol")

    return min(risk_score, 100), flags

def analyze_email(text):
    score = 0
    alerts = []
    
    # --- HIGH RISK (40 PTS) ---
    # 1. Urgency / Pressure
    urgency_words = ['urgent', 'immediately', 'suspend', 'restricted', '24 hours', 'action required', 'unauthorized access']
    for word in urgency_words:
        if word in text.lower():
            score += 40
            alerts.append(f"HIGH: Psychological Pressure Tactic ('{word}')")
            break # Cap at one high urgency alert
            
    # 2. Credential Harvesting Keywords
    harvest_words = ['password', 'social security', 'credit card', 'confirm identity']
    for word in harvest_words:
        if word in text.lower():
            score += 40
            alerts.append(f"HIGH: Request for Sensitive Data ('{word}')")
            break

    # --- MEDIUM RISK (20 PTS) ---
    # 3. Generic Greetings
    greetings = ['dear customer', 'valued member', 'dear user', 'undisclosed recipients']
    for greet in greetings:
        if greet in text.lower():
            score += 20
            alerts.append(f"MED: Impersonal/Generic Greeting ('{greet}')")
            break
            
    # 4. Suspicious Link Indicators (Text based)
    if 'click here' in text.lower() or 'verify now' in text.lower():
        score += 20
        alerts.append("MED: Generic 'Call to Action' Link Text")

    # --- LOW RISK (10 PTS) ---
    # 5. Formatting
    if sum(1 for c in text if c.isupper()) / (len(text) + 1) > 0.3:
        score += 10
        alerts.append("LOW: Unprofessional usage of CAPITAL LETTERS")
        
    return min(score, 100), list(set(alerts))

# -----------------------------------------------------------------------------
# 3. UI COMPONENTS & LAYOUT (TOP NAV NAVIGATION)
# -----------------------------------------------------------------------------

# Initialize Navigation State
if 'active_tab' not in st.session_state:
    st.session_state['active_tab'] = 'X-Ray'

# Top Navigation Bar & Operator Status
rank_name, rank_color = get_rank()
st.markdown(f"""
    <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; border-bottom: 2px solid #00E5FF; padding-bottom: 10px;'>
        <div>
            <h1 class='neon-title' style='margin:0; font-size: 3rem;'>PHISH-SHIELD</h1>
            <div style='display:flex; align-items:center;'>
                <div class='live-signal'></div>
                <span style='color:#00FF41; font-size: 0.8rem; letter-spacing: 2px;'>ENCRYPTED CONNECTION ACTIVE</span>
            </div>
        </div>
        <div style='text-align:right;'>
            <div style='font-size:0.8rem; color:#aaa; letter-spacing:1px;'>OPERATOR_ID: [GUEST]</div>
            <div style='font-size:1.5rem; font-weight:bold; color:{rank_color}; text-shadow:0 0 10px {rank_color}; font-family: "Rajdhani";'>
                {rank_name}
            </div>
            <div style='font-size:0.9rem; color:#00E5FF;'>XP: {st.session_state['xp']}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    if st.button("URL X-RAY", key='nav_xray'): st.session_state['active_tab'] = 'X-Ray'
with c2:
    if st.button("EMAIL SCAN", key='nav_email'): st.session_state['active_tab'] = 'Email'
with c3:
    if st.button("TRAINING", key='nav_quiz'): st.session_state['active_tab'] = 'Quiz'
with c4:
    if st.button("FORENSICS", key='nav_lab'): st.session_state['active_tab'] = 'Lab'
with c5:
    if st.button("NET-TOOLS", key='nav_tools'): st.session_state['active_tab'] = 'Tools'

st.markdown("<br>", unsafe_allow_html=True)

# Main Content Logic
nav_selection = st.session_state['active_tab']

if nav_selection == "X-Ray":
    st.markdown("## // URL INTELLIGENCE VECTOR")
    
    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    
    url_input = st.text_input("ENTER TARGET URL:", placeholder="http://suspicious-link.xyz/login?redirect=evil.com")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("INITIATE SCAN PROTOCOL"):
        if url_input:
            with st.spinner("TRACING PACKETS..."):
                time.sleep(1.0)
                score, alerts = analyze_url(url_input)
                update_xp(10) # XP Reward
                
                # Colors
                if score < 40:
                    score_color = "#00FF41" # Green
                    verdict = "SAFE"
                elif score < 80:
                    score_color = "#FFD700" # Gold
                    verdict = "CAUTION"
                else:
                    score_color = "#FF0000" # Red
                    verdict = "CRITICAL THREAT"
                
                # Visualization
                st.markdown(f"""
                    <div style="text-align:center; margin-top:20px;">
                        <h1 style="font-size: 80px; color:{score_color} !important; text-shadow: 0 0 20px {score_color}; font-family: 'Rajdhani';">{score}%</h1>
                        <h3 style="color:{score_color} !important;">VERDICT: {verdict}</h3>
                    </div>
                """, unsafe_allow_html=True)
                
                # Alerts
                if alerts:
                    st.markdown(f"<div style='border:1px solid {score_color}; padding:15px; margin-top:20px; background: rgba(0,0,0,0.5);'>", unsafe_allow_html=True)
                    for alert in alerts:
                        st.markdown(f"<div style='color:{score_color}; font-weight:bold; font-family:JetBrains Mono;'>[!] {alert}</div>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.balloons()
                    st.success("SYSTEM INTEGRITY MAINTAINED.")
                
                # Report Generation
                report_text = f"""PHISH-SHIELD TACTICAL REPORT
---------------------------
Timestamp: {datetime.now()}
Target URL: {url_input}
Risk Score: {score}/100
Verdict: {verdict}

DETECTED THREATS:
{chr(10).join(['- ' + a for a in alerts]) if alerts else "- None"}

Operator Rank: {rank_name}
---------------------------"""
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.download_button("📂 DOWNLOAD INTEL PACKET (.TXT)", report_text, file_name="incident_report.txt")
                
    st.markdown("</div>", unsafe_allow_html=True)

elif nav_selection == "Email":
    st.markdown("## // EMAIL THREAT DETECTOR")
    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    
    email_text = st.text_area("INJECT RAW DATA STREAM:", height=200, placeholder="Paste headers + body content...")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("RUN HEURISTIC ANALYSIS"):
        if email_text:
            score, alerts = analyze_email(email_text)
            update_xp(10) # XP Reward
            
            color = "#00FF41" if score < 40 else "#FF0000"
            
            st.markdown(f"""
                <div style="background:rgba(255,255,255,0.1); height:20px; width:100%; margin-bottom:20px; border:1px solid #333;">
                    <div style="width:{score}%; height:100%; background: {color}; box-shadow: 0 0 15px {color};"></div>
                </div>
                <h3 style="text-align:right; font-family:'Rajdhani'; color:{color};">THREAT PROBABILITY: {score}%</h3>
            """, unsafe_allow_html=True)
            
            if alerts:
                for a in alerts:
                    st.write(f"🛑 {a}")
            
            # Report Generation
            report_text = f"""PHISH-SHIELD EMAIL ENTROPY REPORT
---------------------------
Timestamp: {datetime.now()}
Source Hash: {hash(email_text)}
Threat Probability: {score}%

DETECTED MARKERS:
{chr(10).join(['- ' + a for a in alerts]) if alerts else "- Clean"}
---------------------------"""
            st.markdown("<br>", unsafe_allow_html=True)
            st.download_button("📂 EXPORT FORENSIC DATA", report_text, file_name="email_forensics.txt")
            
        else:
            st.warning("NO DATA STREAM DETECTED.")
    st.markdown("</div>", unsafe_allow_html=True)

elif nav_selection == "Quiz":
    st.markdown("## // THE GAUNTLET V3.0")
    
    # Initialize Session State
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False

    questions = {
        "Q1: You receive an urgent email from 'IT Support' asking for your password. Action?": 
        ["Reply immediately", "Ignore it", "Report to security team", "Click the link"],
        "Q2: What is the safest way to verify a suspicious link?": 
        ["Click it", "Hover over it", "Forward to a friend", "Open on phone"],
        "Q3: Multi-Factor Authentication (MFA) protects you by...": 
        ["Using a complex password", " requiring a second verification step", "Encrypting your hard drive", "Updating antivirus"],
        "Q4: A bank will NEVER ask for...": 
        ["Your PIN/Password via email", "Your account number", "Your ID for verification at a branch", "Your address"],
        "Q5: Public Wi-Fi logic:": 
        ["Safe for banking", "Use a VPN", "Faster than data", "No risks involved"]
    }
    answers = ["Report to security team", "Hover over it", " requiring a second verification step", "Your PIN/Password via email", "Use a VPN"]
    
    with st.form("quiz_form"):
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        user_answers = []
        for q, options in questions.items():
            st.markdown(f"<div style='color:#00E5FF; margin-bottom:10px;'>{q}</div>", unsafe_allow_html=True)
            user_answers.append(st.radio("", options, key=q))
            st.markdown("<hr style='border-color:rgba(0, 229, 255, 0.2);'>", unsafe_allow_html=True)
        
        submitted = st.form_submit_button("SUBMIT TO MAINFRAME")
        
        if submitted:
            score = 0
            for i, ans in enumerate(user_answers):
                if ans == answers[i]:
                    score += 1
            st.session_state.quiz_score = score
            st.session_state.quiz_submitted = True
            
            # XP Logic
            if score == 5:
                update_xp(50) # Bonus for perfect score
                st.balloons()
            else:
                update_xp(score * 5) # 5XP per question
    
    if st.session_state.quiz_submitted:
        final_score = st.session_state.quiz_score
        st.markdown(f"<h1 style='text-align:center; color:#00E5FF;'>SCORE: {final_score}/5</h1>", unsafe_allow_html=True)
        st.info(f"XP EARNED: {50 if final_score == 5 else final_score*5}")
        st.markdown("</div>", unsafe_allow_html=True)

elif nav_selection == "Lab":
    st.markdown("## // FORENSIC COMPARISON LAB")
    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.info("✅ LEGITIMATE OBJECT")
        st.code("From: support@paypal.com\nLink: paypal.com/activity")
    with c2:
        st.error("⚠️ MALICIOUS CLONE")
        st.code("From: support-paypal@secure.net\nLink: verify-acct.xyz")
    
    if st.button("RUN DIFF ANALYSIS"):
        st.success("ANALYSIS COMPLETE: Malicious clone uses Typo-squatting and High-Risk TLD (.xyz)")
    st.markdown("</div>", unsafe_allow_html=True)

elif nav_selection == "Tools":
    st.markdown("## // OPERATOR TOOLS")
    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    st.write("Intercepted MFA Code Simulation:")
    code = st.text_input("Enter Code:", max_chars=6)
    if st.button("TRANSMIT"):
        st.error(f"PACKET SNIFFED: {code} sent to Command & Control Server.")
    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 4. FOOTER / SYSTEM STATUS
# -----------------------------------------------------------------------------
st.markdown("---")
# Clean simple footer
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
st.markdown(f"<div style='text-align:center; color:rgba(0, 229, 255, 0.5); font-size: 0.8rem; font-family: JetBrains Mono;'>SECURE CHANNEL • {now}</div>", unsafe_allow_html=True)
