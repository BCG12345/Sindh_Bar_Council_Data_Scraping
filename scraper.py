# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
page = scraperwiki.scrape("https://advocates.sindhbarcouncil.org/enrollments_list.php")


element_tree = lxml.html.fromstring(page) 
  
tree_title_element = element_tree.xpath('//table')
print(tree_title_element)
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

   
