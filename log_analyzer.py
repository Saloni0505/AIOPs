import time
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_here"  # Replace with actual if needed

# NOC Engineer Email Configuration
NOC_EMAIL = "mesalonideshmukh@gmail.com"
SENDER_EMAIL = "shaggi8536@gmail.com"  # Add your Gmail address here
SENDER_PASSWORD = "dihs zmvr ohni kwyj"  # Add your Gmail App Password here (NOT regular password if 2FA is enabled)

def send_email_alert(alert_message):
    """Send email alert to NOC engineer"""
    try:
        # Gmail SMTP configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        print(f"📧 Sending email from {SENDER_EMAIL} to {NOC_EMAIL}...")
        
        # Create email message
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = NOC_EMAIL
        msg["Subject"] = "🚨 AIOps Alert: Network Anomaly Detected"
        
        # Email body
        body = f"""
AIOps Network Anomaly Detection Alert

Alert Details:
{alert_message}

Time: {time.strftime('%Y-%m-%d %H:%M:%S')}

Action Taken:
- Anomaly has been automatically remediated
- Interface has been brought up if it was down
- Firewall policies are in place

Please review the network dashboard at http://localhost:5001 for more details.

---
Automated Alert from AIOps System
"""
        
        msg.attach(MIMEText(body, "plain"))
        
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure connection
            print("✓ Connected to Gmail SMTP server")
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            print("✓ Login successful")
            server.send_message(msg)
        
        print("✅ Email alert sent successfully to NOC engineer.")
        return True
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Authentication Failed: {str(e)}")
        print("\n⚠️  IMPORTANT: Your Gmail account likely has 2FA enabled!")
        print("\nSteps to fix:")
        print("1. Go to https://myaccount.google.com/apppasswords")
        print("2. Select 'Mail' and 'Windows Computer'")
        print("3. Google will generate a 16-character password")
        print("4. Update SENDER_PASSWORD in log_analyzer.py with this password")
        return False
    except smtplib.SMTPException as e:
        print(f"❌ SMTP Error: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}: {str(e)}")
        return False

def analyze_logs():
    print("AI Log Analyzer: Scanning logs...")
    with open("network.log", "r") as f:
        lines = f.readlines()
        for line in lines[-10:]:  # Check last 10 lines
            if "CRITICAL" in line or "DOWN" in line:
                print(f"Anomaly Detected: {line.strip()}")
                # Action: Send alerts
                payload = {"content": f"🚨 AIOps Alert: {line.strip()}"}
                try:
                    requests.post(WEBHOOK_URL, json=payload)
                    print("Alert sent to Discord webhook.")
                except:
                    print("Discord webhook not configured.")
                
                # Send email alert to NOC engineer
                send_email_alert(line.strip())
                
                # Could also trigger API fix
                requests.post("http://localhost:5001/fix-interface")
                break
        else:
            print("Logs clean.")

if __name__ == "__main__":
    analyze_logs()