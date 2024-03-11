import http.server
import socketserver
import os

print("                                              Made by AserialDev")    
print("                                     GitHub: https://github.com/AserialDev")
print("------------------------------------------------------------------------------------------------------------------------")


adresse_ip = input("Please, enter the IP adress of the machine with the repertories (local, 127.0.0.1): ") or "127.0.0.1"

directory = os.path.expanduser('~')

port = input("Please enter the port that you want to use (default and recommended, 8000): ") or 8000
port = int(port)

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)

    def send_head(self):
        # Ajouter du style multicolore
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        return super().send_head()

    def end_headers(self):
        self.send_header('Content-type', 'text/html')
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.end_headers()

    def wfile_write(self, data):
        if isinstance(data, str):
            data = data.encode("utf-8")
        self.wfile.write(data)

    def log_message(self, format, *args):
        pass

with socketserver.TCPServer((adresse_ip, port), MyHandler) as httpd:
    print("Server is running on adress", adresse_ip, "and the port", port)
    print("Repertory shared:", directory)
    print("To get access to the shared files, enter this url on your browser: http://{0}:{1}".format(adresse_ip, port))
    print("Python server files sharing by AstendoProject: https://github.com/AserialDev")
    httpd.serve_forever()
