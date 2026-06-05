# Security Awareness Training — Recording Scripts
**Presenter:** Binette  
**Portfolio:** github.com/binette87/cybersecurity-portfolio  
**Frameworks:** NIST AT-2 · ISO 27001 A.6.3 · SOC 2 CC1  
**Total estimated runtime:** 20–25 minutes across all 4 modules

---

## Production Notes

**Setup before recording:**
- Open dashboard in Chrome, fullscreen
- Scroll to the Security Awareness Training section
- Expand one module at a time as you record
- Speak at a steady, measured pace — pause 1–2 seconds after each slide advance
- Use Loom (loom.com) or QuickTime → New Screen Recording for capture

**On-screen actions during recording:**
- Click the module header to expand it before beginning each section
- Advance slides using "Next →" as you narrate each slide
- Click quiz answers at the end of each module

---

## Dashboard Walkthrough Script (5–7 minutes)

---

*[Open dashboard, full screen visible]*

"Welcome to my GRC Command Center — a professional Governance, Risk, and Compliance portfolio I built on top of twelve weeks of hands-on cybersecurity lab work.

Everything you see here is backed by real lab artifacts — scripts, reports, forensic evidence, and configuration files committed to GitHub and mapped directly to industry frameworks.

*[Point to compliance gauges]*

Let's start at the top. These three gauges show my current compliance posture across NIST Special Publication 800-53 Revision 5, ISO 27001 colon 2022, and SOC 2 Trust Services Criteria. I'm sitting at sixty-seven, sixty-nine, and seventy percent respectively — which is honest. My governance and policy documentation has gaps, and this dashboard doesn't hide that.

*[Point to KPI row]*

The KPI row below gives me a quick operational read: fifteen open risks, eight of which are high or critical, ten incidents year-to-date — all closed — eight open remediation items, and fourteen audits on the schedule.

*[Point to risk heatmap]*

This risk heatmap plots every risk on a five-by-five likelihood times impact grid. The red cells in the upper right — those are my critical risks: SQL injection, unpatched CVEs, lateral movement. I can trace any cell directly back to a specific risk ID in my risk register.

*[Point to incident log]*

Every incident I documented during the lab — ten in total — is logged here with severity, detection method, root cause, remediation actions, and lessons learned. INC-001 through INC-010, all closed.

*[Point to control coverage bars]*

The domain scores show where I'm strong — incident response and forensics at ninety percent, access control at eighty-five — and where I have acknowledged gaps. Governance and policy is at fifty-five percent. That's not a failure — that's an accurate assessment with a remediation plan attached.

*[Point to lab evidence map]*

This is my favorite section. Every week of the twelve-week program is mapped to specific NIST, ISO, and SOC 2 controls. Week three Python scripts map to monitoring controls. Week ten forensics work maps to IR evidence collection. Week eleven IDS rules map to boundary protection. This is the proof of work behind every compliance score you see above.

Now let me walk you through the Security Awareness Training section I built into this dashboard."

---

## Module 1 Script — Phishing Awareness (4–5 minutes)

---

*[Click Module 1 header to expand. Navigate to Slide 1.]*

"Module One covers phishing awareness — the entry point for the majority of organizational breaches.

*[Slide 1 — What Is Phishing]*

Phishing is a social engineering attack in which a threat actor impersonates a trusted entity to manipulate individuals into revealing credentials, sensitive data, or executing harmful actions. It is not primarily a technical attack — it is a human attack. And that makes awareness your most effective defense.

The four primary delivery mechanisms are impersonation, malicious links, infected attachments, and manufactured urgency. Attackers rely on you acting quickly without thinking carefully.

*[Advance to Slide 2 — Red Flags]*

These are the red flags you must internalize until they become instinct.

First — sender domain mismatch. An email from support@micros0ft-help.com is not from Microsoft. The domain is different. Always verify the full domain, not just the display name.

Second — urgency language. 'Your account will be suspended in twenty-four hours.' Urgency is a manipulation technique. Legitimate organizations do not threaten you into acting within hours.

Third — generic salutation. If IT knows who you are, they will address you by name.

Fourth — hover before you click. Never click a link without first hovering over it to see where it actually leads.

