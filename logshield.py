import re
import sys
from faker import Faker

fake = Faker()

# Regular expressions for sensitive data
IP_REGEX = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

# Function to anonymize logs
def anonymize_log(file_path, output_path="anonymized_log.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        log_data = file.read()

    anonymized_data = re.sub(IP_REGEX, fake.ipv4(), log_data)
    anonymized_data = re.sub(EMAIL_REGEX, fake.email(), anonymized_data)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(anonymized_data)

    print(f"✅ Anonymized log saved to: {output_path}")

# Run script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python logshield.py <logfile>")
    else:
        anonymize_log(sys.argv[1])
