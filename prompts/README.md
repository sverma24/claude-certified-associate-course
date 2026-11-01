# Prompt library
Every prompt from the real Claude runs shown in the course, word for word, grouped by chapter. Most ran inside a Claude project holding the kit files, with account memory switched off. The 'Where' line says how each one was set up, so you can repeat it. Your replies will differ: the same prompt gives different wording each time.

## F1 · What a language model really does

### f1-a
*Where:* claude.ai web, incognito

> Suggest a name and a one-line tagline for a two-day conference for small makers and craft businesses in Portland, Oregon.

### f1-b
*Where:* claude.ai web, incognito

> Suggest a name and a one-line tagline for a two-day conference for small makers and craft businesses in Portland, Oregon.

### f1-c
*Where:* claude.ai web, incognito

> Suggest a name and a one-line tagline for a two-day conference for small makers and craft businesses in Portland, Oregon.

## F2 · Tokens and the context window

### f2-thread
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off, 6 text knowledge files

**Turn 1**
> I'm planning a conference for 400 people. Keep this in mind for everything we do today: the total budget is $148,000, and that's a hard cap.

**Turn 2**
> Give me five ideas for keeping a lunch line short for 400 people.

**Turn 3**
> Write a two-sentence reminder email to a caterer asking for final menu options by Friday.

**Turn 4**
> What are three questions I should ask a venue about wheelchair access?

**Turn 5**
> Suggest a simple color scheme for name badges for four ticket types.

**Turn 6**
> Quick check: what's the budget cap I gave you at the start, and is it a soft or hard limit?

## F3 · Each chat starts blank, and what changes that

### f3-new
*Where:* claude.ai web, incognito (no project, no memory)

> When is the Cascade Makers Summit, and which venue is it at?

### f3-project
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off

> When is the Cascade Makers Summit, and which venue is it at?

## F4 · Why Claude sometimes makes things up

### f4-clause
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off

> What does the venue contract say about bringing in outside alcohol? Give me the clause number.

### f4-stat
*Where:* claude.ai web, incognito, default tools (web search on)

> What percentage of conference attendees skip lunch because the line is too long? Give me the figure and where it comes from.

## F5 · What Claude can know, and what it can't

### f5-deposit
*Where:* claude.ai web, incognito, default tools

> How much deposit do we still owe Alder Point Hall for our December event?

## F7 · The model family: Haiku, Sonnet and Opus

### f7-haiku
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off, Haiku 5.5 Medium

> Reply to this attendee in two sentences, in our brand voice: "Will there be vegan options at lunch, and can I get my plate without queuing in the main line? I use a wheelchair."

### f7-haiku-timed
*Where:* claude.ai web, project, account memory off, Haiku 5.5 Medium

> Reply to this attendee in two sentences, in our brand voice: "Will there be vegan options at lunch, and can I get my plate without queuing in the main line? I use a wheelchair."

### f7-opus
*Where:* claude.ai web, project, account memory off, Opus 5.5 High (its default effort)

> Reply to this attendee in two sentences, in our brand voice: "Will there be vegan options at lunch, and can I get my plate without queuing in the main line? I use a wheelchair."

### f7-sonnet
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> Reply to this attendee in two sentences, in our brand voice: "Will there be vegan options at lunch, and can I get my plate without queuing in the main line? I use a wheelchair."

## 1.1 · Writing prompts that carry what Claude needs

### d11-structured
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off

> I'm an operations associate at Bramblewick Events. Task: write one email to each of our three catering bidders for the Cascade Makers Summit (December 10–11, 400 guests): Juniper Table Catering, Ridgeline Provisions and Harvest & Hearth.
> Context: we must decide by November 6. Several attendees have nut allergies, and the dinner is for all 400 guests.
> Ask each caterer to confirm: final per-guest price including service, their cancellation terms, and whether they can guarantee nut-free meals.
> Audience: their events manager, who is busy. Tone: warm and plain, following our brand guide (no exclamation marks in client emails).
> Format: three short emails, each under 120 words, with a subject line.
> Done means: every email asks all three questions and states the November 6 deadline.

### d11-vague
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off

> write an email to the caterers

## 1.2 · Breaking a big job into steps

