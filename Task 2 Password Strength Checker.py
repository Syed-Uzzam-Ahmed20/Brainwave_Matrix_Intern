# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 23:44:18 2025

@author: syedu
"""

# Password Strength Checker

import re

# --- Strength Criteria ---
def check_password_strength(password):
    strength_score = 0
    remarks = []

    # Length Check
    if len(password) < 8:
        remarks.append("Password is too short (minimum 8 characters required).")
    elif len(password) >= 8:
        strength_score += 1

    # Uppercase and Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength_score += 1
    else:
        remarks.append("Use both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        strength_score += 1
    else:
        remarks.append("Include at least one digit.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        remarks.append("Add special characters like !, @, #, etc.")

    # Common Passwords (basic example)
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() in common_passwords:
        remarks.append("Avoid using common passwords.")
        strength_score = 0  # Override to weak

    # Final Result
    if strength_score == 4:
        return "Strong", remarks
    elif strength_score >= 2:
        return "Moderate", remarks
    else:
        return "Weak", remarks

# --- Main Program ---
if __name__ == "__main__":
    while True:
        user_input = input("Enter a password to check its strength (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        strength, feedback = check_password_strength(user_input)
        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Feedback:")
            for note in feedback:
                print(f" - {note}")
        print("\n---\n")
