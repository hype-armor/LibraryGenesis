import librarygenesis as lg
import re

readarrurl = 'http://docker:8787/api'
apiversion = 'v1'
apikey = 'ff0b3ac3bc3d41d7857cde59402bcb45'
uri = readarrurl + '/' + apiversion + '/book?includeAllAuthorBooks=true&apikey=' + apikey

import urllib.request, json 
with urllib.request.urlopen(uri) as url:
    data = json.load(url)

for book in data:
    if book['monitored'] == False:
        continue
    if "statistics" in book:
        if book['statistics']['sizeOnDisk'] > 0:
            continue
    title = book['title']
    if len(title) > 60:
        title = title[:60]
    authorTitle = book['authorTitle']
    pattern = ' ' + book['title']
    replacement = "" # replacement text
    author = authorTitle.replace(pattern, replacement)
    releaseYear = re.sub(r'-.*$', '', book['releaseDate'])
    search_str = author + ' ' + title
    search_str = search_str[:56] + " " + releaseYear
    results = lg.Search(search_str, readarr=True)
    
    if len(results) == 1 and  results[0]['Extension'] != '7z':
        print("Found " + title)
        lg.download(results[0])
    elif len(results) > 1:
        picks = {}
        # do they all list pages?
        for r in results:
            if r['Pages'] != '' and (r['Extension'] == 'mobi' or r['Extension'] == 'epub') and r['Extension'] != '7z':
                picks[r['ID']] = r
                
        if len(picks) > 0 :
            lg.download(picks[list(picks.keys())[0]])
        else:
            lg.download(results[0])
    else:
        print("Nothing found for: " + search_str)