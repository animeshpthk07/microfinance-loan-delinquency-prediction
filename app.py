import streamlit as st
import pandas as pd
import joblib

# --- Configuration ---
st.set_page_config(page_title="Microfinance Loan Predictor", layout="wide")

# --- Load Model ---
# Use st.cache_resource to load the model only once
@st.cache_resource
def load_model():
    # Loading directly from the main folder where you uploaded it
    return joblib.load('rf_model.pkl')

model = load_model()

# --- Prediction Logic ---
feature_cols = ['Applicant_Age', 'Annual_Income', 'Credit_Score', 'Loan_Amount',
                'Debt_to_Income_Ratio', 'Existing_Active_Loans', 'Late_Payments_Past_12M']

def generate_risk_assessment(borrower_row):
    features_df = pd.DataFrame([borrower_row], columns=feature_cols)
    prob = model.predict_proba(features_df)[0][1]
    
    # Risk Tier Assignment
    if prob >= 0.70:
        tier = "HIGH RISK (Manual Intervention Required)"
        action = "Freeze automated disbursement; assign field officer for doorstep audit."
        color = "red"
    elif prob >= 0.35:
        tier = "MEDIUM RISK (Review Required)"
        action = "Request collateral/guarantor verification before approval."
        color = "orange"
    else:
        tier = "LOW RISK (Fast-Track)"
        action = "Approve for automated loan disbursement."
        color = "green"
        
    # Reason Codes
    reasons = []
    if borrower_row['Late_Payments_Past_12M'] >= 2:
        reasons.append(f"Frequent past late payments ({borrower_row['Late_Payments_Past_12M']} in last 12M)")
    if borrower_row['Debt_to_Income_Ratio'] > 0.45:
        reasons.append(f"High Debt-to-Income ratio ({borrower_row['Debt_to_Income_Ratio']*100:.1f}%)")
    if borrower_row['Credit_Score'] < 580:
        reasons.append(f"Low credit score ({borrower_row['Credit_Score']})")
    if borrower_row['Existing_Active_Loans'] >= 3:
        reasons.append(f"Multiple active obligations ({borrower_row['Existing_Active_Loans']} loans)")
        
    if not reasons:
        reasons.append("Strong repayment history and balanced debt profile")
        
    return {
        "Default Probability": f"{prob*100:.1f}%",
        "Risk Tier": tier,
        "Recommended Action": action,
        "Primary Risk Drivers": reasons,
        "Color": color
    }

# --- Streamlit UI ---
st.title("Microfinance Loan Delinquency Predictor")
st.markdown("Decision-support tool for predicting loan delinquency.")

st.sidebar.header("Applicant Information")

# Input fields
age = st.sidebar.number_input("Applicant Age", min_value=18, max_value=100, value=35)
income = st.sidebar.number_input("Annual Income", min_value=0, value=500000)
credit_score = st.sidebar.number_input("Credit Score", min_value=300, max_value=850, value=650)
loan_amount = st.sidebar.number_input("Loan Amount", min_value=0, value=100000)
dti_ratio = st.sidebar.slider("Debt-to-Income Ratio", min_value=0.0, max_value=1.0, value=0.3)
active_loans = st.sidebar.number_input("Existing Active Loans", min_value=0, value=1)
late_payments = st.sidebar.number_input("Late Payments (Past 12M)", min_value=0, value=0)

if st.sidebar.button("Assess Risk"):
    # Create input dictionary
    input_data = {
        'Applicant_Age': age,
        'Annual_Income': income,
        'Credit_Score': credit_score,
        'Loan_Amount': loan_amount,
        'Debt_to_Income_Ratio': dti_ratio,
        'Existing_Active_Loans': active_loans,
        'Late_Payments_Past_12M': late_payments
    }
    
    # Get assessment
    assessment = generate_risk_assessment(input_data)
    
    # Display Results
    st.subheader("Risk Assessment Results")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Default Probability", assessment["Default Probability"])
    
    st.markdown(f"**Risk Tier:** <span style='color:{assessment['Color']}'>{assessment['Risk Tier']}</span>", unsafe_allow_html=True)
    st.markdown(f"**Recommended Action:** {assessment['Recommended Action']}")
    
    st.markdown("**Primary Risk Drivers:**")
    for reason in assessment["Primary Risk Drivers"]:
        st.markdown(f"- {reason}")
