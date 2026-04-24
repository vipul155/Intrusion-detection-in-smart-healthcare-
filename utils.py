import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from imblearn.over_sampling import SMOTE


def load_and_preprocess_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path, header=None)

    print("Dataset shape:", df.shape)

    # 🔥 IMPORTANT FIX (NSL-KDD structure)
    # Last column = difficulty → remove
    # Second last = label
    X = df.iloc[:, :-2]
    y = df.iloc[:, -2]

    # 🔥 CLEAN LABELS
    y = y.astype(str).str.strip().str.replace('.', '', regex=False)
    y = y.apply(lambda x: 0 if x == 'normal' else 1)

    print("\nLabel distribution BEFORE SMOTE:")
    print(y.value_counts())

    print("\nUnique labels:", y.unique())

    # 🔥 ENCODE CATEGORICAL FEATURES
    label_encoders = {}

    for col in X.columns:
        if X[col].dtype == 'object':
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col])
            label_encoders[col] = le

    print("\nFeatures shape:", X.shape)

    # 🔥 SCALE FEATURES
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # 🔥 HANDLE IMBALANCE (SMOTE)
    if len(np.unique(y)) > 1:
        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

        print("\nAfter SMOTE:")
        print("X shape:", X_resampled.shape)
        print("y distribution:\n", pd.Series(y_resampled).value_counts())
    else:
        print("\n⚠️ SMOTE skipped (only one class found)")
        X_resampled, y_resampled = X_scaled, y

    return X_resampled, y_resampled, scaler, label_encoders


# 🔥 RULE-BASED DETECTION (extra feature for dashboard)
def rule_based_detection(features):
    try:
        src_bytes = float(features[4])

        if src_bytes > 10000:
            return "🚨 Suspicious Activity - High Source Bytes"

        return "✅ Normal Traffic"

    except:
        return "⚠️ Invalid Input"