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

# Highlighted analysis text with HTML
analysis_text = """
From a total of <b>10,000</b> customer feedback entries, 
<b style='color:green;'>65%</b> were classified as <span style='color:green;'><b>Promoters</b></span> 
and <b style='color:red;'>35%</b> as <span style='color:red;'><b>Detractors & Passives</b></span>. 

The <span style='color:green;'><b>Promoter</b></span> group reflects customers who are 
<b>highly satisfied</b>, highlighting <b>strengths</b>. 

In contrast, the <span style='color:red;'><b>Detractor & Passive</b></span> group reveals 
<b>areas of concern</b>. 

To better understand the feedback, the data was organized into 
<b>20 major themes</b>, each containing <b>5 sub-themes</b>, representing both 
<b>positive experiences</b> and <b>improvement opportunities</b>. 
"""

# Display as a styled info box


st.markdown(analysis_text, unsafe_allow_html=True)
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
    "🎁 Financial Benefits": [
        "Cashback offers",
        "Rewards points",
        "Zero convenience fees",
        "No platform fees",
        "Better offers compared to competitors"
    ],
    "📱 User Interface": [
        "Fast and user-friendly",
        "Easy navigation",
        "Simple application process",
        "Easy registration",
        "Quick scanner access"
    ],
    "📊 Transaction Reliability": [
        "Successful payments",
        "Secure transactions",
        "Trust and security",
        "Quick refunds",
        "Payment confirmation"
    ],
    "🧾 Bill Payment Services": [
        "Electricity bill payments",
        "Mobile recharges",
        "DTH recharges",
        "Broadband/landline bills",
        "Credit card bills"
    ],
    "💱 UPI Features": [
        "Easy UPI setup",
        "Fast UPI transactions",
        "Multiple bank account linking",
        "UPI PIN page loading",
        "Transaction tracking"
    ],
    "☎️ Customer Support": [
        "24/7 service",
        "Quick issue resolution",
        "Timely reminders",
        "Effective communication",
        "Service quality"
    ],
    "💳 Payment Options": [
        "Multiple payment methods",
        "EMI options",
        "Pay Later facility",
        "Credit/Debit cards",
        "Digital wallet"
    ],
    "🔗 Integration Capabilities": [
        "Cross-platform usage",
        "Wide acceptance",
        "Partner app compatibility",
        "Merchant network",
        "QR code scanning"
    ],
    "🎟 Gift Card Features": [
        "Wide usage options",
        "Gift card balance",
        "Purchase flexibility",
        "Balance transfer",
        "Recharge capability"
    ],
    "📂 Transaction Management": [
        "Easy tracking",
        "Transaction history",
        "Balance checking",
        "Auto-reload",
        "Statement access"
    ],
    "💳 Credit Features": [
        "Good credit limit",
        "No-cost EMI",
        "Credit card integration",
        "Pay Later availability",
        "Flexible repayment"
    ],
    "📶 Mobile Recharge Features": [
        "Quick recharge process",
        "Multiple operator support",
        "Instant activation",
        "Plan selection",
        "Recharge success rate"
    ],
    "📑 Bill Fetch Features": [
        "Instant bill fetch",
        "Multiple biller support",
        "Automatic bill detection",
        "Payment scheduling",
        "Bill payment history"
    ],
    "💸 Money Transfer": [
        "Easy friend/family transfers",
        "Quick transfers",
        "Multiple recipient options",
        "Transfer tracking",
        "Transfer success rate"
    ],
    "🎬 Entertainment Services": [
        "Movie ticket booking",
        "Show selection",
        "Seat booking",
        "Entertainment information",
        "Booking management"
    ],
    "✈️ Travel Services": [
        "Bus booking",
        "Train ticket booking",
        "Flight booking",
        "Hotel booking",
        "Travel management"
    ],
    "🚗 FASTag Services": [
        "Quick recharge",
        "Balance check",
        "Multiple operator support",
        "Instant activation",
        "Transaction history"
    ],
    "🛡 Insurance Services": [
        "Premium payments",
        "Policy management",
        "Insurer options",
        "Claim process",
        "Documentation"
    ],
    "🔒 Digital Security": [
        "Secure transactions",
        "Data protection",
        "Account safety",
        "Privacy measures",
        "Authentication process"
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
    "❌ Cashback & Rewards Problems": [
        "Limited cashback offers",
        "Missing cashback credits",
        "Poor reward systems",
        "Tracking difficulties",
        "Delayed cashback"
    ],
    "📞 Customer Service Concerns": [
        "Poor support quality",
        "Difficult to reach support",
        "Delayed responses",
        "Limited support channels",
        "Communication issues"
    ],
    "💻 Technical Difficulties": [
        "App navigation issues",
        "Scanner problems",
        "UPI setup difficulties",
        "Page loading delays",
        "Interface problems"
    ],
    "💳 Payment Limitations": [
        "Limited payment options",
        "Balance transfer restrictions",
        "Usage restrictions",
        "Merchant acceptance issues",
        "Loading money difficulties"
    ],
    "🔍 Transparency Issues": [
        "Hidden charges",
        "Unclear terms",
        "Fee transparency",
        "Billing clarity",
        "Statement confusion"
    ],
    "💳 Credit Related Issues": [
        "Low credit limits",
        "Short repayment windows",
        "EMI restrictions",
        "Credit card integration",
        "Processing fees"
    ],
    "📊 Transaction Tracking": [
        "Difficult transaction history",
        "Invoice tracking issues",
        "Payment status updates",
        "Transaction notes",
        "Contact-wise tracking"
    ],
    "📄 Bill Payment Problems": [
        "Delayed updates",
        "Failed payments",
        "Biller confirmation delays",
        "Partial payment issues",
        "Bill fetch delays"
    ],
    "📱 Mobile Recharge Issues": [
        "Recharge failures",
        "Status update delays",
        "Plan discovery problems",
        "DTH recharge issues",
        "Operator limitations"
    ],
    "🔒 Security Concerns": [
        "Trust issues",
        "Payment security",
        "Data protection",
        "Transaction safety",
        "Account security"
    ],
    "🪪 KYC Related Issues": [
        "Complex KYC process",
        "Registration difficulties",
        "Documentation problems",
        "Verification delays",
        "Update issues"
    ],
    "🌀 User Experience Problems": [
        "Navigation difficulties",
        "Complex interfaces",
        "Feature accessibility",
        "App usability",
        "Payment flow"
    ],
    "📦 Platform Limitations": [
        "Merchant restrictions",
        "App compatibility",
        "Offline usage",
        "Feature availability",
        "Service coverage"
    ],
    "🎟 Gift Card Problems": [
        "Activation issues",
        "Usage restrictions",
        "Balance transfer",
        "Validity extension",
        "Adding to account"
    ],
    "🚚 Service Delivery Issues": [
        "Cylinder delivery delays",
        "Delivery tracking",
        "Service confirmation",
        "Delivery charges",
        "Status updates"
    ],
    "💲 Convenience Fees": [
        "Credit card fees",
        "Transaction charges",
        "Processing fees",
        "Hidden costs",
        "Service charges"
    ],
    "📉 Competitive Disadvantages": [
        "Better competitor offers",
        "Limited features",
        "Market comparison",
        "Service gaps",
        "Product limitations"
    ],
    "🎫 Booking Related Issues": [
        "Movie ticket booking",
        "Travel booking problems",
        "Seat selection",
        "Booking flow",
        "Confirmation delays"
    ],
    "👤 Account Management": [
        "Balance tracking",
        "Account updates",
        "Profile management",
        "Settings configuration",
        "Preference setup"
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
