#!/usr/bin/env python


import xerox
import json

def copy_text_to_clipboard(text):
    xerox.copy(text)

def paste_text_from_clipboard():
    return xerox.paste()

class CopyPasteRequestHandler(BaseHTTPRequestHandler):

    DEFAULT_PORT = 42157
    
    def notFound(self):
        self.send_response(404)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps({"path", self.path})))

    def do_OPTIONS(self):
        if self.path == '/clipboard':
            self.headers.get('Authorization')
            origin = self.headers.get('OriginX')
            if origin == None:
                origin = "*"
            print("Origin: " + str(origin))
            self.send_response(204) # no response body
            self.send_header("Access-Control-Allow-Origin", f"{origin}")
            self.send_header("Access-Control-Allow-Credentials", "true")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.end_headers()
        else:
            self.notFound()

    def do_POST(self):
        if self.path == '/clipboard':
            try:
                content_length = int(self.headers.get('Content-Length'))
                post_body = self.rfile.read(content_length)
                post_body_string = post_body.decode('utf-8');
                print(f"Got post body: {post_body_string}")
                json_data = json.loads(post_body_string)
                text = json_data['text']
                print("text: " + text)
                copy_text_to_clipboard(text)
                xerox.copy(text)
                print("done " + xerox.paste())
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                json_response = json.dumps({"copied": text})
                self.wfile.write(bytes(json_response, "utf-8"))
            except Exception as e:
                print(e)
                self.send_response(500)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes(json.dumps({"error", "Bad!"})))
        else:
            self.notFound()


def main():
    port = CopyPasteRequestHandler.DEFAULT_PORT
    server_address = ('', port)
    httpd = ThreadingHTTPServer(server_address, CopyPasteRequestHandler)
    print(f"Starting Copy-Paste Server on http://localhost:{port}/clipboard")
    httpd.serve_forever()

if __name__ == '__main__':
    main()
