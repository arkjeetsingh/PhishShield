# 🛡️ PHISH-SHIELD (v7.0)
> *Advanced Cyber-Defense Dashboard & Threat Intelligence Suite*

**Phish-Shield** (formerly Phish-Guard) is a high-fidelity phishing detection platform designed for security analysts and red team operators. It features a military-grade **Tactical HUD** interface, real-time threat scoring, and a gamified operator progression system.

---

## 🚀 Key Features

### 1. **Tactical Tech-Stack**
- **Obsidian HUD**: Deep black (`#050505`) interface with a fixed **Cyber-Grid** and animated **Scanline** overlay.
- **Sci-Fi Typography**: Uses `Rajdhani` (Headers) and `JetBrains Mono` (Data) for a true command-line aesthetic.
- **Visual Intelligence**: **Slanted/Hexagonal** containers with glowing Neon Cyan borders (`#00E5FF`) and pulsing "Live Signal" indicators.

### 2. **Intelligence Layer (Detection Engine)**
- **Weighted Risk Scoring**: Precision analysis using a 40/20/10 point system.
    - **High Risk (40pts)**: Punycode/Homoglyphs (`xn--`), Direct IP connection, Urgency Keywords.
    - **Medium Risk (20pts)**: Open Redirects (`url=`, `next=`), Generic Greetings.
    - **Low Risk (10pts)**: Unsecured HTTP, excessive subdomains.
- **Advanced Heuristics**: Detects **Visual Homoglyphs** (spoofing `apple.com` with Cyrillic characters) and **Open Redirect** vulnerabilities.

### 3. **Operator Progression (Gamification)**
- **XP System**: Earn XP for every URL scanned, email analyzed, or quiz completed.
- **Rank Promotion**: 
    - `0 - 100 XP`: **JUNIOR ANALYST** (Green)
    - `101 - 500 XP`: **SENIOR FORENSIC LEAD** (Cyan)
    - `501+ XP`: **ELITE DEFENDER** (Magenta)

### 4. **Forensic Reporting**
- **Incident Reports**: Generate and download detailed `.txt` forensic reports for any scan. Includes timestamp, risk score, specific threat vector breakdown, and the signing Operator's Rank.

---

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.8+
- Streamlit

### Setup
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/phish-shield.git
    cd phish-shield
    ```

2.  **Install Dependencies**
    ```bash
    pip install streamlit
    ```

3.  **Launch the Dashboard**
    ```bash
    python -m streamlit run app.py
    ```
    *Or simply:*
    ```bash
    python app.py
    ```

---

## 🕹️ Modules

| Module | Description |
| :--- | :--- |
| **URL X-RAY** | Deep scan of URLs for structure, TLDs, and obfuscation techniques. |
| **EMAIL SCAN** | Heuristic analysis of email text for social engineering patterns (Urgency, Pressure). |
| **THE GAUNTLET** | Interactive Quiz to test cyber-awareness. earn XP and unlock badges. |
| **FORENSIC LAB** | Side-by-side comparison of legitimate vs. malicious artifacts. |
| **NET-TOOLS** | Simulated operator tools (MFA Interception, Packet Sniffing). |

---

> **Operator Note**: Stay vigilant. The grid is watching. 
> *System Status: ENCRYPTED CONNECTION ACTIVE*
