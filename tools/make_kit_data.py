"""Generate the synthetic files that Bramblewick Events (a fictional
event-planning company in Portland, Oregon) uses throughout the course.

Everything here is made up: the company, its client, the venue, the vendors,
every person and every number. Some mistakes and traps are planted on
purpose, because the course catches them one domain at a time:

  - the venue's banquet capacity (380) is below the attendee count (400)
  - one caterer hides its cancellation fee on page 2
  - another caterer can't guarantee a nut-free kitchen
  - the 2025 price list is stale; the 2026 one is current
  - three people registered twice
  - day-1 survey comments complain about the lunch line, Room B has bad audio

Run:  uv run python tools/make_kit_data.py
"""

import csv
import random
from datetime import date, timedelta
from email.message import EmailMessage
from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path

from fpdf import FPDF

SEED = 3119
ROOT = Path(__file__).resolve().parent.parent / "bramblewick"
COMPANY = ROOT / "company"
SUMMIT = ROOT / "summit"
QUOTES = SUMMIT / "vendor-quotes"
INVOICES = SUMMIT / "vendor-invoices"
GMAIL = ROOT / "gmail-seed"

# The scenario's "now": six weeks before the summit.
NOW = date(2027, 2, 4)
DAY1 = date(2027, 3, 18)
DAY2 = date(2027, 3, 19)
ATTENDEES = 400

FIRST = ["Emma", "Liam", "Olivia", "Noah", "Ava", "James", "Sophia", "Lucas", "Mia",
         "Ethan", "Grace", "Daniel", "Chloe", "Ryan", "Hannah", "Marcus", "Ella",
         "Carlos", "Nora", "Owen", "Leah", "Tyler", "Julia", "Aaron", "Maya", "Caleb",
         "Zoe", "Isaac", "Lily", "Nathan", "Ruby", "Elijah", "Sadie", "Wyatt", "Ivy"]
LAST = ["Walker", "Brooks", "Hayes", "Turner", "Bennett", "Carter", "Reed", "Morgan",
        "Foster", "Ramirez", "Collins", "Parker", "Kim", "Sullivan", "Price", "Ward",
        "Lindqvist", "Okafor", "Delgado", "Nguyen", "Abbott", "Chen", "Hollis", "Vance"]
COMPANIES = ["Fernway Woodworks", "Tidewater Ceramics", "Copper Kettle Forge",
             "Northfold Textiles", "Ashgrove Leather", "Lantern Glass Studio",
             "Mossback Furniture", "Saltmarsh Soap Co.", "Ironbark Tools",
             "Pinecrest Print Shop", "Bluefen Pottery", "Kestrel Bikes",
             "Hollow Oak Candles", "Stonefield Knives", "Wrenfield Paper"]
DOMAINS = ["example.com", "example.net", "example.org"]


def phone(rng):
    # 555-01xx numbers are reserved for fiction, so none of these reach a real person.
    return f"(503) 555-01{rng.randint(0, 99):02d}"


def us(d):
    return d.strftime("%m/%d/%Y")


# ---------- PDF helper ----------

class Doc(FPDF):
    def __init__(self, header_text):
        super().__init__()
        self.header_text = header_text
        self.set_auto_page_break(True, margin=18)
        # A fixed date, so regenerating gives byte-identical files.
        self.set_creation_date(datetime(2027, 1, 15, tzinfo=timezone.utc))

    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(90, 90, 90)
        self.cell(0, 8, self.header_text, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Page {self.page_no()}", align="C")


def write_pdf(path, header_text, blocks):
    """blocks: list of (kind, text) with kind in h1, h2, p, small, pagebreak."""
    pdf = Doc(header_text)
    pdf.add_page()
    for kind, text in blocks:
        if kind == "pagebreak":
            pdf.add_page()
            continue
        size, style, gap = {"h1": (16, "B", 4), "h2": (12, "B", 2),
                            "p": (10.5, "", 2), "small": (7.5, "", 1)}[kind]
        pdf.set_font("Helvetica", style, size)
        pdf.multi_cell(0, size * 0.5, latin(text))
        pdf.ln(gap)
    path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(path))


def latin(s):
    return (s.replace("—", "-").replace("–", "-").replace("’", "'")
             .replace("“", '"').replace("”", '"').replace("•", "-"))


