# app.py
from flask import Flask, render_template, request
import hashlib
import requests
import random
import string

app = Flask(__name__)

# ------------------------------
# Function to check breaches
# ------------------------------
def check_breaches(password):
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1pwd[:5]
    suffix = sha1pwd[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)
    hashes = res.text.splitlines()

    for line in hashes:
        h, count = line.split(":")
        if h == suffix:
            return int(count)
    return 0

# ------------------------------
# Function to generate suggested password
# ------------------------------
def suggest_password(password):
    # Symbols & numbers to append
    symbols = "!@#$%^&*"
    numbers = "1234567890"

    # Pick 2 random symbols and 2 random numbers
    sym_part = ''.join(random.choices(symbols, k=2))
    num_part = ''.join(random.choices(numbers, k=2))

    # Combine original password + symbols + numbers
    base = password + sym_part + num_part

    # ✅ Make first letter uppercase
    if len(base) > 0:
        base = base[0].upper() + base[1:]

    return base

# ------------------------------
# Function to evaluate password strength
# ------------------------------
def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*" for c in password)

    score = 0
    if length >= 8:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak"

# ------------------------------
# Flask Routes
# ------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        strength = password_strength(password)
        breaches = check_breaches(password)
        suggestion = suggest_password(password)

        result = (strength, breaches, suggestion)

    return render_template("index.html", result=result)

# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)