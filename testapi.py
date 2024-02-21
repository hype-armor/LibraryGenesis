import requests, json

#url = 'http://192.168.0.141:8003/downloadapi/jsonrpc'
url = 'http://docker:6789/jsonrpc'
method = 'history'
if method == 'version':
    myobj = '{\
    "jsonrpc": "2.0",\
    "method": "version",\
    "params": [],\
    "id": "50ec45ea"\
    }'
elif method == 'config':
    myobj = '{\
    "jsonrpc": "2.0",\
    "method": "config",\
    "params": [],\
    "id": "7d39413f"\
    }'
elif method == 'status':
    myobj = '{\
    "jsonrpc": "2.0", \
    "method": "status", \
    "params": [], \
    "id": "4e5d9b86"\
    }'
elif method == 'listgroups':
    myobj = '{\
    "jsonrpc": "2.0", \
    "method": "listgroups", \
    "params": [], \
    "id": "4e5d9b86"\
    }'
elif method == 'history':
    myobj = '{\
    "jsonrpc": "2.0", \
    "method": "history", \
    "params": [], \
    "id": "c370ee25"\
    }'
elif method == 'append':
    myobj = "{'jsonrpc': '2.0', 'method': 'append', 'params': ['Obama, Barack - A Promised Land (epub).nzb', 'PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIG56YiBQVUJMSUMgIi0vL25ld3pCaW4vL0RURCBOWkIgMS4xLy9FTiIgImh0dHA6Ly93d3cubmV3emJpbi5jb20vRFREL256Yi9uemItMS4xLmR0ZCI+CjxuemIgeG1sbnM9Imh0dHA6Ly93d3cubmV3emJpbi5jb20vRFRELzIwMDMvbnpiIj4KCjxoZWFkPgogPG1ldGEgdHlwZT0iY2F0ZWdvcnkiPkJvb2tzICZndDsgRWJvb2s8L21ldGE+CiA8bWV0YSB0eXBlPSJuYW1lIj5BIFByb21pc2VkIExhbmQ8L21ldGE+CiA8bWV0YSB0eXBlPSJuYW1lIj5BLlByb21pc2VkLkxhbmQ8L21ldGE+CiA8bWV0YSB0eXBlPSJjYXRlZ29yeSI+Qm9va3MgJmd0OyBFYm9vazwvbWV0YT4KPC9oZWFkPgoKPGZpbGUgcG9zdGVyPSJnZG9NakxacmFOUWtCX0hmUkUxbkh3LVlYb0BueXdmTHZWLl9FaiIgZGF0ZT0iMTcwODUzODgzMiIgc3ViamVjdD0iKHJldGFpbCkgUmU6IFJFUTogQSBQcm9taXNlZCBMYW5kJnF1b3Q7QmFyYWNrIE9iYW1hIC0gQSBQcm9taXNlZCBMYW5kJnF1b3Q7IHlFbmMgKDEvMSkiPgogPGdyb3Vwcz4KICA8Z3JvdXA+YWx0LmJpbmFyaWVzLm1vdmllcy5ta3Y8L2dyb3VwPgogPC9ncm91cHM+CiA8c2VnbWVudHM+CiAgPHNlZ21lbnQgYnl0ZXM9IjE2NjkxMiIgbnVtYmVyPSIxIj5odHRwOi8vbGlicmFyeS5sb2wvbWFpbi9CMjBEMzhCMzIzQ0Q0ODMxMzQ2QURGRkJBRjI5NURBNzwvc2VnbWVudD4KIDwvc2VnbWVudHM+CjwvZmlsZT4KPCEtLSBnZW5lcmF0ZWQgYnkgbmV3em5hYiAwLjIuM3AgLS0+CjwvbnpiPg==', 'Books', 0, False, False, '', 0, 'all', ['drone', '1e4b5350ea2e4037801eb5699d3069b3']], 'id': '95c8e7b1'}"

Headers = { 
"User-Agent" : "Readarr/0.3.18.2411 (alpine 3.18.6)",
"Connection" : "close",
"Authorization" : "Basic Og==",
"Accept-Encoding" : "gzip, br",
"traceparent" : "00-b15da77a39ebf304c0c936b8a1e2d9d2-4e62426a4d5dcdb2-00",
"Content-Type" : "application/json",
"Content-Length" : str(len(myobj.encode('utf-8')))
}
print(str(len(myobj.encode('utf-8'))))
x = requests.post(url, data = myobj, auth = ('greg', 'comeon'), headers=Headers)
#x = requests.post(url, json = myobj)

print(x.text)