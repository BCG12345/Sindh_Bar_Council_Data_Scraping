# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://advocates.sindhbarcouncil.org/enrollments_list.php")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
#root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
#scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
scraperwiki.sql.select("* from data where 'name'='peter'")



"""
url = requests.get('https://advocates.sindhbarcouncil.org/enrollments_list.php')
soup =BeautifulSoup(url.text,'lxml')
result = soup.find_all('td', {'data-field': 'pre_reg_no'})
if (len(result) > 0):
    print(result)
        
        
        
   """     