def md_to_blocks(md):
    blocks = []
    for para in md.strip().split("\n\n"):
        if para.startswith("# "):
            blocks.append(("h1", para[2:]))
        elif para.startswith("## "):
            blocks.append(("h2", para[3:]))
        else:
            blocks.append(("p", para))
    return blocks


def save_md_and_pdf(stem, header_text, md):
    stem.parent.mkdir(parents=True, exist_ok=True)
    stem.with_suffix(".md").write_text(md.strip() + "\n")
    write_pdf(stem.with_suffix(".pdf"), header_text, md_to_blocks(md))


# ---------- company documents ----------

BRAND_GUIDE = """
# Bramblewick Events: Brand and Tone Guide (v3, January 2027)

## Who we are
Bramblewick Events plans conferences, trade shows and community events across the Pacific Northwest. We are a team of 14 based in Portland, Oregon. Our promise to clients: "Every detail handled, nobody left out."

## Voice
Warm, plain and specific. We write like a helpful person, not a brochure. Short sentences. We use "we" and "you". We never use exclamation marks in client emails, and at most one in attendee emails.

## Words we use and avoid
Use: attendee (not "delegate"), session (not "breakout"), accessible (not "handicap"), dietary needs (not "special meals").
Avoid: "world-class", "seamless", "synergy", "game-changing", "cutting-edge".

## Formats
Client emails: a one-line purpose, then at most three short paragraphs, then the next step with a date. Attendee emails: subject line under 50 characters, the key fact in the first sentence. Dates are written as Thursday, March 18. Times as 9:30 AM. Prices always include whether tax and service are included.

## Sign-off
Client emails end with the planner's name and direct line. Attendee emails end with "The Bramblewick team" and the help address help@bramblewick.example.com.
"""

AI_POLICY = """
# Bramblewick Events: AI Use Policy (v2, effective January 6, 2027)

## 1. Approved tools
Staff may use Claude through the company Team plan only. Personal AI accounts must not be used for company or client work.

## 2. Data classes
Public: published schedules, marketing copy, venue addresses.
Internal: budgets, vendor quotes, internal plans.
Confidential: client contracts, pricing agreements, staff records.
Restricted: attendee personal data (names with contact details), dietary and medical needs, accessibility needs, payment details.

## 3. What may go into a prompt
Public and Internal data: yes. Confidential data: yes, inside a company Project, never in a chat shared outside the company. Restricted data: only after names, emails, phone numbers and other identifiers are removed or replaced with codes. Payment details: never.

## 4. Human review
A named person reviews before anything is sent or signed when it involves a contract or legal terms, money above $500, health, safety or accessibility, or anything published outside the company. Claude can draft these; it cannot be the final check.

## 5. Decisions about people
Claude may summarize or organize speaker applications, job applications or attendee requests. It must not be used to reject, rank or score people without a human making and recording the decision.

## 6. Connectors and Skills
Google Drive and Gmail connectors are approved for staff accounts. Any other connector, and any Skill from outside the company, needs approval from operations (Graham Pryce) before use.

## 7. Being open about AI
External communications drafted mostly by AI are reviewed and owned by a named staff member. We do not claim that AI-generated images are photographs of real events.

## 8. Questions and incidents
If something sensitive was shared by mistake, tell operations the same day. Nobody gets in trouble for reporting.
"""

PRICE_2025 = """
# Bramblewick Events: Service Price List 2025

## Planning fees
Event planning fee: $18 per attendee (minimum $4,000).
On-site coordinator: $850 per day.
AV coordinator: $950 per day.
Registration desk staff: $38 per hour per person.

## Notes
Prices exclude tax. Valid January 1 to December 31, 2025.
"""

PRICE_2026 = """
# Bramblewick Events: Service Price List 2026-2027

## Planning fees
Event planning fee: $21 per attendee (minimum $4,500).
On-site coordinator: $900 per day.
AV coordinator: $1,100 per day.
Registration desk staff: $42 per hour per person.

## Notes
Prices exclude tax. Valid January 1, 2026 to June 30, 2027. Replaces the 2025 list.
"""

