import librarygenesis as LG
import datetime
import calendar


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
            r += self.Get_Items(self.q) #self.item.Get_XML()
            r += self.newznab
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
                date = 'Sun, 13 May 2012 14:52:04 +0000' #dayofweek + ', ' + str(dt.day) + ' ' + str(calendar.month_name[int(dt.month) -1])[:3] + ' ' + \
                #       Tue, 19 Jan 2024 16:32:13 +0000
                #str(dt.year) + ' ' + str(dt.time()).split(".")[0] + ' +0000'
                setattr(lgitem, 'guid', lgitem.id or '')
                setattr(lgitem, 'link', lgitem.mirror_1 or '')
                setattr(lgitem, 'comments', lgitem.mirror_1 or '')
                setattr(lgitem, 'pubDate', date)
                setattr(lgitem, 'category', 'Books > Ebook')
                setattr(lgitem, 'description', lgitem.author + ' - ' + lgitem.title)
                setattr(lgitem, 'encludure_url', lgitem.mirror_1 or '')
                setattr(lgitem, 'newznab_category1', "7000")
                setattr(lgitem, 'newznab_category2', "7020")
                setattr(lgitem, 'newznab_size', int(str(lgitem.size).replace(" Mb", "").replace(" Kb", "")) * 1024 * 1024)
                setattr(lgitem, 'newznab_guid', lgitem.id or '')
                setattr(lgitem, 'newznab_grabs', 46)
                setattr(lgitem, 'newznab_usenetdate', date or '')
                items += self.item(lgitem).Get_XML()
                self.item_count += 1

            self.newznab = '<newznab:response offset="0" total="' + str(self.item_count) + '" />'
            return items
            
        class item:
            def __init__(self, book):
                self.title = book.title
                self.guid = book.guid
                self.link = book.link
                self.comments = book.comments
                self.pubdate = book.pubDate
                self.category = book.category
                self.description = book.description
                self.encludure_url = book.mirror_1
                self.newznab_category1 = book.newznab_category1
                self.newznab_category2 = book.newznab_category2
                self.newznab_size = book.newznab_size
                self.newznab_guid = book.newznab_guid
                self.newznab_grabs = book.newznab_grabs
                self.newznab_usenetdate = book.newznab_usenetdate
                
            def Get_XML(self):
                xtitle = '<title>' + str(self.title) + '</title>'
                xguid = '<guid isPermaLink="true">' + str(self.guid) + '</guid>' # https://nzbgeek.info/geekseek.php?guid=be6daa29e818f47d52777ba15f15036a
                xlink = '<link>' + str(self.link) + '</link>' # https://api.nzbgeek.info/api?t=get&amp;id=be6daa29e818f47d52777ba15f15036a&amp;apikey=O4Cf3uNQhti09MLGot5XlWAXM37E9nsa
                xcomments = '<comments>' + str(self.comments) + '</comments>' # https://nzbgeek.info/geekseek.php?guid=be6daa29e818f47d52777ba15f15036a
                xpubdate = '<pubDate>' + str(self.pubdate) + '</pubDate>' # Sun, 01 May 2022 15:30:18 +0000
                xcategory = '<category>' + str(self.category) + '</category>' # Books > Ebook
                xdescription = '<description>' + str(self.description) + '</description>' # James, E L - Fifty Shades 01 - Fifty Shades of Grey (retail)
                xenclosure_url = '<enclosure url="' + str(self.encludure_url) + '" length="' + str(self.newznab_size) + '" type="application/x-nzb"/>' # https://api.nzbgeek.info/api?t=get&amp;id=be6daa29e818f47d52777ba15f15036a&amp;apikey=O4Cf3uNQhti09MLGot5XlWAXM37E9nsa # 2414000
                xnewznab_category1 = '<newznab:attr name="category" value="7000"/>'
                xnewznab_category2 = '<newznab:attr name="category" value="7020"/>'
                xnewznab_size = '<newznab:attr name="size" value="' + str(self.newznab_size) + '"/>' # 2414000
                xnewznab_guid = '<newznab:attr name="guid" value="' + str(self.guid) + '"/>' # be6daa29e818f47d52777ba15f15036a
                xnewznab_grabs = '<newznab:attr name="grabs" value="' + str(self.newznab_grabs) + '"/>' # 46
                xnewznab_usenetdate = '<newznab:attr name="usenetdate" value="' + str(self.newznab_usenetdate) + '"/>' # Sun, 01 May 2022 15:30:18 +0000
                
                r = '<item>' + xtitle + xguid + xlink + xcomments + xpubdate + xcategory
                r += xdescription + xenclosure_url + xnewznab_category1 + xnewznab_category2
                r += xnewznab_size + xnewznab_guid + xnewznab_grabs + xnewznab_usenetdate
                return r + '</item>'
            
            
            
#xml = rss('O4Cf3uNQhti09MLGot5XlWAXM37E9nsa', 'search', 'title+author').Get_XML()
#print (xml)