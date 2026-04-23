from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# This is our "Fake" Router Configuration
config = {
    "hostname": "Core-Switch-01",
    "interfaces": {
        "GigabitEthernet0/1": {"status": "up", "description": "Uplink"},
        "GigabitEthernet0/2": {"status": "down", "description": "User-VLAN"}
    },
    "firewall": {
        "policies": [
            {"id": 1, "name": "Allow_All", "src": "any", "dst": "any", "action": "allow", "enabled": True},
            {"id": 2, "name": "Block_Bad_IP", "src": "192.168.1.100", "dst": "any", "action": "deny", "enabled": False}
        ]
    }
}

print("Config loaded:", config)  # Debug at startup

logs = [
    "2026-04-23 10:00:01 INFO: System started.",
    "2026-04-23 10:05:22 CRITICAL: Interface Gi0/2 is DOWN (Link Failure)",
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/get-config', methods=['GET'])
def get_config():
    print("Debug: get_config called")
    print("Config keys:", list(config.keys()))
    return jsonify(config)

@app.route('/fix-interface', methods=['POST'])
def fix_interface():
    config["interfaces"]["GigabitEthernet0/2"]["status"] = "up"
    logs.append("2026-04-23 10:05:25 INFO: AI Agent executed 'no shutdown' on Gi0/2.")
    return jsonify({"message": "Command 'no shutdown' executed by AI Agent."})

@app.route('/reset', methods=['POST'])
def reset():
    config["interfaces"]["GigabitEthernet0/2"]["status"] = "down"
    logs.append("2026-04-23 10:05:26 INFO: Interface Gi0/2 reset to down for demo.")
    return jsonify({"message": "Interface reset to down for demo."})

@app.route('/get-logs', methods=['GET'])
def get_logs():
    return '\n'.join(logs)

@app.route('/add-firewall-rule', methods=['POST'])
def add_firewall_rule():
    data = request.json
    src = data.get('src')
    dst = data.get('dst')
    action = data.get('action', 'deny')
    name = data.get('name', f'Rule_{len(config["firewall"]["policies"]) + 1}')
    
    if not src or not dst:
        return jsonify({"error": "Source and destination required"}), 400
    
    new_rule = {
        "id": len(config["firewall"]["policies"]) + 1,
        "name": name,
        "src": src,
        "dst": dst,
        "action": action,
        "enabled": True
    }
    config["firewall"]["policies"].append(new_rule)
    logs.append(f"2026-04-23 10:05:30 INFO: Firewall rule added: {name} - {src} -> {dst} ({action})")
    return jsonify({"message": f"Firewall rule '{name}' added successfully.", "rule": new_rule})

@app.route('/run-ai', methods=['POST'])
def run_ai():
    import requests
    import json
    # Simulate AI logic here
    data = config
    network_state = json.dumps(data)
    if "down" in network_state:
        logs.append("2026-04-23 10:05:27 INFO: AI Agent detected anomaly: Interface Gi0/2 DOWN.")
        # Trigger fix
        fix_interface()
        logs.append("2026-04-23 10:05:28 INFO: AI Agent triggered remediation.")
    else:
        logs.append("2026-04-23 10:05:29 INFO: AI Agent: Network healthy.")
    return jsonify({"message": "AI Agent run complete."})

if __name__ == '__main__':
    app.run(port=5001)