import requests
import json
import time

def run_aiops_cycle():
    print("AI Agent: Observing network state...")
    time.sleep(1)  # Simulate processing
    data = requests.get("http://localhost:5001/get-config").json()
    
    print("AI Agent: Analyzing data...")
    time.sleep(1)
    interfaces = data.get("interfaces", {})
    down_interfaces = [name for name, info in interfaces.items() if info.get("status") == "down"]

    if down_interfaces:
        interface = down_interfaces[0]
        print(f"  AI Analysis: Anomaly detected! Interface {interface} is DOWN. Policy requires 100% uptime.")
        print(" AI Action: Executing remediation script...")
        time.sleep(1)
        remediation = requests.post("http://localhost:5001/fix-interface", json={"interface": interface})
        print(f"✅ Result: {remediation.json()['message']}")
        print(" Network healed!")
    else:
        print("✅ AI Analysis: Network healthy. No action needed.")

if __name__ == "__main__":
    run_aiops_cycle()