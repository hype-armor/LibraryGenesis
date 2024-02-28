import requests, json

url = 'http://192.168.0.141:8003/downloadapi/jsonrpc'
#url = 'http://docker:6789/jsonrpc'
method = 'append'
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
    myobj = '{"jsonrpc": "2.0", "method": "append", "params": ["S., C. - The C. S. Lewis Collection(epub).nzb", "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIG56YiBQVUJMSUMgIi0vL25ld3pCaW4vL0RURCBOWkIgMS4xLy9FTiIgImh0dHA6Ly93d3cubmV3emJpbi5jb20vRFREL256Yi9uemItMS4xLmR0ZCI+CjxuemIgeG1sbnM9Imh0dHA6Ly93d3cubmV3emJpbi5jb20vRFRELzIwMDMvbnpiIj4KCjxoZWFkPgogPG1ldGEgdHlwZT0iY2F0ZWdvcnkiPkJvb2tzICZndDsgRWJvb2s8L21ldGE+CiA8bWV0YSB0eXBlPSJuYW1lIj5UaGUgQy4gUy4gTGV3aXMgQ29sbGVjdGlvbjogU2lnbmF0dXJlIENsYXNzaWNzIGFuZCBPdGhlciBNYWpvciBXb3JrczogTWVyZSBDaHJpc3RpYW5pdHksIFRoZSBTY3Jld3RhcGUgTGV0dGVycywgTWlyYWNsZXMsIFRoZSBHcmVhdCBEaXZvcmNlLCBUaGUgUHJvYmxlbSBvZiBQYWluLCBBIEdyaWVmIE9ic2VydmVkLCBUaGUgQWJvbGl0aW9uIG9mIE1hbiwgVGhlIEZvdXIgTG92ZXMsIFJlZmxlY3Rpb25zIG9uIHRoZSBQc2FsbXMsIFN1cnByaXNlZCBieSBKb3ksIExldHRlcnMgdG8uLi48L21ldGE+CiA8bWV0YSB0eXBlPSJuYW1lIj5UaGUuQy4uUy4uTGV3aXMuQ29sbGVjdGlvbjouU2lnbmF0dXJlLkNsYXNzaWNzLmFuZC5PdGhlci5NYWpvci5Xb3JrczouTWVyZS5DaHJpc3RpYW5pdHksLlRoZS5TY3Jld3RhcGUuTGV0dGVycywuTWlyYWNsZXMsLlRoZS5HcmVhdC5EaXZvcmNlLC5UaGUuUHJvYmxlbS5vZi5QYWluLC5BLkdyaWVmLk9ic2VydmVkLC5UaGUuQWJvbGl0aW9uLm9mLk1hbiwuVGhlLkZvdXIuTG92ZXMsLlJlZmxlY3Rpb25zLm9uLnRoZS5Qc2FsbXMsLlN1cnByaXNlZC5ieS5Kb3ksLkxldHRlcnMudG8uLi48L21ldGE+CiA8bWV0YSB0eXBlPSJjYXRlZ29yeSI+Qm9va3MgJmd0OyBFYm9vazwvbWV0YT4KPC9oZWFkPgoKPGZpbGUgcG9zdGVyPSJnZG9NakxacmFOUWtCX0hmUkUxbkh3LVlYb0BueXdmTHZWLl9FaiIgZGF0ZT0iMTcwOTA3NTUyMSIgc3ViamVjdD0iKHJldGFpbCkgUmU6IFJFUTogVGhlIEMuIFMuIExld2lzIENvbGxlY3Rpb246IFNpZ25hdHVyZSBDbGFzc2ljcyBhbmQgT3RoZXIgTWFqb3IgV29ya3M6IE1lcmUgQ2hyaXN0aWFuaXR5LCBUaGUgU2NyZXd0YXBlIExldHRlcnMsIE1pcmFjbGVzLCBUaGUgR3JlYXQgRGl2b3JjZSwgVGhlIFByb2JsZW0gb2YgUGFpbiwgQSBHcmllZiBPYnNlcnZlZCwgVGhlIEFib2xpdGlvbiBvZiBNYW4sIFRoZSBGb3VyIExvdmVzLCBSZWZsZWN0aW9ucyBvbiB0aGUgUHNhbG1zLCBTdXJwcmlzZWQgYnkgSm95LCBMZXR0ZXJzIHRvLi4uJnF1b3Q7Qy4gUy4gTGV3aXMgLSBUaGUgQy4gUy4gTGV3aXMgQ29sbGVjdGlvbjogU2lnbmF0dXJlIENsYXNzaWNzIGFuZCBPdGhlciBNYWpvciBXb3JrczogTWVyZSBDaHJpc3RpYW5pdHksIFRoZSBTY3Jld3RhcGUgTGV0dGVycywgTWlyYWNsZXMsIFRoZSBHcmVhdCBEaXZvcmNlLCBUaGUgUHJvYmxlbSBvZiBQYWluLCBBIEdyaWVmIE9ic2VydmVkLCBUaGUgQWJvbGl0aW9uIG9mIE1hbiwgVGhlIEZvdXIgTG92ZXMsIFJlZmxlY3Rpb25zIG9uIHRoZSBQc2FsbXMsIFN1cnByaXNlZCBieSBKb3ksIExldHRlcnMgdG8uLi4mcXVvdDsgeUVuYyAoMS8xKSI+CiA8Z3JvdXBzPgogIDxncm91cD5hbHQuYmluYXJpZXMubW92aWVzLm1rdjwvZ3JvdXA+CiA8L2dyb3Vwcz4KIDxzZWdtZW50cz4KICA8c2VnbWVudCBieXRlcz0iNTEyMCIgbnVtYmVyPSIxIj5odHRwOi8vbGlicmFyeS5sb2wvbWFpbi8yRjZBNTIwNDdCMEEwMDMyODg2NzlCNjg4RDhGRTlBMDwvc2VnbWVudD4KIDwvc2VnbWVudHM+CjwvZmlsZT4KPCEtLSBnZW5lcmF0ZWQgYnkgbmV3em5hYiAwLjIuM3AgLS0+CjwvbnpiPg==", "Books", 0, "FALSE", "FALSE", "", 0, "all", ["drone", "160ebaa9fdee4a1d803b0a504eabb86a"]], "id": "4d1f948a"}'

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