#!/usr/bin/python3
"""
task_03_http_server.py
A simple HTTP server that serves text and JSON data.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000

class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for our simple API."""

    def _send_response(self, code, content, content_type="text/plain"):
        """Helper method to send HTTP responses with headers."""
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        if isinstance(content, str):
            self.wfile.write(content.encode("utf-8"))
        else:
            self.wfile.write(content)

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self._send_response(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_response(200, json.dumps(data), "application/json")
        elif self.path == "/status":
            self._send_response(200, json.dumps({"status": "OK"}), "application/json")
        else:
            self._send_response(404, "Endpoint not found")

def run_server():
    """Start the HTTP server."""
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running at http://{HOST}:{PORT}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
