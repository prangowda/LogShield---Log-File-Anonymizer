# LogShield - Log File Anonymizer

## 🔍 Project Description
LogShield is a **Python-based tool** that **automatically anonymizes sensitive information in log files**. It detects and replaces **IP addresses, emails, user IDs, and other confidential data** while keeping the file structure intact. This ensures **secure log sharing and compliance with privacy laws** like GDPR and CCPA.

---

## 🛠 Features
✅ Anonymizes **IP addresses, emails, user IDs**  
✅ Supports multiple log formats (`.log`, `.txt`, `.csv`)  
✅ Keeps file structure unchanged  
✅ Customizable masking options (`XXXX`, hash, or fake data)  
✅ Fast processing using **regex**  

---

## 📜 Installation
Install the required dependency using pip:
```sh
pip install faker
```

---

## 📂 Usage
Run the tool on a log file:
```sh
python logshield.py access.log
```
**Anonymized log file is saved as `anonymized_log.txt`**  

---

## 📊 Example Input & Output

### 🔹 **Original Log File (`access.log`)**
```
User: alice@example.com, IP: 192.168.1.15 - Accessed /admin
User: bob@gmail.com, IP: 172.16.0.2 - Accessed /dashboard
```

### 🔹 **Anonymized Output (`anonymized_log.txt`)**
```
User: john.doe@fakeemail.com, IP: 45.76.12.33 - Accessed /admin
User: jane.smith@fakemail.com, IP: 33.89.74.25 - Accessed /dashboard
```

---

## 🚀 Future Enhancements
🔹 **Hash-based anonymization** instead of fake data  
🔹 **Support for additional log formats**  
🔹 **Web-based UI for easy upload and processing**  


