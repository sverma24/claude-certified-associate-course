"""Serve bramblewick/ on 127.0.0.1 with CORS headers, so a browser tab on
drive.google.com or mail.google.com can fetch the kit files while they are
loaded into the course's demo Google account. Local use only.

Run:  python3 tools/serve_kit.py [port]
"""

import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "bramblewick"
ALLOWED = {"https://drive.google.com", "https://mail.google.com", "https://claude.ai"}


# Opened as a popup from the Drive or Gmail tab: it reads the requested kit
# files (same origin, so no CORS) and posts them back to the opener.
SENDER = """<!doctype html><meta charset="utf-8"><title>kit sender</title><body>sending…<script>
const want = new URLSearchParams(location.search).getAll('f');
const to = new URLSearchParams(location.search).get('to');
Promise.all(want.map(async f => ({name: f.split('/').pop(), path: f,
  type: f.endsWith('.pdf') ? 'application/pdf' : f.endsWith('.eml') ? 'message/rfc822' : 'text/plain',
  bytes: await (await fetch('/' + f)).arrayBuffer()})))
  .then(files => { opener.postMessage({kit: files}, to); document.body.textContent = 'sent ' + files.length; setTimeout(() => close(), 500); });
</script>"""


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/_sender.html"):
            body = SENDER.encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def end_headers(self):
        origin = self.headers.get("Origin", "")
        if origin in ALLOWED:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Access-Control-Allow-Private-Network", "true")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, directory=str(ROOT))).serve_forever()
