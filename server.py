import http.server
import socketserver
import subprocess

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
  def end_headers(self):
    self.send_header('Access-Control-Allow-Origin', '*')
    http.server.SimpleHTTPRequestHandler.end_headers(self)

  def do_GET(self):
    if self.path == '/':
      self.path = '/index.html'
    elif self.path == '/download':
      subprocess.run(['termux-open', '/path/to/your/files'], check=True)
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write(b'Files downloaded successfully!')
      return
    return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Porti në të cilin serveri do të punojë
port = 8000

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
  print("Serveri po punon në portin:", port)
  httpd.serve_forever()
