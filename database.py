import sqlite3
import pandas as pd
from datetime import datetime

def init_db():
    conn = sqlite3.connect('predictions.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            duration REAL,
            src_bytes REAL,
            dst_bytes REAL,
            prediction TEXT,
            confidence REAL,
            rule_alert TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def log_prediction(duration, src_bytes, dst_bytes, prediction, confidence, rule_alert):
    conn = sqlite3.connect('predictions.db')
    
    conn.execute('''
        INSERT INTO predictions (timestamp, duration, src_bytes, dst_bytes, prediction, confidence, rule_alert)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        duration, src_bytes, dst_bytes, prediction, confidence, rule_alert
    ))
    
    conn.commit()
    conn.close()

def get_recent_logs(limit=50):
    conn = sqlite3.connect('predictions.db')
    df = pd.read_sql_query("SELECT * FROM predictions ORDER BY timestamp DESC LIMIT ?", conn, params=(limit,))
    conn.close()
    return df