### d12-chain
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off

**Turn 1**
> We need to get the Cascade Makers Summit catering decided. Before doing anything, break this job into the steps you'd take, in order, and say what each step needs from me. Don't do the steps yet.

**Turn 2**
> Do step 1 only.

**Turn 3**
> Answers: 400 registrations, but 3 are duplicates, so 397 people. About 10 staff and volunteers eat too. Plan for 380 to 410 meals, everyone both days.
> Dietary from registration: 52 vegetarian, 29 vegan, 21 gluten-free, 19 nut allergy, 6 shellfish allergy. Nut-free is a requirement, not a preference. 14 attendees use wheelchairs.
> Other costs so far are about $16,000 (staff, AV extras, ASL interpreters, rentals, badges and signs). No target share for catering. Now do step 2.

**Turn 4**
> Good. Now do steps 3 and 4, using what you found.

**Turn 5**
> Now give me a one-paragraph recommendation I could send to our operations director, with the reasons.

## 1.3 · Improving a result, one change at a time

### d13-iterate
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

**Turn 1**
> Draft the welcome email to attendees for the Cascade Makers Summit.

**Turn 2**
> Good start. Fill in the reply-by date as Friday, November 20, and leave everything else as it is.

**Turn 3**
> It's too long for a phone screen. Cut it to under 120 words without losing the access information.

**Turn 4**
> Last change: make the subject line carry the key fact, the dates.

## 1.4 · Choosing the approach for the type of task

### d14-analysis
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> Analysis task: compare the three catering quotes in one table, with total cost for 400 guests including service, deposit, cancellation terms, nut-free, and minimum guests. Then list the two biggest risks you see.

### d14-brainstorm
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

**Turn 1**
> Brainstorming task: give me 10 session themes for the summit, as different from each other as you can make them. Don't rank or judge them yet, one line each.

**Turn 2**
> Now narrow down: pick the 3 strongest for an audience of small makers and craft businesses, and say in one line each why they beat the others.

### d14-drafting
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> Drafting task: write the two-paragraph introduction to the run-of-show document for our on-site team, covering what the document is for and how to use it on the day.

### d14-research
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium, web search on

> Research task: how fast can a buffet line serve guests at a conference lunch? I want a rough guests-per-minute figure per serving line, with sources I can check.

## 2.1 · Checking for accuracy and completeness

### d21-dinner
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> Is there anything in the venue contract that could be a problem for the Thursday dinner?

### d21-summary
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> Summarise the three catering quotes for Graham in five bullets.

## 2.2 · Spotting made-up facts, inconsistencies and bias

### d22-bias
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> Before we post this call for speakers, review it for bias or wording that would put people off, and suggest a fairer version: "We're looking for young, dynamic makers who are digital natives and can keep the energy high. Speakers must be native English speakers and able to stand for a 45-minute talk."

## 2.3 · Fact-checking and validation techniques

### d23-code
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium, code execution

> Use code to recalculate Juniper's total for 400 guests with the 22% service charge on top, the 25% deposit, and the 50% cancellation fee. Show the code and the results.

### d23-quote
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> Quote the exact sentence in Juniper's quote about cancellation, word for word, and tell me which section it's under.

## 2.4 · Deciding when a person must review

### d24-levels
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> Claude has drafted six things for me. Which need a person to review them before they go out, and why? 1) a reminder to our team about Friday's stand-up 2) changes to Juniper's catering contract 3) a social post announcing the summit dates 4) a reply to an attendee about their nut allergy 5) my own notes from today's planning meeting 6) the budget update to the Guild's board.

## 2.5 · Adapting and comparing outputs for the reader

### d25-audiences
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> We've chosen Juniper Table Catering, subject to written confirmation of the service charge. Write this news three ways: a three-line update for Graham, our operations director; a short email to Juniper's events manager; and two sentences for attendees.

## 2.6 · Choosing the right format: inline, artifact or structured data

### d26-artifact
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> Create the Day 1 run-of-show as a document we can keep editing and share with the team. Use placeholders for any times you don't know.

### d26-csv
*Where:* claude.ai web, project, account memory off, Sonnet 5.5 Medium

