import pandas as pd
import urllib.request
import os

urls = [
    "https://raw.githubusercontent.com/nslkdd001/NSL-KDD/master/KDDTrain+.txt",
    "https://github.com/defcom17/NSL_KDD/raw/master/KDDTrain+.txt",
    "https://raw.githubusercontent.com/rahulvigneswaran/Intrusion-Detection/master/dataset/KDDTrain+.txt"
]

for url in urls:
    try:
        print(f"🔄 Trying {url}")
        os.makedirs("dataset", exist_ok=True)
        urllib.request.urlretrieve(url, "dataset/KDDTrain+.txt")
        
        # Verify file
        with open("dataset/KDDTrain+.txt", 'r') as f:
            first_line = f.readline().strip()
        
        if first_line.startswith('0,tcp') or 'normal' in first_line:
            print("✅ SUCCESS! Dataset downloaded correctly!")
            print("📊 First line:", first_line[:100])
            print("📏 File size:", os.path.getsize("dataset/KDDTrain+.txt"), "bytes")
            break
        else:
            print("❌ Invalid file (HTML error page)")
            os.remove("dataset/KDDTrain+.txt")
    except Exception as e:
        print(f"❌ Failed: {e}")
        if os.path.exists("dataset/KDDTrain+.txt"):
            os.remove("dataset/KDDTrain+.txt")
        continue

print("\n🎉 Ready to train model!")
