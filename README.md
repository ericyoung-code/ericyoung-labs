# Eric Young's Cybersecurity & Infrastructure Project Portfolio

Welcome to **ericyoung-labs** — a curated showcase of real-world technical projects demonstrating cybersecurity, infrastructure automation, and system integration projects.

---

## 🔍 About Me

I'm a Senior Technology Leader with 20+ years of experience across government, defense, and mission-critical systems. I specialize in:

- Cybersecurity Governance & Security Program Management
- Infrastructure as Code (IaC) & Network Optimization
- Large-Scale Systems Integration & Technical Program Management
- Federal IT Operations, Emergency Ops, and DoD Systems

This portfolio highlights my practical skills using modern tooling like Terraform, Ansible, Python, AWS, and log analysis frameworks. These projects are built to reflect real-world problems and solutions.

---

## 🛠️ Projects

| Project | Description |
|--------|-------------|
| [`n-ether`](./n-ether) | Network enumeration tool for host exploration and recon. |
| [`secure-vpc-network-deploy`](./secure-vpc-network-deploy) | Deploys a secure VPC on AWS with public/private subnets using Terraform. |
| [`ics-sensor-sim-lab`](./ics-sensor-sim-lab) | Simulates control system sensor traffic to test network visibility and monitoring infrastructure. |
| [`splunk-logparser-toolkit`](./splunk-logparser-toolkit) | Parses structured logs for anomalies or alerts, built for use with Splunk or local triage. |
| [`incident-response-automation`](./incident-response-automation) | Automates actions based on alert log patterns for basic incident response tasks. |
| [`dod-sys-hardening-benchmark`](./dod-sys-hardening-benchmark) | Ansible-based system hardening project aligned with DISA STIG and NIST 800-53 controls. |


---

## 📌 How to Use This Repo

Each project includes:
- 📁 Scaffold and/or starter template
- 📄 Documentation in `/docs`
- ⚙️ CI/CD configuration (where applicable)
- 🧪 Test examples or scripts
- 1.  Run the Simulator:
python lab_runner.py ics-sim --duration 60 --output my_traffic.log

- 2.  Run the Parser:
python lab_runner.py log-parser --input my_traffic.log

- 3.  Run the Responder:
python lab_runner.py incident-response --ip 1.2.3.4 --reason "Suspicious behavior"

- 4.  Run the Auditor:
python lab_runner.py compliance-audit --profile standard

- 5.  Run the VPC Generator:
python lab_runner.py vpc-gen --cidr 10.0.0.0/16 --subnets 3 --output vpc.tf

- 6.  Run N-ETHER:
python lab_runner.py n-ether --target 127.0.0.1 --quick

Fork, clone, or adapt these projects for your own infrastructure or study.

---

## 📫 Connect With Me

- LinkedIn: [linkedin.com/in/eric-young-996915157](https://www.linkedin.com/in/eric-young-996915157)

Let's connect if you're interested in collaborating on secure, resilient, and scalable systems.
