from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import mimetypes

mimetypes.add_type(
    "application/javascript",
    ".mjs"
)

mimetypes.add_type(
    "application/wasm",
    ".wasm"
)

PORT = 8000

Handler = SimpleHTTPRequestHandler

with TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()