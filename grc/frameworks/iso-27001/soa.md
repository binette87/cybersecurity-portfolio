# ISO 27001:2022 — Statement of Applicability (SoA)

**Organization:** Binette Cybersecurity Portfolio  
**Standard:** ISO/IEC 27001:2022  
**Version:** 1.0  
**Date:** June 2026  
**Author:** Binette  

---

## Scope

This SoA applies to the cybersecurity lab environment documented in `Foundations_Lab_Final`, encompassing:
- Linux and Windows Server lab systems
- Network infrastructure (virtual)
- Container-based services (Docker)
- Security tooling (Suricata, Metasploit, Wireshark, Nmap)
- Lab-produced scripts and documentation

---

## Summary of Applicability

| Category | Total Controls | Applicable | Not Applicable | Implemented | Partial | Not Implemented |
|----------|---------------|------------|----------------|-------------|---------|-----------------|
| Organizational | 12 | 11 | 1 | 8 | 2 | 1 |
| People | 3 | 2 | 1 | 0 | 1 | 1 |
| Physical | 3 | 2 | 1 | 1 | 1 | 0 |
| Technological | 16 | 16 | 0 | 12 | 3 | 1 |
| **Total** | **34** | **31** | **3** | **21** | **7** | **3** |

**Overall Score: 69%** (implemented / applicable)

---

## Controls Excluded and Justification

| Control | Reason for Exclusion |
|---------|---------------------|
| A.6.1 Screening | Lab environment; no personnel hiring in scope |
| A.6.4 Disciplinary Process | Lab environment; no employee relations in scope |
| A.7.2 Physical Entry (full) | Virtual lab only; physical datacenter not in scope |

---

## Key Implemented Controls (Highlights)

**A.5.26 — Incident Response** ✅  
Full incident response capability demonstrated across Weeks 10–12. Evidence: `Incident_Response_Report.md`, `Operation_Fortress_Report.md`, `tepp_postmortem.md`.

**A.8.8 — Vulnerability Management** ✅  
Systematic vulnerability identification via Nmap, CVE research, and formal remediation planning. Evidence: `nmap_scan_results.txt`, `remediation_plan.md`.

**A.8.20 — Network Security** ✅  
UFW firewall hardening and network protocol analysis. Evidence: `firewall_config.sh`, `network_audit.txt`.

**A.8.25 — Secure Development** ✅  
Web application security testing integrated into development assessment. Evidence: `OmniPortal_Assessment.md`, `sqli_report.txt`.

---

## Gaps and Remediation Plan

| Gap | Priority | Target Date | Owner |
|-----|----------|-------------|-------|
| A.5.30 ICT Business Continuity | High | 2026-09-01 | Binette |
| A.6.3 Formal Training Program | Medium | 2026-08-01 | Binette |
| A.8.24 Cryptography Policy | Medium | 2026-08-01 | Binette |
| A.5.2 RACI Matrix | Low | 2026-10-01 | Binette |

---

*This SoA is reviewed annually and updated following any significant changes to the scope, risk environment, or control effectiveness.*
