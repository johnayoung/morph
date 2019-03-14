from http.server import BaseHTTPRequestHandler
import json
import debugserver

def capitalize(string, lower_rest=False):
  return string[:1].upper() + (string[1:].lower() if lower_rest else string[1:])

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
      path = self.path
      print('path is ', path)

      self.send_response(200)
      self.send_header("Content-type", "application/json")
      self.end_headers()

      response = {"output": capitalize('diabolical')}
      self.wfile.write(json.dumps(response).encode("utf-8"))

      return

if __name__ == '__main__':
    debugserver.serve(handler)