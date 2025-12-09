from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract requirement_id from path
        path = self.path
        requirement_id = path.split('/')[-1] if path else 'unknown'
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({"id": requirement_id, "data": {}}).encode())
        return
    
    def do_PUT(self):
        # Extract requirement_id from path
        path = self.path
        requirement_id = path.split('/')[-1] if path else 'unknown'
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({"id": requirement_id, "message": "Requirement updated"}).encode())
        return
    
    def do_DELETE(self):
        # Extract requirement_id from path
        path = self.path
        requirement_id = path.split('/')[-1] if path else 'unknown'
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({"id": requirement_id, "message": "Requirement deleted"}).encode())
        return

