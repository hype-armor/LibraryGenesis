# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import unquote

import xml.etree.ElementTree as ET
import requests
import nbzget as nbzgetrss
import nzbdownloader as NZBDownloader
import os

if os.name == 'nt':
    DOWNLOAD_DIR = "P:\\media\\"
    INCOMPLETE_DIR = DOWNLOAD_DIR + "incomplete\\books\\"
    COMPLETED_DIR = DOWNLOAD_DIR + "completed\\books\\"
else:
    DOWNLOAD_DIR = "/downloads/"
    INCOMPLETE_DIR = DOWNLOAD_DIR + "incomplete/books/"
    COMPLETED_DIR = DOWNLOAD_DIR + "completed/books/"

nzbdownloader = NZBDownloader.Downloader(INCOMPLETE_DIR, COMPLETED_DIR)

HOSTNAME = "0.0.0.0"
SERVERPORT = 8003

class MyServer(BaseHTTPRequestHandler):
    """_summary_

    Args:
        BaseHTTPRequestHandler (_type_): _description_
    """
    def read_file(self, path):
        """_summary_

        Args:
            path (_type_): _description_
        """
        in_file = open(path, "rb") # opening for [r]eading as [b]inary
        data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
        in_file.close()
        self.wfile.write(bytes(data))
        
    def do_GET(self):
        """_summary_
        """
        self.send_response(200)
        
        # 'GET /api?t=search&cat=3030,7020,8010&extended=1&apikey=test&offset=0&limit=100 HTTP/1.1'
        querystrings = unquote(self.path)
        querystrings = querystrings.split('&')
        caps = "nzb/templates/caps.xml"
        search = "nzb/templates/search.xml"
        
        if '/api?t=search' in querystrings:
            for qstring in querystrings:
                if qstring.startswith('q='):
                    
                    print(qstring.split('q=')[1])
                    #actions = nbzgetrss.action()
                    #feed = actions.search('O4Cf3uNQhti09MLGot5XlWAXM37E9nsa', qstring.split('q=')[1])
                    feed = nbzgetrss.rss('O4Cf3uNQhti09MLGot5XlWAXM37E9nsa', 'search', qstring.split('q=')[1])
                    xml = feed.Get_XML()
                    self.send_header("Content-type", "application/xml")
                    self.end_headers()
                    self.wfile.write(bytes(xml, 'utf-8'))
                    
                    return
                
            # we are testing the api
            self.send_header("Content-type", "application/xml")
            self.end_headers()
            self.read_file(search)
        elif '/api?t=caps' in querystrings:
            # we are testing the api
            self.send_header("Content-type", "application/xml")
            self.end_headers()
            self.read_file(caps)
        elif '/downloadapi' in querystrings:
            self.send_header('Content-type','application/json')
            self.end_headers()
        elif '/api?t=get' in querystrings:
            # this is from enclosure url.
            self.send_header('Content-type','application/x-nzb')
            self.end_headers()
            for qstring in querystrings:
                if qstring.startswith('reallink='):
                    reallink = qstring.split('=')[1]
                elif qstring.startswith('category='):
                    category = qstring.split('=')[1]
                elif qstring.startswith('name1='):
                    name1 = qstring.split('=')[1]
                elif qstring.startswith('name2='):
                    name2 = qstring.split('=')[1]
                elif qstring.startswith('subject='):
                    subject = qstring.split('=')[1]
                elif qstring.startswith('size='):
                    size = qstring.split('=')[1]

            headers = {
            "User-Agent" : "Readarr/0.3.18.2411 (alpine 3.18.6)",
            "Connection" : "close",
            "Authorization" : "Basic Og==",
            "Accept-Encoding" : "gzip, br",
            "traceparent" : "00-b15da77a39ebf304c0c936b8a1e2d9d2-4e62426a4d5dcdb2-00",
            "Content-Type" : "application/x-nzb"#,
            #"Content-Length" : str(len(myobj.encode('utf-8')))
            }
            x = requests.post(reallink, headers=headers, timeout=60)
            print(x)
            nbz = nbzgetrss.nzb(category, name1, name2, subject, size, reallink)
            xml = nbz.get()
            self.wfile.write(bytes(xml, 'utf8'))
            
        else:
            print('idk')
            
            self.send_header("Content-type", "application/json")
            self.end_headers()
            message = '{"version" : "1.1","error" : {"name" : "JSONRPCError","code" : 1,"message" : "Invalid procedure"}}'
            self.wfile.write(bytes(message, "utf8"))
    
    def read_sysfile(self, path):
        """_summary_

        Args:
            path (_type_): _description_

        Returns:
            _type_: _description_
        """
        f = open (path, 'r', encoding='utf-8')
        text = f.read()
        f.close()
        return text
    
    def do_POST(self):
        """_summary_
        """
        self.send_response(200)
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(data_string.decode('utf8').replace("\\", "").replace("'", '"'))
        print(data)
        #data = json.dumps(data)
        querystrings = self.path.split('&')
        if '/downloadapi/jsonrpc' in querystrings:
            self.send_header("Content-type", "application/json")
            self.end_headers()
            storeddata = {}
            if data['method'] == 'version':
                storeddata = json.loads('{"version" : "1.1","id" : "50ec45ea","result" : "21.1"}')
            elif data['method'] == 'config':
                storeddata = json.loads(self.read_sysfile('nzb/templates/nbzget-config.json'))
            elif data['method'] == 'status':
                storeddata = json.loads(self.read_sysfile('nzb/templates/nbzget-status.json'))
            elif data['method'] == 'listgroups':
                storeddata = nzbdownloader.get_list_groups(data['id'])
            elif data['method'] == 'history':
                storeddata = nzbdownloader.get_history(data['id'])
                #storeddata = json.loads(self.read_sysfile('nzb/templates/nbzget-history.json'))
            elif data['method'] == 'append':
                nbzdatab64 = data['params'][1]
                rid = nzbdownloader.append(nbzdatab64)
                #storeddata = nzbdownloader.get_list_groups(data['id'])
                storeddata = json.loads('{"version": "1.1", "id": "b7e810e0", "result": ' + str(rid) + '}')
            elif data['method'] == 'editqueue':
                if data['params'][0] == 'GroupFinalDelete':
                    nzbdownloader.group_final_delete(data['params'][3])
                    storeddata = json.loads('{"version": "1.1", "id": "b7e810e0", "result": ' + str(data['params'][3]) + '}')
                elif data['params'][0] == 'HistoryDelete':
                    nzbdownloader.history_delete(data['params'][3])
                    storeddata = json.loads('{"version": "1.1", "id": "b7e810e0", "result": ' + str(data['params'][3]) + '}')
            else:
                print(json.dumps(data))
                
            storeddata['id'] = data['id']
            storeddata = json.dumps(storeddata)
            self.wfile.write(bytes(storeddata, "utf8"))
        else:
            print(querystrings)
        #for header in self.headers._headers:
        #    print(header[0] + ' : ' + header[1])
 

if __name__ == "__main__":
    webServer = HTTPServer((HOSTNAME, SERVERPORT), MyServer)
    print(f"Server started http://{HOSTNAME}:{SERVERPORT}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")