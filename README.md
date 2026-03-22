# 📊 Rossmann Store Sales Prediction

## 📌 Overview
This project focuses on predicting daily sales for Rossmann stores using machine learning. It demonstrates a complete end-to-end data science workflow, from data analysis to model deployment.

---

## 🎯 Problem Statement
The goal is to predict store sales based on historical data and external factors such as promotions, competition, and seasonality.

---

## 📂 Dataset
The dataset used in this project is from Kaggle:

👉 https://www.kaggle.com/competitions/rossmann-store-sales/data
- Store details (type, assortment)
- Daily sales data
- Promotions and holidays
- Competition information

---

## 🔍 Exploratory Data Analysis (EDA)
Key insights:
- Sales vary significantly across stores
- Promotions increase sales
- Seasonal patterns exist (monthly trends)
- Competition distance has limited impact

---

## ⚙️ Feature Engineering

### 📅 Time Features
- Year
- Month
- Day

### 🔁 Lag Features
- **Lag_1** → Previous day sales
- **Lag_7** → Previous week sales

> These features helped capture temporal patterns and significantly improved model performance.

---

## 🧠 Models Used
- Linear Regression
- Random Forest

Both models were trained **without** and **with** lag features.

---

## 📊 Model Performance

| Model | MAE | R² |
|---|---|---|
| Linear Regression | ~2007 | ~0.19 |
| Random Forest | ~1611 | ~0.46 |

| **Random Forest + Lag** | **~866** | **~0.83** |

---

## 🏆 Final Model

> 👉 **Random Forest with Lag Features**

**Reason:**
- Best overall performance
- Captures non-linear relationships
- Handles time dependencies effectively

---

## 🚀 Deployment (Streamlit App)
A simple web application was built using Streamlit to make predictions.

Users can:
- Input store details
- Provide lag values (previous sales)
- Get predicted sales instantly

---

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit

---

## 📁 Project Structure
```
rossmann-sales-project/
│
├── data/
├── notebooks/
│   └── analysis.ipynb
├── src/
│   └── train_model.py
├── models/
│   └── rossmann_rf_lag.pkl
├── app/
│   └── app.py
└── README.md
```

---

## 🧠 Key Learnings
- Feature engineering is critical for model performance
- Lag features significantly improve time-series predictions
- Non-linear models outperform linear models on complex data
- Building an end-to-end solution adds strong value

---

## ⚠️ Limitations
- Lag features require previous sales values
- Model may not generalize well to unseen future conditions
- No hyperparameter tuning applied

---

## 🔮 Future Improvements
- Hyperparameter tuning
- Try advanced models (XGBoost, LightGBM)
- Improve UI for better usability
- Deploy app online

---

## 👨‍💻 Author
**Lovish Haider**  
BSc International Business Information Systems  
Aspiring Data Scientist
