from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# This is our "Fake" Router Configuration
config = {
    "hostname": "Core-Switch-01",
    "interfaces": {
        "GigabitEthernet0/1": {"status": "up", "description": "Uplink"},
        "GigabitEthernet0/2": {"status": "down", "description": "User-VLAN"},
        "GigabitEthernet0/3": {"status": "down", "description": "DMZ"},
        "GigabitEthernet0/4": {"status": "up", "description": "Management"}
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
    "2026-04-23 10:06:10 CRITICAL: Interface Gi0/3 is DOWN (Packet Loss)",
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
    request_data = request.get_json(silent=True) or {}
    interface = request_data.get("interface", "GigabitEthernet0/2")
    if interface not in config["interfaces"]:
        return jsonify({"error": f"Interface {interface} not found."}), 404

    config["interfaces"][interface]["status"] = "up"
    logs.append(f"2026-04-23 10:05:25 INFO: AI Agent executed 'no shutdown' on {interface}.")
    return jsonify({"message": f"Command 'no shutdown' executed on {interface} by AI Agent."})

@app.route('/reset', methods=['POST'])
def reset():
    request_data = request.get_json(silent=True) or {}
    interface = request_data.get("interface", "GigabitEthernet0/2")
    if interface not in config["interfaces"]:
        return jsonify({"error": f"Interface {interface} not found."}), 404

    config["interfaces"][interface]["status"] = "down"
    logs.append(f"2026-04-23 10:05:26 INFO: Interface {interface} reset to down for demo.")
    return jsonify({"message": f"Interface {interface} reset to down for demo."})

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
    # Simulate AI logic here
    down_interfaces = [name for name, info in config["interfaces"].items() if info.get("status") == "down"]
    if down_interfaces:
        interface = down_interfaces[0]
        logs.append(f"2026-04-23 10:05:27 INFO: AI Agent detected anomaly: Interface {interface} DOWN.")
        config["interfaces"][interface]["status"] = "up"
        logs.append(f"2026-04-23 10:05:28 INFO: AI Agent triggered remediation on {interface}.")
    else:
        logs.append("2026-04-23 10:05:29 INFO: AI Agent: Network healthy.")
    return jsonify({"message": "AI Agent run complete."})

if __name__ == '__main__':
    app.run(port=5001, debug=True)