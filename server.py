#!/usr/bin/env python3
"""Lightweight local server that reads GOOGLE_MAPS_API_KEY from .env or api_key.txt
at runtime without hardcoding the key into source code files."""

import http.server
import json
import os
from pathlib import Path
import socketserver

PORT = int(os.environ.get("PORT", "8080"))
ROOT_DIR = Path(__file__).resolve().parent


def parse_key_from_file(file_path: Path) -> str:
    if not file_path.exists():
        return ""
    for line in file_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            if k.strip() == "GOOGLE_MAPS_API_KEY":
                val = v.strip().strip('"').strip("'")
                if val and val != "YOUR_GOOGLE_MAPS_API_KEY_HERE":
                    return val
        elif line.startswith("AIza"):
            # Support pasting the raw key directly on its own line
            return line.strip().strip('"').strip("'")
    return ""


def load_env_key() -> str:
    # 1. Check process environment variable first
    env_val = os.environ.get("GOOGLE_MAPS_API_KEY", "").strip()
    if env_val and env_val != "YOUR_GOOGLE_MAPS_API_KEY_HERE":
        return env_val

    # 2. Check .env and visible api_key.txt in workspace root
    for fname in (".env", "api_key.txt"):
        val = parse_key_from_file(ROOT_DIR / fname)
        if val:
            return val
    return ""


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT_DIR), **kwargs)

    def do_GET(self):
        if self.path.split("?")[0] == "/env-config.js":
            api_key = load_env_key()
            payload = f"window.GOOGLE_MAPS_API_KEY = {json.dumps(api_key)};\n"
            data = payload.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        super().do_GET()


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
