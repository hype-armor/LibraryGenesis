import librarygenesis as LG
import datetime
import calendar
import urllib.parse
from threading import Thread



class action:
    def __init__(self):
        pass
    
    def search(self, apikey, query):
        from urllib.parse import unquote
        
        if '+' in query:
            self.title = unquote(query.split('+')[0])
            self.author = unquote(query.split('+')[1])
            self.results = LG.Search(self.title, self.author)
            return self.results
        self.title = unquote(query)
        self.results = LG.Search(self.title, readarr=True)
        return self.results


class rss:
    xml = '<?xml version="1.0" encoding="utf-8" ?>'
    rss = '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:newznab="http://www.newznab.com/DTD/2010/feeds/attributes/">'
    def __init__(self, apikey, action, query):
        self.Channel = self.channel(apikey, action, query)
    
    def Get_XML(self):
        channel_xml = self.Channel.Get_XML()
        r = self.xml + self.rss
        r += channel_xml
        r += '</rss>'   
        return r
        
    class channel:
        def __init__(self, apikey, action, query):
            self.apikey = apikey
            self.t = action
            self.q = query
            self.image = self.image()
            self.url = '192.168.0.141:8003'
            self.href = 'http://' + self.url + '/api'
            #self.t = 'search'
            self.cat = '3030,7020,8010'
            #self.apikey = 'O4Cf3uNQhti09MLGot5XlWAXM37E9nsa'
            #self.q = 'Fifty%20Shades%20of%20Grey+E%20L%20James'
            
            self.atom = '<atom:link href="' + self.href + '?t=' + self.t + '&amp;cat=' + self.cat + \
            '&amp;extended=1&amp;apikey=' + self.apikey + '&amp;offset=0&amp;limit=100&amp;q=' + self.q + \
            '" rel="self" type="application/rss+xml" />'
            self.title = '<title>' + self.url + '</title>'
            self.description = '<description>python API</description>'
            self.link = '<link>http://' + self.url + '/</link>'
            self.language = '<language>en-gb</language>'
            self.webMaster = '<webMaster>info@example.info (example)</webMaster>'
            self.category = '<category></category>'
            
            
        def Get_XML(self):
            r = '<channel>'
            r += self.atom + self.title + self.description + self.link + self.language + self.webMaster + self.category
            r += self.image.Get_XML()
            tr = self.Get_Items(self.q) #self.item.Get_XML()
            r += self.newznab
            r += tr
            r += '</channel>'
            return r

        class image:
            def __init__(self):
                self.url = '<url>https://api.nzbgeek.info/covers/nzbgeek.png</url>'
                self.title = '<title>api.nzbgeek.info</title>'
                self.link = '<link>http://api.nzbgeek.info/</link>'
                self.description = '<description>NZBgeek</description>'
                
            def Get_XML(self):
                return '<image>' + self.url + self.title + self.link + self.description + '</image>'
        
        
        def Get_Items(self, query):
            lgitems = action().search(self.apikey, query)
            
            items = ''
            self.item_count = 0
            for lgitem in lgitems.values():
                dt=datetime.datetime.now()
                dayofweek = calendar.day_name[dt.weekday()][:3]
                date = 'Sun, 14 Mar 2021 14:52:04 +0000' #dayofweek + ', ' + str(dt.day) + ' ' + str(calendar.month_name[int(dt.month) -1])[:3] + ' ' + \
                #       Tue, 19 Jan 2024 16:32:13 +0000
                #str(dt.year) + ' ' + str(dt.time()).split(".")[0] + ' +0000'
                guid = lgitem.mirror_1.split('/')[-1]
                setattr(lgitem, 'guid', guid or '')
                setattr(lgitem, 'link', lgitem.mirror_1 or '')
                setattr(lgitem, 'comments', lgitem.mirror_1 or '')
                setattr(lgitem, 'pubDate', date)
                setattr(lgitem, 'category', 'Books > Ebook')
                author = lgitem.author
                if ' ' in lgitem.author:
                    author = lgitem.author.split(' ')[1] + ', ' + lgitem.author.split(' ')[0]
                setattr(lgitem, 'description', author + ' - ' + lgitem.title)
                eurl = 'api?t=get&reallink=' + lgitem.mirror_1 + '&category=Books > Ebook&name1=' + lgitem.title + '&name2=' + lgitem.title + '&subject=' + lgitem.author + ' - ' + lgitem.title + '&size=' + str(int(str(lgitem.size).replace(" Mb", "").replace(" Kb", "")) * 1024)
                eurl = urllib.parse.quote(eurl)
                setattr(lgitem, 'enclosure_url', eurl)
                # you were about to setup enclosure url to match the format of 
                #http://192.168.0.141:8003/api?t=get&reallink=http://library.lol/main/F452F3B5B9E8F6E32C9D8603C4E59B99&category=books&name1=title&name2=title2&subject=titlesubject&size=23425616
                setattr(lgitem, 'newznab_category1', "7000")
                setattr(lgitem, 'newznab_category2', "7020")
                # calc size
                size = 1024
                if 'Mb' in lgitem.size:
                    size = int(lgitem.size.replace(' Mb', '')) * 1024 * 1024
                elif 'Kb' in lgitem.size:
                    size = int(lgitem.size.replace(' Kb', '')) * 1024
                elif 'Gb' in lgitem.size:
                    size = int(lgitem.size.replace(' Gb', '')) * 1024 * 1024 * 1024
                setattr(lgitem, 'newznab_size', str(size))
                setattr(lgitem, 'newznab_guid', guid )
                setattr(lgitem, 'newznab_grabs', 46)
                setattr(lgitem, 'newznab_usenetdate', date or '')
                items += self.item(lgitem).Get_XML()
                self.item_count += 1

            self.newznab = '<newznab:response offset="0" total="' + str(self.item_count) + '" />'
            return items
            
        class item:
            def __init__(self, book):
                self.title = book.description
                self.guid = book.guid
                self.link = book.link
                self.comments = book.comments
                self.pubdate = book.pubDate
                self.category = book.category
                self.description = book.description
                self.enclosure_url = book.enclosure_url
                self.newznab_category1 = book.newznab_category1
                self.newznab_category2 = book.newznab_category2
                self.newznab_size = book.newznab_size
                self.newznab_guid = book.newznab_guid
                self.newznab_grabs = book.newznab_grabs
                self.newznab_usenetdate = book.newznab_usenetdate
                if 'epub' in book.extension:
                    self.quality = '(epub)'
                elif 'pdf' in book.extension:
                    self.quality = '(pdf)'
                elif 'mobi' in book.extension:
                    self.quality = '(mobi)'
                else:
                    self.quality = '(' + book.extension + ')'
                self.nbzfilename = str(self.title) + ' ' + self.quality + '.nbz'
                
            def Get_XML(self):
                xtitle = '<title>' + str(self.title) + ' ' + self.quality + '</title>'
                xguid = '<guid isPermaLink="true">' + str(self.guid) + '</guid>' # https://nzbgeek.info/geekseek.php?guid=be6daa29e818f47d52777ba15f15036a
                xlink = '<link>' + str(self.link) + '</link>' # https://api.nzbgeek.info/api?t=get&amp;id=be6daa29e818f47d52777ba15f15036a&amp;apikey=O4Cf3uNQhti09MLGot5XlWAXM37E9nsa
                xcomments = '<comments>' + str(self.comments) + '</comments>' # https://nzbgeek.info/geekseek.php?guid=be6daa29e818f47d52777ba15f15036a
                xpubdate = '<pubDate>' + str(self.pubdate) + '</pubDate>' # Sun, 01 May 2022 15:30:18 +0000
                xcategory = '<category>' + str(self.category) + '</category>' # Books > Ebook
                xdescription = '<description>' + str(self.description) + '</description>' # James, E L - Fifty Shades 01 - Fifty Shades of Grey (retail)
                xenclosure_url = '<enclosure url="' + str(self.enclosure_url) + '" length="' + str(self.newznab_size) + '" type="application/x-nzb"/>' # https://api.nzbgeek.info/api?t=get&amp;id=be6daa29e818f47d52777ba15f15036a&amp;apikey=O4Cf3uNQhti09MLGot5XlWAXM37E9nsa # 2414000
                xnewznab_category1 = '<newznab:attr name="category" value="7000"/>'
                xnewznab_category2 = '<newznab:attr name="category" value="7020"/>'
                xnewznab_size = '<newznab:attr name="size" value="' + str(self.newznab_size) + '"/>' # 2414000
                xnewznab_guid = '<newznab:attr name="guid" value="' + str(self.guid) + '"/>' # be6daa29e818f47d52777ba15f15036a
                xnewznab_grabs = '<newznab:attr name="grabs" value="' + str(self.newznab_grabs) + '"/>' # 46
                xnewznab_usenetdate = '<newznab:attr name="usenetdate" value="' + str(self.newznab_usenetdate) + '"/>' # Sun, 01 May 2022 15:30:18 +0000
                
                r = '<item>' + xtitle + xguid + xlink + xcomments + xpubdate + xcategory
                r += xdescription + xenclosure_url + xnewznab_category1 + xnewznab_category2
                r += xnewznab_size + xnewznab_guid + xnewznab_grabs + xnewznab_usenetdate
                r = r.replace(' & ', '&amp;') + '</item>'
                return r


        
      
