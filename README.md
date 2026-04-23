# AIOps Network Anomaly Detection Prototype

This is a comprehensive AIOps demo with network monitoring, AI-driven remediation, log analysis, and advanced firewall policy management for corporate presentations.

## Architecture
- **Mock Router API** (`router_api.py`): Simulates network device with REST API, web dashboard, and firewall management.
- **AI Agent** (`ai_agent.py`): Observes network state, detects anomalies, triggers remediation.
- **Log Analyzer** (`log_analyzer.py`): AI-based log analysis for anomaly detection and alerting.
- **Firewall Policy Manager** (`firewall_policy.py`): Corporate-level security policy push with validation.
- **Reset Script** (`reset.py`): Resets demo state.
- **Web Dashboard**: Interactive interface at `http://localhost:5001` for monitoring and control.

## Advanced Use Cases
1. **Network Anomaly Detection**: AI monitors interfaces and auto-heals failures.
2. **AI Log Analyzer**: Scans logs for critical errors and sends alerts.
3. **Firewall Policy Management**: Push security policies with source/destination controls.
   - Add rules via dashboard form or CLI script
   - Supports allow/deny actions
   - IP validation and policy logging

## Setup
1. Install dependencies: `pip install flask requests`
2. Run server: `python router_api.py` (runs on http://localhost:5001)
3. Open dashboard: `http://localhost:5001`
4. Test scenarios:
   - Reset interface → Run AI agent
   - Add firewall rules via form or CLI
   - Run log analyzer

## CLI Commands
- **Start Server**: ``python router_api.py`` (port 5001)
- **Reset Demo**: `python reset.py`
- **Run AI Agent**: `python ai_agent.py`
- **Analyze Logs**: `python log_analyzer.py`
- **Push Firewall Policy**: `python firewall_policy.py` (interactive)

## Corporate-Level Features
- **Policy Validation**: IP format checking before rule deployment
- **Audit Logging**: All actions logged with timestamps
- **Interactive Dashboard**: Real-time monitoring and rule management
- **Error Handling**: Connection failures and validation errors demonstrated
- **Security Simulation**: Block suspicious IPs, allow trusted traffic

## Demo Flow
1. Show dashboard with initial "any any allow" rule
2. Simulate attack: Reset interface (anomaly)
3. AI detects and fixes network issue
4. Add firewall rule to block attacker IP
5. Demonstrate log analysis for additional insights

This demonstrates enterprise-grade AIOps with automated security policy enforcement!