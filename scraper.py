# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#import dateutil.parser
import datetime
import time

print "Hello, scrapertest!"

html = scraperwiki.scrape("https://www.doffin.no/Notice?&IsAdvancedSearch=false&NoticeType=2&IncludeExpired=false")
root = lxml.html.fromstring(html)
n = 0
for el in root.cssselect("div.notice-search-item div"):           
    #contentref = root.cssselect("div.notice")

    abstract = root.cssselect("div.notice-search-item-header")
    
    #pubdate = get_value(root,"span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblPubDate")
    #appdocdeadline = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblAppdeadline")
    #appdeadlinedate = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblDeadlineDate")
    #appdeadlinetime = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblDeadlineTime")
    #title = root.cssselect("span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblTitle")
    #publisher = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblAuth")
    #apptype = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblDocType")

    data = {
	   #'title'       : title,
	   'abstract'    : abstract
	   #'publisher'   : publisher,
	   #'publishdate' : dateutil.parser.parse(pubdate, dayfirst=True).date(),
	   #'scrapestamputc' : datetime.datetime.now(),
	   #'apptype'     : apptype
    }
    scraperwiki.sqlite.save(unique_keys=["abstract"], data=data)
    n = n+1

print "And done!"
