import streamlit as st
import numpy as np
import joblib
from database import log_prediction, get_recent_logs, init_db

# 🔥 INIT DB
init_db()

# 🔥 LOAD FILES
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoders = joblib.load("encoders.pkl")

st.set_page_config(page_title="Smart Healthcare IDS", layout="centered")

st.title("🛡️ Smart Healthcare IDS")

# ================= INPUT =================

duration = st.number_input("Duration", 0)

protocol = st.selectbox("Protocol", ["tcp", "udp", "icmp"])
service = st.selectbox("Service", ["http", "ftp_data", "smtp", "other"])
flag = st.selectbox("Flag", ["SF", "S0", "REJ"])

src_bytes = st.number_input("Src Bytes", 0)
dst_bytes = st.number_input("Dst Bytes", 0)

count = st.number_input("Count", 0)
srv_count = st.number_input("Srv Count", 0)

# ================= PREDICTION =================

if st.button("🚨 Detect Intrusion"):

    # 🔥 Create 41 feature vector
    data = np.zeros(41)

    try:
        data[0] = duration
        data[1] = encoders[1].transform([protocol])[0]
        data[2] = encoders[2].transform([service])[0]
        data[3] = encoders[3].transform([flag])[0]
        data[4] = src_bytes
        data[5] = dst_bytes
        data[22] = count
        data[23] = srv_count

    except Exception as e:
        st.error(f"Encoding error: {e}")
        st.stop()

    X = data.reshape(1, -1)
    X_scaled = scaler.transform(X)

    # 🔥 ML Prediction
    pred = model.predict(X_scaled)[0]
    prob = model.predict_proba(X_scaled)[0]
    confidence = max(prob) * 100

    # ================= RULE-BASED FIRST =================

    rule_alert = "Normal"

    if count > 100 and srv_count > 100:
        rule_alert = "🚨 Possible DoS Attack"
        st.error(rule_alert)

    elif src_bytes == 0 and dst_bytes == 0 and flag == "S0":
        rule_alert = "🚨 Connection Flood / Probe Attack"
        st.error(rule_alert)

    elif src_bytes > 10000:
        rule_alert = "⚠️ Suspicious High Traffic"
        st.warning(rule_alert)

    # ================= FINAL RESULT =================

    if pred == 0 and "🚨" not in rule_alert:
        result = "Normal Traffic"
        st.success("✅ Normal Traffic Detected")
    else:
        result = "Attack"
        st.error("🚨 Attack Detected")

    st.write(f"🎯 Confidence: {confidence:.2f}%")

    # ================= LOGGING =================

    log_prediction(duration, src_bytes, dst_bytes, result, confidence, rule_alert)

# ================= SHOW LOGS =================

st.subheader("📊 Recent Predictions")

logs = get_recent_logs()

if not logs.empty:
    st.dataframe(logs)
else:
    st.info("No logs yet")