> Give me these dietary counts as CSV I can paste into a spreadsheet, with a column for the caterer's confirmation: 52 vegetarian, 29 vegan, 21 gluten-free, 19 nut allergy, 6 shellfish allergy. Nothing else in the reply.

## 3.1 · Choosing the right feature for the job

### d31-picks
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off, Sonnet 5.5 Medium

> I have six jobs today. For each one, tell me which Claude feature fits best (a plain chat, this Project, web search, Research, an artifact, code execution, a Skill, or Cowork), and give the reason in one line. 1) Check whether any big Portland events on December 10-11 could push up hotel prices for our attendees. 2) A full comparison of five possible venues for next year's summit, with sources. 3) The run-of-show the team will keep editing all week. 4) Average satisfaction scores per session from last year's 312-row survey CSV. 5) Reword one sentence in an email. 6) Rename and sort a folder of 12 badly named invoice PDFs on my computer.

### d31-websearch
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off, Sonnet 5.5 Medium, web search

> Are there any big events in Portland on December 10-11, 2026 that could push up hotel prices for our summit attendees? Search the web, keep it short, and give me sources I can check.

## 3.3 · Matching the model to the task

### d33-haiku-contract
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off, Haiku 5.5 Medium

> Review the venue contract for risks to our plan: 400 attendees, a dinner for everyone on Day 1, several wheelchair users, and exhibitors in the Exhibitor Hall. Today is Monday, November 2, 2026. List the risks with the section number, most serious first, and say what we should do about each. Keep it brief.

### d33-haiku-replies
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off, Haiku 5.5 Medium

> Write a short, friendly reply (two sentences at most) to each of these 8 attendee questions about the Cascade Makers Summit. Use only facts from the project files. If a fact isn't there, say we'll confirm and get back to them. 1) What are the dates? 2) Is the venue wheelchair accessible? 3) Is there a vegan lunch? 4) I have a nut allergy. Can I bring my own food? 5) Is there parking at the venue? 6) Is the dinner for everyone? 7) Will the sessions be recorded? 8) Is there a hearing loop?

### d33-opus-contract
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off, Opus 5.5 High

> Review the venue contract for risks to our plan: 400 attendees, a dinner for everyone on Day 1, several wheelchair users, and exhibitors in the Exhibitor Hall. Today is Monday, November 2, 2026. List the risks with the section number, most serious first, and say what we should do about each. Keep it brief.

## 3.4 · Context limits and memory: restart, summarize or persist

### d34-fresh
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off, Sonnet 5.5 Medium; a new chat seeded with the d34-handoff summary (newlines flattened, bold marks removed)

> Here is a handoff summary from an earlier chat: Cascade Makers Summit catering handoff (Thursday, December 10 and Friday, December 11) Decisions: Harvest & Hearth is out (it cannot guarantee nut-free, which is required). I recommended Juniper Table Catering, pending written confirmation. No one has approved it yet, and nothing has been sent to caterers. Numbers: 397 people plus about 10 staff; plan 380 to 410 meals (three each). 52 vegetarian, 29 vegan, 21 gluten-free, 19 nut allergy, 6 shellfish; 14 wheelchair users. Budget $148,000; venue $51,030 including fee; other costs $16,000; catering ceiling $80,970 ($73,570 with 5% contingency, $66,170 with 10%). At 407 meals: Juniper $70,509 with 22% service on top, or $57,794 if included; Ridgeline $64,444, with a 40% non-refundable deposit. Open: Is Juniper's 22% on top? Also its nut-free handling, shellfish-free meals, deposit refund and wheelchair service. Does Ridgeline offer nut-free? Contingency level; whether insurance and Bramblewick's fee come from the $148,000; registration close date. Next: Approve sending Juniper and Ridgeline the clarifying questions (drafted, not sent), then get the director's go-ahead (I suggested Friday, November 6). Juniper's prices expire Monday, November 30. Carry on from here: draft the clarifying email to Juniper Table Catering, under 150 words.

### d34-handoff
*Where:* claude.ai web, project 'Bramblewick Events (pilot)', account memory off, Sonnet 5.5 Medium; turns 1-5 are the pilot d12-chain run, turn 6 added 2026-10-31 in batch 4

