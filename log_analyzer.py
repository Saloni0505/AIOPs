import time
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_here"  # Replace with actual if needed

def analyze_logs():
    print("AI Log Analyzer: Scanning logs...")
    with open("network.log", "r") as f:
        lines = f.readlines()
        for line in lines[-10:]:  # Check last 10 lines
            if "CRITICAL" in line or "DOWN" in line:
                print(f"Anomaly Detected: {line.strip()}")
                # Action: Send alert
                payload = {"content": f"🚨 AIOps Alert: {line.strip()}"}
                try:
                    requests.post(WEBHOOK_URL, json=payload)
                    print("Alert sent to NOC.")
                except:
                    print("Webhook not configured, but alert simulated.")
                # Could also trigger API fix
                requests.post("http://localhost:5000/fix-interface")
                break
        else:
            print("Logs clean.")

if __name__ == "__main__":
    analyze_logs()