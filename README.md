# 🛡️ Intrusion Detection in Smart Healthcare Using Machine Learning

## 📌 Project Overview
This project presents a Machine Learning-based Intrusion Detection System (IDS) designed for smart healthcare environments. The system analyzes network traffic and classifies it as **Normal** or **Attack**, helping to enhance cybersecurity in healthcare systems.

With the increasing use of IoT devices and digital platforms in hospitals, healthcare networks have become vulnerable to cyber threats. This project aims to provide an intelligent and efficient solution for detecting malicious activities in real-time.

---

## 🎯 Objectives
- Detect and classify network traffic as normal or malicious
- Improve security in smart healthcare systems
- Reduce false positives using machine learning techniques
- Provide real-time monitoring using a dashboard

---

## 🧠 Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Streamlit (for dashboard)
- Joblib (for model saving)

---

## 📊 Dataset
- **NSL-KDD Dataset**
- Contains network traffic records with 41 features
- Includes multiple attack types:
  - DoS (Denial of Service)
  - Probe
  - R2L (Remote to Local)
  - U2R (User to Root)

---

## ⚙️ Project Workflow

1. Data Collection (NSL-KDD Dataset)
2. Data Preprocessing
   - Label Encoding
   - Feature Scaling
   - Handling Imbalance (SMOTE)
3. Model Training
4. Model Evaluation
5. Deployment (Streamlit Dashboard)

---

## 🤖 Machine Learning Models Used
- Logistic Regression
- Decision Tree
- Random Forest (Best Performing)
- Support Vector Machine (SVM)

---

## 📈 Performance
| Model               | Accuracy |
|--------------------|----------|
| Logistic Regression| ~91%     |
| Decision Tree      | ~94%     |
| SVM                | ~95%     |
| Random Forest      | ~97%     |

---

## 💻 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/ids-healthcare.git
cd ids-healthcare
