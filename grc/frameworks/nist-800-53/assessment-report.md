# NIST SP 800-53 Rev 5 — Control Assessment Report

**System Name:** Cybersecurity Foundations Lab Environment  
**Assessor:** Binette  
**Assessment Date:** June 2026  
**Baseline:** Moderate  
**System Category:** FIPS 199 Moderate (Confidentiality: Moderate, Integrity: Moderate, Availability: Low)

---

## Executive Summary

This assessment evaluated 42 NIST SP 800-53 Rev 5 controls from the Moderate baseline against lab artifacts produced during a 12-week cybersecurity foundations program. Controls were assessed using artifact review, configuration inspection, and process observation.

| Result | Count | Percentage |
|--------|-------|-----------|
| Implemented | 28 | 67% |
| Partially Implemented | 10 | 24% |
| Not Implemented | 4 | 10% |
| **Total Assessed** | **42** | **100%** |

**Overall Compliance Score: 67%** (targeting 80%+ for authorization)

---

## Assessment Results by Family

### Access Control (AC) — 6 controls assessed

| Control | Result | Evidence |
|---------|--------|---------|
| AC-2 Account Management | ✅ Implemented | `onboard_engineers.ps1` — AD lifecycle automation |
| AC-3 Access Enforcement | ✅ Implemented | `gpo_audit.txt` — GPO enforces RBAC |
| AC-6 Least Privilege | ✅ Implemented | `harden.sh` — permission hardening |
| AC-7 Unsuccessful Logon Attempts | ✅ Implemented | `brute_detector.py` — automated detection |
| AC-11 Session Lock | ⚠️ Partial | GPO covers Windows; Linux incomplete |
| AC-17 Remote Access | ⚠️ Partial | UFW restricts access; policy not formalized |

### Audit and Accountability (AU) — 5 controls assessed

| Control | Result | Evidence |
|---------|--------|---------|
| AU-2 Event Logging | ✅ Implemented | `custom_ids.rules` — event definition |
| AU-3 Content of Audit Records | ✅ Implemented | `security_alert.json` — structured records |
| AU-6 Audit Review | ✅ Implemented | `brute_detector.py` — automated review |
| AU-9 Protection of Audit Info | ⚠️ Partial | Access restricted; no integrity protection |
| AU-12 Audit Record Generation | ✅ Implemented | `system_auditor.py` — JSON audit records |

### Configuration Management (CM) — 5 controls assessed

| Control | Result | Evidence |
|---------|--------|---------|
| CM-2 Baseline Configuration | ✅ Implemented | `docker-compose.yml` — codified baseline |
| CM-6 Configuration Settings | ✅ Implemented | `harden.sh` — secure configuration |
| CM-7 Least Functionality | ✅ Implemented | Air-gapped Docker stack |
| CM-8 System Component Inventory | ⚠️ Partial | Nmap discovery; no formal CMDB |

### Identification and Authentication (IA) — 4 controls assessed

| Control | Result | Evidence |
|---------|--------|---------|
| IA-2 Identification/Authentication | ✅ Implemented | AD unique accounts |
| IA-4 Identifier Management | ✅ Implemented | `onboard_engineers.ps1` |
| IA-5 Authenticator Management | ✅ Implemented | GPO password policies |

### Incident Response (IR) — 5 controls assessed

| Control | Result | Evidence |
|---------|--------|---------|
| IR-4 Incident Handling | ✅ Implemented | `Incident_Response_Report.md` |
| IR-5 Incident Monitoring | ✅ Implemented | `attack_timeline.csv` |
| IR-6 Incident Reporting | ✅ Implemented | `escalation_path.txt` |
| IR-8 Incident Response Plan | ✅ Implemented | `Operation_Fortress_Report.md` |

### Risk Assessment (RA) — 3 controls assessed

| Control | Result | Evidence |
|---------|--------|---------|
| RA-3 Risk Assessment | ✅ Implemented | `ThreatProfile_CloudNano.md` |
| RA-5 Vulnerability Scanning | ✅ Implemented | `nmap_scan_results.txt` + `remediation_plan.md` |

### System and Communications Protection (SC) — 2 controls assessed

| Control | Result | Evidence |
|---------|--------|---------|
| SC-7 Boundary Protection | ✅ Implemented | `firewall_config.sh` — UFW rules |
| SC-28 Protection at Rest | ⚠️ Partial | Volume isolation; no encryption at rest |

### System and Information Integrity (SI) — 3 controls assessed

| Control | Result | Evidence |
|---------|--------|---------|
| SI-3 Malicious Code Protection | ✅ Implemented | `custom_ids.rules` — Suricata |
| SI-4 System Monitoring | ✅ Implemented | IDS + Python monitoring |
| SI-10 Input Validation | ✅ Implemented | `sqli_report.txt` — findings + remediation |

---

## Findings and Recommendations

### High Priority (address within 30 days)
1. **AC-22 Publicly Accessible Content** — Establish policy for any public-facing content
2. **SC-28 Encryption at Rest** — Implement encryption for Docker volumes containing sensitive data

### Medium Priority (address within 90 days)
3. **AC-11 Session Lock (Linux)** — Implement `vlock` or PAM-based session timeout on Linux hosts
4. **CA-7 Continuous Monitoring** — Formalize continuous monitoring strategy document
5. **CM-8 Asset Inventory** — Maintain live CMDB (consider `netdisco` or spreadsheet-based tracker)

### Low Priority (address within 180 days)
6. **AT-2 Security Awareness Training** — Document formal training program beyond lab notes
7. **AU-9 Audit Log Integrity** — Implement `auditd` with remote syslog for tamper-evident logging

---

## Authorization Recommendation

**Risk Level: MODERATE**  
Recommend authorization with conditions — complete High and Medium priority findings before production deployment. Current posture demonstrates strong technical controls with gaps in policy documentation and formal program artifacts.
