#  Machine Learning for Vehicle Insurance Fraud Detection  
## A High-Recall Random Forest Approach

---

###  **Project Overview**

Vehicle insurance fraud is a **multi-billion dollar issue**, costing the U.S. industry over **$40 billion annually** and driving up premiums for honest policyholders. As fraud schemes become more complex, traditional detection methods are falling behind.

This project aims to develop a **machine learning model** capable of proactively identifying fraudulent claims and uncovering the features most predictive of fraud.

---

###  **Data & Methods**

- **Dataset**: 15,420 insurance claims  
- **Fraud Rate**: ~6% labeled as fraudulent  
- **Models Tested**:  
  - Logistic Regression  
  - Decision Trees  
  - Random Forest  
  - XGBoost  

- **Preprocessing**:  
  - Feature engineering  
  - Stratified sampling  
  - SMOTE for class imbalance  
  - Class weighting  

---

###  **Model Performance**

The final **Random Forest model** achieved:  
- **Recall**: 0.97  
- **ROC AUC**: 0.81  

 It **outperformed other models** while maintaining interpretability—critical for high-stakes fraud screening.

---

###  **Key Insights from SHAP & Feature Importance**

The model consistently highlighted the following **key fraud signals**:
- Fault attribution  
- Policy type  
- Vehicle price  
- Deductible amount  
- Customer age  
- Recent address change  

These features proved crucial in distinguishing between fraudulent and legitimate claims.

---

###  **Business Impact**

By flagging **high-risk claims early**, insurers can:
- Allocate investigative resources more efficiently  
- **Reduce false payouts**  
- **Protect policyholders** from rising premiums  

This model provides a **transparent**, high-recall fraud detection foundation with real-world utility.

---

###  **Future Directions**

- Integration of **external data sources** (e.g., credit history, geolocation)  
- **Real-time deployment** in claims processing pipelines  
- Cross-insurer **collaborative modeling** to improve system-wide fraud detection  

---
