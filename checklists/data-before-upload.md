# Before data goes into a prompt (Domain 6, objective 6.2)

## 1. Classify
| Class (Bramblewick policy) | Examples | Into a prompt? |
|---|---|---|
| Public | published schedule, venue address | yes |
| Internal | budgets, vendor quotes | yes |
| Confidential | client contracts, pricing agreements | yes, inside a company project, never in a chat shared outside |
| Restricted | attendee names with contact details, dietary and medical needs, accessibility needs, payment details | only after identifiers are removed; payment details never |

## 2. Minimize
- [ ] Keep only the columns the task needs. A seating plan needs ticket type and access needs, not dietary needs or emails.

## 3. Anonymize
- [ ] Remove names, emails, phone numbers, company names and IDs.
- [ ] Give each person a code. Base the code on something stable (like the email), so duplicates keep the same code. `tools/anonymize_attendees.py` does this for the course's attendee list.

## Not protection
- Telling Claude "don't keep this". The data has already been shared.
- An incognito chat. It changes what's saved, not what's shared.

## If something was shared by mistake
- [ ] Tell the named contact the same day (Bramblewick policy, section 8), delete the chat, and anonymize from now on.