class nzb:
    # this is part of the indexer
    def __init__(self, category='', name1='', name2='', subject='', size='', url=''): 
        self.category = category
        self.name1 = name1.replace('%20', ' ')
        self.name2 = name2.replace('%20', '.').replace(' ', '.')
        self.subject = 'Re: REQ: ' + name1 + '&quot;' + subject.replace('%20', ' ') + '&quot;'
        self.size = size
        self.url = url
        self.dt=datetime.datetime.now()
        
    def download(self, url):
        result = LG.result(url)
        
        thread = Thread(target = result.download)
        thread.start()
        return result.file_name
    
    def get(self):
        xml  = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<!DOCTYPE nzb PUBLIC "-//newzBin//DTD NZB 1.1//EN" "http://www.newzbin.com/DTD/nzb/nzb-1.1.dtd">\n'
        xml += '<nzb xmlns="http://www.newzbin.com/DTD/2003/nzb">\n'
        xml += '\n'
        xml += '<head>\n'
        xml += ' <meta type="category">Books &gt; Ebook</meta>\n'
        xml += ' <meta type="name">' + self.name1 + '</meta>\n'
        xml += ' <meta type="name">' + self.name2 + '</meta>\n'
        xml += ' <meta type="category">Books &gt; Ebook</meta>\n'
        xml += '</head>\n'
        xml += '\n'
        xml += '<file poster="gdoMjLZraNQkB_HfRE1nHw-YXo@nywfLvV._Ej" date="' + str(self.dt.timestamp()).split('.')[0] + '" subject="(retail) ' + self.subject + ' yEnc (1/1)">\n'
        xml += ' <groups>\n'
        xml += '  <group>alt.binaries.movies.mkv</group>\n'
        xml += ' </groups>\n'
        xml += ' <segments>\n'
        data = self.url#.split('/')[-1] + '@' + '4ax.com'
        xml += '  <segment bytes="' + self.size + '" number="1">' + data + '</segment>\n'
        xml += ' </segments>\n'
        xml += '</file>\n'
        xml += '<!-- generated by newznab 0.2.3p -->\n'
        xml += '</nzb>'
        return xml