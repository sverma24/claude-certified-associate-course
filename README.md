# Claude Certified Associate Course: Course Kit

The files used in the free **Claude Certified Associate Foundations Full Course** on YouTube. Every demo in the course runs on these files, so you can repeat each one in your own Claude account.

> **Bramblewick Events is a fictional company.** So are its client (Cascade Makers Guild), the venue (Alder Point Hall), every vendor and every person. All data is synthetic, made by `tools/make_kit_data.py`. Emails use reserved `example.com/.net/.org` domains, and phone numbers use the 555-01xx range kept for fiction.

## What's inside

| Folder | What it is | Used in |
|---|---|---|
| `bramblewick/company/` | the brand and tone guide, the AI use policy, and two price lists (one of them out of date) | Projects, instructions, governance, keeping knowledge current |
| `bramblewick/summit/` | the client brief, a messy kickoff email thread, the venue contract, three catering quotes, the attendee list, speaker applications, the post-event survey, and a folder of badly named invoices | every domain, and the capstone |
| `bramblewick/gmail-seed/` | the same emails as `.eml` files, for loading into a test Gmail account if you want to try connectors | connectors |
| `tools/` | the script that makes all of the above | |

The prompt library, Project instruction and Skill templates, the "Your turn" tasks with answers, the checklists and the cheat sheets are added as the course is built.

## Use it

You need a Claude account. Some features in the course (Research, Cowork, chat search) need a paid plan; the course says which, chapter by chapter.

To make the files again (optional, they're already here):

```bash
uv sync
uv run python tools/make_kit_data.py
```

**Don't put real personal data into the exercises.** The attendee list is fake on purpose, so you can practise anonymizing it safely.
