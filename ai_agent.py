import requests
import json
import time

def run_aiops_cycle():
    print("AI Agent: Observing network state...")
    time.sleep(1)  # Simulate processing
    data = requests.get("http://localhost:5001/get-config").json()
    
    print("AI Agent: Analyzing data...")
    time.sleep(1)
    network_state = json.dumps(data)
    
    if "down" in network_state:
        print("  AI Analysis: Anomaly detected! Interface Gi0/2 is DOWN. Policy requires 100% uptime.")
        print(" AI Action: Executing remediation script...")
        time.sleep(1)
        remediation = requests.post("http://localhost:5000/fix-interface")
        print(f"✅ Result: {remediation.json()['message']}")
        print(" Network healed!")
    else:
        print("✅ AI Analysis: Network healthy. No action needed.")

if __name__ == "__main__":
    run_aiops_cycle()