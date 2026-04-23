import requests
import json

def push_firewall_policy(src, dst, action='deny', name=None):
    """
    Corporate-level firewall policy push function.
    Simulates pushing a security policy to block/allow traffic.
    """
    if not name:
        name = f"Policy_{src.replace('.', '_')}_to_{dst.replace('.', '_')}"
    
    print(f"   Pushing Firewall Policy: {name}")
    print(f"   Source: {src}")
    print(f"   Destination: {dst}")
    print(f"   Action: {action}")
    
    # Simulate policy validation
    if not validate_ip(src) or not validate_ip(dst):
        print("❌ ERROR: Invalid IP address format")
        return False
    
    # Push to API
    payload = {
        "name": name,
        "src": src,
        "dst": dst,
        "action": action
    }
    
    try:
        response = requests.post("http://localhost:5001/add-firewall-rule", json=payload)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Policy pushed successfully: {result['message']}")
            return True
        else:
            print(f"❌ Failed to push policy: {response.json()}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")
        return False

def validate_ip(ip):
    """Basic IP/CIDR validation (simplified)"""
    if '/' in ip:
        ip, mask = ip.split('/')
        if not mask.isdigit() or int(mask) > 32:
            return False
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    return True

if __name__ == "__main__":
    # Example corporate use case: Block suspicious IP
    src_ip = input("Enter source IP to block: ")
    dst_ip = input("Enter destination IP/network: ")
    action = input("Enter action (deny/allow) [deny]: ") or "deny"
    
    push_firewall_policy(src_ip, dst_ip, action)