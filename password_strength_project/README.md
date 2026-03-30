# 🔐 Password Security Analyzer

A **Flask web application** that analyzes password strength, checks if passwords have been exposed in real-world data breaches, and generates **strong, human-readable suggested passwords**.  

This project is ideal for showcasing **cybersecurity skills** and **web development**.

---

## 🛠 Features

- ✅ Check if a password has been leaked (via k-anonymity using [Have I Been Pwned API](https://haveibeenpwned.com/API/v3))  
- ✅ Evaluate password strength: **Weak, Medium, Strong**  
- ✅ Generate suggested strong passwords:
  - Includes the original password  
  - Adds random symbols and numbers  
  - **First letter always uppercase**  
- ✅ Tips for creating strong passwords  
- ✅ Professional cyber-themed UI with high contrast  
- ✅ Eye-symbol toggle to show/hide password  

---

## 📁 Project Structure
password_security_project/
│
├── app.py # Main Flask application
├── templates/
│ └── index.html # HTML template for the web page
├── screenshots/ # Folder containing project screenshots
│ ├── home_page.png
│ └── password_result.png
├── README.md # Project description



> Note: `requirements.txt` lists the Python packages needed to run this project (`flask`, `requests`).  

---

## ⚡ How to Run

1. Clone GitHub repository and go into the project folder.  
2. Install the required Python packages: `flask` and `requests`.  
3. Run the Flask app using `python app.py`.  
4. Open your web browser and go to `http://127.0.0.1:5000/` to see the app.  

---

## 💡 Tips for Strong Passwords

- Use **8–12 characters or more**  
- Mix **uppercase & lowercase letters**  
- Add **numbers and special symbols**  
- Avoid common words or personal information  
- Do **not reuse passwords** across multiple sites  

---

## 📌 Technologies Used

- Python 3.x  
- Flask  
- Requests library  
- HTML / CSS  
- k-Anonymity API (Have I Been Pwned)  

---

## 🎯 Project Goal

To help users **understand password security**, learn about breaches, and **generate safe, memorable passwords**.  

---

## 🔗 Screenshots

**Home Page:**  
![Home Page](screenshots/homepage.png)

**Suggested Password Result:**  
![Suggested Password](screenshots/password_result.png)
