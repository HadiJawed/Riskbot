import streamlit as st

st.set_page_config(page_title="RiskBot 💼", page_icon="📊")
st.title("📊 RiskBot — Your Risk Analyst Assistant")
st.write("Ask about any risk-related term (like 'credit risk' or 'charge-off').")

# Knowledge base
risk_knowledge_base = {
    "credit risk": "Credit risk is the possibility that a borrower will fail to repay a loan or meet contractual obligations.",
    "residual value": "Residual value is the estimated value of a leased asset at the end of the lease term.",
    "charge-off": "A charge-off is when a lender writes off a debt as unlikely to be collected, usually after repeated missed payments.",
    "risk exposure": "Risk exposure refers to the potential loss or impact an organization faces due to risk events.",
    "early termination": "Early termination happens when a lease is ended before its scheduled maturity date."
}

# User input
user_input = st.text_input("🔍 What would you like to learn about?")

if user_input:
    response = "🤔 Sorry, I don’t know that one yet. Try another term."

    for keyword in risk_knowledge_base:
        if keyword in user_input.lower():
            response = "🧠 " + risk_knowledge_base[keyword]
            break

    st.write(response)
