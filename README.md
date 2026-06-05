# 🛡️ Cybersecurity Portfolio — GRC Command Center

**Binette | binette87** · [Foundations_Lab_Final](https://github.com/binette87/Foundations_Lab_Final)

[![NIST 800-53](https://img.shields.io/badge/NIST%20800--53-Rev%205-0078D4?style=flat-square)](grc/frameworks/nist-800-53/)
[![ISO 27001](https://img.shields.io/badge/ISO%2027001-2022-00A36C?style=flat-square)](grc/frameworks/iso-27001/)
[![SOC 2](https://img.shields.io/badge/SOC%202-Type%20II-7B2FBE?style=flat-square)](grc/frameworks/soc2/)
[![GRC Dashboard](https://img.shields.io/badge/GRC-Dashboard-FF6B35?style=flat-square)](dashboard/index.html)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-Automated-2EA44F?style=flat-square)](.github/workflows/grc-sync.yml)

---

## 📌 Overview

This repository is a **professional cybersecurity portfolio and GRC (Governance, Risk & Compliance) Command Center** built on top of 12 weeks of hands-on security lab work. It demonstrates:

- Mapping real lab artifacts to enterprise security frameworks (NIST 800-53 Rev 5, ISO 27001:2022, SOC 2)
- Operating a full GRC lifecycle: risk identification → control implementation → audit → remediation
- Automated compliance reporting via GitHub Actions
- Interactive web dashboard for real-time compliance posture visibility

---

## 🗂️ Repository Structure

```
cybersecurity-portfolio/
├── README.md                          ← You are here
├── dashboard/
│   └── index.html                     ← GRC Command Center (open in browser)
├── grc/
│   ├── frameworks/
│   │   ├── nist-800-53/
│   │   │   ├── control-library.csv    ← Full NIST SP 800-53 Rev 5 control set
│   │   │   └── assessment-report.md  ← Control assessment against lab evidence
│   │   ├── iso-27001/
│   │   │   ├── control-library.csv   ← ISO 27001:2022 Annex A controls
│   │   │   └── soa.md                ← Statement of Applicability
│   │   └── soc2/
│   │       ├── control-library.csv   ← SOC 2 Trust Services Criteria
│   │       └── readiness-report.md   ← SOC 2 readiness assessment
│   ├── risk-register/
│   │   └── risk-register.csv         ← Live risk register (likelihood × impact)
│   ├── incident-log/
│   │   └── incident-log.csv          ← Incident log with timeline & status
│   ├── assessments/
│   │   └── security-assessment.md    ← Comprehensive security assessment
│   ├── audits/
│   │   └── audit-schedule.csv        ← Audit schedule and findings tracker
│   └── remediation/
│       └── remediation-tracker.csv   ← Remediation plan with owners & due dates
├── .github/
│   └── workflows/
│       └── grc-sync.yml              ← Automated GRC reporting pipeline
└── grc-workbook.xlsx                  ← Master GRC Excel workbook (all sheets)
```

---

## 🔗 Source Lab Evidence

All GRC controls are mapped to real lab artifacts from [`Foundations_Lab_Final`](https://github.com/binette87/Foundations_Lab_Final):

| Week | Domain | Key Artifacts | Frameworks |
|------|--------|--------------|-----------|
| 01 | Linux Fundamentals | `harden.sh`, `discovery.txt` | NIST AC-2, CM-6; ISO A.8; SOC CC6 |
| 02 | Network Analysis | `network_audit.txt`, `protocol_audit.txt` | NIST SC-7, SI-4; ISO A.8.20; SOC CC7 |
| 03 | Python/Scripting | `brute_detector.py`, `system_auditor.py` | NIST SI-3, SI-4; ISO A.8.16; SOC CC7 |
| 04 | Docker/Containers | `docker-compose.yml`, `deploy_web.sh` | NIST CM-7, SC-28; ISO A.8.25; SOC CC6 |
| 05 | Identity & AD | `onboard_engineers.ps1`, `gpo_audit.txt` | NIST AC-2, AC-3, IA-5; ISO A.5.15; SOC CC6 |
| 06 | Capstone | `HardenedOutpost_SAD.pdf` | NIST PL-2; ISO A.5.1; SOC CC1 |
| 07 | Recon & Vuln | `remediation_plan.md`, `nmap_scan_results.txt` | NIST RA-3, RA-5; ISO A.8.8; SOC CC7 |
| 08-09 | Exploitation | `sqli_report.txt`, `OmniPortal_Assessment.md` | NIST SA-11, SI-10; ISO A.8.25; SOC CC7 |
| 10 | DFIR | `forensic_report.pdf`, `attack_timeline.csv` | NIST IR-4, IR-6; ISO A.5.26; SOC CC7 |
| 11 | Active Defense | `firewall_config.sh`, `custom_ids.rules` | NIST SC-7, SI-4; ISO A.8.20; SOC CC6 |
| 12 | Final Reckoning | `Incident_Response_Report.md` | NIST IR-8; ISO A.5.24; SOC CC7 |

---

## 📊 Compliance Posture Summary

| Framework | Controls Assessed | Implemented | Partial | Not Implemented | Score |
|-----------|------------------|-------------|---------|-----------------|-------|
| NIST 800-53 Rev 5 | 42 | 28 | 10 | 4 | **67%** |
| ISO 27001:2022 | 35 | 24 | 8 | 3 | **69%** |
| SOC 2 (Trust Criteria) | 30 | 21 | 7 | 2 | **70%** |

> Live scores update automatically via GitHub Actions on every push.

---

## 🚀 Quick Start

### View the Dashboard
Open `dashboard/index.html` in any browser — no server required.

### Run GRC Sync Locally
```bash
# Clone this repo
git clone https://github.com/binette87/cybersecurity-portfolio.git
cd cybersecurity-portfolio

# Link to source lab repo
git remote add labs https://github.com/binette87/Foundations_Lab_Final.git
git fetch labs

# Trigger GRC report generation
python3 grc/scripts/generate_report.py
```

### GitHub Actions
The GRC pipeline runs automatically on:
- Every push to `main`
- Weekly on Sunday at 00:00 UTC (scheduled audit)
- Manual trigger via `workflow_dispatch`

---

## 🛠️ GRC Methodology

This portfolio follows the **NIST Risk Management Framework (RMF)** lifecycle:

1. **Categorize** — System categorization per FIPS 199 (Moderate impact)
2. **Select** — Baseline controls from NIST 800-53 Rev 5 Moderate baseline
3. **Implement** — Lab artifacts as control evidence
4. **Assess** — Control testing documented in assessment reports
5. **Authorize** — Risk acceptance decisions in risk register
6. **Monitor** — Continuous monitoring via GitHub Actions + dashboard

---

*Built by Binette | Powered by real lab work, not theory.*
