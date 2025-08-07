from http.server import SimpleHTTPRequestHandler, HTTPServer
from datetime import datetime

class LoggingHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Gather information
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        ip = self.client_address[0]
        path = self.path

        # Basic headers
        user_agent = self.headers.get('User-Agent', 'None')
        referer = self.headers.get('Referer', 'None')
        accept = self.headers.get('Accept', 'None')
        host = self.headers.get('Host', 'None')
        connection = self.headers.get('Connection', 'None')
        cookie = self.headers.get('Cookie', 'None')

        # Capture ALL headers for further detail
        headers_full = '; '.join([f'{k}: {v}' for k, v in self.headers.items()])

        # Prepare detailed log entry
        log_entry = (
            f"[{timestamp}] Path: {path}, From: {ip}\n"
            f"   User-Agent: {user_agent}\n"
            f"   Referer: {referer}\n"
            f"   Accept: {accept}\n"
            f"   Host: {host}\n"
            f"   Connection: {connection}\n"
            f"   Cookie: {cookie}\n"
            f"   ALL Headers: {headers_full}\n"
            "-------------------------------------------------\n"
        )

        with open("pixel_requests.txt", "a") as f:
            f.write(log_entry)

        # Serve the file or return 404 for others
        if self.path == "/pixel.png":
            super().do_GET()
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), LoggingHandler)
    print("Serving on port 8000...")
    server.serve_forever()