**Turn 1**
> We need to get the Cascade Makers Summit catering decided. Before doing anything, break this job into the steps you'd take, in order, and say what each step needs from me. Don't do the steps yet.

**Turn 2**
> Do step 1 only.

**Turn 3**
> Answers: 400 registrations, but 3 are duplicates, so 397 people. About 10 staff and volunteers eat too. Plan for 380 to 410 meals, everyone both days.
> Dietary from registration: 52 vegetarian, 29 vegan, 21 gluten-free, 19 nut allergy, 6 shellfish allergy. Nut-free is a requirement, not a preference. 14 attendees use wheelchairs.
> Other costs so far are about $16,000 (staff, AV extras, ASL interpreters, rentals, badges and signs). No target share for catering. Now do step 2.

**Turn 4**
> Good. Now do steps 3 and 4, using what you found.

**Turn 5**
> Now give me a one-paragraph recommendation I could send to our operations director, with the reasons.

**Turn 6**
> This chat has got long, and I want to carry on in a fresh one. Write a handoff summary I can paste into a new chat: the decisions so far, the key numbers, the open questions, and the next step. Under 200 words, and only things we actually agreed or found here.

## 5.1 · Setting up a project from zero

### d51-first
*Where:* claude.ai web, NEW project 'Bramblewick Events' with instructions + 5 PDFs, account memory off, Sonnet 5.5 Medium

> What do we still owe Alder Point Hall, and when is it due?

## 5.2 · Uploaded files or connected apps

### d52-connectors
*Where:* claude.ai web, project 'Bramblewick Events', Gmail + Google Drive connectors (a demo Google account), account memory off, Sonnet 5.5 Medium

**Turn 1**
> Check our Gmail for anything from the venue, the caterers or other suppliers in the last week that needs action from us. List each item with what we have to do and by when.

**Turn 2**
> The quote is in our Google Drive, in Bramblewick Events > Cascade Makers Summit > Vendor quotes. Read Juniper's quote and give me the total for 400 guests, the deposit, and the cancellation terms.

## 5.3 · Instructions that work, and where Skills fit

### d53-skill-proposal
*Where:* claude.ai web, project 'Bramblewick Events' (knowledge holds price-list-2025 only), Skill 'Bramblewick proposal style' on, Gmail + Drive connectors, account memory off, Sonnet 5.5 Medium

> Draft a proposal for a new client, the Fernhollow Weavers Guild. Their contact is Maren Calloway. They're holding a one-day winter open studio on Saturday, November 21, 2026, for 150 attendees. They want us to handle event planning, provide one on-site coordinator for the day, and two registration desk staff for 6 hours. Their goals: a calm, well-signed check-in, no queue longer than ten minutes, and a day that feels welcoming to first-time visitors.

## 5.4 · Keeping it current

### d54-fixed
*Where:* claude.ai web, project 'Bramblewick Events' after the fix (price-list-2025 removed, price-list-2026 uploaded, owner line added to instructions), Skill on, connectors OFF, account memory off, Sonnet 5.5 Medium

> Draft a proposal for a new client, the Fernhollow Weavers Guild. Their contact is Maren Calloway. They're holding a one-day winter open studio on Saturday, November 21, 2026, for 150 attendees. They want us to handle event planning, provide one on-site coordinator for the day, and two registration desk staff for 6 hours. Their goals: a calm, well-signed check-in, no queue longer than ten minutes, and a day that feels welcoming to first-time visitors.

### d54-stale
*Where:* claude.ai web, project 'Bramblewick Events' (knowledge holds price-list-2025 only), Skill on, Gmail + Drive connectors switched OFF for this chat, account memory off, Sonnet 5.5 Medium

> Draft a proposal for a new client, the Fernhollow Weavers Guild. Their contact is Maren Calloway. They're holding a one-day winter open studio on Saturday, November 21, 2026, for 150 attendees. They want us to handle event planning, provide one on-site coordinator for the day, and two registration desk staff for 6 hours. Their goals: a calm, well-signed check-in, no queue longer than ten minutes, and a day that feels welcoming to first-time visitors.

## 4.1 · From a messy request to clear requirements

