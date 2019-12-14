# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
page = scraperwiki.scrape("https://advocates.sindhbarcouncil.org/enrollments_list.php")
print(lxml.html.tostring(page))

#
# # Find something on the page using css selectors
#print (lxml.html.tostring(html))
#root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
#scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
#scraperwiki.sql.select("* from data where 'name'='peter'")

   
