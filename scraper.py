# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
import dateutil.parser
import datetime
import time

# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")


print "Hello, scrapertest!"

html = scraperwiki.scrape("https://www.doffin.no/Notice?query=&PageNumber=1&PageSize=10&OrderingType=0&OrderingDirection=1&RegionId=&CountyId=20&MunicipalityId=&IsAdvancedSearch=false&location=20&NoticeType=2&PublicationType=1&IncludeExpired=false&Cpvs=&EpsReferenceNr=&DeadlineFromDate=&DeadlineToDate=&PublishedFromDate=&PublishedToDate=")

root = lxml.html.fromstring(html)

for el in root.cssselect("div.notice-search-item div"):           
    contentref = root.cssselect("div.notice")
    abstract = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblAbstract")
    pubdate = get_value(root,"span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblPubDate")
    appdocdeadline = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblAppdeadline")
    appdeadlinedate = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblDeadlineDate")
    appdeadlinetime = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblDeadlineTime")
    title = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblTitle")
    publisher = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblAuth")
    apptype = get_value(root, "span#ctl00_ContentPlaceHolder1_tab_StandardNoticeView1_notice_introduction1_lblDocType")

    data = {
	   'month' : month,
	   'seq' : seq,
	   'scrapedurl'  : url,
	   'title'       : title,
	   'abstract'    : abstract,
	   'publisher'   : publisher,
	   'publishdate' : dateutil.parser.parse(pubdate, dayfirst=True).date(),
	   'scrapestamputc' : datetime.datetime.now(),
	   'apptype'     : apptype,
    }
    scraperwiki.sqlite.save(unique_keys=['Ref'], data=data)

print "And done!"
