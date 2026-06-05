import pandas as pd, os, sys

nist = pd.read_csv("grc/frameworks/nist-800-53/control-library.csv")
iso  = pd.read_csv("grc/frameworks/iso-27001/control-library.csv")
soc2 = pd.read_csv("grc/frameworks/soc2/control-library.csv")
risk = pd.read_csv("grc/risk-register/risk-register.csv")
rem  = pd.read_csv("grc/remediation/remediation-tracker.csv")
inc  = pd.read_csv("grc/incident-log/incident-log.csv")

def score(df, col):
    impl    = int(df[col].str.lower().str.contains("implemented", na=False).sum())
    partial = int(df[col].str.lower().str.contains("partial", na=False).sum())
    total   = len(df)
    pct     = round((impl + partial * 0.5) / total * 100, 1) if total else 0
    return impl, partial, total, pct

ni, np_, nt, ns  = score(nist, "Implementation_Status")
ii, ip,  it, is_ = score(iso,  "Implementation_Status")
si, sp,  st, ss  = score(soc2, "Implementation_Status")

open_risks = int(risk["Status"].str.lower().str.contains("open", na=False).sum())
open_rem   = int((~rem["Status"].str.lower().str.contains("completed", na=False)).sum())
open_inc   = int(inc["Status"].str.lower().str.contains("open", na=False).sum())

print(f"NIST {ns}%  |  ISO {is_}%  |  SOC2 {ss}%")
print(f"Open risks: {open_risks}  |  Open remediations: {open_rem}  |  Open incidents: {open_inc}")

out = os.environ.get("GITHUB_OUTPUT")
if out:
    with open(out, "a") as f:
        f.write(f"nist={ns}\niso={is_}\nsoc2={ss}\n")
        f.write(f"risks={open_risks}\nrem={open_rem}\ninc={open_inc}\n")
        f.write(f"ni={ni}\nnp={np_}\nnt={nt}\n")
        f.write(f"ii={ii}\nip={ip}\nit={it}\n")
        f.write(f"si={si}\nsp={sp}\nst={st}\n")