### d41-requirements
*Where:* claude.ai web, project 'Bramblewick Events', Gmail + Drive on, account memory off, Sonnet 5.5 Medium

> Find Rachel Ostrander's latest email in Gmail and turn it into a requirements list for the summit: must-haves, nice-to-haves, and open questions we need to ask her. Then score Theo's chatbot idea on value, risk and how often it would be used, and say whether it's something we can set up ourselves or something that needs a developer.

## 4.2 · Research, planning and fixing a slow process

### d42-process
*Where:* claude.ai web, project 'Bramblewick Events', Gmail + Drive on, account memory off, Sonnet 5.5 Medium

> Here's how attendee sign-up works today. 1) The attendee fills in a web form. 2) The form emails Tessa. 3) Tessa copies each entry into the attendee spreadsheet by hand. 4) She emails the attendee an invoice from the accounting tool. 5) When payment arrives, she marks them paid and sends a confirmation email. 6) She copies dietary and access needs again into a separate catering sheet. It takes Tessa about 6 minutes per attendee, and we have 400. Map the steps, find the bottleneck, and suggest the two changes that would save the most time. Say which changes Claude could help with and which need someone to set up a tool.

### d42-research
*Where:* claude.ai web, project 'Bramblewick Events', Research mode on, account memory off, model picker Sonnet 5.5 Medium (Research runs its own task); report artifact saved separately as d42-research-report.md

> Research three Portland, Oregon venues that could host next year's Cascade Makers Summit: about 400 attendees over two days, a seated dinner for everyone, and step-free access throughout. For each venue give the banquet capacity, accessibility notes, catering rules (in-house only or outside caterers allowed), and any published prices, with sources I can check. Keep the report short and say where information was missing.

## 4.3 · Building through feedback, and knowing when to hand off

### d43-faq
*Where:* claude.ai web, project 'Bramblewick Events', account memory off, Sonnet 5.5 Medium; output is a Claude Docs artifact 'Cascade Makers Summit 2026: Attendee FAQ'

**Turn 1**
> Instead of a chatbot, let's give attendees a one-page FAQ. Build it as an artifact we can share and keep editing, using only facts from our files. Cover dates and venue, getting there, accessibility, food and dietary needs, and who to contact. Where a fact isn't in our files, put [to confirm] rather than guessing.

**Turn 2**
> Feedback from Rachel: most attendees will read this on a phone, so it's too long, and she wants food and accessibility at the top because those were last year's complaints. Update the FAQ for that, and keep everything else as it is.

**Turn 3**
> Theo has seen the FAQ and still wants attendees to type questions and get instant answers, including their own registration and payment status from our sign-up system. Can we do that with this FAQ, or does it need a developer? Tell me what we can do ourselves now, and what I should hand to a developer, as a short brief I can send them.

## 4.4 · Reshaping a workflow: augment or redesign

### d44-invoices
*Where:* claude.ai web, project 'Bramblewick Events' session, vendor-invoices.zip attached (12 kit PDFs zipped, upload sha matched), account memory off, Sonnet 5.5 Medium; ran as a multi-step task (TaskCreate, Bash, SendUserFile) and returned a zip

> This zip is our shared folder of supplier invoices, and the file names are a mess. Open every file, rename each one as vendor_item_amount (for example Juniper-Table-Catering_Deposit_17324.pdf), sort them into one folder per vendor, and give me the tidy folder back as a zip. Also give me a table of every file with its old name, new name and amount, the total, and flag anything that doesn't look like a real invoice.

## 4.5 · Explaining value and limits to stakeholders

### d45-stakeholder
*Where:* claude.ai web, project 'Bramblewick Events', account memory off, Sonnet 5.5 Medium

> Graham wants real numbers on time saved before we use Claude on other events. Here's what I logged this week, using my own rough timings: summarizing the three catering quotes took 10 minutes including checking, against about 45 minutes by hand. Eight attendee replies took 10 minutes including checking, against about 40 by hand. Mapping the sign-up process found about 40 hours a year of re-typing we could remove. One proposal was priced from an expired price list and came out $598 too low; a reviewer caught it before it went out. Write Graham a one-page brief with the time saved, the limits we hit, what still needs a person, and a recommendation. Be clear about which numbers are measured and which are estimates, and don't oversell it.

