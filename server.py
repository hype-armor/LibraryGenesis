# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "spaceheater"
serverPort = 8003

class MyServer(BaseHTTPRequestHandler):
    def read_file(self, path):
        in_file = open(path, "rb") # opening for [r]eading as [b]inary
        data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
        in_file.close()
        self.wfile.write(bytes(data))
        
    def do_GET(self):
        self.send_response(200)
        
        # 'GET /api?t=search&cat=3030,7020,8010&extended=1&apikey=test&offset=0&limit=100 HTTP/1.1'
        querystrings = self.path.split('&')
        caps = "N:\\Users\\Greg\\Documents\\GitHub\\python-proxy-server-main\\src\\caps.xml"
        search = "N:\\Users\\Greg\\Documents\\GitHub\\python-proxy-server-main\\src\\search.xml"
        if '/api?t=search' in querystrings:
            for qstring in querystrings:
                if qstring.startswith('q='):
                    import nbzget as nbzgetrss
                    print(qstring.split('q=')[1])
                    actions = nbzgetrss.action()
                    feed = actions.search('O4Cf3uNQhti09MLGot5XlWAXM37E9nsa', qstring.split('q=')[1])
                    feed = nbzgetrss.rss('O4Cf3uNQhti09MLGot5XlWAXM37E9nsa', 'search', qstring.split('q=')[1])
                    xml = feed.Get_XML()
                    self.send_header("Content-type", "application/xml")
                    self.end_headers()
                    self.wfile.write(bytes(xml, 'utf-8'))
                    
                    return
                
            # we are testing the api
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.read_file(search)
        elif '/api?t=caps' in querystrings:
            # we are testing the api
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.read_file(caps)
        
        
        
        

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")