Fifth — requests for credentials. Your IT department, your bank, and your organization will never ask for your password via email. Full stop.

*[Advance to Slide 3 — Anatomy of a Phishing Email]*

Here is a simulated phishing email. Notice the sender domain — corp-helpdesk-portal.net — not an official organizational domain. The subject line opens with a warning symbol and the word URGENT. The salutation is generic. There is a shortened, obfuscated link. And the core request is that you act within two hours.

Every one of these elements is a deliberate manipulation technique. When you see a combination of these indicators, treat the email as malicious until proven otherwise.

*[Advance to Slide 4 — Response Protocol]*

When you identify a suspected phishing email, your response is this: do not click, do not reply, do not forward. Report it immediately to your security team through the designated reporting mechanism. If you already clicked a link or entered credentials, report it immediately and initiate a password reset. And preserve the email as evidence — do not delete it.

*[Click answer C on the quiz]*

The knowledge check here: IT support will never legitimately ask for your password via email. The correct response is always to report the email and delete it — not engage with it."

---

## Module 2 Script — Password Hygiene & MFA (4–5 minutes)

---

*[Click Module 2 header. Navigate to Slide 1.]*

"Module Two covers password hygiene and multi-factor authentication.

*[Slide 1 — Why Credentials Are the Primary Target]*

According to the Verizon Data Breach Investigations Report, over eighty percent of hacking-related breaches involve compromised or weak credentials. This is not an abstract statistic — it means your password is the most targeted element of your security posture. Attackers invest significant effort in credential theft because a valid credential bypasses almost every perimeter control.

*[Advance to Slide 2 — Strong Password Characteristics]*

What makes a strong password? Length is the most important factor. A sixteen-character passphrase is exponentially harder to crack than an eight-character complex password. 'correct-horse-battery' is stronger than 'P-at-sign-dollar-sign-w-zero-r-d' — despite appearing simpler.

Three rules: minimum sixteen characters, unique per account — meaning never reused anywhere — and managed by a dedicated password manager such as Bitwarden or 1Password. A password manager removes the cognitive burden of memorizing credentials and enables true uniqueness.

*[Advance to Slide 3 — MFA]*

Multi-factor authentication requires a second verification factor beyond your password. Even if your credentials are fully compromised, MFA blocks unauthorized access in ninety-nine point nine percent of cases — that is Microsoft's own research.

The three factor categories are something you know, something you have, and something you are. An authenticator application like Google Authenticator or Microsoft Authenticator generates time-based one-time passwords. A hardware key like YubiKey is the strongest form available.

One critical note: SMS-based MFA is the weakest option. SIM-swapping attacks allow adversaries to intercept SMS codes. Where possible, use an authenticator application.

*[Advance to Slide 4 — Best Practices]*

The operational rules: use a password manager, enable MFA on every account — especially email, VPN, and administrative systems — change your password immediately upon suspected compromise, and never share credentials with anyone, including IT staff.

*[Click answer B on the quiz]*

Password reuse is the critical vulnerability here. If one account in a data breach exposes your password and you have reused that password elsewhere, every account with that password is now at risk through a technique called credential stuffing. Complexity alone does not protect you from this."

---

## Module 3 Script — Incident Reporting (4–5 minutes)

---

*[Click Module 3 header. Navigate to Slide 1.]*

"Module Three covers security incident recognition and reporting.

*[Slide 1 — What Is a Security Incident]*

A security incident is any event that threatens the confidentiality, integrity, or availability of organizational information or systems. This definition is broad by design. Unauthorized access, data exfiltration, malware infection, policy violations — all of these qualify. And critically: you do not need to be certain something is an incident to report it. Uncertainty is sufficient justification.

*[Advance to Slide 2 — Common Incident Indicators]*

These are the behavioral and technical indicators that should trigger an immediate report.

Unusual system slowness or unexplained crashes — these can indicate a malware process consuming resources in the background. Unexpected account lockouts or password change notifications — these may indicate someone else is attempting to access your account. Unfamiliar programs or files — malware frequently creates or modifies files and processes. Abnormal outbound traffic — data exfiltration often manifests as unusual network activity. Colleagues reporting suspicious emails from your account — this may indicate your account has been compromised and is being used to propagate an attack.

No single indicator is definitive. Multiple indicators in combination are significant.