CLIENT_BRIEF = f"""
# Client brief: Cascade Makers Summit 2027

## Client
Cascade Makers Guild, a nonprofit for small makers and craft manufacturers in Oregon and Washington. Contact: Rachel Ostrander, Executive Director, (503) 555-0142.

## Event
Two days, {DAY1.strftime('%A, %B %d')} and {DAY2.strftime('%A, %B %d, %Y')}, at Alder Point Hall, Portland. 400 attendees: makers, exhibitors, speakers and students. Day 1 ends with a dinner for all attendees.

## What the client asked for
Book catering for two lunches and the dinner. A welcome email to attendees. A run-of-show for both days. Accessibility handled properly, because last year a wheelchair user could not reach the exhibitor hall. A short report after the event that the board can read in five minutes.

## Budget
Total event budget $148,000, set by the Guild's board. Venue and AV are already agreed (see the venue contract).
"""

KICKOFF_THREAD = """
From: Rachel Ostrander <rachel@cascademakers.example.org>
To: Bramblewick planning <plan@bramblewick.example.com>
Date: Mon, 01 Feb 2027 08:12
Subject: Re: Re: Summit - next steps??

Hi all, sorry this is late. Board met Friday. They LOVED last year's speakers but the lunch line was a disaster, people missed the 1pm session. Can we fix that. Also budget is 148k total not 140k like I said before. Oh and Theo wants a "chatbot" for attendee questions?? not sure what that means, can you advise. The dinner has to be for everyone this time, last year only half fit.

Also we need to send the welcome email by Feb 15 latest. And someone asked about vegan + nut allergy options, we had complaints. Sorry for the essay.
Rachel

> From: Tessa Morrow <tessa@bramblewick.example.com>
> Date: Thu, 28 Jan 2027 16:40
> Hi Rachel, quick check-in before your board meeting. Do you have final numbers? We're holding Alder Point Hall for March 18-19 and need the catering decision by Feb 12 to keep the dates.
> Tessa

>> From: Rachel Ostrander
>> Date: Tue, 19 Jan 2027 10:03
>> We're thinking 400 people this year, maybe a few more. Budget around 140k. Will confirm after the board.
"""


def make_company():
    save_md_and_pdf(COMPANY / "brand-and-tone-guide", "Bramblewick Events", BRAND_GUIDE)
    save_md_and_pdf(COMPANY / "ai-use-policy", "Bramblewick Events - Internal", AI_POLICY)
    save_md_and_pdf(COMPANY / "price-list-2025", "Bramblewick Events", PRICE_2025)
    save_md_and_pdf(COMPANY / "price-list-2026", "Bramblewick Events", PRICE_2026)


def make_venue_contract():
    rental, av = 41_200, 7_400
    subtotal = rental + av
    deposit = round(subtotal * 0.30)
    blocks = [
        ("h1", "Alder Point Hall - Event Space Agreement"),
        ("p", f"Agreement No. APH-2027-0318. Client: Bramblewick Events on behalf of Cascade Makers Guild. "
              f"Event dates: {us(DAY1)} and {us(DAY2)}. Signed {us(date(2027, 1, 11))}."),
        ("h2", "Section 1. Spaces"),
        ("p", "Main Hall (theater seating up to 450; banquet seating up to 380). Exhibitor Hall (60 tables). "
              "Room A (120 seats). Room B (90 seats)."),
        ("h2", "Section 2. Fees"),
        ("p", f"Space rental for two days: ${rental:,}. AV package (main hall and two rooms): ${av:,}. "
              f"Subtotal: ${subtotal:,}. Oregon has no sales tax. A 5% venue service fee is added to the final invoice."),
        ("h2", "Section 3. Deposit"),
        ("p", f"A deposit of 30% of the subtotal is due at signing. The balance is due 14 days before the first event day."),
        ("h2", "Section 4. Accessibility"),
        ("p", "All public spaces are step-free. The Exhibitor Hall is reached by the north ramp or the service lift; "
              "the lift must be booked in advance for event use. Two wheelchair spaces per 50 theater seats are provided on request."),
        ("h2", "Section 5. Catering"),
        ("p", "Outside caterers are permitted if listed on the venue's approved list, which includes Juniper Table Catering, "
              "Ridgeline Provisions and Harvest & Hearth."),
        ("pagebreak", ""),
        ("h2", "Section 6. Insurance"),
        ("p", "The client provides proof of event liability insurance of at least $1,000,000 no later than 30 days before the event."),
        ("h2", "Section 7. Cancellation"),
        ("p", "7.1 Notice of cancellation must be given in writing. "
              "7.2 Cancellation charges: more than 90 days before the event, 25% of the subtotal; "
              "30 to 90 days before, 50%; fewer than 30 days before, 100%. "
              "7.3 The deposit counts toward any cancellation charge."),
        ("h2", "Section 8. Signatures"),
        ("p", "For Alder Point Hall: Simone Achterberg, Events Manager. For Bramblewick Events: Dana Whitlock, CEO."),
    ]
    write_pdf(SUMMIT / "venue-contract.pdf", "Alder Point Hall", blocks)
    return deposit


