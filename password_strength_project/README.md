# 🔐 Password Security Analyzer

A **Flask web application** to analyze password strength, check if passwords have been exposed in real-world breaches, and generate **strong, human-readable suggested passwords**.  

Perfect for showcasing **cybersecurity skills** and **web development**.

---

## 🛠 Features

- Check if a password has been leaked (k-anonymity via [Have I Been Pwned API](https://haveibeenpwned.com/API/v3))  
- Evaluate password strength: **Weak, Medium, Strong**  
- Suggest strong passwords:
  - Includes the original password  
  - Adds random symbols and numbers  
  - **First letter always uppercase** ✅  
- Tips for creating strong passwords  
- Professional cyber-themed UI with high contrast  
- Eye-symbol toggle to show/hide password  

---

## 📁 Project Structure

password_security_project/
│
├── app.py
├── templates/
│   └── index.html
├── README.md
└── requirements.txt
---

## ⚡ How to Run

1. Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd password_security_project
pip install flask requests

---

To run App or USE Password analyzer:

python app.py  and 
Open the browser at http://127.0.0.1:5000/


💡 Tips for Strong Passwords:

Use 8–12 characters or more
Mix uppercase & lowercase letters
Add numbers and special symbols
Avoid common words or personal information
Do not reuse passwords across multiple sites


📌 Technologies Used:

Python 3.x
Flask
Requests library
HTML / CSS
k-Anonymity API (Have I Been Pwned)


🎯 Project Goal:

To help users understand password security, learn about breaches, and generate safe, memorable passwords.
 


## 🔗 Screenshots

**Home Page:**  

![Home Page](screenshots/home_page.png)

**Suggested Password Result:**  

![Suggested Password](screenshots/password_result.png)
