print("Loading...")

from libgen_api import LibgenSearch
import os.path
s = LibgenSearch()
calibreimportdir = f'P:\media\calibre\import\\'
readarrdownloaddir = f'P:\media\watch\\'
from urllib.parse import unquote

""" 
col_names = [
    "ID",
    "Author",
    "Title",
    "Publisher",
    "Year",
    "Pages",
    "Language",
    "Size",
    "Extension",
    "Mirror_1",
    "Mirror_2",
    "Mirror_3",
    "Mirror_4",
    "Mirror_5",
    "Edit",
]
"""

class book:
    def __init__(self, author, title, publisher, year, id, pages, language, size, extension, 
                 mirror_1, mirror_2, mirror_3, mirror_4, mirror_5, edit):
        self.id = id
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.language = language
        self.size = size
        self.extension = extension
        self.mirror_1 = mirror_1
        self.mirror_2 = mirror_2
        self.mirror_3 = mirror_3
        self.mirror_4 = mirror_4
        self.mirror_5 = mirror_5
        self.edit = edit
        
def Get_Item(array, key):
    if key in array:
        return array[key]
    else:
        return None
    
# workflow
# search for book title maybe author and maybe year.
def Search (Title, Author="", Year="", Extension="", readarr=False):
    filters = {}
    if (Author != ""):
        filters["Author"] = Author
    if (Year != ""):
        filters["Year"] = Year
    if (Extension != ""):
        filters["Extension"] = Extension
    
    if readarr:
        results = s.search(Title)
    elif filters == None:
        results = s.search(Title)
    else:
        results = s.search_filtered(Title, filters, exact_match=False)
    
    books = {}
    for result in results:
        b = book(
            Get_Item(result, 'Author'), 
            Get_Item(result, 'Title'), 
            Get_Item(result, 'Publisher'), 
            Get_Item(result, 'Year'), 
            Get_Item(result, 'ID'), 
            Get_Item(result, 'Pages'), 
            Get_Item(result, 'Language'), 
            Get_Item(result, 'Size'), 
            Get_Item(result, 'Extension'),
            Get_Item(result, 'Mirror_1'), 
            Get_Item(result, 'Mirror_2'), 
            Get_Item(result, 'Mirror_3'), 
            Get_Item(result, 'Mirror_4'), 
            Get_Item(result, 'Mirror_5'), 
            Get_Item(result, 'Edit')
        )
        books[b.id] = b
    return books

def __init__():
    print("Searching...")
    while True:
        query = input("Please enter query: ")
        results = Search(query, Extension="pdf")
        # return top result(s) that matches for approval
        for i in range(len(results)):
            print("" + str(i) + " | ", end="")
            print(results[i]["Author"], end=" - ")
            print(results[i]["Title"], end=" (")
            print(results[i]["Year"], end=") ")
            print(results[i]["Extension"].upper())
                
        # select / approve result
        if len(results) == 0:
            print("No results")
            continue
        result = results[0]
        if len(results) > 1:
            user_selection = input("Enter a number: ")
            if user_selection == "": continue
            user_selection = int(user_selection)
            result = results[user_selection]
            break
        elif len(results) == 1:
            user_selection = 'y'#input("Download? [y|N]: ").lower()
            if user_selection != 'y':
                continue
            break

        
def slugify(value, allow_unicode=False):
    import unicodedata
    import re
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value).replace('%20', ' ')
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', ' ', value)
    value = value.replace('  ', ' ')
    return value
    #return re.sub(r'[-\s]+', '-', value).strip('-_')    
        
def download(result):
    # resolve download link
    print("Getting Download Link...")
    download_link = s.resolve_download_links(result)
    # download
    print("Downloading....")
    import urllib.request
    import ssl

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    urifilename = unquote(download_link['GET'].split('/')[-1])
    if 'Author' not in result:
        result['Author'] = urifilename.split('-')[0]
    if 'Title' not in result:
        result['Title'] = urifilename.split('-')[1].split('.')[0]
    if 'Year' not in result:
        if '(' in result:
            result['Year'] = urifilename.split('(')[1]
            result['Year'] = result['Year'].split(')')[0]
        else:
            result['Year'] = ''
    if 'Extension' not in result:
        result['Extension'] = urifilename.split('.')[-1]

    #print (result["Author"])
    #print (slugify(result["Author"]))
    file_path = slugify(result["Author"]) + '-' + slugify(result["Title"]) + ' (' + result["Year"] + ').' + result["Extension"]
    file_path = readarrdownloaddir + file_path
    if os.path.isfile(file_path): 
        print('Already downloaded.')
        return
    #file_path = slugify(file_path)
    print(file_path)


    response = urllib.request.urlopen(download_link['GET'], context=ctx)
    total_size = response.length

    try:
        with open(file_path, 'wb+') as f:
            while True:
                chunk = response.read(1024)
                if not chunk:
                    break

                progress = abs(int(float(response.length) / float(total_size) * 100) - 100)
                f.write(chunk)
    except:
        print("Failed to save: " + file_path)
    
    print("Move to import folder...")
    #import shutil
    #shutil.move(file_path, calibreimportdir + file_path)
    print("Done!")