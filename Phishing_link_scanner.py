import re
from urllib.parse import urlparse

# Suspicious keywords commonly found in phishing URLs
suspicious_keywords = [
    'login', 'verify', 'update', 'secure', 'account', 'banking', 'ebay', 'paypal',
    'signin', 'security', 'webscr', 'confirm'
]

def is_ip_address(url):
    pattern = r"(https?:\/\/)?(\d{1,3}\.){3}\d{1,3}(:\d+)?(\/.*)?"
    return bool(re.match(pattern, url))

def contains_suspicious_keywords(url):
    return any(keyword in url.lower() for keyword in suspicious_keywords)

def excessive_dots(domain):
    return domain.count('.') > 3

def contains_at_symbol(url):
    return '@' in url

def check_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    print(f"\n🔍 Scanning URL: {url}")

    score = 0
    reasons = []

    if is_ip_address(url):
        score += 2
        reasons.append("Uses IP address instead of domain")

    if contains_at_symbol(url):
        score += 2
        reasons.append("Contains '@' symbol")

    if contains_suspicious_keywords(url):
        score += 2
        reasons.append("Contains suspicious keyword")

    if excessive_dots(domain):
        score += 1
        reasons.append("Contains excessive dots in domain")

    if len(domain) > 75:
        score += 1
        reasons.append("Domain name is unusually long")

    if score == 0:
        print("✅ URL appears to be safe.")
    else:
        print("⚠️ Suspicious URL detected!")
        print("Reason(s):")
        for reason in reasons:
            print(f" - {reason}")

if __name__ == "__main__":
    while True:
        url = input("\nEnter a URL to scan (or type 'exit' to quit): ").strip()
        if url.lower() == 'exit':
            break
        check_url(url)