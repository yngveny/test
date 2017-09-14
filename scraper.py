# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

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

for el in root.cssselect("div.right-col *"):           
    #print lxml.html.tostring(el, pretty_print=True)
    print(el.text_content().encode("utf-8")) 
    tds = el.cssselect("div")
    data = {
            'ref' : tds[0].text_content(),
            'frist' : tds[1].text_content()
        }
    
    #print el.text
    #scraperwiki.sqlite.save(unique_keys=[el.text], data=lxml.html.tostring(el, pretty_print=True))

print "And done!"
