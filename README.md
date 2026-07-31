# Microfinance Loan Delinquency Early Warning System

## 👤 Team Members
* Animesh Pathak

## 🎯 Problem Statement
Microfinance institutions need to identify borrowers who may miss repayments early so that support or restructuring can be offered. This project builds a working delinquency risk prediction system that processes borrower data and produces an actionable output for decision-makers.

## 📊 Dataset / Reference Source
* **Name:** Microfinance Loan Credit Scoring
* **Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/shahrukhkhan/microfinance-loan-credit-scoring)
* **Usage:** Borrower and loan features (Age, Income, Credit Score, DTI Ratio, etc.) were used to predict repayment risk.

## 🛠️ Tools Used
* **Languages & Libraries:** Python, Pandas, NumPy, Scikit-Learn (Random Forest, SMOTE)
* **Deployment:** Streamlit Community Cloud
* **Version Control:** GitHub

## 🔄 Project Workflow
1. **Data Preparation:** Cleaned and inspected borrower data.
2. **EDA:** Analyzed risk distributions and handled class imbalance.
3. **Modeling:** Trained a machine learning classifier to predict delinquency probabilities.
4. **Decision Support:** Designed logic to map probabilities into actionable Risk Tiers (High, Medium, Low).
5. **Deployment:** Built and deployed an interactive web application.

## 🧠 AI / ML Component
A **Random Forest Classification model** is used to predict the probability of default based on borrower attributes. The innovation here is that the output does not stop at a raw probability score. It translates the score into specific **Risk Tiers** and generates **reason codes** (e.g., "High Debt-to-Income ratio") to help loan officers understand exactly *why* a borrower was flagged, ensuring transparency.

## 🚀 How to Run the Project
The project is deployed live on Streamlit! 
* **Live Demo:** [Microfinance Loan Predictor](https://microfinance-loan-delinquency-prediction-7imbdkerqybsodmv9iwrm.streamlit.app/)

*(To run locally):*
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## 📈 Results and Insights
The model successfully segments borrowers into actionable risk categories. Key drivers of delinquency identified include low credit scores, multiple existing active loans, and high debt-to-income ratios.

## ⚠️ Limitations & Responsible Use
* **Limitations:** The model relies on historical data, which may not capture sudden economic downturns or personal emergencies. 
* **Responsible Use:** This tool is designed strictly for *decision-support*, not automated rejection. Human oversight (like a field officer audit) is required for high-risk flags to ensure fairness and avoid bias against vulnerable microfinance borrowers.

## 🔮 Future Improvements
* Add more diverse features (e.g., alternative credit data).
* Implement a dashboard for tracking overall portfolio health.
* Integrate algorithmic fairness checks to ensure equitable lending.
