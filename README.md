# 🛡️ Phishing Link Scanner

The **Phishing Link Scanner** is a Python-based tool designed to detect and classify URLs as **safe**, **suspicious**, or **malicious (phishing)** using a combination of heuristic analysis and open threat intelligence.

## 🚀 Features

- 🔗 Accepts user input or file-based list of URLs  
- 🧠 Analyzes URL structure, domain age, shortening services, and redirection patterns  
- 🧪 Integrates threat intelligence lookups (optional: VirusTotal, PhishTank)  
- ⚠️ Classifies links based on defined risk indicators  
- 📊 Outputs results in terminal or logs to a CSV/JSON report  
- 💡 Lightweight, fast, and ideal for integration into cybersecurity workflows

---

## 📽️ Demo

Check out the video demonstration on how the tool works: 

LinkedIn: https://www.linkedin.com/feed/update/urn:li:activity:7341883789419167745/

🧠 How It Works:-

-The scanner performs the following checks:

-Checks for known URL shorteners (bit.ly, tinyurl, etc.)

-Validates domain reputation and age (WHOIS)

-Examines redirection chains

-Matches against blacklists (optional APIs)

-Flags use of IP-based domains or suspicious patterns


Use Cases:-

-SOC automation

-Email phishing simulations

-Web proxy integration

-Awareness training programs