def make_quotes():
    guests = ATTENDEES
    quotes = {
        "juniper-table-catering": [
            ("h1", "Juniper Table Catering - Quote Q-2207"),
            ("p", f"Prepared for Bramblewick Events, Cascade Makers Summit, {us(DAY1)}-{us(DAY2)}. Guests: {guests}."),
            ("h2", "Package"),
            ("p", "Two buffet lunches and one plated dinner. $142 per guest for the full package. "
                  "Includes vegetarian, vegan and gluten-free options at no extra cost. Nut-free meals prepared in a separate area."),
            ("h2", "Service"),
            ("p", "Service charge 22% on food and beverage. Six serving stations for lunch, about 15 minutes to serve 400 guests."),
            ("h2", "Minimums and deposit"),
            ("p", "Minimum guarantee: 360 guests. Deposit: 25% to confirm."),
            ("pagebreak", ""),
            ("h2", "Terms"),
            ("small", "Final numbers are due 10 days before the event. A cancellation fee of 50% of the estimated total applies "
                      "to cancellations made within 21 days of the event. Prices valid until 02/28/2027."),
        ],
        "ridgeline-provisions": [
            ("h1", "Ridgeline Provisions - Proposal"),
            ("p", f"Event: Cascade Makers Summit. Guests: {guests}."),
            ("h2", "Menu package"),
            ("p", "Two lunches (boxed) and one buffet dinner: $129 per guest. Vegan and gluten-free meals add $8 each. "
                  "Service charge 20%. Boxed lunches pick up from four tables."),
            ("h2", "Deposit and cancellation"),
            ("p", "Deposit 40%, non-refundable. Balance due on the first event day."),
        ],
        "harvest-and-hearth": [
            ("h1", "Harvest & Hearth - Catering Estimate"),
            ("p", f"For: Bramblewick Events. Dates: {us(DAY1)} and {us(DAY2)}. Guests: {guests}."),
            ("h2", "Pricing"),
            ("p", "$136 per guest, service included. Two plated lunches, one family-style dinner."),
            ("h2", "Dietary"),
            ("p", "Vegetarian and vegan on request. Our kitchen handles tree nuts and peanuts; we cannot guarantee nut-free meals."),
            ("h2", "Minimum and cancellation"),
            ("p", "Minimum 380 guests. Full refund for cancellations more than 30 days out."),
        ],
    }
    for stem, blocks in quotes.items():
        write_pdf(QUOTES / f"{stem}.pdf", stem.replace("-", " ").title(), blocks)


def make_attendees(rng):
    rows, seen = [], set()
    types = ["General"] * 70 + ["Exhibitor"] * 15 + ["Speaker"] * 5 + ["Student"] * 10
    dietary = [""] * 66 + ["vegetarian"] * 14 + ["vegan"] * 8 + ["gluten-free"] * 6 + \
              ["nut allergy"] * 4 + ["shellfish allergy"] * 2
    access = [""] * 92 + ["wheelchair access"] * 3 + ["ASL interpreter"] * 1 + \
             ["hearing loop"] * 2 + ["reserved front seating"] * 2
    while len(rows) < ATTENDEES - 3:
        first, last = rng.choice(FIRST), rng.choice(LAST)
        if (first, last) in seen:
            continue
        seen.add((first, last))
        rows.append({
            "reg_id": f"R{1000 + len(rows)}",
            "first_name": first,
            "last_name": last,
            "email": f"{first.lower()}.{last.lower()}@{rng.choice(DOMAINS)}",
            "phone": phone(rng),
            "company": rng.choice(COMPANIES),
            "ticket_type": rng.choice(types),
            "dietary_needs": rng.choice(dietary),
            "accessibility_needs": rng.choice(access),
            "registered_on": us(NOW - timedelta(days=rng.randint(3, 80))),
        })
    # Planted mess: three people registered twice, with small differences.
    for i in (12, 57, 203):
        dup = dict(rows[i])
        dup["reg_id"] = f"R{1000 + len(rows)}"
        dup["email"] = dup["email"].upper() if i == 12 else dup["email"]
        dup["first_name"] = dup["first_name"] + " " if i == 57 else dup["first_name"]
        dup["registered_on"] = us(NOW - timedelta(days=1))
        rows.append(dup)
    write_csv(SUMMIT / "attendees.csv", rows)
    return rows