## 6.1 · Appropriate and inappropriate use

### d61-inappropriate
*Where:* claude.ai web, project 'Bramblewick Events', account memory off, Sonnet 5.5 Medium

**Turn 1**
> We got 36 speaker applications for the summit and I don't have time to read them. I'll paste them in next. Score each one out of 10, then send rejection emails to the bottom 20 automatically so they're off my plate.

**Turn 2**
> Different question. An attendee with a severe nut allergy asked whether Juniper's nut-free meal will be safe for her. Write a reply telling her it's completely safe, so she stops worrying.

## 6.2 · Data sensitivity, privacy and anonymizing

### d62-anonymized
*Where:* claude.ai web, project 'Bramblewick Events', attendees-anonymized.csv attached in the chat (made by kit/tools/anonymize_attendees.py; upload sha matched the kit file), account memory off, Sonnet 5.5 Medium

> This is our attendee list. Names, emails, phone numbers and companies have already been replaced with attendee codes. Use code to count how many people (not rows) need each dietary option and each access need, and tell me if anyone registered twice.

## 6.3 · Following your organization's AI policy

### d63-policy
*Where:* claude.ai web, project 'Bramblewick Events', account memory off, Sonnet 5.5 Medium

> Check each of these five requests from the team against our AI use policy. For each, say allowed, allowed with conditions, or not allowed, give the policy section, and say what to do instead if needed. 1) Tessa wants to finish the welcome email tonight on her personal Claude account at home. 2) Jordan wants to paste the full attendee list, with emails, into a chat to lay out the name badges. 3) Marco found a free "event budget" Skill online and wants to add it. 4) Priya wants Claude to write the post-event social post and publish it straight away. 5) Dana wants each of the 36 speaker applications summarized in one paragraph for the selection panel.

## 7.1 · Diagnosing a weak output

### d71-diagnose
*Where:* claude.ai web, project 'Bramblewick Events', account memory off, Sonnet 5.5 Medium

> Help me troubleshoot. A colleague typed "write an email to the caterers" in a chat outside any project. The email asked caterers to reply by Friday, November 13, but our real deadline is November 6, and it asked a vegan-only caterer about steak options. Which of these causes explains it best: missing context, a vague task, the wrong feature or model, stale knowledge, or an overflowing chat? Give the most likely cause first, what evidence points to it, and the fix that would stop it happening again, not just this once.

### d71-garbled-survey
*Where:* claude.ai web, project 'Bramblewick Events' session, survey-2025-summit.csv attached (rebuilt in the page from a compact encoding of the kit file; the in-page sha check didn't return because the page wasn't ready on the first call, so the stats below were checked against the kit file instead), account memory off, Sonnet 5.5 Medium

> This is last year's post-event survey: 312 responses, no names. Use code to work out the average score for each session, the share of people who would return, and the comment themes with counts. Make one chart of the session averages. Then tell me the two problems we should fix first for this year's summit, with the numbers behind them.

## 7.2 · Adjusting from feedback, with fixes that stick

### d72-skill-v2
*Where:* claude.ai web, project 'Bramblewick Events' (price-list-2026 in knowledge), Skill 'Bramblewick proposal style' v2 (service-and-tax rule added), connectors back on, account memory off, Sonnet 5.5 Medium

> Draft a proposal for a new client, the Fernhollow Weavers Guild. Their contact is Maren Calloway. They're holding a one-day winter open studio on Saturday, November 21, 2026, for 150 attendees. They want us to handle event planning, provide one on-site coordinator for the day, and two registration desk staff for 6 hours. Their goals: a calm, well-signed check-in, no queue longer than ten minutes, and a day that feels welcoming to first-time visitors.

## Capstone · Capstone

### dcap-survey
*Where:* claude.ai web, project 'Bramblewick Events' session, survey-2025-summit.csv attached (in-page sha matched the kit file), account memory off, Sonnet 5.5 Medium, code execution + chart

> This is last year's post-event survey: 312 responses, no names. Use code to work out the average score for each session, the share of people who would return, and the comment themes with counts. Make one chart of the session averages. Then tell me the two problems we should fix first for this year's summit, with the numbers behind them.

