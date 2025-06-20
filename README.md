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


# Password Strength Checker

A Python-based CLI tool to evaluate the strength of a user's password. It analyzes a password's complexity based on length, character variety, and common password patterns, and provides clear feedback to help users improve their password hygiene.

---

## 🔧 Features

* Checks password length (minimum 8 characters)
* Ensures a mix of uppercase and lowercase letters
* Validates presence of digits
* Recommends adding special characters
* Detects and flags common weak passwords
* Categorizes passwords as **Weak**, **Moderate**, or **Strong**
* Provides improvement suggestions

---

## 🚀 Getting Started

### Prerequisites

* Python 3.6 or higher

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
```

2. Run the script:

```bash
python password_strength_checker.py
```

---

## ✨ Example Output

```
Enter a password to check its strength: Hello123!

Password Strength: Strong
```

```
Enter a password to check its strength: admin

Password Strength: Weak
Feedback:
 - Password is too short (minimum 8 characters required).
 - Use both uppercase and lowercase letters.
 - Include at least one digit.
 - Add special characters like !, @, #, etc.
 - Avoid using common passwords.
```

---

## 📦 Future Enhancements

* Integration with HaveIBeenPwned API
* GUI version with Tkinter or PyQt
* Web-based implementation (Flask/Django)
* Password generator module

---

## 📄 License

MIT License. Feel free to use and modify.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📬 Contact

Created by \[Your Name] - feel free to reach out via [LinkedIn](https://linkedin.com/in/yourprofile) or open an issue!

---

## 📢 Show some love

If you found this helpful, give it a ⭐️ on GitHub and share it on LinkedIn!

---

## 🔗 Hashtags for Social Sharing

```
#Python #CyberSecurity #OpenSource #PasswordSecurity #InfoSec #DevTools
```