def make_speakers(rng):
    topics = ["pricing your work", "selling at markets", "wholesale for beginners",
              "photographing products", "shipping fragile goods", "hiring your first helper",
              "sustainable materials", "running a workshop", "custom orders", "online shops"]
    regions = ["Portland", "Seattle", "Eugene", "Bend", "Spokane", "Salem", "Tacoma", "rural Oregon"]
    rows = []
    for i in range(36):
        name = f"{rng.choice(FIRST)} {rng.choice(LAST)}"
        topic = rng.choice(topics)
        rows.append({
            "app_id": f"S{201 + i}",
            "name": name,
            "talk_title": f"{topic.capitalize()}: what I learned the hard way",
            "topic": topic,
            "years_making": rng.randint(1, 30),
            "spoke_before": rng.choice(["yes", "no", "no"]),
            "region": rng.choice(regions),
        })
    write_csv(SUMMIT / "speaker-applications.csv", rows)


def make_survey(rng):
    sessions = ["Opening keynote", "Pricing panel", "Room A: Wholesale", "Room B: Photography",
                "Room A: Shipping", "Closing talk"]
    good = ["Loved the keynote.", "Great speakers again.", "Met three new stockists.",
            "Exhibitor hall was easy to get around.", "Dinner was lovely.", ""]
    day1_lunch = ["The lunch line was far too long, I missed the start of the 1 PM session.",
                  "Waited 25 minutes for lunch on Thursday.", "Lunch queue on day 1 was chaotic."]
    room_b = ["Couldn't hear the speaker in Room B.", "Room B microphone kept cutting out.",
              "Audio in Room B was bad."]
    rows = []
    for i in range(312):
        r = {"response_id": f"A-{i + 1:03d}", "ticket_type": rng.choice(
            ["General"] * 7 + ["Exhibitor", "Student", "Speaker"])}
        for s in sessions:
            base = 4.2 if "Room B" not in s else 3.1
            r[s] = max(1, min(5, round(rng.gauss(base, 0.8))))
        r["nps_0_10"] = max(0, min(10, round(rng.gauss(8.1, 1.7))))
        r["would_return"] = "yes" if r["nps_0_10"] >= 7 or rng.random() < 0.3 else "no"
        roll = rng.random()
        r["comment"] = (rng.choice(day1_lunch) if roll < 0.18 else
                        rng.choice(room_b) if roll < 0.30 else rng.choice(good))
        rows.append(r)
    write_csv(SUMMIT / "survey-responses.csv", rows)


