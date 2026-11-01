"""Replace attendee identifiers with codes before the list goes anywhere near a prompt (AI policy, section 3).

Names, emails, phones, companies and reg ids are dropped. Each person gets a code from their email
(lower-cased), so someone who registered twice keeps the same code and duplicates can still be found.

usage: python3 tools/anonymize_attendees.py  ->  bramblewick/summit/attendees-anonymized.csv
"""
import csv
from collections import Counter
from pathlib import Path

SUMMIT = Path(__file__).resolve().parent.parent / "bramblewick" / "summit"
KEEP = ["ticket_type", "dietary_needs", "accessibility_needs", "registered_on"]

rows = list(csv.DictReader(open(SUMMIT / "attendees.csv")))
codes = {}
out = []
for r in rows:
    key = r["email"].strip().lower()
    codes.setdefault(key, f"A{len(codes) + 1:03d}")
    out.append({"attendee_code": codes[key], **{k: r[k] for k in KEEP}})

with open(SUMMIT / "attendees-anonymized.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["attendee_code", *KEEP])
    w.writeheader()
    w.writerows(out)

people = {r["attendee_code"]: r for r in out}
print(f"{len(out)} rows, {len(people)} people")
print("dietary:", dict(Counter(p["dietary_needs"] or "none" for p in people.values())))
print("access:", dict(Counter(p["accessibility_needs"] or "none" for p in people.values())))
print("tickets:", dict(Counter(p["ticket_type"] for p in people.values())))