*[Advance to Slide 3 — The Reporting Process]*

Time is the most critical variable in incident response. Every minute of delay increases the potential impact of a breach.

Step one: contain. If it is safe to do so, disconnect the affected system from the network — not from power. Powering off can destroy volatile evidence.

Step two: preserve. Do not delete files, clear logs, or modify the system in any way. Evidence preservation is essential for forensic analysis.

Step three: report. Contact your security team immediately through the designated channel. Do not use the affected system to report — use a different device.

Step four: document. Record exactly what you observed, when you observed it, and every action you took. Timestamps matter.

*[Advance to Slide 4 — Escalation Chain]*

Severity determines timing. Critical incidents — active breaches, ransomware, active data exfiltration — require a report within fifteen minutes. High severity within one hour. Medium within four hours. Low within twenty-four.

And the most important principle in this module: when in doubt, report. There is no organizational penalty for over-reporting a security event. There is significant penalty for under-reporting one.

*[Click answer C on the quiz]*

The correct response to suspected active exfiltration: disconnect from the network immediately to stop the transfer, preserve the system state for forensic analysis, and notify the security team. Do not restart or delete anything."

---

## Module 4 Script — Insider Threat Awareness (4–5 minutes)

---

*[Click Module 4 header. Navigate to Slide 1.]*

"Module Four covers insider threat awareness — arguably the most sensitive topic in security training.

*[Slide 1 — Defining the Insider Threat]*

An insider threat originates from individuals with authorized access to organizational systems. This includes employees, contractors, and vendors. Unlike external attackers who must defeat perimeter controls, insiders already have legitimate access. This makes detection significantly more difficult.

Insider threats fall into three categories: malicious — intentional data theft or sabotage; negligent — accidental policy violations or data exposure through carelessness; and compromised — a legitimate account taken over by an external attacker who exploits that insider's access.

*[Advance to Slide 2 — Behavioral Warning Signs]*

These behavioral indicators are drawn from CISA and CERT research into historical insider threat cases. They are not accusations — they are patterns that, in combination, warrant reporting to security leadership.

Accessing systems outside normal working hours without a documented business reason. Downloading or transferring large data volumes to personal storage. Expressing significant dissatisfaction with the organization while simultaneously increasing data access. Attempting to access resources outside their job function. And disabling or circumventing security tools on their workstation.

I want to be explicit: the presence of any one of these behaviors does not confirm malicious intent. The combination of multiple behaviors is what warrants attention and reporting.

*[Advance to Slide 3 — Protecting Sensitive Data]*

Your role in preventing insider threats is active. Access only the data your role requires. Lock your workstation whenever you step away — even for two minutes. Never copy sensitive data to personal devices or unauthorized cloud services. Properly dispose of sensitive information — shred physical documents, securely delete digital files.

And report behavior that raises concern through the designated confidential channel. You are not required to investigate or confront — only to report.

*[Advance to Slide 4 — Your Responsibility]*

The distinction I want to draw here: reporting a security concern is a professional responsibility, not a personal accusation. You are reporting an observed behavior pattern to people equipped to assess it — not making a judgment about a colleague's character.

Report through proper channels. Do not confront directly. Document specific behaviors with timestamps. And know that all reports are treated as confidential, and that organizational policy prohibits retaliation against good-faith reporters.

*[Click answer C on the quiz]*

Sharing credentials is prohibited without exception — regardless of the colleague's tenure, the urgency of the situation, or the apparent legitimacy of the request. The correct response is to decline and direct them to IT to unlock their account through proper channels. An emergency is not justification for bypassing security controls."

---

## Closing Statement (30 seconds)

---

"That concludes the Security Awareness Training section of my GRC Command Center.

These four modules — phishing, password hygiene, incident reporting, and insider threat — represent the core of NIST AT-2 security awareness training requirements, ISO 27001 Annex A control 6.3, and SOC 2 Common Criteria CC1.

The full portfolio, including all control libraries, risk registers, incident logs, and this training content, is available at github.com/binette87/cybersecurity-portfolio.

Thank you."

---

*Total runtime estimate: 20–25 minutes*  
*Recommended recording tool: Loom (loom.com) — free, records screen + face camera, auto-uploads*