def make_invoices(rng):
    # Deliberately messy names, the kind that pile up in a shared folder.
    items = [
        ("INV_0347 final(2).pdf", "Juniper Table Catering", "Deposit, Q-2207 (25% of $69,296)", 17_324),
        ("scan0012.pdf", "Alder Point Hall", "Deposit, APH-2027-0318", 14_580),
        ("Lumen Rig AV - invoice.pdf", "Lumen Rig AV", "Microphones and Room B speakers", 2_340),
        ("receipt (1).pdf", "Fernway Signs", "Wayfinding signs, 24 pieces", 1_180),
        ("IMG_4471.pdf", "Portland Badge Print", "Name badges, 420", 610),
        ("Copy of lanyards inv.pdf", "Portland Badge Print", "Lanyards, 420", 395),
        ("Ridgeline_proposal_OLD.pdf", "Ridgeline Provisions", "Tasting fee", 150),
        ("interp-booking.pdf", "Northwest ASL Partners", "ASL interpreter, 2 days", 1_920),
        ("invoice-march.pdf", "Cascade Rentals", "Exhibitor tables, 60", 1_500),
        ("scan0013.pdf", "Cascade Rentals", "Extra chairs, 40", 240),
        ("hearing loop hire.pdf", "Lumen Rig AV", "Portable hearing loop, Main Hall", 480),
        ("photog_quote_v3.pdf", "Mira Okafor Photography", "Event photography, 2 days", 2_800),
    ]
    for name, vendor, what, amount in items:
        write_pdf(INVOICES / name, vendor, [
            ("h1", f"{vendor} - Invoice"),
            ("p", f"Invoice number: {rng.randint(1000, 9999)}. Date: {us(NOW - timedelta(days=rng.randint(1, 30)))}."),
            ("p", f"Bill to: Bramblewick Events. Item: {what}. Amount due: ${amount:,}."),
            ("p", "Payment terms: net 30."),
        ])


def make_gmail_seed():
    """.eml files to load into the demo Google account's Gmail."""
    GMAIL.mkdir(parents=True, exist_ok=True)
    mails = [
        ("rachel@cascademakers.example.org", "Re: Re: Summit - next steps??",
         datetime(2027, 2, 1, 8, 12), KICKOFF_THREAD.split("\n\n", 1)[1]),
        ("events@juniper-table.example.com", "Quote Q-2207 - any questions?",
         datetime(2027, 2, 2, 11, 5),
         "Hi Tessa,\n\nJust checking you received our quote Q-2207. We can hold March 18-19 until Feb 12. "
         "Happy to walk through the menu or the terms.\n\nBest,\nCole Bastien\nJuniper Table Catering"),
        ("simone@alderpointhall.example.com", "Insurance certificate reminder",
         datetime(2027, 2, 3, 9, 40),
         "Hello Bramblewick team,\n\nA reminder that proof of event liability insurance is due 30 days before "
         "the event (Section 6). Also, if you need the service lift for the Exhibitor Hall, please book it now.\n\n"
         "Simone Achterberg\nEvents Manager, Alder Point Hall"),
        ("graham@bramblewick.example.com", "Before we use Claude on the summit",
         datetime(2027, 2, 3, 15, 22),
         "Team,\n\nI keep hearing Claude will 'run' the summit. It won't. Before anyone uploads the attendee list, "
         "read section 3 of the AI policy. And I want to see real numbers on time saved before we roll this out "
         "to the other events.\n\nGraham"),
        ("hello@lumenrig.example.com", "Room B audio fix",
         datetime(2027, 2, 3, 17, 2),
         "Hi,\n\nWe've added two extra speakers for Room B after last year's feedback. Invoice attached separately. "
         "Hearing loop for the Main Hall is booked.\n\nPriya Halvorsen\nLumen Rig AV"),
    ]
    for i, (frm, subj, when, body) in enumerate(mails, 1):
        m = EmailMessage()
        m["From"] = frm
        m["To"] = "bramblewick.demo@example.com"  # replaced with the demo account's address on load
        m["Subject"] = subj
        m["Date"] = format_datetime(when.replace(tzinfo=timezone.utc))
        m.set_content(body)
        (GMAIL / f"{i:02d}-{subj.lower().replace(' ', '-').replace('?', '').replace(':', '')[:40]}.eml"
         ).write_bytes(bytes(m))


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main():
    rng = random.Random(SEED)
    make_company()
    SUMMIT.mkdir(parents=True, exist_ok=True)
    (SUMMIT / "client-brief.md").write_text(CLIENT_BRIEF.strip() + "\n")
    write_pdf(SUMMIT / "client-brief.pdf", "Cascade Makers Guild", md_to_blocks(CLIENT_BRIEF))
    (SUMMIT / "kickoff-email-thread.txt").write_text(KICKOFF_THREAD.strip() + "\n")
    deposit = make_venue_contract()
    make_quotes()
    make_attendees(rng)
    make_speakers(rng)
    make_survey(rng)
    make_invoices(rng)
    make_gmail_seed()
    print(f"Wrote {ROOT} (venue deposit ${deposit:,})")


if __name__ == "__main__":
    main()
