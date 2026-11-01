# Claude Certified Associate Course: Course Kit

The files used in the free **Claude Certified Associate Foundations Full Course** on YouTube. Every demo in the course runs on these files, so you can repeat each one in your own Claude account.

> **Bramblewick Events is a fictional company.** So are its client (Cascade Makers Guild), the venue (Alder Point Hall), every vendor and every person. All data is synthetic, made by `tools/make_kit_data.py`. Emails use reserved `example.com/.net/.org` domains, and phone numbers use the 555-01xx range kept for fiction.

## What's inside

| Folder | What it is | Used in |
|---|---|---|
| `bramblewick/company/` | the brand and tone guide, the AI use policy, and two price lists (one of them out of date) | Projects, instructions, governance, keeping knowledge current |
| `bramblewick/summit/` | the client brief, a messy kickoff email thread, the venue contract, three catering quotes, the attendee list, speaker applications, the post-event survey, and a folder of badly named invoices | every domain, and the capstone |
| `bramblewick/gmail-seed/` | the same emails as `.eml` files, for loading into a test Gmail account if you want to try connectors | connectors |
| `prompts/` | every prompt from the real Claude runs in the course, word for word, by chapter, with how each was set up | every chapter with a demo |
| `templates/` | the project instructions and the proposal Skill used on camera, plus a checklist for writing your own | Domains 5 and 7 |
| `your-turn/` | all 46 "Your turn" tasks with hints and worked answers | every chapter |
| `checklists/` | the self-check, plus checklists for accuracy, review levels, keeping knowledge current, stakeholder briefs, data before upload, and troubleshooting | 1.4, Domains 2 and 4–7 |
| `cheat-sheets/` | one page per part or domain (Markdown and PDF): every chapter's takeaway and common mistakes | revision before the exam |
| `GLOSSARY.md` | every term defined on screen, with the chapter that introduces it | |
| `tools/` | `make_kit_data.py` makes the Bramblewick files; `anonymize_attendees.py` makes `attendees-anonymized.csv` (Domain 6) | |

The prompt library, your-turn answers, glossary and cheat sheets are generated from the course's own runs and scripts, so they match the video word for word.

## Use it

You need a Claude account. Some features in the course (Research, Cowork, chat search) need a paid plan; the course says which, chapter by chapter.

To make the files again (optional, they're already here):

```bash
uv sync
uv run python tools/make_kit_data.py
uv run python tools/anonymize_attendees.py
```

**Don't put real personal data into the exercises.** The attendee list is fake on purpose, so you can practise anonymizing it safely.
