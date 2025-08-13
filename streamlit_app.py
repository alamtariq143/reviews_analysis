import streamlit as st

# Page setup
st.set_page_config(page_title="Promoter vs Detractor & Passive", layout="wide")

# Custom CSS for card styling
st.markdown("""
    <style>
    .category-card {
        background-color: #f7f9fc;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        transition: 0.2s;
    }
    
    .category-title {
        font-weight: bold;
        font-size: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .promoter-title {
        color: #2e7d32;
    }
    .detractor-title {
        color: #c62828;
    }
    .point-item {
        padding-left: 25px;
        font-size: 14px;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💬 Promoter vs Detractor & Passive Feedback")
st.markdown("### Expand the cards to see detailed points in each category")

# Example 20 categories
promoter = {
    "💳 Payment Experience": [
        "Speed of transactions",
        "Ease of making payments",
        "Single click payment",
        "No OTP hassle",
        "Contactless payments"
    ],
    "🎁 Rewards & Offers": [
        "Attractive cashback",
        "Discount vouchers",
        "Reward points accumulation",
        "Exclusive partner offers",
        "Seasonal promotions"
    ],
    "📱 User Interface": [
        "Clean app design",
        "Easy navigation",
        "Customizable dashboard",
        "Dark mode availability",
        "Quick access shortcuts"
    ],
    "🔒 Security & Trust": [
        "Two-factor authentication",
        "Fraud protection alerts",
        "Secure payment gateway",
        "Face ID / Fingerprint login",
        "Instant transaction alerts"
    ],
    "☎️ Customer Support": [
        "Quick resolution",
        "24/7 availability",
        "Knowledgeable staff",
        "Live chat support",
        "Email follow-up"
    ],
    "🔗 Integration": [
        "Linked bank accounts",
        "Multiple payment modes",
        "UPI integration",
        "Bill payment automation",
        "Wallet top-up ease"
    ],
    "⚡ Speed of Onboarding": [
        "Instant account setup",
        "Simple KYC process",
        "Easy document upload",
        "Auto verification",
        "Clear guidance"
    ],
    "🚀 App Performance": [
        "Fast load times",
        "No crashes",
        "Low battery usage",
        "Offline functionality",
        "Lightweight size"
    ],
    "🎯 Personalization": [
        "Custom payment reminders",
        "Personalized offers",
        "Favorite merchants list",
        "Custom spend categories",
        "Language options"
    ],
    "🛠 Additional Features": [
        "Expense tracker",
        "Split bill option",
        "Loan offers",
        "QR code payments",
        "Subscription management"
    ]
}

detractor = {
    "⚠️ Transaction Issues": [
        "Payment failures",
        "Transaction delays",
        "Pending transactions",
        "Failed UPI payments",
        "Processing time"
    ],
    "❌ Rewards Problems": [
        "Delayed cashback",
        "Incorrect reward points",
        "Inaccessible offers",
        "Reward expiry issues",
        "Poor reward value"
    ],
    "🌀 App Usability Issues": [
        "Difficult navigation",
        "Cluttered layout",
        "Confusing options",
        "Search not working",
        "No clear instructions"
    ],
    "🔓 Security Concerns": [
        "Fraud incidents",
        "Unverified merchants",
        "Weak password enforcement",
        "No transaction alerts",
        "Slow fraud resolution"
    ],
    "📞 Customer Service Complaints": [
        "Slow response",
        "Unhelpful staff",
        "No resolution",
        "Disconnected calls",
        "Generic responses"
    ],
    "🔌 Integration Problems": [
        "Bank linking failures",
        "UPI setup errors",
        "Bill payment errors",
        "Wallet recharge failure",
        "Unsupported payment mode"
    ],
    "📝 Onboarding Issues": [
        "KYC delays",
        "Account verification failure",
        "Confusing process",
        "Rejected documents",
        "No guidance"
    ],
    "🐢 Performance Problems": [
        "App crashes",
        "Slow loading",
        "High battery drain",
        "Lag during payments",
        "Update issues"
    ],
    "📢 Personalization Gaps": [
        "Irrelevant offers",
        "Too many notifications",
        "No language support",
        "Unwanted merchant suggestions",
        "No customization options"
    ],
    "🔍 Missing Features": [
        "No expense tracker",
        "No bill split option",
        "No loan offers",
        "No QR scan option",
        "No subscription management"
    ]
}

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Promoter")
    for category, points in promoter.items():
        with st.expander(f"{category}"):
            st.markdown(f"<div class='category-card'><div class='category-title promoter-title'>{category}</div>", unsafe_allow_html=True)
            for point in points:
                st.markdown(f"<div class='point-item'>✅ {point}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.subheader("Detractor & Passive")
    for category, points in detractor.items():
        with st.expander(f"{category}"):
            st.markdown(f"<div class='category-card'><div class='category-title detractor-title'>{category}</div>", unsafe_allow_html=True)
            for point in points:
                st.markdown(f"<div class='point-item'>⚠️ {point}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
