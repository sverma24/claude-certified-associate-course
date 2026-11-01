"""Build tools/seed.gs: a one-off Google Apps Script that loads the kit into
a demo Google account that holds only the fictional company's files and emails.

  - Drive: moves any older copy of each kit PDF to the trash, then adds the
    current one, in the course's folders
  - Gmail: puts the gmail-seed emails into the inbox (inserted, never sent)

The script needs the Gmail advanced service turned on in the Apps Script
editor (Services > Gmail API).

Run:  KIT_DEMO_ACCOUNT=you.demo@gmail.com python3 tools/make_seed_script.py

Use a fresh account made only for this. The script refuses to run in any other account.
"""

import base64
import json
import os
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent / "bramblewick"
OUT = Path(__file__).resolve().parent / "seed.gs"
DEMO = os.environ.get("KIT_DEMO_ACCOUNT") or sys.exit("Set KIT_DEMO_ACCOUNT to the demo Google account's address.")

# Drive folder ids in the course's own demo account (created 2026-10-31). Replace them with your own folders.
FOLDERS = {
    "company": "1kdbJaLaNQEoW8QlFxEOQM9aqkbjkbDlE",
    "summit": "1p9hUw6_5o6CsH8QR8owj1nzq4ptbW_QT",
    "quotes": "190-Oi6_P1E8F990Bq7-63EMMLq5zOtoe",
}
FILES = {
    "company": ["company/brand-and-tone-guide.pdf", "company/ai-use-policy.pdf",
                "company/price-list-2025.pdf", "company/price-list-2026.pdf"],
    "summit": ["summit/client-brief.pdf", "summit/venue-contract.pdf"],
    "quotes": ["summit/vendor-quotes/juniper-table-catering.pdf",
               "summit/vendor-quotes/ridgeline-provisions.pdf",
               "summit/vendor-quotes/harvest-and-hearth.pdf"],
}


def main():
    drive = [{"folder": FOLDERS[k], "name": Path(f).name,
              "b64": base64.b64encode((KIT / f).read_bytes()).decode()}
             for k, fs in FILES.items() for f in fs]
    mails = [p.read_text().replace("bramblewick.demo@example.com", DEMO)
             for p in sorted((KIT / "gmail-seed").glob("*.eml"))]
    OUT.write_text(f"""// One-off loader for the course's fictional Bramblewick Events data.
// Made by tools/make_seed_script.py. Nothing here is sent to anyone.
const DRIVE = {json.dumps(drive)};
const MAIL = {json.dumps(mails)};

function seed() {{
  if (Session.getActiveUser().getEmail() !== '{DEMO}') throw new Error('Run this only in {DEMO}');
  DRIVE.forEach(function (f) {{
    const folder = DriveApp.getFolderById(f.folder);
    const old = folder.getFilesByName(f.name);
    while (old.hasNext()) old.next().setTrashed(true);
    folder.createFile(Utilities.newBlob(Utilities.base64Decode(f.b64), 'application/pdf', f.name));
  }});
  MAIL.forEach(function (raw) {{
    Gmail.Users.Messages.insert(
      {{raw: Utilities.base64EncodeWebSafe(raw, Utilities.Charset.UTF_8), labelIds: ['INBOX', 'UNREAD']}},
      'me', null, {{internalDateSource: 'dateHeader'}});
  }});
  Logger.log('Drive files: ' + DRIVE.length + ', emails: ' + MAIL.length);
}}
""")
    print(f"{OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
