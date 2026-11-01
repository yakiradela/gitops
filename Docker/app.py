import os
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler

APP_VERSION = "v1.0.0"
MESSAGE = "Hello from GitOps Kubernetes Cluster!"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/" or self.path == "":
            pod_name = os.getenv("HOSTNAME", socket.gethostname())
            html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>GitOps App</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }}
        .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }}
        h1 {{ color: #333; }}
        p {{ color: #666; font-size: 18px; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{MESSAGE}</h1>
        <p><strong>App Version:</strong> {APP_VERSION}</p>
        <p><strong>Serving Pod:</strong> {pod_name}</p>
    </div>
</body>
</html>
"""
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
