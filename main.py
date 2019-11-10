import VK
import os, sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()