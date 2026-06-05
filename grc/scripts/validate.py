import pandas as pd, sys

checks = [
    ("grc/frameworks/nist-800-53/control-library.csv", ["Control_ID","Implementation_Status"]),
    ("grc/frameworks/iso-27001/control-library.csv",   ["Control_ID","Implementation_Status"]),
    ("grc/frameworks/soc2/control-library.csv",        ["Criteria_ID","Implementation_Status"]),
    ("grc/risk-register/risk-register.csv",            ["Risk_ID","Risk_Level","Status"]),
    ("grc/incident-log/incident-log.csv",              ["Incident_ID","Severity","Status"]),
    ("grc/remediation/remediation-tracker.csv",        ["Remediation_ID","Status","Percent_Complete"]),
    ("grc/audits/audit-schedule.csv",                  ["Audit_ID","Status"]),
]

errors = []
for path, cols in checks:
    try:
        df = pd.read_csv(path)
        missing = [c for c in cols if c not in df.columns]
        if missing:
            errors.append(f"FAIL {path}: missing columns {missing}")
        else:
            print(f"OK   {path} ({len(df)} rows)")
    except Exception as e:
        errors.append(f"FAIL {path}: {e}")

if errors:
    for e in errors:
        print(e)
    sys.exit(1)

print("All GRC data files valid.")
