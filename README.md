# Phishing-Simulation-Tool
# Phishing Simulation and Awareness Tool

This project demonstrates a phishing simulation tool designed to educate users on recognizing phishing emails. The tool sends fake phishing emails to users, simulates common phishing techniques (such as fake login pages), and provides feedback to help users understand how to identify phishing attempts.

---

## **Features**

1. **Phishing Email Simulation**:
   - Sends fake phishing emails containing a link to a simulated fake login page.

2. **Fake Login Page**:
   - Mimics a legitimate login page to demonstrate how phishing attacks deceive users.
   - Styled realistically to increase awareness.

3. **Logging User Responses**:
   - Captures and stores usernames and passwords entered on the fake login page in a SQLite database.

4. **Educational Feedback**:
   - After submitting credentials, users are provided with educational content about phishing awareness.

---

## **Technologies Used**

- **Programming Language**: Python
- **Email Automation**: `smtplib` (Python standard library)
- **Web Development**: HTML, CSS, and Python's `http.server` module
- **Database**: SQLite

---

## **How to Use**

### **Prerequisites**

1. Python 3 installed on your system.
2. A Gmail account or another SMTP-enabled email account for sending emails.
3. Install the required libraries:
   ```bash
   pip install sqlite3
   ```

### **Steps to Run**

1. Clone this repository:
   ```bash
   git clone https://github.com/vinaygummadi/phishing-simulation-tool.git
   cd phishing-simulation-tool
   ```

2. Open the `phishing_simulation.py` file and configure the following:
   - Replace `your_email@example.com` and `your_email_password` with your sender email credentials (use an App Password if using Gmail).
   - Replace `target_email@example.com` with the recipient's email address.

3. Run the script:
   ```bash
   python phishing_simulation.py
   ```

4. The script will:
   - Send a phishing email to the recipient.
   - Host a fake login page at `http://localhost:8080`.

5. Open the fake login page in a browser and test the simulation by entering dummy credentials.

6. Check the logged responses in the SQLite database:
   ```bash
   sqlite3 phishing_simulation.db
   SELECT * FROM responses;
   ```


## **Educational Use Only**

This project is intended **strictly for educational purposes**. It should only be used in controlled environments and with the explicit consent of participants. Unauthorized use of this tool to conduct phishing attacks is illegal and unethical.

---

## **Future Enhancements**

- Add a dashboard to visualize user responses.
- Integrate more realistic phishing scenarios (e.g., mimicking banking or social media pages).
- Provide detailed phishing awareness tutorials after the simulation.

---
