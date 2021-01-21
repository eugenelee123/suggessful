import urllib
from bs4 import BeautifulSoup
from googlesearch import search
req = urllib.request.Request("https://www.urbanoutfitters.com/", headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen( req )
soup = BeautifulSoup(con.read(), features = "html.parser")

#get company name
meta_title = soup.find("meta", property = "og:title")
title = soup.find("title")
title = title.string
url = soup.find("meta", property = "og:url")

# print("meta title: ", meta_title)
# print("title: ", title)
# print("url: ", url)

query = "Brands like {}".format(title)
print(query)

for i in search(query, tld = "co.in", num = 10, stop = 10, pause = 2):
    print(i)



