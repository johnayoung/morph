import datetime
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def max_n(lst, n=1, reverse=True):
        return sorted(lst, reverse=reverse)[:n]
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(str(max_n([1, 2, 3]).encode())
        return
