# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

print "Hello, scrapertest!"

import scraperwiki           
# html = scraperwiki.scrape("http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm")

# html = scraperwiki.scrape("https://www.doffin.no/Notice?query=&PageNumber=1&PageSize=10&OrderingType=0&OrderingDirection=1&RegionId=&CountyId=20&MunicipalityId=&IsAdvancedSearch=false&location=20&NoticeType=2&PublicationType=1&IncludeExpired=false&Cpvs=&EpsReferenceNr=&DeadlineFromDate=&DeadlineToDate=&PublishedFromDate=&PublishedToDate=")

html = scraperwiki.scrape("https://www.doffin.no/Notice?query=&PageNumber=1&PageSize=10&OrderingType=0&OrderingDirection=1&RegionId=&CountyId=20&MunicipalityId=&IsAdvancedSearch=false&location=20&NoticeType=2&PublicationType=1&IncludeExpired=false&Cpvs=&EpsReferenceNr=&DeadlineFromDate=&DeadlineToDate=&PublishedFromDate=&PublishedToDate=")

root = lxml.html.fromstring(html)

for el in root.cssselect("div.notice-search-item-header a"):           
    print el

print "And done!"
