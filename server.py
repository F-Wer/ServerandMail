from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps
import json
import E_Mail
class RequestHandler(BaseHTTPRequestHandler):

  def _send_cors_headers(self):
      self.send_header("Access-Control-Allow-Origin", "*")
      self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
      self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")

  def do_OPTIONS(self):
      self.send_response(200)
      self._send_cors_headers()
      self.end_headers()


  def do_POST(self):
      url = 'prolific.co/studies'
      self.send_response(200)
      self._send_cors_headers()
      self.send_header("Content-Type", "text/html")
      self.end_headers()

      dataLength = int(self.headers["Content-Length"])
      data = self.rfile.read(dataLength)


      json_data = json.loads(data)
      jd2 = json_data + '\n' + url
      print(jd2)
      E_Mail.send(jd2.encode('utf8'))
      response = {}
      response["status"] = "OK"

print("Starting server")
httpd = HTTPServer(("127.0.0.1", 8000), RequestHandler)
print("Hosting server on port 8000")
httpd.serve_forever()
